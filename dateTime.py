import datetime

x=datetime.datetime.now()
print(x)  # Output: Current date and time in the format YYYY-MM-DD HH:


t=datetime.datetime.now().year
print(t)  # Output: Current date and time in the format YYYY-MM-DD HH:MM:SS.mmmmmm


month=datetime.datetime.now().month
print(month)  # Output: Current month as an integer (1-12)


# Format code :
# %A -> Full weekday name
# %B -> Full month name
# %d -> Day of the month as a zero-padded decimal number (01-31)
# %Y -> Year with century as a decimal number
# %H -> Hour (24-hour clock) as a zero-padded decimal number (00-23)
# %M -> Minute as a zero-padded decimal number (00-59)
# %S -> Second as a zero-padded decimal number (00-59)

print(datetime.datetime.now().strftime("%A"))