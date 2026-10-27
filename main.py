from Interface import print_seating_chart, load_unavailable_seats, load_selected_seats

booked_seats = load_unavailable_seats("booked_seats.txt")
from cart import Cart
cart = Cart()
selected_seats = load_selected_seats(cart.cart_items())
#first render seating chart print
print_seating_chart(booked_seats, selected_seats)

#Now I want to start a continuous loop for user interaction. 
while True:
    action = input("Enter 'add' to add a seat, 'checkout' to checkout, or 'quit' to exit: ").strip().lower()
    #Let's print out selected seats for the user if they have any
    if cart.cart_items():
        print("Selected seats:", ", ".join(cart.cart_items()))
    if action == "add":
        seat = input("Enter the seat to add (e.g., A0): ").strip().upper()
        cart.add_item(seat)
        selected_seats = load_selected_seats(cart.cart_items())
        print_seating_chart(booked_seats, selected_seats)
    elif action == "checkout":
        cart.checkout()
        booked_seats = load_unavailable_seats("booked_seats.txt")
        selected_seats = load_selected_seats(cart.cart_items())
        print_seating_chart(booked_seats, selected_seats)
    elif action == "quit":
        break
    else:
        print("Invalid action. Please try again.")
