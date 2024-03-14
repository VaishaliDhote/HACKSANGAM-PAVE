class Theater:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.bike_seats = {}
        self.car_seats = {}
        for row in range(1, rows + 1):
            for seat in range(1, seats_per_row + 1):
                self.bike_seats[(row, seat)] = 'Available'
                self.car_seats[(row, seat)] = 'Available'

    def display_seating(self, vehicle_type):
        print(f"Parking arrangement for {vehicle_type}s:")
        if vehicle_type.lower() == 'car':
            seats = self.car_seats
        elif vehicle_type.lower() == 'bike':
            seats = self.bike_seats
        else:
            print("Invalid vehicle type.")
            return
        for row in range(1, self.rows + 1):
            for seat in range(1, self.seats_per_row + 1):
                status = seats[(row, seat)]
                print(f'[{row}-{seat}: {status}]', end=' ')
            print()


    def book_seat(self, row, seat, vehicle_type):
        if vehicle_type.lower() == 'car':
            seats = self.car_seats
        elif vehicle_type.lower() == 'bike':
            seats = self.bike_seats
        else:
            print("Invalid vehicle type.")
            return
        if (row, seat) in seats:
            if seats[(row, seat)] == 'Available':
                seats[(row, seat)] = 'Booked'
                print(f'Seat {row}-{seat} booked successfully for {vehicle_type}!')
            else:
                print(f'Seat {row}-{seat} is already booked.')
        else:
            print(f'Seat {row}-{seat} does not exist in the parking.')
            

    def cancel_booking(self, row, seat, vehicle_type):
        if vehicle_type.lower() == 'car':
            seats = self.car_seats
        elif vehicle_type.lower() == 'bike':
            seats = self.bike_seats
        else:
            print("Invalid vehicle type.")
            return
        if (row, seat) in seats:
            if seats[(row, seat)] == 'Booked':
                seats[(row, seat)] = 'Available'
                print(f'Booking for Seat {row}-{seat} canceled successfully for {vehicle_type}!')
            else:
                print(f'Seat {row}-{seat} is not booked.')
        else:
            print(f'Seat {row}-{seat} does not exist in the parking.')

            

    def check_availability(self, row, seat, vehicle_type):
        if vehicle_type.lower() == 'car':
            seats = self.car_seats
        elif vehicle_type.lower() == 'bike':
            seats = self.bike_seats
        else:
            print("Invalid vehicle type.")
            return False
        if (row, seat) in seats:
            return seats[(row, seat)] == 'Available'
        else:
            return False


def main():
    rows = 5
    seats_per_row = 10
    theater = Theater(rows, seats_per_row)

    while True:
        print("\nWelcome to the ParkEase Booking System")
        print("1. Display Parking-Arrangement")
        print("2. Book your parking")
        print("3. Cancel your booking")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_type = input("Enter your vehicle type (car/bike): ")
            theater.display_seating(vehicle_type)
        elif choice == '2':
            vehicle_type = input("Enter your vehicle type (car/bike): ")
            row = int(input("Enter the row number: "))
            seat = int(input("Enter the column number: "))
            if theater.check_availability(row, seat, vehicle_type):
                theater.book_seat(row, seat, vehicle_type)
            else:
                print("This area is already booked.")
        elif choice == '3':
            vehicle_type = input("Enter your vehicle type (car/bike): ")
            row = int(input("Enter the row number: "))
            seat = int(input("Enter the column number: "))
            theater.cancel_booking(row, seat, vehicle_type)
        elif choice == '4':
            print("Exiting the booking system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
