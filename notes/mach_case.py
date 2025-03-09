# Mach-case statement (switch): Alternative to using maniy "elif". More Cleaner and readable.

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case _:
            return False
print(is_weekend("Monday"))