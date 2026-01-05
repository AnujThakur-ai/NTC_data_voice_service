def SMS():
    while True:
        print('''\nSMS Pack Menu:
                1. 200 SMS @ Rs 35 – 1 Day
                2. 200 SMS @ Rs 60 – 7 Days
                3. 500 SMS @ Rs 150 – 28 Days
                4. Back to Main Menu''')
        
        try:
            user_choice = int(input("Please select an option (1-4): "))
        except ValueError:
            print("Please select a valid option (1-4).")
            continue    
        match user_choice:
            case 1:
                print("You selected 200 SMS @ Rs 35 – 1 Day. successfully activated !!")
                print('-'*40)
            case 2:
                print("You selected 200 SMS @ Rs 60 – 7 Days. successfully activated !!")
                print('-'*40)
            case 3:
                print("You selected 500 SMS @ Rs 150 – 28 Days. successfully activated !!")
                print('-'*40)
            case 4:
                print("Returning to Main Menu...")
                
                break
            case _:
                print("Invalid choice. Select 1–4.")
                print('-'*40)


