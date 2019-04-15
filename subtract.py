# Don't try to break me! I am merely written to save time on survey exams.
# Written by Ryan Prasad. Contact: ryan@mysurveyhw.tv

import classes
import functions

# Prompt user for two angles
print("Subtract angles")

angle1 = classes.Angle(input("Enter angle #1 name: "), int(input("Enter angle #1 degrees: ")),
                       int(input("Enter angle #1 minutes: ")), int(input("Enter angle #1 seconds: ")))
angle2 = classes.Angle(input("Enter angle #2 name: "), int(input("Enter angle #2 degrees: ")),
                       int(input("Enter angle #2 minutes: ")), int(input("Enter angle #2 seconds: ")))

# Subtract the angles
difference = functions.subtract_angles(angle1, angle2)

# Print output to console
print(angle1.name + " -", angle2.name + " =")
print(difference.degrees, difference.minutes, difference.seconds)