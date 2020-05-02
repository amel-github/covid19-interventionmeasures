##################################################
## Project: CCCSL: Complexity Science Hub Covid-19 Control Strategies List (2020)
## Clustering of countries based on implemented measures
## Script purpose: This scripts reads binary data of measures and make dataframe

## Date:12.04.2020.
## Authors:  Elma Hot Dervic, Nils Haug, Amélie Desvars-Larrive
##################################################

library(dplyr)
library(stringr)

# Data -- MEASURES ---
NAMES_measures_csv <- read.table("bin_COVID19_measures_cumulative.csv", nrow = 1, stringsAsFactors = FALSE, sep = ";")
measures <- read.table("bin_COVID19_measures_cumulative.csv", skip = 1, stringsAsFactors = FALSE, sep = ";")
measures <- measures[, 1:length(NAMES_measures_csv)]
names(measures) <-  NAMES_measures_csv
# str(measures)
# names(measures)

measures <- measures[, c(1:dim(measures)[2])]
for( i in 3:dim(measures)[2]){
  measures[,i] <- measures[,i]=="True"
}
# summary(measures)
# names(measures)
# dim(measures)
# delete Stage 4 measure
select_measures_to_delete <- c(which(str_detect(names(measures), "L1: Returning to normal life")), which(str_detect(names(measures), "L2: Deportation of Chinese nationals")))
measures <- measures[,-select_measures_to_delete]

# set names of some countries 
measures$Country[measures$Country=="France (metropole)"]<- "France"
measures$Country[measures$Country=="Taiwan"]<- "Taiwan*"
measures$Country[measures$Country=="South Korea"]<- "Korea, South"
measures$Country[measures$Country=="Czech Republic"]<- "Czechia"
measures$Country[measures$Country=="Republic of Ireland"]<- "Ireland"
measures <- measures[-which(measures$Country=="Diamond Princess"), ]

# str(measures)
# dim(measures)


countries_with_measures <- unique(measures$Country)
# NAMES L2
names_l2 <- names(measures[,c(3:dim(measures)[2])])
for(ii in 1: length(names_l2)){
  names_l2[ii]<- substr(names_l2[ii], str_locate(names_l2[ii], "L2")[2]+3, nchar(names_l2[ii]))
}
# str(names_l2)
# str(unique(names_l2))
# add dot to duplciated l2 names !! to keep them for plots
names_l2[duplicated(names_l2)] <- paste0(names_l2[duplicated(names_l2)], ".")
numer_of_measures <- length(names_l2)

# select names of L1
# name_l1 
# 7 unique levels
names_l1 <- names(measures[,c(3:dim(measures)[2])])
for(ii in 1:length(names_l1)){
  names_l1[ii]<- substr(names_l1[ii], 5, str_locate(names_l1[ii], "L2")[1]-4)
}
# str(names_l1)
# str(unique(names_l1))


