total = 30

while True:
    print("--- Movie Ticket Booking ---")
    print("1. Check Seats")
    print("2. Book Ticket")
    print("3. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Available Seats:", total)

    elif ch == 2:
        qty = int(input("Enter tickets needed: "))
        if qty > 0 and qty <= total:
            total = total - qty
            print("Booking Successful")
        else:
            print("Tickets not available")

    elif ch == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
