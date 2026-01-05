def recurring_pack():
    while True:
        print('\nRecurring Pack Menu:')
        print('''
            1. 700MB / Day @ Rs 299 – 28 Days
            2. 1.5GB / Day @ Rs 599 – 28 Days
            3. Back to Main Menu
              ''')
        
        try:
            user_choice = int(input("Please select an option (1-3): "))
        except ValueError:
            print("Please select a valid option (1-3).")
            continue
        match user_choice:
            case 1:
                print("You selected 700MB / Day @ Rs 299 – 28 Days. successfully activated !!")
                print('-'*40)
            case 2:
                print("You selected 1.5GB / Day @ Rs 599 – 28 Days. successfully activated !!")
                print('-'*40)
            case 3:
                print("Returning to Main Menu...")
                
                break
            case _:
                print("Invalid choice. Select 1–3.")
                print('-'*40)
