##################################################
## Project: CCCSL: Complexity Science Hub Covid-19 Control Strategies List (2020)
## Network - overlap of measures in time
## Script purpose: This scripts call all scripts from the project
## Date:12.04.2020.
## Authors: Elma Hot Dervic, Nils Haug, Amélie Desvars-Larrive
##################################################


# Call first script 
# download raw data from github
# make binary file of measures data
# Install and load packages
my_packages <- c("reticulate", "dplyr", "stringr", "reshape2", "ggplot2", "RColorBrewer", 
                 "rgexf", "tidyverse", "svglite")                                       
not_installed <- my_packages[!(my_packages %in% installed.packages()[ , "Package"])]    # Extract not installed packages
if(length(not_installed)) install.packages(not_installed)                               # Install not installed packages


# use static data!!!


library("reticulate")
py_install("pandas", pip = TRUE)
py_install("networkx", pip = TRUE)
py_install("requests", pip = TRUE)
py_run_file("make_binary_measure_tables.py")



source("Get_JohnsHopkins_data.R")

source("Get_measures_data.R")

source("Plot_heatmap_activation_of_measures_zeroday_1stdeath.R")

source("Plot_heatmap_activation_of_measures_zeroday_10cases.R")


source("Plot_heatmap_activation_of_measures_zeroday_100cases.R")

source("Plot_heatmap_activation_of_measures_zeroday_200cases.R")

source("Clustering_kmeans.R")
p


orca(p, "Clustering_kmeans_static.svg",  scale = 6, width = 1200, height = 1200)
orca(p, "Clustering_kmeans_static.png",  scale = 6, width = 1200, height = 1200)
