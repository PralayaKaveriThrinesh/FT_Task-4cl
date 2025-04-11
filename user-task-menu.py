def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [User.from_dict(u) for u in data]
    return []

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump([u.to_dict() for u in users], f, indent=4)

def find_user(users, username):
    for user in users:
        if user.username == username:
            return user
    return None

def task_statistics(user):
    print("\n--- Task Statistics ---")
    total = len(user.tasks)
    done = len([t for t in user.tasks if t.completed])
    pending = total - done
    print(f"Total: {total}, Completed: {done}, Pending: {pending}")
    priorities = Counter(t.priority for t in user.tasks)
    for prio, count in priorities.items():
        print(f"{prio}: {count} tasks")

def user_menu(user, users):
    while True:
        print(f"\n--- Welcome {user.username} ---")
        print("1. Add Task")
        print("2. View My Tasks")
        print("3. Assign Task to User")
        print("4. Mark Task as Completed")
        print("5. View Statistics")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == '1':
            title = input("Title: ")
            desc = input("Desc: ")
            due = input("Due date: ")
            prio = input("Priority: ")
            task = Task(title, desc, due, prio, assigned_to=user.username)
            user.add_task(task)

        elif choice == '2':
            for i, task in enumerate(user.tasks):
                print(f"{i+1}. {task}")

        elif choice == '3':
            other = input("Assign to (username): ")
            target = find_user(users, other)
            if target:
                title = input("Title: ")
                desc = input("Desc: ")
                due = input("Due date: ")
                prio = input("Priority: ")
                task = Task(title, desc, due, prio, assigned_to=other)
                target.add_task(task)
                print(f"Task assigned to {other}!\n")
            else:
                print("User not found!")

        elif choice == '4':
            for i, task in enumerate(user.tasks):
                print(f"{i+1}. {task}")
            idx = int(input("Mark which task? ")) - 1
            user.tasks[idx].completed = True

        elif choice == '5':
            task_statistics(user)

        elif choice == '6':
            save_users(users)
            break
