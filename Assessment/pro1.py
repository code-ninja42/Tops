class HotelReservation:
    def __init__(self):
        self.booking = {}
    def book_name(self):
        name = input("Enter your name :")
        if name in self.booking:
            print("You already have a booking")
            return
        contact = input("Enter your contact number")
        if not contact.isdigit() or len(contact) != 10:
            print("Invalid contact number")
            return
        nights = int(input("Enter number of nights of your stay"))
        print("\nRoom Types:")
        print("1. Standard - ₹2000 / night")
        print("2. Deluxe   - ₹3500 / night")
        print("3. Suite    - ₹5000 / night")
        
        choice = int(input("select room type(1-3)"))
        if choice == 1:
            room_type = "Standard"
            rate = 2000
        elif choice == 2:
            room_type = "Deluxe"
            rate = 3500
        elif choice == 3:
            room_type = "Suite"
            rate = 5000
        else:
            print("Invalid room type") 
            return
        total_cost = nights * rate
        print(f"Total cost for{nights} nights are {total_cost}") 
        confirm = input("Do you want to confirm booking?(yes/no()").lower()
        if confirm == "yes":
            booking_id = len(self.booking) + 1
            self.booking[name] = {
                "Booking id":booking_id,
                "Name":name,
                "Contact":contact,
                "Room Type":room_type,
                "Nights":nights,
                "Total_cost":total_cost,
                "Status":"Booked"
            }      
            print("Booking confirm successfully")
        else:
            print("Booking cancelled")
        
    def view_booking(self):
            name = input("Enter your name to view booking")
            if name in self.booking:
                for k,v in self.booking.items():
                    print(f"{k}:{v}")
            else:
                print("No booking found")

    def cancel_booking(self):
        name = input("Enter your name to cancel booking")
        if name in self.booking:
            confirm = input("Are you sure you want to cancel booking (yes/no)").lower()
            if confirm == "yes":
                del self.booking[name]
                print("Booking cancelled successfully")
            else:
                print("cancellation aborted")
        else:
            print("No booking found")
    def menu(self):
        while True:
            print("\n--- Hotel Reservation System ---")
            print("1. Book Room")
            print("2. View Booking")
            print("3. Cancel Booking")
            print("4. Exit")
            choice = int(input("Enter your choice"))
            if choice == 1:
                self.book_name()
            elif choice == 2:
                self.view_booking()
            elif choice == 3:
                self.cancel_booking()
            elif choice == 4:
                print("Exiting")
                break
            else:
                print("Invalid choice")
hotel = HotelReservation()
hotel.menu()