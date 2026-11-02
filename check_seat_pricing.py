Base_Price = 8 # Variable so the base price can easily be adjusted if necessary
def check_seat_pricing(seat, base = Base_Price):
    """Returns the price of a seat."""
    row = seat.strip().upper()[0] # Takes the row letter off of the front of the seat label
    if row == "A":
        return base + 1  # Adds one to the base price for seats in the front row
    elif row == "J":
        return base - 1  # Subtracts one from the base price for seats in the back row
    elif "B" <= row <= "I":
        return base  # Returns the base price for seats in the middle row
    else:
        raise ValueError("Invalid Row. Must be between A and J.")  # Raises an error if an invalid letter is entered
