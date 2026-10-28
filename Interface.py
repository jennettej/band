"""
Generates a seating chart 
"""

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