import math

# We imagine wrapping a basketball in clothesline with a length of 1 lightyear, where
# each layer of the ball is assumed to be uniformly covered by the clothesline.
# While there would normally be some parts of the ball growing faster in radius than
# others, we assume that compared to the size of the ball, and if spun randomly enough
# it would grow relatively uniform. At the very least, this will give a lower
# limit to how small the ball could be.
#
# The number of loops it takes to cover a layer = [circumference of layer]/[cable thickness]
# or 2*pi*[layer's distance from center]/thickness. The length of cable this represents would be
# [number of loops]*[length of each loop]=[2*pi*radius/thickness]*[2*pi*radius]=4*pi^2*radius^2/thickness
# Since the total length of the wire = length of layer 1 + length of layer 2 + ... + length of layer n
# we can write this as summation, where
# [Length of Layer n] = 4*pi^2/thickness*[initial radius + n*[cable thickness]]

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