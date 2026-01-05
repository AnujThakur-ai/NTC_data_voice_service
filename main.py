




def main_menu():
    while True:
        print("""Welcome to the Main Menu

1. All Time Pack
2. Recurring Pack
3. SMS Pack
4. Unlimited Facebook / YouTube Pack
5. Exit
""")
        print('-' * 40)

        try:
            option = int(input("Select an option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match option:
            case 1:
                from all_time_pack import all_time_pack
                all_time_pack()
            case 2:
                from recurring_pack import recurring_pack
                recurring_pack()
            case 3:
                from Sms_pack import SMS
                SMS()
            case 4:
                from Unlimited_pack import unlimited_pack
                unlimited_pack()
            case 5:
                print("Thank you for choosing us. Goodbye!")
                break
            case _:
                print("Invalid option. Choose between 1 and 5.")

if __name__ == "__main__":
    main_menu()
