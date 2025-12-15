def create_mulitiplication_table():
    table = []
    for row in range(1, 6):       
        current_row = []
        for col in range(1, 11):  
            current_row.append(row * col)
        table.append(current_row)
    return table


def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(value, end=" ")
        print()  


def main():
    while True:
        table = create_mulitiplication_table()
        display_multiplication_table(table)

        answer = input("Do you want to continue? (y/n): ").lower()
        if answer != "y":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
