# Scope dependes where you createing the variable

# This scope respect the LEGB order, first local, enclosed, global and built-in.

def func_one():
 #   x = 1
    print(x)

x = 10

func_one()