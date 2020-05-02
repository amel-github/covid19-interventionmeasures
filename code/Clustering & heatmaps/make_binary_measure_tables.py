import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta

# Define urls for accessing data

measurelist_url = 'https://raw.githubusercontent.com/amel-github/covid19-interventionmeasures/master/COVID19_non-pharmaceutical-interventions.csv'

categorylist_url = 'https://raw.githubusercontent.com/amel-github/covid19-interventionmeasures/master/List_measures_by_categoryL1-L2.csv'

###### Import data on intervention measures

measure_df = pd.read_csv(measurelist_url,sep=',',quotechar = '"',
                         encoding = 'latin-1',parse_dates=['Date'],dayfirst=True).iloc[:,:10]

# Homogenize the country names with those used in the Johns Hopkins data set

to_rename = {
    'Czech Republic':'Czechia',
    'France (metropole)':'France',
    'Republic of Ireland':'Ireland',
    'South Korea': 'Korea, South',
    'Taiwan': 'Taiwan*',
    'UK':'United Kingdom'
}

measure_df['Country'] = measure_df['Country'].replace(to_rename)

measure_df['Date_ordinal'] = measure_df['Date'].apply(lambda x: x.toordinal())

# Load table of measure categories and give unique ID to each category

measurelist = pd.read_csv(categorylist_url,
                          usecols=['Measure_L1','Measure_L2']).applymap(lambda x: x.strip())

measurelist = measurelist.drop_duplicates().sort_values(['Measure_L1','Measure_L2'])    
measurelist['Measure_id'] = np.arange(measurelist.shape[0])
measurelist = measurelist.set_index('Measure_id',drop=False)
measurelist['Measure'] = measurelist.apply(lambda x: 'L1: '+x.Measure_L1+' / L2: '+x.Measure_L2,axis=1)

# Join measure_df with measurelist to get ID of each measure

measure_df = measure_df.merge(measurelist[['Measure_L1','Measure_L2','Measure_id']],
                              left_on=['Measure_L1','Measure_L2'],
                              right_on=['Measure_L1','Measure_L2'],how='left')
measure_df.drop(measure_df.loc[lambda x: np.isnan(x.Measure_id)].index,inplace=True)
measure_df['Measure_id'] = measure_df['Measure_id'].apply(lambda x: int(x)) 

###### For each country, binarily encode implemented measures

day0 = date(2019,1,1) #day from which to start registering measures
mindate = day0.toordinal()
maxdate = date.today().toordinal()

# Get list of all countries appearing in the data set
countries = list(set(measure_df.Country))
countries.sort()

# Initialize data frames for binary measure data
bindata = pd.DataFrame()
bindata_cumulative = pd.DataFrame()

for country in countries:
    
    countrymeasures = measure_df.loc[measure_df.Country==country][['Date_ordinal','Measure_id']]

    binmatrix = np.zeros((maxdate-mindate+1,measurelist.shape[0])).astype(bool)
    binmatrix_cumulative = binmatrix.copy()
    
    i = 0
    
    for day in range(mindate,maxdate+1):
        # loop over days from day0 until today
        
        newmeasures = countrymeasures.loc[countrymeasures.Date_ordinal==day,'Measure_id'].values
        previousmeasures = countrymeasures.loc[countrymeasures.Date_ordinal<day,'Measure_id'].values
        binmatrix[i,newmeasures] = True
        binmatrix_cumulative[i,newmeasures] = True
        binmatrix_cumulative[i,previousmeasures] = True        
        
        i += 1
    
    # binary encoding of measures taken in country
    bindata_country = pd.DataFrame(data=binmatrix,
                                   columns=measurelist['Measure']).set_index(np.arange(mindate,maxdate+1))
    bindata_country['Country'] = country
    bindata_country_cumulative = pd.DataFrame(data=binmatrix_cumulative,
                                              columns=measurelist['Measure'])
    bindata_country_cumulative.index = np.arange(mindate,maxdate+1)
    bindata_country_cumulative['Country'] = country
    
    # append to big table containing binary data on all countries
    bindata = bindata.append(bindata_country,ignore_index=False)
    bindata_cumulative = bindata_cumulative.append(bindata_country_cumulative,ignore_index=False)
    
bindata['Date'] = list(pd.Series(bindata.index).apply(lambda x: date.fromordinal(x)))
bindata_cumulative['Date'] = list(pd.Series(bindata_cumulative.index)
         .apply(lambda x: date.fromordinal(x)))

bindata = bindata.set_index(['Country', 'Date'],drop=True)
bindata_cumulative = bindata_cumulative.set_index(['Country', 'Date'])

##### Export to csv

bindata.to_csv('bin_COVID19_measures.csv',sep=';')
bindata_cumulative.to_csv('bin_COVID19_measures_cumulative.csv',sep=';')