print "Enter the radius of the circle"

pi = 3.14
radius = float(raw_input())

print "The radius is", radius

diameter = 2 * radius
print "The diameter is", diameter

print "The area is", pi * radius ** 2

print "The circumference is", pi * diameter

print "The sum of the circumference and area is", pi * radius ** 2 + pi * diameter

print "The difference between the circumference and area is", abs(pi * radius ** 2 - pi * diameter)

print "The circumference divided by diameter is", (pi * diameter) / diameter
