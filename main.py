from models.sales import get_total_seats_sold, get_total_revenue, get_fill_percentage
from utilities.seat_chart import print_seating_chart
from utilities.load_unavailable_seats import load_unavailable_seats
from utilities.load_selected_seats import load_selected_seats

#Main function calling from other functions. Not connected to all functions, interface needs a lot of work.

booked_seats = load_unavailable_seats("data/booked_seats.txt")
from models.cart import Cart
cart = Cart()
selected_seats = load_selected_seats(cart.cart_items())
#first render seating chart print
print_seating_chart(booked_seats, selected_seats)
# Main loop for user interaction
# prompt to enter the managers view. Prompt only shown once
print("To enter the managers view, enter the password")
while True:
    action = input("Enter: 'add' to add a seat to the cart, 'remove' to remove a seat from the cart,"
                   "\n'checkout' to checkout, or 'quit' to exit: ").strip().lower()
    #Let's print out selected seats for the user if they have any from the cart class
    if cart.cart_items():
        print("Selected seats:", ", ".join(cart.cart_items()))
    #User wants to add a seat
    if action == "add":
        seat = input("Enter the seat to add (e.g., A0): ").strip().upper()
        #add to cart
        cart.add_item(seat)
        #Call load selected_seats and print_seating_chart to update the seating chart after adding a seat
        selected_seats = load_selected_seats(cart.cart_items())
        print_seating_chart(booked_seats, selected_seats)

    #user wants to remove a seat from the cart
    if action == "remove":
        seat = input("Enter the seat to remove (e.g., A0): ").strip().upper()
        #check if the seat selected is in the cart
        if seat in selected_seats:
            print("Removing seat:", seat)
            cart.remove_item(seat)
            selected_seats = load_selected_seats(cart.cart_items())
            print_seating_chart(booked_seats, selected_seats)
        # if the seat is not found reprompt the user
        elif seat not in selected_seats:
            print("Invalid seat. Please try again.")

    #Accessing the managers view
    elif action == "password123": #Temporary password for testing
        print("percent of seats sold :",get_fill_percentage())
        print("amount of seats sold  :", get_total_seats_sold())
        print("revenue from the seats:", get_total_revenue())

    elif action == "checkout":
        #Call the checkout method to write to booked_seats.txt and clear the cart
        cart.checkout()
        #After checkout, reload the booked seats and selected seats, then print the updated seating chart
        booked_seats = load_unavailable_seats("data/booked_seats.txt")
        #After checkout, reload the booked seats and selected seats, then print the updated seating chart
        selected_seats = load_selected_seats(cart.cart_items())
        #Call print_seating_chart to update the seating chart after checkout
        print_seating_chart(booked_seats, selected_seats)
    elif action == "quit":
        break
    else:
        print("Invalid action. Please try again.")
