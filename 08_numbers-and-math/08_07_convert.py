# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
a_int = 42
con_int_to_float = float(a_int)
print(a_int, "is a ", type(a_int))
print(con_int_to_float, "is a ",type(con_int_to_float))
# 2) Convert a float to an int
a_float = 5.5
print(a_float, "is a ", type(a_float))
con_float_to_int = int(a_float)
print(con_float_to_int, "is a ", type(con_float_to_int))
# 3) Perform division using a float and an int.
div_float_to_int = a_float / a_int
print(div_float_to_int)
# 4) Use two variables to perform a multiplication.
multiplication = a_int * a_float
print(multiplication)
# What information is lost during which conversions?
# when converting a float into an integer the value after the decimal point is lost.