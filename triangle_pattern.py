def lower_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end="")
        print()

def upper_triangle(n):
    for i in range(n):
        for j in range(n, i, -1):
            print('*', end="")
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(end=" ")
        for j in range(i + 1):
            print('*', end=" ")
        print()

def main():
    while True:
        try:
            n = int(input("Enter the number of rows (positive integer): "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
            continue

        print("\nChoose a pattern to display:")
        print("1. Lower Triangular Pattern")
        print("2. Upper Triangular Pattern")
        print("3. Pyramid Pattern")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print("\nLower Triangular Pattern:")
            lower_triangle(n)
        elif choice == '2':
            print("\nUpper Triangular Pattern:")
            upper_triangle(n)
        elif choice == '3':
            print("\nPyramid Pattern:")
            pyramid(n)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
