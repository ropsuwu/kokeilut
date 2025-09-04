def get_season(month):
    if month == 12 or 1 <= month <= 2:
        return "The season is winter."
    elif 3 <= month <= 5:
        return "The season is spring."
    elif 6 <= month <= 8:
        return "The season is summer."
    elif 9 <= month <= 11:
        return "The season is autumn."
    return "Please enter a number between 1 and 12."

month = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {month}")
print(get_season(month))
