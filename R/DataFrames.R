#@  CREATING
emp.data <- data.frame(
   emp_id = c (1:5), 
   emp_name = c("Rick","Dan","Michelle","Ryan","Gary"),
   salary = c(623.3,515.2,611.0,729.0,843.25), 
   start_date = as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11", "2015-03-27")),
   stringsAsFactors = FALSE
)



#@ ANALYSIS
#* Get the structure of the data frame.
str(emp.data)

#* Get the summary.
summary(emp.data)
describe(emp.data) # for more details

#* Extract Specific columns.
(result <- select(emp.data, emp_name, salary))



#@ SELECTING ROWS
#* Method 1: Indexing
# Versicolor
versicolorPetals <- iris$Petal.Length[iris$Species == "versicolor"] 
# Versicolor and Setosa
virginicaPetals <- iris$Sepal.Length[!iris$Species == "virginica"] # use ! for negation property
# Multiple selectors
shortVirginica <- iris$Sepal.Length[iris$Species == "virginica" & iris$Petal.Length < 5.5]

# Subsamples - Format: data[rows, columns]
# Leave rows or columns blank to select all
i.setosa <- iris[iris$Species == "setosa", ] # select rows where species is setosa and keep all columns
first2 <- iris[0:2, ] # first 2 rows, all cols
niche <- iris[c(3,5),c(2,4)] # Extract 3rd and 5th row with 2nd and 4th column.

#* Method 2: The Subset function.
df1 <- subset(iris, Species == 'Setosa') # pick only setosa samples
df2 <- subset(iris, Species != 'Setosa') # Drop setosa samples

#* Method 3: The which function.
# which() is used to return the position of the specified values in the logical vector.
df <- df[which(df$salary >= 100000.0), ] # select ballers only
df <- df[-c(which(df$age > 80 | df$age < 15)), ] # exclude very old and very young people

#@ SELECT COLS
#* Method 1: The Select function.
df3 <- select(iris, Petal.Length, Sepal.Length) # select petal and sepal lengths cols from iris and drop others
df4 <- select(iris, !Petal.Length) # drop petal length column
select(!Petal.Length & !Sepal.Length) # df clustering: Drop Petal and Sepal Lengths cols.



#@ EXPANDING
#* Manually
# Add the "dept" column.
emp.data$dept <- c("IT","Operations","IT","HR","Finance")

#* Add cols with cbind func
emp.data2 <- cbind(emp.data, gender=c('Male', 'Male', 'Female', 'Male', 'Male'))

#* Add rows with rbind func
# Multiple employees
emp.newdata <- 	data.frame(
   emp_id = c (6:8), 
   emp_name = c("Rasmi","Pranab","Tusar"),
   salary = c(578.0,722.5,632.8), 
   start_date = as.Date(c("2013-05-21","2013-07-30","2014-06-17")),
   dept = c("IT","Operations","Fianance"),
   stringsAsFactors = FALSE
)
# Bind the two data frames.
emp.finaldata <- rbind(emp.data,emp.newdata)



#@ CLEANING
#* Rename
iris <- iris %>% rename(sepalLength = Sepal.Length)

#* Change data types
str(iris) # check types
typeof(iris$species) # check single col
iris$species <- as.factor(iris$species)

#* Remove duplicates
#with duplicated()
df <- df[!duplicated(df$ID_Column_Name), ]
#with distinct()
df <- df %>% distinct(ID_Column_Name, .keep_all = TRUE)

#* Remove inconsistency
unique(df$gender) # check all unique values in gender
df$gender <- gsub("(?i)F|(?i)Female", "1", df$gender)
df$gender <- gsub("(?i)M|(?i)Male", "0", df$gender)

#* Handling outliers
#looking at number of values above 95th percentile 
sum(df$total_dx > quantile(df$total_dx, .95))
# The Winsorize func. In Winsorizing, values outside a predetermined percentile of the data are identified and set to said percentile.
df <- df %>% mutate(wins_total_dx = Winsorize(total_dx))

#* Handling missing values
sum(is.na(df)) # quickly check total number of null values in the dataset
# removing all observations with atleast 1 NA value
df_clean <- df %>% na.omit()
df <- df[!is.na(df)]
# using dplyr replace_na func
my_df %>% 
  mutate(x1 = replace_na(col1, mean(x1, na.rm = TRUE))) # replace col1 with its mean and update itself
# replace multiple cols with mutate_at func
my_df %>% 
  mutate_at(vars(col1, col2), ~replace_na(.,mean(., na.rm = TRUE))) 
# replace multiple cols given a condition with mutate_if func
my_df %>% 
  group_by(type) %>% 
  mutate_if(is.numeric, ~replace_na(., mean(., na.rm = TRUE))) # replace the missing values with the group’s mean in all (numeric) columns



#@ LAMBDA FUNC
myfunc <- function(height) {
    return (height-10)
}
(starwars %>%
	mutate(height = myfunc(height)))
