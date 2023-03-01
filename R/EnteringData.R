#@ COLON OPERATOR
#* Assigns number from x through y 
# Ascending order
x1 <- 0:10
# Descending order
x2 <- 10:0



#@ SEQUENCE FUNC
#* Ascending values
x3 <- seq(10) # duplicates 1:10
#* Descending values
x4 <- seq(10,0)
#* Specify change in values
x4 <- seq(30, 0, -3) # decrease from 30 to 0 by -3



#@ ENTER MULTIPLE VALUES WITH THE COMBINE/CONCAT/COLLECT FUNC
#* can take any data type
x5 <- c(5, 4, 1, 6, 7, 2, 2, 3, 2, 8)



#@ SCAN
#* Scan allows to collect data interactively through the console
x6 <- scan()
# After running this command, go to console. Hit return after each number to save it. Hit return twice to stop.



#@ REPEAT FUNC
#* Single values
x7 <- rep(TRUE, 5)
#* Repeats set
x8 <- rep(c(TRUE, FALSE), 5)
#* Repeats items in set
x9 <- rep(c(TRUE, FALSE), each = 5)

