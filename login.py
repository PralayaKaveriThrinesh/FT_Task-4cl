def main():
    users = load_users()

    while True:
        print("\n--- Task Manager ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == '1':
            uname = input("New username: ")
            if find_user(users, uname):
                print("User already exists!")
            else:
                users.append(User(uname))
                print("User registered!\n")

        elif choice == '2':
            uname = input("Username: ")
            user = find_user(users, uname)
            if user:
                user_menu(user, users)
            else:
                print("User not found!")

        elif choice == '3':
            save_users(users)
            break

if __name__ == "__main__":
    main()
