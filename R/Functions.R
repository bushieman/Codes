#@ BASIC
my_function <- function() {
  print("Hello World!")
}

my_function() # call the function named my_function



#@ WITH ARGS
my_function <- function(fname) {
  paste(fname 'is a genius!')
}

my_function("Bushman")



#@ DEFAULT PARAMS
my_function <- function(country = "Norway") {
  paste("I am from", country)
}

my_function() # will get the default value, which is Norway



#@ RETURN
my_function <- function(x) {
  return (5 * x)
}

print(my_function(3))
