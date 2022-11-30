# define "calc" function: counting string through evaluate(eval) function
def calc(user_expression):
    user_expression = input("Enter expression:\n")
    math_result = eval(str(user_expression))

    return print(f"{user_expression}={math_result}")


# asking user about his needs
# loop the calc function while user needs it. no need=break
# Removing errors: zerodivision, syntax, name
if __name__ == '__main__':
    user_start = input("Shall we calculate?(1 - yes; other - exit)\n")
    while user_start == "1" or user_start == "yes":
        user_math = None
        try:
            calc(user_math)
        except ZeroDivisionError:
            print(f"{user_math} Wrong entry. Try again.\n")
        except SyntaxError:
            print(f"{user_math} Wrong entry. Try again.\n")
        except NameError:
            print(f"{user_math} Wrong entry. Try again.\n")
        user_start = input("More calculations? (1 - yes; other - exit)\n")
    else:
        exit(print("Ok. Cya next time! :D "))
