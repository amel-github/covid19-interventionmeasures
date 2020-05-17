import csv
import sqlite3
import os
import logging
import copy
import psycopg2
from psycopg2 import extras

try:
	from local_postgres import conninfo
except ImportError:
	conninfo = {'host':'localhost','port':5432}


logger = logging.getLogger('intervention_measures')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)


DB_INIT = """

CREATE TABLE IF NOT EXISTS tags(
id INTEGER NOT NULL PRIMARY KEY,
tag TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS countries(
id INTEGER NOT NULL PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
iso TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS regions(
id INTEGER NOT NULL PRIMARY KEY,
name TEXT NOT NULL,
country INTEGER NOT NULL REFERENCES countries(id),
UNIQUE(name,country)
);

CREATE TABLE IF NOT EXISTS measure_types(
id INTEGER NOT NULL PRIMARY KEY,
level INTEGER NOT NULL,
name TEXT NOT NULL UNIQUE,
parent INTEGER REFERENCES measure_types(id)
);

CREATE TABLE IF NOT EXISTS sources(
id INTEGER NOT NULL PRIMARY KEY,
name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS measures(
id INTEGER NOT NULL PRIMARY KEY,
measure INTEGER NOT NULL REFERENCES measure_types(id),
source INTEGER REFERENCES sources(id),
comment TEXT,
country INTEGER REFERENCES countries(id),
region INTEGER REFERENCES regions(id),
day DATE,
tag INTEGER REFERENCES tags(id)
);

"""

DB_INIT_PG = """

CREATE TABLE IF NOT EXISTS tags(
id SERIAL NOT NULL PRIMARY KEY,
tag TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS countries(
id SERIAL NOT NULL PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
iso TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS regions(
id SERIAL NOT NULL PRIMARY KEY,
name TEXT NOT NULL,
country INTEGER NOT NULL REFERENCES countries(id),
UNIQUE(name,country)
);

CREATE TABLE IF NOT EXISTS measure_types(
id SERIAL NOT NULL PRIMARY KEY,
level INT NOT NULL,
name TEXT NOT NULL UNIQUE,
parent INT REFERENCES measure_types(id)
);

CREATE TABLE IF NOT EXISTS sources(
id SERIAL NOT NULL PRIMARY KEY,
name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS measures(
id SERIAL NOT NULL PRIMARY KEY,
measure INT NOT NULL REFERENCES measure_types(id),
source INT REFERENCES sources(id),
comment TEXT,
country INT REFERENCES countries(id),
region INT REFERENCES regions(id),
day DATE,
tag INT REFERENCES tags(id)
);

SET DATESTYLE TO PostgreSQL,European;

"""

def clean_int(i):
	if i[0]=='"':
		return int(i.split('"')[1])
	else:
		try:
			return int(i)
		except:
			print(i)
			return None

def final_measure(m_list):
	for l in m_list:
		if l != '':
			ans = l
		else:
			break
	return ans

class InterventionMeasuresDB(object):
	def __init__(self,folder='.',db_name='intervention_measures',db_type='sqlite',conninfo=conninfo):
		self.db_type = db_type
		if db_type == 'sqlite':
			self.connection = sqlite3.connect(os.path.join(folder,db_name+'.db'))
		else:
			self.conninfo = copy.deepcopy(conninfo)
			conninfo['database'] = db_name
			self.connection = psycopg2.connect(**conninfo)
		self.cursor = self.connection.cursor()
		self.logger = logger

	def init_db(self):
		if self.db_type == 'sqlite':
			init_script = DB_INIT
		else:
			init_script = DB_INIT_PG
		for cmd in init_script.split(';')[:-1]:
			self.cursor.execute(cmd)
			self.logger.info(cmd)
		self.connection.commit()

	def fill_complete(self,filename,tag=None):
		self.logger.info("reading file {}".format(filename))
		if tag is None:
			tag = '.'.join(filename.split('.')[:-1])
			if self.db_type == 'sqlite':
				self.cursor.execute("INSERT OR IGNORE INTO tags(tag) VALUES(?);",(tag,))
			else:
				self.cursor.execute("INSERT INTO tags(tag) VALUES(%s) ON CONFLICT DO NOTHING;",(tag,))
		self.connection.commit()
		self.logger.info("added tag {}".format(tag))
		self.fill_countries(filename=filename)
		self.fill_regions(filename=filename)
		self.fill_sources(filename=filename)
		self.fill_measure_types(filename=filename)
		self.fill_measures(filename=filename,tag=tag)

	def fill_countries(self,filename):
		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO countries(name,iso) VALUES(?,?);',((r[1],r[2]) for r in reader if print(r) is None))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO countries(name,iso) VALUES(%s,%s) ON CONFLICT DO NOTHING;',((r[1],r[2]) for r in reader))
		self.connection.commit()
		self.logger.info('Filled table countries')

	def fill_regions(self,filename):
		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO regions(name,country) VALUES(?,(SELECT id FROM countries WHERE name=?));',((r[4],r[1]) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO regions(name,country) VALUES(%s,(SELECT id FROM countries WHERE name=%s)) ON CONFLICT DO NOTHING;',((r[4],r[1]) for r in reader))
		self.connection.commit()
		self.logger.info('Filled table regions')

	def fill_sources(self,filename):
		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO sources(name) VALUES(?);',((r[11],) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO sources(name) VALUES(%s) ON CONFLICT DO NOTHING;',((r[11],) for r in reader))
		self.connection.commit()
		self.logger.info('Filled table sources')

	def fill_measure_types(self,filename):
		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO measure_types(level,name) VALUES(?,?);',((1,r[6],) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO measure_types(level,name) VALUES(%s,%s) ON CONFLICT DO NOTHING;',((1,r[6],) for r in reader))
		self.connection.commit()
		self.logger.info('Filled table measure_types level 1')

		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO measure_types(level,name,parent) VALUES(?,?,(SELECT id FROM measure_types WHERE name=?));',((2,r[7],r[6]) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO measure_types(level,name,parent) VALUES(%s,%s,(SELECT id FROM measure_types WHERE name=%s)) ON CONFLICT DO NOTHING;',((2,r[7],r[6]) for r in reader if r[7]!=''))
		self.connection.commit()
		self.logger.info('Filled table measure_types level 2')

		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO measure_types(level,name,parent) VALUES(?,?,(SELECT id FROM measure_types WHERE name=?));',((3,r[8],r[7]) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO measure_types(level,name,parent) VALUES(%s,%s,(SELECT id FROM measure_types WHERE name=%s)) ON CONFLICT DO NOTHING;',((3,r[8],r[7]) for r in reader if r[8]!=''))
		self.connection.commit()
		self.logger.info('Filled table measure_types level 3')

		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT OR IGNORE INTO measure_types(level,name,parent) VALUES(?,?,(SELECT id FROM measure_types WHERE name=?));',((4,r[9],r[8]) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO measure_types(level,name,parent) VALUES(%s,%s,(SELECT id FROM measure_types WHERE name=%s)) ON CONFLICT DO NOTHING;',((4,r[9],r[8]) for r in reader if r[9]!=''))
		self.connection.commit()
		self.logger.info('Filled table measure_types level 4')

	def fill_measures(self,filename,tag):
		with open(filename,'r') as f:
			reader = csv.reader(f,delimiter=',')
			next(reader)
			if self.db_type == 'sqlite':
				self.cursor.executemany('INSERT INTO measures(id,measure,source,comment,day,tag,country,region) VALUES(?,(SELECT id FROM measure_types WHERE name=?),(SELECT id FROM sources WHERE name=?),?,?,(SELECT id FROM tags WHERE tag=?),(SELECT id FROM countries WHERE name=?),(SELECT id FROM regions WHERE name=?));',((clean_int(r[0]),final_measure(r[5:9]),r[11],r[10],r[5],tag,r[1],r[4]) for r in reader))
			else:
				extras.execute_batch(self.cursor,'INSERT INTO measures(id,measure,source,comment,day,tag,country,region) VALUES(%s,(SELECT id FROM measure_types WHERE name=%s),(SELECT id FROM sources WHERE name=%s),%s,%s,(SELECT id FROM tags WHERE tag=%s),(SELECT id FROM countries WHERE name=%s),(SELECT id FROM regions WHERE name=%s));',((clean_int(r[0]),final_measure(r[5:9]),r[11],r[10],r[5],tag,r[1],r[4]) for r in reader))
		self.connection.commit()
		self.logger.info('Filled table measures')


if __name__ == '__main__':
	db = InterventionMeasuresDB(db_type='sqlite',db_name='covid_measures')
	# db = InterventionMeasuresDB(db_type='postgres',db_name='playground_alex')
	db.init_db()
	db.fill_complete(filename='../COVID19_non-pharmaceutical-interventions_version2_utf8.csv')
