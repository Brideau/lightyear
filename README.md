lightyear
=========

We imagine wrapping a basketball in clothesline with a length of 1 lightyear, where
each layer of the ball is assumed to be uniformly covered by the clothesline.
While there would normally be some parts of the ball growing faster in radius than
others, we assume that compared to the size of the ball, and if spun randomly enough
it would grow relatively uniform. At the very least, this will give a lower
limit to how small the ball could be.

The number of loops it takes to cover a layer = [circumference of layer]/[cable thickness]
or 2*pi*[layer's distance from center]/thickness. The length of cable this represents would be
[number of loops]*[length of each loop]=[2*pi*radius/thickness]*[2*pi*radius]=4*pi^2*radius^2/thickness
Since the total length of the wire = length of layer 1 + length of layer 2 + ... + length of layer n
we can write this as summation, where
[Length of Layer n] = 4*pi^2/thickness*[initial radius + n*[cable thickness]]
