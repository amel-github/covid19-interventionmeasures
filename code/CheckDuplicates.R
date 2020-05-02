library(dplyr)

df <- read.csv("COVID19_non-pharmaceutical-interventions.csv") 

df %>% 
  group_by(iso3, Region, Date, Measure_L1, Measure_L2, Measure_L3, Measure_L4) %>% 
  filter(n()>1) %>% arrange(iso3, Date) -> reps

write.csv(reps, file="reps.csv", row.names = F)