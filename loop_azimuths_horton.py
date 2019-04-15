# I am giving Todd Horton's loop azimuth video a spin. He is a great educator!
# https://www.youtube.com/watch?v=x3cAL1raSDY&t=842s
# I will write an interface for this eventually, when I need it for class.
# Written by Ryan Prasad. Contact: ryan@mysurveyhw.tv

import classes
import functions


angle_cd = classes.Angle("CD", 205, 27, 53)
angle_d = classes.Angle("D", 112, 54, 17)
angle_e = classes.Angle("E", 105, 41, 56)
angle_a = classes.Angle("A", 72, 32, 2)
angle_b = classes.Angle("B", 142, 26, 5)
angle_c = classes.Angle("C", 106, 25, 40)


print("Solved clockwise:")

print("CD")
print(angle_cd.degrees, angle_cd.minutes, angle_cd.seconds)

angle_de = functions.subtract_angles_ba(angle_cd, angle_d)
print("DE")
print(angle_de.degrees, angle_de.minutes, angle_de.seconds)

angle_ea = functions.subtract_angles_ba(angle_de, angle_e)
print("EA")
print(angle_ea.degrees, angle_ea.minutes, angle_ea.seconds)

angle_ab = functions.subtract_angles_ba(angle_ea, angle_a)
print("AB")
print(angle_ab.degrees, angle_ab.minutes, angle_ab.seconds)

angle_bc = functions.subtract_angles_ba(angle_ab, angle_b)
print("BC")
print(angle_bc.degrees, angle_bc.minutes, angle_bc.seconds)

check = functions.subtract_angles_ba(angle_bc, angle_c)
print("CHECK")
print(check.degrees, check.minutes, check.seconds)

print("Solved counterclockwise:")


angle_dc = angle_cd  # The back azimuth is already calculated from the previous computation
print("DC")
print(angle_dc.degrees, angle_dc.minutes, angle_dc.seconds)

angle_cb = functions.add_angles_ba(angle_dc, angle_c)
print("CB")
print(angle_cb.degrees, angle_cb.minutes, angle_cb.seconds)

angle_ba = functions.add_angles_ba(angle_cb, angle_b)
print("BA")
print(angle_ba.degrees, angle_ba.minutes, angle_ba.seconds)

angle_ae = functions.add_angles_ba(angle_ba, angle_a)
print("AE")
print(angle_ae.degrees, angle_ae.minutes, angle_ae.seconds)

angle_ed = functions.add_angles_ba(angle_ae, angle_e)
print("ED")
print(angle_ed.degrees, angle_ed.minutes, angle_ed.seconds)

check_ccw = functions.add_angles_ba(angle_ed, angle_d)
print("CHECK")
print(check_ccw.degrees, check_ccw.minutes, check_ccw.seconds)