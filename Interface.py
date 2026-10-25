"""
Generates a seating chart, marking unavailable seats loaded from a text file.
"""

def load_unavailable_seats(filepath: str) -> dict:
    """Loads unavailable seats from a text file into a dictionary."""
    unavailable_seats = {}

    try:
        with open(filepath, 'r') as file:
            for line in file:
                seat = line.strip().upper()
                if seat:
                    unavailable_seats[seat] = True
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")

    return unavailable_seats

def load_selected_seats(selected_seats: list) -> dict:
    """Reads selected seats from a cart class file into a dictionary."""

def print_seating_chart(unavailable_seats: dict, selected_seats: dict) -> None:
    """Prints a 10x10 seating chart, replacing unavailable seats with an "X"."""
    rows = "ABCDEFGHIJ"
    columns = range(10)

    for row in rows:
        for col in columns:

            if col == 5:
                """Print a blank space for the aisle."""
                print(" | ", end="  ")
        
            seat = f"{row}{col}"

            if seat in unavailable_seats:
                print("\033[33m XX \033[0m", end="  ")
            elif seat in selected_seats:
                print("\033[32m OO \033[0m", end="  ")
            else:
                print(f"[{seat}]", end="  ")
                
        print()


if __name__ == "__main__":
    booked_seats = load_unavailable_seats("booked_seats.txt")
    print_seating_chart(booked_seats)
