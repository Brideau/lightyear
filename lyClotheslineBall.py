import math

n = 589900 #Number of layers of cable on the ball
lineThickness = 0.0035 #3.5mm, or the thickness of a clothesline
radSum = 0 # Used in the while loop below to keep track of the square of the radius of the ball

x = 0 #counter
while (x < n):
    rad = (0.12 + x*lineThickness)**2 # 12cm is the radius of a basket ball
    radSum += rad
    x += 1

length = 4*(math.pi**2)/lineThickness*radSum
print "The length of the cable in the ball is", math.floor(length), "meters, which is", math.floor(length)/1000, "kilometres.",

if length < 9454254955488000:
    print "This is shorter than a light year.\n\n"
else:
    print "This is longer than a light year.\n\n"
    
BallRad = n*lineThickness/1000

print "This ball would have a diameter of", 2*BallRad, "kilometres."