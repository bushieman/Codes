#@ DATA TYPES
#* Numeric
n1 <- 15  # Int; Double precision by default
typeof(n1)

n2 <- 1.5 # Float; Double precision
typeof(n2)

#* Character
c1 <- "c"
typeof(c1)

c2 <- "a string of text" # String: Character by default
typeof(c2)

# Logical
l1 <- TRUE
typeof(l1)

l2 <- F
typeof(l2)



#@ DATA STRUCTURES
#* Vector - 1D array
v1 <- c(1, 2, 3, 4, 5) # use the combine/concat function (c) to create vectors
is.vector(v1)

v2 <- c("a", "b", "c") # character vector
is.vector(v2)

v3 <- c(TRUE, TRUE, FALSE, FALSE, TRUE) # logical vector
is.vector(v3)

v4 <- c(TRUE, "a", 1, 0.5) # combination vector
is.vector(v3)

#* Matrix - 2D array
m1 <- matrix(c(T, T, F, F, T, F), nrow = 2)

m2 <- matrix(c("a", "b", 
               "c", "d"), 
               nrow = 2,
               byrow = T)
is.matrix(m2)

#* Array
# Give data, then dimemensions (rows, columns, tables)
a1 <- array(c( 1:24), c(4, 3, 2)) # both data and dimensions should be equal?

#* Data frame
# Can combine vectors of the same length
vNumeric   <- c(1, 2, 3)
vCharacter <- c("a", "b", "c")
vLogical   <- c(T, F, T)

# cbind for column bind to create data frames
df1 <- cbind(vNumeric, vCharacter, vLogical) # Makes a data frame of one data type: character by default

df2 <- as.data.frame(cbind(vNumeric, vCharacter, vLogical)) # Makes a data frame with three different data types

#* List
# 1D lists with combine func
o1 <- c(1, 2, 3)
o2 <- c("a", "b", "c", "d")
o3 <- c(T, F, T, T, F)
# 2D lists with list func
list1 <- list(o1, o2, o3)
# Nested lists
list2 <- list(o1, o2, o3, list1)  # Lists within lists!



#@ COERCING TYPES
#> This is changing from one data type or structure to another

#* Automatic coercions
# Goes to "least restrictive" data type i.e character type
coerce1 <- c(1, "b", TRUE)
typeof(coerce1)

# Coerce numeric to integer more specifically double type
coerce2 <- 5
typeof(coerce2)

#* Numeric to integer
coerce3 <- as.integer(5)
typeof(coerce3)

#* Character to numeric
coerce5 <- as.numeric(c("1", "2", "3"))
typeof(coerce5)

#* Matrix to data frame
coerce7 <- as.data.frame(matrix(1:9, nrow= 3))
typeof(coerce7)

#* Sequence to list
coerce8 <- as.list(seq(0:10, 2))
typeof(coerce8)

#* Character to factor
coerce9 <- as.factor(c('1', '2', '3')) # for categorical variables

#* Character to date
coerce10 <- as.Date(c("2012-01-01", "2013-09-23", "2014-11-15", "2014-05-11", "2015-03-27"))
