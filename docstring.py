def readable_timedelta(days):
    '''function to calculate weeks and days for input number of days
    INPUT: no of days
    OUTPUT: string
    '''

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)

name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))