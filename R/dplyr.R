# Dplyr is a data manipulation package that is part of the tidyverse,
# Dplyr leverages the pipe (%>%) structure, a better way to encapsulate functions.

# Install Dplyr - You can also install via tidyverse
install.packages('dplyr')
# Loading the library
library(dplyr)



#@ FILTER 
# Filter rows from dataframes using one or multiple conditions.
#* Single condition
(filter_droids <- starwars %>%
  filter(species == 'Droid'))

#* Multiple conditions
(filter_droids_gold <- starwars %>%
 filter(species == 'Droid', skin_color == 'gold'))



#@ ARRANGE
# Arrange sorts our table according to specific columns. 
#* Ascending order
(sorted_height <- starwars %>%
 arrange(height))

#* Descending order
(reverse_sorted_height <- starwars %>%
 arrange(-height))

#* Sort by Multiple cols
(sorted_hair_height <- starwars %>%
 arrange(hair_color, height)) # first by hair color alphabetically then by height numerically



#@ MUTATE
# Mutate is a cool function to add new columns to a table.
#* Single col
(starwars_df <- starwars %>%
  mutate(height_x_mass = height*mass))

#* Multiple cols
(starwars_df <- starwars %>%
 mutate(height_x_mass = height*mass,
 franchise = 'Star Wars'))



#@ SAMPLE
#* Sample_n n number of samples
(starwars_sample_n <- starwars %>%
  sample_n(size=5))

#* Sample_frac - fraction of the dataset
(starwars_sample_frac <- starwars %>%
 sample_frac(0.01))



#@ DUPLICATES
# Remove duplicates in the ID col
df <- df %>% distinct(ID_Column_Name, .keep_all = TRUE)



#@ SUMMARISE
#* Mean
starwars %>%
 summarise(height_mean = mean(height, na.rm = TRUE)) # remove null values then perform mean

#* Max
starwars %>%
 summarise(height_max = max(height, na.rm = TRUE)) # get the max height - Note: Null values affect max height

#* With group_by func
mean_height_by_species <- starwars %>%
 group_by(species) %>% # first perform the grouping 
 summarise(height_mean = mean(height, na.rm = TRUE)) # then summarise



#@ Inner, Left and Right Join
#* Inner join
# Inner_join returns rows where the key is in both dataframes.
species_origin <-data.frame(species=c('Human', 'Ewok'), origin=c('Earth', 'Endor'))
(starwars_inner <- starwars %>%
 inner_join(species_origin, by='species')) # all other species in starwars not in species_origin are dropped

#* Left join
# Left_join returns NA values where a key is not in both dataframes therefore all rows in main table are returned
starwars_left <- starwars %>%
 left_join(species_origin, on=’Species’)

#* Right join
# Same as left join. However the main table is the one stated in the first argument of the function — species_origin .
(starwars_right <- starwars %>%
 right_join(species_origin, on=’Species’))
