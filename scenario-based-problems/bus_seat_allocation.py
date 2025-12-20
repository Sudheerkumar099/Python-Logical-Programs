n = int(input("Enter the number of requests: "))
total_seats = 40
lst = []
for i in range(n):
    request = int(input("Enter the number of seats: "))
    lst.append(request)
for i in lst:
    request = i
    if request <= total_seats:
        total_seats -= request
        print("CONFIRMED")
    else:
        print("WAITLISTED")