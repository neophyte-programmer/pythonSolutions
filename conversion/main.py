rods_str = input("Input rods: ")
rods_float = float(rods_str)

# Constants
mile = 1609.34  # in meters
foot = 0.3048   # in meters

# Conversion Values
# e.g 1rod = meter_val = 5.0292 => 1 rod = 5.0292
meter_val = 5.0292
furlong_val = float(1/40)
mile_val = float(1 / (mile/meter_val))
feet_val = float(meter_val/foot)

# Conversion
meter_answer = rods_float * meter_val
furlong_answer = rods_float * furlong_val
mile_answer = rods_float * mile_val
feet_answer = rods_float * feet_val

# Rounded-Up Output
print("You input", rods_float, "rods")
print("Conversions")
print("Meters:", round(meter_answer, 3))
print("Feet:", round(feet_answer, 3))
print("Mile:", round(mile_answer, 3))
print("Furlongs:", round(furlong_answer, 3))
