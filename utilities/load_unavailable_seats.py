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