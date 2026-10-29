def load_selected_seats(selected_seats: list) -> dict:
    """
    Converts a list of selected seats from the cart class into a dictionary for easy lookup.
    Keys are seat identifiers and values are True.
    """
    selected_seats_dict = {}
    for seat in selected_seats:
        selected_seats_dict[seat.upper()] = True
    return selected_seats_dict

