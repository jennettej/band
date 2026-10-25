from Interface import print_seating_chart, load_unavailable_seats, load_selected_seats

booked_seats = load_unavailable_seats("booked_seats.txt")
from cart import Cart
cart = Cart()
selected_seats = load_selected_seats(cart.cart_items())
#first render seating chart print
print_seating_chart(booked_seats, selected_seats)

