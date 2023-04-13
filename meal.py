def convert(time):
    """Converts a string in 24-hour format to a float representing the number of hours"""
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


def main():
    # Define the time ranges for each meal
    breakfast_start, breakfast_end = 6, 10
    lunch_start, lunch_end = 12, 14
    dinner_start, dinner_end = 18, 20

    # Prompt the user for a time
    time_str = input("Enter a time in 24-hour format (hh:mm): ")

    # Convert the time string to a float representing the number of hours
    time = convert(time_str)

    # Determine which meal (if any) the time falls within and output a message
    if breakfast_start <= time < breakfast_end:
        print("It's breakfast time!")
    elif lunch_start <= time < lunch_end:
        print("It's lunch time!")
    elif dinner_start <= time < dinner_end:
        print("It's dinner time!")