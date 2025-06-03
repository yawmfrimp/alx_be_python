task = input("Enter your task: ") #asking for the type of task
priority = input("Priority (high/medium/low): ") #asking for the priority of task
time_bound = input("Is it time-bound? (yes/no): ") #asking if the task is time bound

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case 'low':
        if time_bound == 'yes':
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"'{task}' is a {priority} priority task. Consider completing it when you have free time.")



