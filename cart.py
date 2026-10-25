class Cart:
    """Represents a shopping cart for seat selection."""
    def __init__(self):
        self.items = []

    def cart_items(self) -> list:
        """Returns a list of items in the cart."""
        return self.items
    
    def add_item(self, item: str) -> None:
        """Adds seat to cart.items"""
        #First check if the seat is already in the cart 
        if item in self.items:
            print(f"Seat {item} is already in the cart.")
            return
        self.items.append(item)

        #Check if the seat is already booked
        with open("booked_seats.txt", "r") as file:
            booked_seats = [line.strip().upper() for line in file]
        if item.upper() in booked_seats:
            print(f"Seat {item} is already booked.")
            self.items.remove(item)

    def clear_cart(self) -> None:
        """Clears all items from the cart."""
        self.items = []

    def checkout(self) -> None:
        """Write to booked_seats.txt and call the clear_cart if write was successful"""
        try:
            with open("booked_seats.txt", "a") as file:
                for item in self.items:
                    file.write(f"{item.upper()}\n")
            self.clear_cart()
        except Exception as e:
            print(f"Error during checkout: {e}")