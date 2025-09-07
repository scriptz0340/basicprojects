# given data points
x1, x2 = 3, 4
y1, y2 = 2, 4

# calculate slope
b = (y2 - y1)/(x2 - x1) 


# calculate y-int
a = y1 - (b * x1) 

# linear regression formula (x can be any number)
x = 6 
y = a + (b*x)

# print formatted results
print("a:{}, b:{}, y:{}".format(
    a, b, y
))