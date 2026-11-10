class MovieTicket:
    def __init__(self, movie_name, theatre, seat_number):
        self.movie_name = movie_name
        self.theatre = theatre
        self.seat_number = seat_number

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Theatre:", self.theatre)
        print("Seat Number:", self.seat_number)


# Creating three ticket objects
ticket1 = MovieTicket("Avatar", "INOX", "A1")
ticket2 = MovieTicket("Pushpa 2", "PVR", "B5")
ticket3 = MovieTicket("Leo", "INOX", "C3")


# Displaying ticket details
print("Ticket 1:")
ticket1.display()

print("\nTicket 2:")
ticket2.display()

print("\nTicket 3:")
ticket3.display()