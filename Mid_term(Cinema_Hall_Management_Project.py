class Star_Cinema:
    pass

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

    def _initialize_seats(self):
        for row in range(self._rows):
            row_list = [0] * self._cols
            self._seats[row + 1] = row_list

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        show_seats = [[0] * self._cols for _ in range(self._rows)]
        self._seats[id] = show_seats

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print("Invalid show ID")
            return

        for seat in seat_list:
            row, col = seat
            if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                print(f"Invalid seat: ({row}, {col})")
                continue

            if self._seats[id][row - 1][col - 1] == 1:
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self._seats[id][row - 1][col - 1] = 1
                print(f"Seat ({row}, {col}) booked for show {id}")

    def view_show_list(self):
        print("Shows today:")
        for show in self._show_list:
            print(f"Movie Name: {show[1]} ({show[0]}) Show ID: {show[0]} Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID")
            return

        print(f"\nAvailable seats for Show {id}:")
        for row in self._seats[id]:
            print(row)

hall1 = Hall(6, 13, 1)

# Adding a show to the hall
hall1.entry_show(111, "Animal", "25-01-2024   11:00 AM")
hall1.entry_show(222, "Animal", "25-01-2024   2:00 PM")

# Displaying available options
while True:
    print("\n1. View all shows today\n2. View available seats\n3. Book seats\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        hall1.view_show_list()

    elif choice == '2':
        show_id = input("Enter Show ID: ")
        hall1.view_available_seats(int(show_id))

    elif choice == '3':
        show_id = input("Enter Show ID: ")
        num_tickets = int(input("Number of Tickets? : "))
        seat_list = [(int(input("Enter seat row: ")), int(input("Enter seat col: "))) for _ in range(num_tickets)]
        hall1.book_seats(int(show_id), seat_list)

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please choose again.")
