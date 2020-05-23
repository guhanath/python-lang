# write your function here
def readable_timedelta(no_of_days):
    no_of_weeks = int(no_of_days / 7)
    remaining_days = no_of_days % 7
    return "{} week(s) and {} day(s).".format(no_of_weeks, remaining_days)

# test your function
print(readable_timedelta(6))