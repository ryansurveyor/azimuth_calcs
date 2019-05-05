# My Python solution to Todd Horton's Traverse angle adjustment video
# https://www.youtube.com/watch?v=3JoIkovf0e0&t=241s
# Written by Ryan Prasad on a rainy 5/5/19. Email: contact@mysurveyhw.tv

import classes
import functions


# Exercise angles hard coded:
angle_ab = classes.Angle("AB", 94, 16, 27)
angle_a = classes.Angle("A", 89, 35, 50)
angle_b = classes.Angle("B", 56, 51, 51)
angle_c = classes.Angle("C", 233, 38, 51)
angle_d = classes.Angle("D", 64, 57, 52)
angle_e = classes.Angle("E", 94, 55, 15)

# Create a list containing interior angles
interior_angles = [angle_a, angle_b, angle_c, angle_d, angle_e]

# Initialize an angle at 0 for the following operation
sum_interior = classes.Angle("ZZZ", 0, 0, 0)

# Sum the interior angles
for angle in interior_angles:
    sum_interior = functions.add_angles_raw(sum_interior, angle)

print("Sum of interior angles:")
print(sum_interior.degrees, sum_interior.minutes, sum_interior.seconds)
print()

# Calculate the sum of angles of a perfect polygon
sum_perfect_int = (len(interior_angles) - 2) * 180
sum_perfect = classes.Angle("Sum of interior angles of a perfect polygon: ", sum_perfect_int, 0, 0)
print(sum_perfect.name)
print(sum_perfect.degrees, sum_perfect.minutes, sum_perfect.seconds)
print()

# Calculate the difference between the two sums. Subtract the interior angles from the perfect polygon,
# then flip the sign.
error = functions.subtract_angles(sum_perfect, sum_interior)
error.degrees *= -1
error.minutes *= -1
error.seconds *= -1

print("Error:")
print(error.degrees, error.minutes, error.seconds)
print()

# For the purposes of this problem, I am only doing work on the seconds part of the error

# Divide error by the number of interior angles
# Floor division rounds towards negative infinity, so add 1
print("Distributing the following among all interior angles for adjustment:")
adjustment = error.seconds // len(interior_angles) + 1
print(adjustment)

# The remainder is
# Modulo is picky about the divisor, so I swapped signs
print("Tacking on the remainder to the first interior angle:")
adjustment_last = error.seconds % (len(interior_angles) * -1)
print(adjustment_last)
print()

# Apply remainder to first interior angle. Swap sign.
interior_angles[0].seconds += (adjustment_last * -1)

print("Adjusted angles are as follows:")

# Apply adjustment to interior angles. Swap signs again.
for angle in interior_angles:
    angle.seconds += (adjustment * -1)
    print(angle.name, angle.degrees, angle.minutes, angle.seconds)

# Zero out the sum variable for reuse
sum_interior = classes.Angle("ZZZ", 0, 0, 0)

# Sum the interior angles
for angle in interior_angles:
    sum_interior = functions.add_angles_raw(sum_interior, angle)
print()

print("New sum of interior angles:")
print(sum_interior.degrees, sum_interior.minutes, sum_interior.seconds)
print()

# Compare adjusted angles to the perfect polygon
if sum_interior.degrees == sum_perfect.degrees and sum_interior.minutes == sum_perfect.minutes and \
        sum_interior.seconds == sum_perfect.seconds:
    print("Adjustment applied correctly.")
else:
    print("Adjustment incorrect.")
    sys.exit()

print()

print("Known exterior angle:")
print(angle_ab.degrees, angle_ab.minutes, angle_ab.seconds)
print()

# Start off the azimuth loop
print("Proceeding around the loop CCW from the known exterior angle:")
bc = functions.add_angles_ba(angle_ab, interior_angles[1])
print(bc.degrees, bc.minutes, bc.seconds)

dummy = bc

# Calculate the three remaining exterior azimuths
for i in range(3):
    dummy = functions.add_angles_ba(dummy, interior_angles[i+2])
    print(dummy.degrees, dummy.minutes, dummy.seconds)

# Check
print()
print("CHECK")
check = functions.add_angles_ba(dummy, interior_angles[0])
print(check.degrees, check.minutes, check.seconds)

