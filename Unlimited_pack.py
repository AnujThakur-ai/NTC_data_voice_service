def unlimited_pack():
    while True:
        print('''\nUnlimited Facebook / YouTube Pack Menu:
                1. Unlimited Facebook @ Rs 55 – 3 Days
                2. Unlimited YouTube @ Rs 55 – 3 Days
                3. Back to Main Menu''')
        
        
        try:
            user_choice = int(input("Please select an option (1-3): "))
        except ValueError:
            print("Please select a valid option (1-3).")
            continue 
        match user_choice:
            case 1:
                print("You selected Unlimited Facebook @ Rs 55 – 3 Days. successfully activated !!")
                print('-'*40)
            case 2:
                print("You selected Unlimited YouTube @ Rs 55 – 3 Days. Successfully activated !!")
                print('-'*40)
            case 3:
                print("Returning to Main Menu...")
               
                break
            case _:
                print("Invalid choice. Select 1–3.")
                print('-'*40)
