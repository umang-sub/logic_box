print("Welcome to the pattern generator and number analyzer!")

while True:
    option = int(input("\nselect an option from the menu below:\n1. Generate a pattern\n2. Analyze a number\n3. Exit\nEnter Your choice:"))

    if option == 1:
        row = int(input("enter the number of rows for the pattern: "))
        for i in range(row+1):
            for j in range(i):
                print("*", end=" ")
            print()
        
    elif option == 2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        for i in range(start,end+1):
            if i % 2 == 0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")
            sum = 0
            num = start
            while num <= end:
                sum += num
                num += 1
        print(f"sum of all numbers from {start} to {end} is: {sum}")
    else:
        print("Exiting the program. Goodbye!")
        break