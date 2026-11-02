from utilities.seat_chart import print_seating_chart
from utilities.load_unavailable_seats import load_unavailable_seats
from utilities.load_selected_seats import load_selected_seats
from models.cart import Cart
from utilities.check_seat_pricing import check_seat_pricing

#Main function calling from other functions. Not connected to all functions, interface needs a lot of work.

booked_seats = load_unavailable_seats("data/booked_seats.txt")
cart = Cart()
selected_seats = load_selected_seats(cart.cart_items())
#first render seating chart print
print_seating_chart(booked_seats, selected_seats)

# Main loop for user interaction
while True:
    action = input("Enter 'add' to add a seat, 'checkout' to checkout, or 'quit' to exit: ").strip().lower()
    
    #Let's print out selected seats and the running total for the user if they have any from the cart class
    if cart.cart_items():
        print(f"Selected seats: {', '.join(cart.cart_items())} | Total Price: ${cart.total_price:.2f}")
        
    #User wants to add a seat
    if action == "add":
        seat = input("Enter the seat to add (e.g., A0): ").strip().upper()
        
        try:
            # Check the price for the entered seat
            price = check_seat_pricing(seat)
            
            # add to cart with both seat and price
            cart.add_item(seat, price)
            
            # Show individual seat price and running total
            if seat in cart.cart_items():
                print(f"\nSeat {seat} added. Price: ${price:.2f}")
                print(f"Total of selected seats: ${cart.total_price:.2f}\n")
                
        except ValueError as e:
            print(f"Error: {e}")
            
        #Call load selected_seats and print_seating_chart to update the seating chart after adding a seat
        selected_seats = load_selected_seats(cart.cart_items())
        print_seating_chart(booked_seats, selected_seats)
        
    elif action == "checkout":
        #Call the checkout method to write to booked_seats.txt and clear the cart
        cart.checkout()
        #After checkout, reload the booked seats and selected seats, then print the updated seating chart
        booked_seats = load_unavailable_seats("data/booked_seats.txt")
        selected_seats = load_selected_seats(cart.cart_items())
        print_seating_chart(booked_seats, selected_seats)
        
    elif action == "quit":
        break
    else:
        print("Invalid action. Please try again.")