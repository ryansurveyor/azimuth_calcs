import classes


def add_angles(angle1, angle2):
    # Initialize sum
    sum = classes.Angle("Sum", 0, 0, 0)

    # If sum of seconds is greater than 60, add 1 minute and subtract 60 seconds
    if angle1.seconds + angle2.seconds > 60:
        sum.minutes = 1
        sum.seconds = angle1.seconds + angle2.seconds - 60
    else:
        sum.seconds += angle1.seconds + angle2.seconds

    # If sum of minutes is greater than 60, add 1 degree and subtract 60 minutes
    if angle1.minutes + angle2.minutes > 60:
        sum.degrees = 1
        sum.minutes += angle1.minutes + angle2.minutes - 60
    else:
        sum.minutes += angle1.minutes + angle2.minutes

    # If sum is greater than 360 degrees, subtract 360
    if angle1.degrees + angle2.degrees + sum.degrees > 360:
        sum.degrees += angle1.degrees + angle2.degrees - 360
    else:
        sum.degrees += angle1.degrees + angle2.degrees

    return sum


def subtract_angles(angle1, angle2):
    # Initialize difference
    difference = classes.Angle("Difference", 0, 0, 0)

    # If difference of seconds is less than 0, subtract 1 minute and add 60 seconds
    if (angle1.seconds - angle2.seconds) < 0:
        difference.minutes = -1
        difference.seconds = (60 + angle1.seconds - angle2.seconds)
    else:
        difference.seconds = (angle1.seconds - angle2.seconds)

    # If difference of minutes is less than 0, subtract 1 degree and add 60 minutes
    if (angle1.minutes - angle2.minutes + difference.minutes) < 0:
        difference.degrees = -1
        difference.minutes += (60 + angle1.minutes - angle2.minutes)
    else:
        difference.minutes += (angle1.minutes - angle2.minutes)

    # If difference is less than 0 degrees, add 360
    if (angle1.degrees - angle2.degrees + difference.degrees) < 0:
        difference.degrees += (360 + angle1.degrees - angle2.degrees)
    else:
        difference.degrees += (angle1.degrees - angle2.degrees)

    return difference


# Subtract angles using back azimuth


def subtract_angles_ba(angle1, angle2):
    # Initialize difference
    difference = classes.Angle("Difference", 0, 0, 0)
    angle1.degrees -= 180  #...

    # If difference of seconds is less than 0, subtract 1 minute and add 60 seconds
    if (angle1.seconds - angle2.seconds) < 0:
        difference.minutes = -1
        difference.seconds = (60 + angle1.seconds - angle2.seconds)
    else:
        difference.seconds = (angle1.seconds - angle2.seconds)

    # If difference of minutes is less than 0, subtract 1 degree and add 60 minutes
    if (angle1.minutes - angle2.minutes + difference.minutes) < 0:
        difference.degrees = -1
        difference.minutes += (60 + angle1.minutes - angle2.minutes)
    else:
        difference.minutes += (angle1.minutes - angle2.minutes)

    # If difference is less than 0 degrees, add 360
    if (angle1.degrees - angle2.degrees + difference.degrees) < 0:
        difference.degrees += (360 + angle1.degrees - angle2.degrees)
    else:
        difference.degrees += (angle1.degrees - angle2.degrees)

    return difference


# Add angles using back azimuth

def add_angles_ba(angle1, angle2):
    # Initialize sum
    sum = classes.Angle("Sum", 0, 0, 0)
    angle1.degrees += 180  # Same deal...

    # If sum of seconds is greater than 60, add 1 minute and subtract 60 seconds
    if angle1.seconds + angle2.seconds > 60:
        sum.minutes = 1
        sum.seconds = angle1.seconds + angle2.seconds - 60
    else:
        sum.seconds += angle1.seconds + angle2.seconds

    # If sum of minutes is greater than 60, add 1 degree and subtract 60 minutes
    if angle1.minutes + angle2.minutes > 60:
        sum.degrees = 1
        sum.minutes += angle1.minutes + angle2.minutes - 60
    else:
        sum.minutes += angle1.minutes + angle2.minutes

    # If sum is greater than 360 degrees, subtract 360
    if angle1.degrees + angle2.degrees + sum.degrees > 360:
        sum.degrees += angle1.degrees + angle2.degrees - 360
    else:
        sum.degrees += angle1.degrees + angle2.degrees

    return sum
