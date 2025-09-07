# This program will take the two features (# of rooms, year built) of a house 
# and predict it's value based on two points of data 


# x = features, y = value in millions of dollars
# features = [rooms, year built]

x1, x2 = [3, 2015], [5, 2023]    
y1, y2 = 0.8, 1.6

# we have two features so there will be two slopes (multi-feature slopes)
b0 = (y2 - y1)/(x2[0] - x1[0]) # slope for rooms
b1 = (y2 - y1)/(x2[1] - x1[1]) # slope for year built

# since we have two slopes and two features we will have two y-intercepts
a = y1 - (b0 * x1[0] + b1 * x1[1]) # multi-feature y-int

# linear regression formula  
x = [8, 2000] # two known features
y = a + (b0 * x[0]) + (b1 * x[1]) # y = predicted value of new house



# print formatted results
# a = multi-feature y-int, b = multi-feature slope, y = predicted value of new house
print("a: {}, b0: {}, b1: {}, y: {}".format(
    a, b0, b1, y
))

## In practice, however:
#  1. we'd be dealing with millions of sample data points, not just two.
#  2. some features will be more meaningful than others (we have no idea if the number
#  of rooms a house has will have the same impact on its value as the year it was built)
#  This just isn't something we can know based on so little data.
#  In my example, the rooms and year built have the same weight. here is what the linear
#  regression formula would look like if rooms were 3 times more impactful than year built
#  ( y = a + (b0 * x[0])*(3/4) + (b1 * x[1])*(1/4) )