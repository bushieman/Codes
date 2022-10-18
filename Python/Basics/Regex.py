import re

#* Identifiers
'/word/g' # match all instances of the word/characters in a given string
'/e+/g' # match atleast one e
'/ea?/g' # match e or e with a; a is optional i.e e, ea, ee
'/ea*/g' # match e or e with any given no of a i.e r, re, ree, reee
'/.at/g' # match anything with at i.e fat, cat, eat
'/\./g' # match the given character i.e . for this example
'/.\./g' # match the character before the period and the period i.e t.
'/\d=/g' # match any number
'/\D=/g' # match anything but a number
'/.=/g' # match anything but letters i.e periods
'/\b/g' # match any character except for new line
'/\w/g' # match any alphanumeric character
'/\W/g' # match anything but alphanumeric character
'/\s/g' # match any whitespace
'/\S/g' # match anything but whitespace
'/\w{4}/g' # match any words of 4 characters
'/\w{4,}/g' # match any words of 4 or more characters
'/\w{4,5}/g' # match any words between 4 and 5 characters
'/[fc]at/g' # match any characters inside the brackets with the characters outside i.e fat, cat
'/[a-z]at/g' # match any lower-case characters between a-z with the characters outside i.e fat, cat
'/[a-zA-Z]at/g' # match any characters between a-z(both lower & upper case) with the characters outside i.e fat, cat
'/[a-zA-Z0-9]at/g' # match any alpha-numeric character with the characters outside i.e fat, cat
'/(t|T)he/g' # match either the or The
'/(t|e|r){2,3}/g' # match either 2 or 3 combinations of the group i.e tweet can have a 3 combination group(twe) and a 2 combination group(et)
'/^T/g' # match T at the beginning of a whole statement
'/^T/gm' # match T at the beginning of each sentence i.e global multiline
'/*at\.$/g' # match the expression result at the end of a sentence

#* Modifiers
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324
'/\d[1,5]/g' # match any number between 1 and 5 i.e 452,324

#* methods
string = 'bush is a cool guy'

re.sub(pattern, repl, string)
re.match('pattern', string) # returns the index of the first instance of a match
re.split('pattern', string) # splits the string at the occurence of the pattern
re.sub('pattern', '', string) # substitute the pattern for the second string
re.findall('pattern', string) # return a list of all non-overlapping matches in the string
re.search('pattern', string) # scan through string looking for a match to the pattern, returning a match
