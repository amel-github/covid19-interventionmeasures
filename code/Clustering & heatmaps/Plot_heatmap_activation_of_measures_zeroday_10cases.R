##################################################
## Project: CCCSL: Complexity Science Hub Covid-19 Control Strategies List (2020)
## Clustering of countries based on implemented measures
## Script purpose: This scripts makes heatmaps based on time of implementation of measures
## Date:12.04.2020.
## Authors:  Elma Hot Dervic, Nils Haug, Amélie Desvars-Larrive
##################################################


library(reshape2)
library(ggplot2)
library( RColorBrewer)
library(svglite)

first_date_matrix <- matrix(NA, nrow=length(countries_with_measures), ncol=(ncol(measures)-2))
min_date_10_cases <- rep(0, length(countries_with_measures))

for(i in 1:length(countries_with_measures)) {
  country.name <- countries_with_measures[i]
  onecountry_measures <- measures[measures$Country==country.name, ]
  JH_data_one_country <-  JH_data %>% filter(country == country.name)
  date_cases <- JH_data_one_country$date[JH_data_one_country$cases>=10]
  if(length(date_cases)!=0){
    min_date_10_cases[i] <- min(date_cases)
    if(nrow(JH_data_one_country)>1 & nrow(onecountry_measures)>0){
      for(j in 3:dim(measures)[2]){
        if(sum(onecountry_measures[,j])>0){
          min_date <- min(onecountry_measures$Date[onecountry_measures[,j]])
          if(!is.na(min_date) & !is.na(min_date_10_cases[i])){i
            min_date <- as.Date(min_date)
            first_date_matrix[i,(j-2)] <- as.numeric(min_date - min_date_10_cases[i])
          } }
      } } } } 


data_for_plot <- as.data.frame(first_date_matrix)
names(data_for_plot) <- names_l2
data_for_plot$Country <- countries_with_measures
# str(data_for_plot)
# dim(data_for_plot)
# sum(!is.na(data_for_plot))

df <- melt(data_for_plot ,  id.vars = c('Country'), variable.name = 'Measures')
names(df) <- c("Country", "Measures","Time_difference_Days"  )
# head(df)
names_l1_l2 <- data.frame(names_l1, names_l2, stringsAsFactors = F)


df <- merge(df, names_l1_l2, by.x = "Measures", by.y ="names_l2")
# df$names_l1 <- as.factor(df$names_l1)
# names(df)
# head(df)
df <- df[order(df$names_l1),]
# head(df)



cols <- brewer.pal(length(unique(names_l1)),"Dark2")
x <- table(names_l1_l2$names_l1)
x <- unname(x)
# x
col <- NULL
for(i in 1:length(x)){
  col <- c(col, rep(cols[i], x[i]))
}



plot <- ggplot(df, aes(Country, Measures,  fill= Time_difference_Days)) + 
  geom_tile() +
  scale_fill_gradient(low="lightgreen", high="red", na.value="darkgray", breaks=c(-75, -50, -25, 0, 25, 50, 75)) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, face = "bold"), 
        axis.text.y = element_text(colour = col, size = 8, face = "bold"),
        text = element_text(family = "Helvetica")) +
  guides(fill=guide_legend(title="Time difference [Days]"))            
name <- "Measures_Countries_time_of_activation_zeroday10cases.png"
ggsave(plot,  file = name,  width = 33*1.25, height = 27 *1.25, units = "cm", dpi=96) 
name <- "Measures_Countries_time_of_activation_zeroday10cases.svg"
ggsave(plot,  file = name,  width = 33*1.25, height = 27 *1.25, units = "cm", dpi=96) 


