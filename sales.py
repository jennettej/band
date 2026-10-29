from check_seat_pricing import check_seat_pricing


def get_total_seats_sold():
    """returns the total number of seats sold."""

    #reads all booked seats from the file
    with open("booked_seats.txt", "r") as file:
        seats = file.readlines()

    #each line represents one booked seat
    return len(seats)


def get_fill_percentage():
    """calculates the percentage of seats that have been sold."""

    total_seats = 260
    seats_sold = get_total_seats_sold()

    #divides seats sold by total seats to gets the percentage
    return (seats_sold / total_seats) * 100


def get_total_revenue():
    """calculates the total revenue from all booked seats."""

    total = 0

    #goes through each booked seat and adds its price to the total
    with open("booked_seats.txt", "r") as file:
        for seat in file:
            row = seat.strip().upper()[0]

            #gets the price based on the row and adds it to revenue
            total += check_seat_pricing(row)

    return total
