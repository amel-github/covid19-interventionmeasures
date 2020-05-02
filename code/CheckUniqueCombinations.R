## Find unique combination of L1-, L2-, L3-, and L4-category measures.

unique.combi <- unique(measures[,c("Measure_L1","Measure_L2","Measure_L3", "Measure_L4")])

write.csv (unique.combi, file = "Unique.combi.csv")