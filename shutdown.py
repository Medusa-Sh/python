def shutdown():
    print("Do you want to shutdown the system? (yes/no)")
    choice = input()
    if choice == "no":
        print("So sorry to hear that.")
    elif choice == "yes":
        print("Do you really want to shutdown the system? (yes/no)")
        confirmation = input()
        if confirmation == "yes":
            print("Shutting down the system...")
        elif confirmation == "no":
            print("Shutdown cancelled.")
shutdown()