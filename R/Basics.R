
# @ INSTALLING AND LOADING PACKAGES
#* Manually
# installing 
install.packages('package name')
# loading
library('package name') # No message.
require('package name') # Gives a confirmation message.

#* Using pacman package for managing add-on packages.
# Pacman will install packages, if needed, and then load the packages.
install.packages("pacman")

# Installs pacman ("package manager") if needed
if (!require("pacman")) install.packages("pacman")

# Use the p_load function from pacman without actually loading pacman
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, stringr, tidyr) 



#@ CLEAN UP 
#* Clear packages
p_unload(dplyr, tidyr, stringr) # Clear specific packages
p_unload(all)  # Easier: clears all add-ons
detach("package:datasets", unload = TRUE)  # For base

#* Clear plots
dev.off()  # But only if there IS a plot

#* Clear console
cat("\014")  # ctrl+L



#@ IMPORTING DATA
#* With rio package
# Adv: Uses same syntax for all file types

rio_csv <- import("Data/mbb.csv")
rio_txt <- import("Data/mbb.txt")
rio_xlsx <- import("Data/mbb.xlsx")

#* R's built-in function read
r_txt1 <- read.table("Data/mbb.txt", header=TRUE)

# This works with missing data by specifying the separator:  \t is for tabs, sep = "," for commas. R converts missing to "NA"
r_txt2 <- read.table("Data/mbb.txt", header=TRUE, sep="\t")

trends.csv <- read.csv("Data/mbb.csv", header = TRUE)



#@ LOAD BASE DATA
# load the base datasets package
library(datasets) 
# use the iris dataset directly from datasets package
head(iris) 



#@ SUMMARY FUNCTION 
#* Gives statistical analysis of the data

summary(iris$Species)       # Categorical variable
summary(iris$Sepal.Length)  # Quantitative variable
summary(iris)               # Entire data frame



#@ DESCRIBE FUNCTION
#* Use the describe function from psych package to get more details like stdev, skew. For quantitative variables only.

pacman::p_load(psych) # load psych package
describe(iris$Sepal.Length)  # One quantitative variable
describe(iris)               # Entire data frame



#@ DATA VIEWER 
View(iris) # view the iris csv
View(r_txt1) # view text table



#@ HELPER 
#* Using ? before a func will open up a help page
?summary
?view



#@ TYPEOF
# check the type of data type or structure
typeof(1)
typeof('2')
typeof(as.list(c('a', 'b', 'c')))



#@ SAVING FILES
#* CSV
write.csv(df,'main.csv')
#* Plots
ggsave("Data/mtcars.pdf") # saves the last plot in the given directory
ggsave("Data/mtcars.png", width = 20, height = 20, units = "cm") 



#@ CLEAN UP 
#* Clear environment
rm(list = ls()) 

#* Clear packages
p_unload(all)  # Remove all add-ons
detach("package:datasets", unload = TRUE)   # For base

#* Clear console
cat("\014")  # ctrl+L

