def all_time_pack():
    while True:
        print("\nAll Time Pack Menu:")
        print("1. 1GB @ Rs 30 – 1 Day")
        print("2. 4GB @ Rs 99 – 1 Day")
        print("3. 5GB @ Rs 109 – 7 Days")
        print("4. 12GB @ Rs 199 – 7 Days")
        print("5. Back to Main Menu")

        try:
            user_choice = int(input("Please select an option (1-5): "))
        except ValueError:
            print("Please select a valid option (1-5).")
            continue

        match user_choice:
            case 1:
                print("You selected 1GB @ Rs 30 – 1 Day. successfully activated !!")
                print('-'*40)
            case 2:
                print("You selected 4GB @ Rs 99 – 1 Day. successfully activated !!")
                print('-'*40)
            case 3:
                print("You selected 5GB @ Rs 109 – 7 Days. successfully activated !!")
                print('-'*40)
            case 4:
                print("You selected 12GB @ Rs 199 – 7 Days. successfully activated !!")
                print('-'*40)
            case 5:
                print("Returning to Main Menu...")
                break
            case _:
                print("Invalid choice. Select 1–5.")
                print('-'*40)

            
        
    

  
    