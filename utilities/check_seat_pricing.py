# Checks the pricing of selected seats based on their location in the seating chart.
#Front row seats are $9 for A row seats
#B through I seats are $8
#J row seats are $7

def check_seat_pricing(seat: str) -> int:
    """Returns the price of a seat based on its row."""
    row = seat[0].upper()
    if row == "A":
        return 9
    elif row in "BCDEFGHI":
        return 8
    elif row == "J":
        return 7
    else:
        raise ValueError(f"Invalid seat: {seat}")