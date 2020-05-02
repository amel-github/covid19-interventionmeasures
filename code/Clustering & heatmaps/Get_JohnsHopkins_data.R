##################################################
## Project: CCCSL: Complexity Science Hub Covid-19 Control Strategies List (2020)
## Clustering of countries based on implemented measures
## Script purpose: This scripts get Johns Hopkins raw data and make dataframe
## JH_data --- "confirmed"  "date"      "deaths"    "recovered" "country"   "newcases" 
## Date:12.04.2020.
## Authors:  David Garcia, Amélie Desvars-Larrive, Thomas Niederkrotenthaler
## Modified by Elma Dervic
##################################################

library(dplyr)
library(incidence)

# JH DATA
confirmeddf <- read.csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv", stringsAsFactors = F)
deathsdf <- read.csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv", stringsAsFactors = F)
recovereddf <- read.csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv", stringsAsFactors = F)

# List of countries to iterate
countries <-  unique(c(confirmeddf$Country.Region, deathsdf$Country.Region, recovereddf$Country.Region))

# ADD HONG KOND as a country
HongKong <- confirmeddf[1,]
HongKong$Province.State <- ""
HongKong$Country.Region <- "Hong Kong"
HongKong[3:dim(HongKong)[2]] <- confirmeddf[confirmeddf$Province.State=="Hong Kong",3:dim(HongKong)[2]]
confirmeddf <- rbind(confirmeddf,HongKong)

HongKong <- recovereddf [1,]
HongKong$Province.State <- ""
HongKong$Country.Region <- "Hong Kong"
HongKong[3:dim(HongKong)[2]] <- recovereddf[recovereddf$Province.State=="Hong Kong",3:dim(HongKong)[2]]
recovereddf <- rbind(recovereddf ,HongKong)


HongKong <- deathsdf[1,]
HongKong$Province.State <- ""
HongKong$Country.Region <- "Hong Kong"
HongKong[3:dim(HongKong)[2]] <- deathsdf[deathsdf$Province.State=="Hong Kong",3:dim(HongKong)[2]]
deathsdf <- rbind(deathsdf, HongKong)
countries <- c(countries, "Hong Kong")


# We convert the data frame from wide to long format
ldf <- data.frame(country=NULL, date=NULL, confirmed=NULL, deaths=NULL, recovered=NULL)

for (country in countries)
{
  # The first four columns contain the name of the country, location, etc. The time series win wide format starts from the fifth.
  confirmeddf %>% 
    filter(Country.Region == country) %>% 
    summarise_at(5:ncol(confirmeddf), sum) -> confirmedcounts
  date <- names(confirmeddf)[5:ncol(confirmeddf)] 
  
  # date are in a weird format, we convert them for R
  date <- as.Date(gsub("\\.", "-", sub(".", "", date)), format = "%m-%d-%y")
  confirmeddfsel <- data.frame(confirmed = as.numeric(confirmedcounts), date=date)
  
  # We repeat the above process for deaths and recovered time series
  deathsdf %>% 
    filter(Country.Region == country) %>% 
    summarise_at(5:ncol(deathsdf), sum) -> deathscounts
  date <- names(deathsdf)[5:ncol(deathsdf)] 
  date <- as.Date(gsub("\\.", "-", sub(".", "", date)), format = "%m-%d-%y")
  deathsdfsel <- data.frame(deaths = as.numeric(deathscounts), date=date)
  
  recovereddf %>% 
    filter(Country.Region == country) %>% 
    summarise_at(5:ncol(recovereddf), sum) -> recoveredcounts
  date <- names(recovereddf)[5:ncol(recovereddf)] 
  date <- as.Date(gsub("\\.", "-", sub(".", "", date)), format = "%m-%d-%y")
  recovereddfsel <- data.frame(recovered = as.numeric(recoveredcounts), date=date)
  
  # inner_joins map all data by date so the long format has a column for confirmed, another for deaths, and a third one for recovered
  newdf <- inner_join(confirmeddfsel, deathsdfsel)
  newdf <- inner_join(newdf, recovereddfsel)
  
  # We add the country name and include this country in the full data frame
  newdf$country = country
  ldf <- rbind(ldf, newdf)
}


JH_data <- ldf[c(2:nrow(ldf)),]
JH_data$newcases <- diff(ldf$confirmed)
names(JH_data)[1] <- "cases"

