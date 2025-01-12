# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# # Process the task using Match Case for priority levels
# match priority:
#     case "high":
#         reminder = f"'{task}' is a high priority task."
#     case "medium":
#         reminder = f"'{task}' is a medium priority task."
#     case "low":
#         reminder = f"'{task}' is a low priority task."
#     case _:
#         reminder = "Invalid priority level entered. Please enter high, medium, or low."
#         print(reminder)
#         exit()  # Exit the program for invalid priority input

# # Modify the reminder if the task is time-bound
# if time_bound == "yes":
#     reminder += " It requires immediate attention today!"
# elif time_bound == "no":
#     reminder += " Consider completing it at your convenience."

# # Display the customized reminder
# print("\nReminder:", reminder)

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate a reminder message based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
        exit()  # Exit if priority is not valid

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
else:
    print("Invalid input for time sensitivity. Please enter yes or no.")
    exit()  # Exit if time_bound is not valid

# Display the customized reminder
print(f"Reminder: {reminder}")
