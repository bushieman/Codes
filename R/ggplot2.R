suppressPackageStartupMessages(library(tidyverse))
install.packages('showtext') # for font_add and showtext_auto funcs
install.packages("maps")
install.packages("gridExtra") # for grid,arrange func
install.packages("ggpmisc")
install.packages("scales")
install.packages("igraph")
install.packages("grid")
install.packages('showtextdb')
install.packages('sysfonts')
library(tidyverse)
library(showtext) 
library(ggpmisc)
library(scales)
library(igraph)
library(lubridate)
library(gridExtra)
library(grid)

# Loading csv files
messages <- readr::read_csv('Data/messages.csv', show_col_types = FALSE)
employees <- readr::read_csv('Data/employees.csv', show_col_types = FALSE)
doctors <- readr::read_csv('Data/doctors.csv', show_col_types = FALSE)
orders <- readr::read_csv('Data/orders.csv', show_col_types = FALSE)
complaints <- readr::read_csv('Data/complaints.csv', show_col_types = FALSE)
instructions <- readr::read_csv('Data/instructions.csv', show_col_types = FALSE)



#@ PLOT 1
messageLocation <- messages %>%
 	left_join(employees, by=c('sender'='id')) %>%
 	rename(locationSent=location) %>%
 	left_join(employees, by=c('receiver'='id')) %>%
 	rename(locationReceived=location) %>%
 	select(locationSent, locationReceived)

options(repr.plot.width=10, repr.plot.height=8) # scale the desired window size

font_add(family='comic', regular='Comic_Sans_MS.ttf') # add custom fonts
showtext_auto() # show the fonts
(plot1 <- messageLocation %>%
	count(locationReceived, locationSent) %>% # count for each locationreceived a unique locationsent
 	group_by(locationSent) %>%
    mutate(pct = round(n / sum(n),2)) %>% # perform math computations on numerical variables
 	ggplot(aes(y = locationSent, x = pct, fill = locationReceived, label = paste0(locationReceived,' ',pct*100,'%'))) + # paste0 avoids using the sep=' ' option
 	geom_col(width = 0.5, position = position_dodge(0.7), alpha = 0.6, show.legend = FALSE) + # position_dodge for spacing between the categories
    geom_text(width = 0.5, position = position_dodge(0.7), hjust = -0.4, vjust = 0.5, size = 5, family='comic',  color = '#333232') + # hjust and vjust for adjusting the positioning of the text
 	scale_x_continuous(labels = percent, limits = c(0,0.6)) + # defining your scales. You can include custom breakpoints
 	theme_minimal() +
	xlab('% Messages sent to') + 
 	ylab('Messages sent from') +
 	ggtitle('Fig_3: Proportion of messages sent by a branch to other branches') +
 	scale_fill_brewer(palette="Dark2") + # apply themes on Data portions of the plot
 	theme(plot.title=element_text(family='comic', size = 20,  hjust=0.2, color = '#333232'), # apply themes on non-Data portions of the plot
        
        axis.text.x = element_text(family='comic', size = 15, color = '#333232'),
        axis.text.y = element_text(family='comic', size = 15, color = '#333232'),
        axis.title.x = element_text(family='comic', size = 18, color = '#333232'),
        axis.title.y = element_text(family='comic', size = 18, color = '#333232'),
        axis.ticks.x = element_blank()
  	) + 
   	annotate("curve", x = 0.5, y = 4.6, xend = 0.35, yend = 4.95, arrow = arrow(length = unit(0.3, "cm"), type = "closed"), color = "grey") + 
 	annotate("text", x = 0.5, y = 4.6, label =  " e.g. 27% of all mesages sent from \n US goes to France", vjust = 1, size = 5, color = "grey", family='comic')
)



#@ PLOT 2
df1 <- doctors %>%
	select('Region', 'Category')

df1$Category <- as.factor(df1$Category)
df1$Region <- as.factor(df1$Region)

options(repr.plot.width=10, repr.plot.height=9) # Defining the plot area

# use custom fonts
font_add(family='comic', regular='Comic_Sans_MS.ttf')
showtext_auto()

(plot2 <- ggplot(df1, aes(y = fct_rev(fct_infreq(Region)), fill=Category)) + # use fct_infreq to reorder from highest to lowest frequency and then fct_rev to reverse the order
	geom_bar(alpha=0.9, show.legend = TRUE, width=0.6) + # width adjusts the spacing between the samples, ~1 are very tighly packed
 	scale_x_continuous(limits = c(0,35), breaks = seq(0,35,5)) +
 	theme_minimal() +
	xlab('Total no of doctors per category in each region') + 
 	ggtitle('Fig_1: Number of doctors per region & their average number of purchases') + 
 	scale_fill_brewer(palette="Paired") + 
 	theme(plot.title=element_text(family='comic', size = 20,  hjust=-0.3, color = '#333232'),
        axis.text.x = element_text(family='comic', size = 15, color = '#323232'),
        axis.text.y = element_text(family='comic', size = 15, color = '#323232'),
        axis.title.x = element_text(family='comic', size = 18, color = '#323232'),
        axis.title.y = element_blank(),
        axis.ticks.x = element_blank(),
        panel.grid.major.x = element_line(size=1),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
          
        # legend features
        legend.title = element_blank(),
        legend.text = element_text(family='comic', size=17, color='#323232'), 
    	legend.text.align = 0, # 0 (left) to 1 (right)
    	# legend.margin = margin(0.1, 0.1, 0.2, 0.2, "cm"), # create a legend margin
   		legend.background = element_rect(fill='white', color = NA), # color=NA to remove the border
        legend.key.size = unit(0.7, "cm"), # the size of each legend key. Same as both legend.key.height and legend.key.width
        legend.spacing.y = unit(0.4, 'cm'), # create a padding for each legend key on the y axis. Dependent on byrow=TRUE 
        legend.key.height = unit(0.7, 'cm'), #change legend key height
        legend.key.width = unit(0.7, 'cm'), # change legend key width 
        legend.margin = margin(0, -2, 0.5, 0.5, 'cm'),
      	# legend.spacing.x = unit(1.9, "mm"),
     	legend.position=c(.8,.75) # the positions are relative to the whole plot size ie 0.5 is in the middle
  	) + 
	guides(fill = guide_legend(byrow = TRUE)) + 
    geom_label(aes(x = 35, y = 6, label = stringr::str_wrap("There seems to be a relationship between doctor's category and the number of purchases. The regions which have general practitioners as their sole customers, tend to have lower average of purchases.", 50)), size = 6, color = "black", family='comic', fill='white', label.size=NA, hjust=1, lineheight = 0.8, fontface = "italic",  label.padding=unit(1, "lines")) # str_wrap with a set width to wrap our long text, label.size=NA to remove text borders and hjust=1 for right_justified, fill for background color, lineheight for spacing between lines, label.padding to create some margin around the borders
)

# The width value controls the spacing between clusters while the position_dodge() value controls the spacing between bars within the same cluster.
# You can also use the annotate func for annotation by setting the geom to label: annotate(geom='label' x = 3.5, y = 3, label = "Text Over Line", fill = "yellow", label.size=NA, label.padding=......)
# hjust stands for horizontal justification, hjust=0 will be left-justified, 0.5 will be centered, and 1 will be right-justified. Similar case with vjust=0 for top, 0.5 for middle and 1 for bottom.



#@ PLOT 3
options(repr.plot.width=10, repr.plot.height=12)

font_add(family='comic', regular='Comic_Sans_MS.ttf')
showtext_auto()

mean_value = mean <- as.double(doctors %>%
	summarise(mean(Purchases)))

(plot3 <- doctors %>%
	select(Region, Purchases) %>%
	group_by(Region) %>%
 	summarise(mean = mean(Purchases)) %>% # if you do summarise without grouping first you get the results for the whole dataset
 	subset(Region!="1 19 20") %>% # drop the outlier region '1 19 20'
 	ggplot(aes(x=mean, y = fct_rev(fct_infreq(Region)), label=paste0(round(mean, 0)))) + # use fct_infreq to reorder from highest to lowest frequency and then fct_rev to reverse the order
	geom_col(alpha=0.9, show.legend = TRUE, width=0.6, fill='#03C0C1') + # width adjusts the spacing between the samples, ~1 are very tighly packed
 	geom_text(width = 0.5, hjust = -0.8, vjust = 0.5, size = 5, family='comic',  color = 'white') +
 	# scale_x_continuous(limits = c(0,30), breaks = seq(0,30,5)) +
 	theme_minimal() +
	xlab('Average no of purchases per region in the last year.') + 
 	ggtitle('Fig_1: Number of doctors per region & their average number of purchases.') + 
 	# scale_fill_brewer(palette="Greens") +
 	theme(plot.title=element_text(family='comic', size = 20,  hjust=0.3, color = '#333232'),
        axis.text.x = element_text(family='comic', size = 15, color = '#323232'),
        axis.text.y = element_text(family='comic', size = 15, color = '#323232'),
        axis.title.x = element_text(family='comic', size = 18, color = '#323232'),
        axis.title.y = element_blank(),
        axis.ticks.x = element_blank(),
        panel.grid.major.x = element_line(size=1),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank()
       ) +
 	scale_x_reverse(limits = c(30,0), breaks=seq(0,30,5)) + # reverse the order of values on the x axis. You need to change the limits to be reversed but the breaks are the same
  	# scale_y_reverse()
 	geom_vline(xintercept = mean_value, color="#f8a278", linetype='longdash') + # add a mean line
	 annotate("curve", x = 10.8, y = 10, xend = 16, yend = 15, arrow = arrow(length = unit(0.5, "cm"), type = "closed"), color = "grey") +
 	annotate("text", x = 19, y = 15.4, label =  "mean purchases", vjust = 1, size = 7, color = "grey", family='comic') # make sure you put the text near the curve ends
 )


# geom_bar() makes the height of the bar proportional to the number of cases in each group (or if the weight aesthetic is supplied, the sum of the weights).
# If you want the heights of the bars to represent values in the Data, use geom_col() instead.
# geom_bar() uses stat_count() by default: it counts the number of cases at each x position. geom_col() uses stat_identity(): it leaves the Data as is.



#@ PLOT 4
doclist <- unique(as.list(doctors$DoctorID))

options(repr.plot.width=13, repr.plot.height=4)
df4 <- complaints %>%
 	rename(ComplaintType='Complaint Type') %>%
	subset(DoctorID %in% doclist) %>%
 	group_by(ComplaintType) %>%
 	summarise(sum = sum(Qty)) %>%
 	subset(!ComplaintType=='R&R')

plot4 <- ggplot(df4, aes(x=fct_reorder(ComplaintType, sum, .desc = TRUE), y=sum, label=paste0(sum))) + # sometimes using summarise might affect the fct_infreq thus opt for fct_reorder func
 	geom_col(width=0.8, fill='#03C0C1') +
 	geom_text(width = 0.5, hjust = 0.5, vjust=-0.3, size = 5, family='comic',  color = '#323232') +
	theme_minimal() +
 	# labs func
 	labs(
    	x='Complaint types',
        y='Count',
        title= expression("Figure 2."~'Complaint types frequency')
    ) +
 	scale_y_continuous(limits = c(0,150), breaks = seq(0,140,20)) +
 	theme(plot.title=element_text(family='comic', size = 20,  hjust=0.3, color = '#333232'),
        axis.text.x = element_text(family='comic', size = 15, color = '#323232'),
        axis.text.y = element_text(family='comic', size = 15, color = '#323232'),
        axis.title.x = element_text(family='comic', size = 18, color = '#323232'),
        axis.title.y = element_text(family='comic', size = 18, color = '#323232'),
        axis.ticks.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
       ) +
 	geom_hline(yintercept=0, color='grey') # create a baseline at the bottom

grid.arrange(plot4, plot4, nrow = 1) # create subplots. Note: all plots share the same size defined by the options function



#@ PLOT 5
nmonths = 24
x = seq(as.Date("2015/1/1"), by = "month", length.out = nmonths)
df1 <- data.frame(dates = x,Variable = rnorm(mean = 0.75,nmonths))
df2 <- data.frame(dates = x,Variable = rnorm(mean = -0.75,nmonths))

df3 <- df1 %>%  mutate(Type = 'Amocycillin') %>%
       bind_rows(df2 %>%
           mutate(Type = 'Penicillin'))

df4 <- subset(df3, Type == 'Amocycillin')
df5 <- subset(df3, Type == 'Penicillin')
options(repr.plot.width=13, repr.plot.height=6)
(plot5 <- ggplot() + 
  geom_line(data=df4, aes(x=dates, y=Variable), color='#03C0C1', linetype='dashed', size=2) + # use different lines to allow for individual customization
  geom_line(data=df5, aes(x=dates, y=Variable), color='#673147', size=2) + 
  theme_minimal() +
  # labs func
  labs(
     x='Dates',
     y='% Change',
     title= expression("Figure 3."~'% Change of bacteria mutations.')
  ) +
  scale_y_continuous(limits = c(-4,4), breaks = seq(-4,4,2)) +
  theme(plot.title=element_text(family='comic', size = 30,  hjust=0.4, color = '#333232'),
      axis.text.x = element_text(family='comic', size = 20, color = '#323232'),
      axis.text.y = element_text(family='comic', size = 20, color = '#323232'),
      axis.title.x = element_text(family='comic', size = 25, color = '#323232'),
      axis.title.y = element_text(family='comic', size = 25, color = '#323232'),
      axis.ticks.x = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.minor.x = element_blank(),
      panel.grid.major.y = element_blank(),
      panel.grid.minor.y = element_blank(),
   ) +
 geom_hline(yintercept=-4, color='grey', size=2) # create a baseline at the bottom
) 



#@ PLOT 6
options(repr.plot.width=7, repr.plot.height=4)

font_add(family='comic', regular='Comic_Sans_MS.ttf') # add custom fonts
showtext_auto() # show the fonts

employeesTotal <- employees %>%
  mutate(department = 'Total') %>%
  group_by(department) %>%
  summarize(employeesNumber = n())

employeesDepartments <- employees %>%
  group_by(department) %>%
  summarize(employeesNumber = n())

employeesMap <- rbind(employeesDepartments, employeesTotal)

employeesMap <- employeesMap %>%
  mutate(employeesPerc = round(employeesNumber/employeesTotal$employeesNumber,2), employeesPerc = percent(employeesPerc))
  

funEmployees <- function(country) { 
  
  employeesTotalCountry <- employees %>%
    filter(location == country) %>%
    mutate(department = 'Total') %>%
    group_by(department) %>%
    summarize(employeesNoCountry = n())
  
  employeesDepartmentsCountry <- employees %>%
    filter(location == country) %>%
    group_by(department) %>%
    summarize(employeesNoCountry = n())
  
  employeesMapCountry <- rbind(employeesDepartmentsCountry, employeesTotalCountry)
  
  employeesMapCountry <- employeesMapCountry %>%
    mutate(employeesPercCountry = round(employeesNoCountry/employeesTotalCountry$employeesNoCountry,2), employeesPercCountry = percent(employeesPercCountry))
  
  colName <- paste0(country,' depts')
  
  employeesMapCountry <- employeesMap %>%
    left_join(employeesMapCountry, by = 'department') %>%
    select(department, employeesNoCountry, employeesPercCountry) %>%
    rename(!!country := department,
           count = employeesNoCountry, 
           perc = employeesPercCountry
    )  
  employeesMapCountry
}

thismap = map_data("world")
thismap <- mutate(thismap, fill = ifelse(region %in% c('UK','Germany',"Brazil", "France", "USA")
                                         ,"brown", "white"))

thismap <- thismap %>%
  mutate(fill1 = case_when(region == 'UK' ~ 'red',
                           region == 'Germany' ~ 'orange',
                           region == 'France' ~ 'slategray',
                           region == 'USA' ~ 'navy',
                           region == 'Brazil' ~ 'green',
                           FALSE ~ 'white'))

(plot6 <- ggplot(thismap, aes(long, lat, fill = fill1, group=group)) + 
  geom_polygon(alpha = 0.6, colour="#ebe9f2") + 
  scale_fill_identity() +
  theme_minimal() +
  ggtitle('Fig_1: Number of employees in departments') +
     theme(plot.title=element_text(size = 10,  hjust=0.5, color = '#333232'))+

  annotate(geom = 'rect', fill = "orange", alpha = 0.3, 
           xmin=45+10, ymin=45-3,
           xmax=68*1.8+5, ymax=100+3) +
  annotate(geom = 'table', color = "black", alpha = 0.8, size = 2,
           table.theme = ttheme_gtminimal,
           family='comic',
           x=125, y=100,
           label=list(funEmployees('Germany'))) +
  annotate("curve", x = 13, y = 52,
           xend = 60, yend = 56,
           arrow = arrow(length = unit(0.2, "cm"), type = "closed"),
           color = "orange") +
  
  annotate(geom = 'rect', fill = "slategray", alpha = 0.2, 
           xmin=95-60+1, ymin=-40+3-17,
           xmax=173-70+1, ymax=20+3-16)+
  annotate(geom = 'table', color = "black", alpha = 0.8, size = 2,
           table.theme = ttheme_gtminimal,
           family='comic',
           x=173-70, y=-50,
           label=list(funEmployees('France'))) +
  annotate("curve", x = 3, y = 48,
           xend = 30, yend = 0,
           arrow = arrow(length = unit(0.2, "cm"), type = "closed"),
           color = "grey") +
  
  annotate(geom = 'rect', fill = "red", alpha = 0.2,
           xmin=-80, ymin=50-2,
           xmax=-7, ymax=105+2)+
  annotate(geom = 'table', color = "black", alpha = 0.8, size = 2,
           table.theme = ttheme_gtminimal,
           family='comic',
           x=-80, y=105,
           label=list(funEmployees('UK')))  +
  annotate("curve", x = -2, y = 53,
           xend = -5, yend = 65,
           arrow = arrow(length = unit(0.2, "cm"), type = "closed"),
           color = "red") +
  
  annotate(geom = 'rect', fill = "navy", alpha = 0.6,
           xmin=-220+35, ymin=30-60,
           xmax=-145+35, ymax=35)+
  annotate(geom = 'table', color = "black", alpha = 0.8, size = 2,
           table.theme = ttheme_gtminimal,
           family='comic',
           x=-220+40, y=30,
           label=list(funEmployees('US'))) +
  
  annotate(geom = 'rect', fill = "green", alpha = 0.2,
           xmin=-68, ymin =-25,
           xmax=34-35, ymax =-85)+
  annotate(geom = 'table', color = "black", alpha = 0.8, size = 2,
           table.theme= ttheme_gtminimal,
           family='comic',
           x=-68, y=-83,
           label=list(funEmployees('Brasil'))) +
  
  theme(plot.title=element_text(family='comic', size = 20,  hjust=0.2, color = '#333232'),    
        axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.title.x = element_blank(),
        axis.title.y = element_blank(),
        axis.ticks.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.y = element_blank(),
        panel.grid.minor.y = element_blank(),
  	)
)



#@ PLOT 7
options(repr.plot.width=7, repr.plot.height=6)

font_add(family='comic', regular='Comic_Sans_MS.ttf') # add custom fonts
showtext_auto() # show the fonts

employeesCount <- employees %>%
  mutate(flag = 1) %>%
  group_by(location, department) %>%
  summarise(employeesNo = sum(flag))

messagesSentSum <- messages %>%
  mutate(flag = 1, message= 'sent') %>%
  left_join(employees, by = c('sender' = 'id')) %>%
  group_by(message, location, department) %>%
  summarise(messagesSent = sum(flag))

messagesReceivedSum <- messages %>%
  mutate(flag = 1, message= 'received') %>%
  left_join(employees, by = c('receiver' = 'id')) %>%
  group_by(message, location, department) %>%
  summarise(messagesSent = sum(flag))

messagesSum <- rbind(messagesSentSum , messagesReceivedSum)

(plot7 <-employeesCount %>%
  left_join(messagesSum, by = c('department','location')) %>%
  mutate(messagesSent = replace_na(messagesSent, 0)) %>%
  mutate(messagesSentPerEmployee = round(messagesSent / employeesNo,1)) %>%
  mutate(message = factor(message,levels = c("sent","received"))) %>%
  ggplot(aes(x = department, y = location, size = messagesSentPerEmployee,
             group = message,  
             label = messagesSentPerEmployee)) +
  scale_size(range = c(.1, 15)) +
  geom_point(aes(color = message), position = position_dodge(width = 0.7), alpha = 0.5) +
  geom_text(position = position_dodge(width = 0.7),show.legend = FALSE, size = 3, vjust = 0.4, family='comic') +
  theme_minimal() +
  xlab('') +
  ylab('') +
  ggtitle('Fig_2: Number of messages sent / received per employee') +
  theme(plot.title=element_text(size = 20,  hjust=0.6, color = '#333232', family='comic'),
        legend.position="top",
        axis.text.x = element_text(family='comic', size = 15, color = '#333232'),
        axis.text.y = element_text(family='comic', size = 15, color = '#333232'),
        axis.title.x = element_text(family='comic', size = 18, color = '#333232'),
        axis.title.y = element_text(family='comic', size = 18, color = '#333232'),
        axis.ticks.x = element_blank(),
        legend.title = element_blank(),
        legend.text = element_text(family='comic', size=18, color='#323232')
       ) + 
  guides(size = FALSE) +
  scale_color_manual(values = c("received" = "black", "sent" = "red"))
)
