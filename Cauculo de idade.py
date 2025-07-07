import datetime

def calculate_age_in_days(birth_year):
    """
    Calculates a person's age in days based on their birth year.

    Args:
        birth_year (int): The year of birth (e.g., 1990).

    Returns:
        int: The age in days. Returns -1 if the birth year is in the future.
    """
    current_date = datetime.date.today()
    birth_date = datetime.date(birth_year, 1, 1)  # Assuming Jan 1st for simplicity

    if birth_date > current_date:
        return -1  # Birth year is in the future

    delta = current_date - birth_date
    return delta.days

def main():
    """
    Main function to get user input and display the calculated age in days.
    """
    try:
        birth_year_input = int(input("Enter the year of birth (e.g., 1990): "))
        age_days = calculate_age_in_days(birth_year_input)

        if age_days != -1:
            print(f"You are approximately {age_days} days old.")
        else:
            print("The birth year cannot be in the future. Please enter a valid year.")
    except ValueError:
        print("Invalid input. Please enter a valid year as a number.")

if __name__ == "__main__":
    main()