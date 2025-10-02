# Real numbers in Python are represented using the float data type, which is based on the IEEE 754 double-precision binary floating-point format. This allows for a wide range of values, including very large and very small numbers, as well as special values like infinity and NaN (not a number).

import sys
from fractions import Fraction

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp : {ideal_temp}")
print(f"Current temp : {current_temp}")
print(f"difference between temp : {ideal_temp - current_temp}")
print(sys.float_info)
