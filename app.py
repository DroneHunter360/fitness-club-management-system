import psycopg2
from datetime import date, datetime, timedelta

# global variables
curr_user = ''
curr_user_id = 0
curr_user_name = ''
curr_user_type = ''

# parameters used for database connection - MODIFY AS REQUIRED
dbname = 'Final_Project'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'

### MEMBER FUNCTIONS ###
def register_user(member_username, member_password, email, phone, join_date, first_name, last_name, home_number, street, postal_code):
    query = f"INSERT INTO Members (member_username, member_password, email, join_date, first_name, last_name, home_number, street, postal_code) VALUES ('{member_username}', '{member_password}', '{email}', '{join_date}', '{first_name}', '{last_name}', {int(home_number)}, '{street}', '{postal_code}')"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Unable to register new user')

def manage_health_metric():
    print('What would you like to do?\n'
                  '1 - Add new health metric\n'
                  '2 - Delete existing health metric\n'
                  '3 - Update existing health metric\n'
                  '4 - Cancel\n')
    option = int(input())

    if option == 1:
        add_health_metric()
    elif option == 2:
        delete_health_metric()
    elif option == 3:
        update_health_metric()
    elif option == 4:
        return

def manage_fitness_goal():
    print('What would you like to do?\n'
                  '1 - Add new fitness goal\n'
                  '2 - Delete existing fitness goal\n'
                  '3 - Update existing fitness goal\n'
                  '4 - Cancel\n')
    option = int(input())

    if option == 1:
        add_fitness_goal()
    elif option == 2:
        delete_fitness_goal()
    elif option == 3:
        update_fitness_goal()
    elif option == 4:
        return

def update_personal_information():
    print('What would you like to update?\n'
                  '1 - Password\n'
                  '2 - Email\n'
                  '3 - First name\n'
                  '4 - Last name\n'
                  '5 - Address\n')
    option = int(input())

    if option == 1:
        new_pwd = input("Enter a new password: ")
        query = f"UPDATE Members SET member_password = '{new_pwd}' WHERE member_username = '{globals()['curr_user']}'"
    elif option == 2:
        new_email = input("Enter a new password: ")
        query = f"UPDATE Members SET member_email = '{new_email}' WHERE member_username = '{globals()['curr_user']}'"
    elif option == 3:
        new_fname = input("Enter a new first name: ")
        query = f"UPDATE Members SET first_name = '{new_fname}' WHERE member_username = '{globals()['curr_user']}'"
    elif option == 4:
        new_lname = input("Enter a new last name: ")
        query = f"UPDATE Members SET last_name = '{new_lname}' WHERE member_username = '{globals()['curr_user']}'"
    elif option == 5:
        new_address = input("Enter a new address in the following space-separated format [HOUSE #] [STREET] [POSTAL CODE]: ")
        new_house_number, new_street, new_postal = new_address.split()
        query = f"UPDATE Members SET home_number = {int(new_house_number)}, street = '{new_street}', postal_code = '{new_postal} WHERE member_username = '{globals()['curr_user']}'"

    try:
        cursor.execute(query)
        conn.commit()
    except psycopg2.errors.UniqueViolation as e:
        print(f'\nERROR! Could not complete personal information update: {e}')
    except:
        print('\nERROR: Could not complete personal information update')

def display_dashboard():
    print(f"{globals()['curr_user_name'].upper()}'S DASHBOARD DISPLAY")

    # Display Member's exercise routines
    print("Exercise Routines - A list of all the exercise routines you've completed with a trainer during personal training sessions:\n")
    query = f"SELECT exercise_routine FROM Personal_Sessions WHERE member_id = '{globals()['curr_user_id']}'"
    cursor.execute(query)

    exercise_routines = cursor.fetchall()
    for routine in exercise_routines:
        print(f"- {routine[0]}")

    print("-----------------------------------------------------------------------------------------------------------------------")

    # Display Member's fitness achievements
    print("\nFitness Goal Achievements - A list of all the fitness goals you've achieved:")
    query = f"SELECT goal_type FROM Fitness_Goals WHERE member_id = {globals()['curr_user_id']} AND goal_achieved = true"
    cursor.execute(query)

    achievements = cursor.fetchall()
    for achievement in achievements:
        display_goal(achievement[0])

    print("\nFitness Goals - A list of all the fitness goals that you are still working towards achieving:")
    query = f"SELECT goal_type FROM Fitness_Goals WHERE member_id = {globals()['curr_user_id']} AND goal_achieved = false"
    cursor.execute(query)

    working_towards = cursor.fetchall()
    for goal in working_towards:
        display_goal(goal[0])

    print("\n-----------------------------------------------------------------------------------------------------------------------")

    # Display Member's health statistics
    print("\nHealth Statistics - A list of all your existing health metrics:")
    query = f"SELECT metric_type FROM Health_Metrics WHERE member_id = {globals()['curr_user_id']}"
    cursor.execute(query)

    health_stats = cursor.fetchall()
    for stat in health_stats:
        display_health_metric(stat[0])

def manage_schedule():
    print('What would you like to do?\n'
                  '1 - Schedule New Personal Training Session\n'
                  '2 - Reschedule Existing Personal Training Session\n'
                  '3 - Cancel Existing Personal Training Session\n'
                  '4 - Enroll In Group Fitness Class\n'
                  '5 - Cancel\n')
    option = int(input())

    if option == 1:
        schedule_personal_session()
    elif option == 2:
        reschedule_personal_session()
    elif option == 3:
        delete_personal_session()
    elif option == 4:
        enroll_in_group_class()
    elif option == 5:
        return

### TRAINER FUNCTIONS ###
def update_availability():
    print('What would you like to update?\n'
                  '1 - Start Availability Time\n'
                  '2 - End Availability Time\n'
                  '3 - Cancel\n')
    option = int(input())

    if option == 1:
        new_start_availability = input("Enter your updated start availability time for today (HH:MM:SS): ")
        query = f"UPDATE Trainers SET start_availability = '{new_start_availability}' WHERE trainer_username = '{globals()['curr_user']}'"
        print(query)
    elif option == 2:
        new_end_availability = input("Enter your updated end availability time for today (HH:MM:SS): ")
        query = f"UPDATE Trainers SET end_availability = '{new_end_availability}' WHERE trainer_username = '{globals()['curr_user']}'"
    elif option == 3:
        return

    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not update availability')

def view_member_profile(name):
    fname, lname = name.split()
    query = f"SELECT member_username FROM Members WHERE first_name = '{fname}' AND last_name = '{lname}'"
    cursor.execute(query)

    users = cursor.fetchall()
    if not users:
        print(f"No Members were found that matched the name '{fname} {lname}'")
    else:
        print(f"Here are the Members with the name '{fname} {lname}':")
        for user in users:
            display_user_info(user[0]) # user[0] simply extracts the actual value of the username from the tuple return result

### ADMIN FUNCTIONS ###
def manage_rooms():
    query = f"SELECT * FROM Group_Fitness_Classes"
    cursor.execute(query)

    classes = cursor.fetchall()
    print("Here are all the currently scheduled group fitness classes for today: \n")

    for c in classes:
        display_group_class(c)

    desired_class = input("Enter the ID of the group fitness class for which you want to manage the room booking: ")
    new_room = input("Enter the ID of the new room you'd like this class to be booked for: ")
    new_capacity = input("Enter the new capacity of the updated room: ")

    query = f"UPDATE Group_Fitness_Classes SET room_id = {int(new_room)}, room_capacity = {int(new_capacity)} WHERE class_id = {int(desired_class)}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not update group fitness classe\'s room booking')

def manage_equipment_maintenance():
    print('What would you like to do?\n'
                  '1 - View maintenance schedule/information\n'
                  '2 - Update maintenance schedule/information\n'
                  '3 - Cancel\n')
    option = int(input())

    if option == 1:
        display_maintenances()
    elif option == 2:
        update_maintenance()
    elif option == 3:
        return

def manage_class_schedule():
    print('What would you like to do?\n'
                  '1 - Schedule new group fitness class\n'
                  '2 - Update existing group fitness class details\n'
                  '3 - Cancel existing group fitness class\n'
                  '4 - Cancel\n')
    option = int(input())

    if option == 1:
        add_group_fitness_class()
    elif option == 2:
        update_group_fitness_class()
    elif option == 3:
        delete_group_fitness_class()
    elif option == 4:
        return

def manage_billing():
    print('What would you like to do?\n'
                  '1 - Create a new bill\n'
                  '2 - Process an existing bill\n'
                  '3 - Cancel\n')
    option = int(input())

    if option == 1:
        add_bill()
    elif option == 2:
        user = input("Enter the full name of the member who's bill you want to process: ")
        process_bill(user)
    elif option == 3:
        return

# HELPER FUNCTIONS

# function that authenticates a returning user as part of the login process
def authenticate_user(username, pwd):
    query = f"SELECT member_id, member_username, member_password, first_name FROM Members WHERE member_username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        if result[2] == pwd:
            globals()['curr_user'] = username
            globals()['curr_user_id'] = result[0]
            globals()['curr_user_name'] = result[3]
            return True
    
    return False

# function that authenticates a trainer as part of the login process
def authenticate_trainer(username, pwd):
    query = f"SELECT first_name, trainer_password FROM Trainers WHERE trainer_username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        if result[1] == pwd:
            globals()['curr_user'] = username
            globals()['curr_user_name'] = result[0]
        return True
    
    return False

# function that authenticates an admin as part of the login process
def authenticate_admin(username, pwd):
    query = f"SELECT first_name, admin_password, admin_id FROM Admin_Staff WHERE admin_username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        if result[1] == pwd:
            globals()['curr_user'] = username
            globals()['curr_user_name'] = result[0]
            globals()['curr_user_id'] = result[2]
        return True
        
    return False

def display_user_info(user=''):
    user_to_display = globals()['curr_user']
    if globals()['curr_user_type'] == 'TRAINER':
        user_to_display = user

    query = f"SELECT member_id, member_username, email, join_date, first_name, last_name, home_number, street, postal_code FROM Members WHERE member_username = '{user_to_display}'"
    cursor.execute(query)

    id, username, email, date_joined, fname, lname, home_num, street, postal = cursor.fetchone()
    print(f"\nUser ID: {id}")
    print(f"Name: {fname} {lname}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Date first joined: {date_joined}")
    print(f"Address: {home_num} {street}, {postal}\n")

def display_goal(goal_type):
    query = f"SELECT goal_type, goal_description, goal_value, goal_achieved FROM Fitness_Goals WHERE member_id = {globals()['curr_user_id']} AND goal_type = '{goal_type}'"
    cursor.execute(query)

    goal_type, description, value, achieved = cursor.fetchone()
    print(f"\nGoal type: {goal_type}")
    print(f"Description: {description}")
    print(f"Target value: {value}")
    print(f"Goal achieved?: {achieved}\n")

def display_health_metric(metric_type):
    query = f"SELECT metric_type, metric_value FROM Health_Metrics WHERE member_id = {globals()['curr_user_id']} AND metric_type = '{metric_type}'"
    cursor.execute(query)

    metric_type, value = cursor.fetchone()
    print(f"\nMetric type: {metric_type}")
    print(f"Metric value: {value}\n")

def display_group_class(c):
    cursor.execute(f"SELECT first_name, last_name FROM Trainers WHERE trainer_id = {c[4]}")
    trainer_name = cursor.fetchone()

    cursor.execute(f"SELECT COUNT(*) FROM EnrollsIn WHERE class_id = {int(c[0])}")
    curr_enrollment = cursor.fetchone()[0]

    print(f"Class ID: {c[0]}")
    print(f"Date: {c[1]}")
    print(f"Time: {c[2]} - {c[3]}")
    print(f"Trainer: {trainer_name[0]} {trainer_name[1]}")
    print(f"Workout type: {c[5]}")
    print(f"Class description: {c[6]}")
    print(f"Location: Room {c[7]} (Current Capacity: {curr_enrollment}/{c[8]} people)\n")

def display_personal_sessions():
    query = f"SELECT * FROM Personal_Sessions WHERE member_id = {globals()['curr_user_id']}"
    cursor.execute(query)

    sessions = cursor.fetchall()
    for session in sessions:
        display_session(session)
        
def display_session(c):
    cursor.execute(f"SELECT first_name, last_name FROM Trainers WHERE trainer_id = {c[2]}")
    trainer_name = cursor.fetchone()

    print(f"Session ID: {c[0]}")
    print(f"Date: {c[3]}")
    print(f"Time: {c[4]} - {c[5]}")
    print(f"Trainer: {trainer_name[0]} {trainer_name[1]}")
    print(f"Exercise Routine: {c[6]}")

def display_bill(b):
    print(f"Bill ID: {b[0]} (Created by Admin with ID {b[1]})")
    print(f"Billed to Member with ID: {b[2]}")
    print(f"Bill type: {b[3]}")
    print(f"Bill amount: ${b[4]}")
    print(f"Bill paid?: {b[5]}\n")

def display_maintenance(m):
    print(f"Maintenance ID: {m[0]}")
    print(f"Maintenance summary: {m[1]}")
    print(f"Associated equipment: {m[3]} (ID: {m[2]})")
    print(f"Last serviced: {m[4]}")
    print(f"Next service: {m[5]}\n")

def display_maintenances():
    query = "SELECT * FROM Maintenance_Equipment"
    cursor.execute(query)

    logs = cursor.fetchall()
    print("Here is the complete maintenance log for all the equipment: \n")

    for log in logs:
        display_maintenance(log)

def display_available_trainers(start_time, end_time, duration=-1):
    query = f"""SELECT trainer_id, first_name, last_name
FROM 
(
SELECT trainer_id 
FROM Trainers 
WHERE start_availability <= '{start_time}' AND end_availability >= '{end_time.time()}' 
EXCEPT
(
SELECT trainer_id
FROM 
(
	SELECT trainer_id, start_time, end_time
	FROM group_fitness_classes
	UNION
	SELECT trainer_id, start_time, end_time
	FROM personal_sessions
) AS joined_data
WHERE (start_time = '{start_time}' AND end_time = '{end_time.time()}') OR (start_time < '{start_time}' AND end_time > '{end_time.time()}') OR (start_time > '{start_time}' AND end_time < '{end_time.time()}') OR (start_time <= '{start_time}' AND end_time > '{start_time}' AND end_time <= '{end_time.time()}') OR (start_time >= '{start_time}' AND start_time < '{end_time.time()}' AND end_time >= '{end_time.time()}')
)
ORDER BY trainer_id
) NATURAL JOIN Trainers"""
    cursor.execute(query)

    available_trainers = cursor.fetchall()

    if not available_trainers:
        print("\nNOTICE: There are no available trainers for the specified time. Please try again")
        return False

    if duration == -1:
        print("Here are the trainers available for the desired session/class:")
    else:
        print(f"Here are the trainers available for a {duration} minute session/class:")
    for trainer in available_trainers:
        print(f"- {trainer[1]} {trainer[2]} (ID: {trainer[0]})")

    return True

def is_trainer_still_available(trainer_id, start_time, end_time):
    query = f"""SELECT trainer_id, first_name, last_name
FROM 
(
SELECT trainer_id 
FROM Trainers 
WHERE start_availability <= '{start_time}' AND end_availability >= '{end_time.time()}' 
EXCEPT
(
SELECT trainer_id
FROM 
(
	SELECT trainer_id, start_time, end_time
	FROM group_fitness_classes
	UNION
	SELECT trainer_id, start_time, end_time
	FROM personal_sessions
) AS joined_data
WHERE (start_time = '{start_time}' AND end_time = '{end_time.time()}') OR (start_time < '{start_time}' AND end_time > '{end_time.time()}') OR (start_time > '{start_time}' AND end_time < '{end_time.time()}') OR (start_time <= '{start_time}' AND end_time > '{start_time}' AND end_time <= '{end_time.time()}') OR (start_time >= '{start_time}' AND start_time < '{end_time.time()}' AND end_time >= '{end_time.time()}')
)
ORDER BY trainer_id
) NATURAL JOIN Trainers"""
    cursor.execute(query)

    available_trainers = cursor.fetchall()

    if not available_trainers:
        return False

    for trainer in available_trainers:
        if trainer_id == trainer[0]: # if the trainer is still available for the new start and end times, they will appear in available_trainers
            return True
        
    return False

def update_maintenance():
    display_maintenances()

    query_maintenance = input("Please enter the ID of the maintenance record you would like to update: ")
    next_service = input("Please enter the next service date for this equipment (YYYY-MM-DD): ")
    
    query = f"UPDATE Maintenance_Equipment SET last_serviced_date = next_service_date, next_service_date = '{next_service}' WHERE maintenance_id = {int(query_maintenance)}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not update maintenance record')

def add_fitness_goal():
    new_goal_type = input("Enter a new fitness goal type: ")
    new_goal_description = input("Enter a description for the new goal: ")
    new_goal_value = input("Enter the goal's target value: ")

    query = f"INSERT INTO Fitness_Goals (member_id, goal_type, goal_description, goal_value, goal_achieved) VALUES ({globals()['curr_user_id']}, '{new_goal_type}', '{new_goal_description}', '{new_goal_value}', 'false')"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not add new fitness goal')

def delete_fitness_goal():
    delete_goal = input("Enter the goal type of the fitness goal you want to delete: ")
    query = f"DELETE FROM Fitness_Goals WHERE goal_type = '{delete_goal}' AND member_id = {globals()['curr_user_id']}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print(f"ERROR: Could not delete the {delete_goal} fitness goal")

def update_fitness_goal():
    goal_type = input("Enter the goal type of the goal you want to update (tip: you can view all your fitness goals in your dashboard): ").upper()
    display_goal(goal_type)

    print('What would you like to update?\n'
                  '1 - Fitness goal type\n'
                  '2 - Fitness goal description\n'
                  '3 - Fitness goal target value\n'
                  '4 - Fitness goal achieved\n'
                  '5 - Cancel\n')
    option = int(input())

    if option == 1:
        new_goal_type = input('Enter the new goal type: ')
        query = f"UPDATE Fitness_Goals SET goal_type = '{new_goal_type}' WHERE member_id = '{globals()['curr_user_id']}'"
    elif option == 2:
        new_goal_description = input('Enter the goal\'s new description: ')
        query = f"UPDATE Fitness_Goals SET goal_description = '{new_goal_description}' WHERE member_id = '{globals()['curr_user_id']}'"
    elif option == 3:
        new_goal_value = input('Enter the goal\'s new target value: ')
        query = f"UPDATE Fitness_Goals SET goal_value = '{new_goal_value}' WHERE member_id = '{globals()['curr_user_id']}'"
    elif option == 4:
        goal_achieved = input('Did you achieve this goal? Enter either true or false: ')
        query = f"UPDATE Fitness_Goals SET goal_achieved = {goal_achieved} WHERE member_id = '{globals()['curr_user_id']}'"
    elif option == 5:
        return

    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not complete fitness goal update')

def add_health_metric():
    new_metric_type = input("Enter a new health metric type: ")
    new_metric_value = input("Enter the metric's value: ")

    query = f"INSERT INTO Health_Metrics (member_id, metric_type, metric_value) VALUES ({globals()['curr_user_id']}, '{new_metric_type}', '{new_metric_value}')"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not add new health metric')

def delete_health_metric():
    delete_metric = input("Enter the metric type of the health metric you want to delete: ")
    query = f"DELETE FROM Health_Metrics WHERE metric_type = '{delete_metric}' AND member_id = {globals()['curr_user_id']}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print(f"ERROR: Could not delete the {delete_metric} health metric")

def update_health_metric():
    metric_type = input("Enter the metric type of the health metric you want to update (tip: you can view all your health metrics in your dashboard): ").upper()
    display_health_metric(metric_type)
    print('What would you like to update?\n'
                  '1 - Health metric type\n'
                  '2 - Health metric value\n'
                  '3 - Cancel\n')
    option = int(input())
    if option == 1:
        new_metric_type = input('Enter the updated health metric type: ')
        query = f"UPDATE Health_Metrics SET metric_type = '{new_metric_type}' WHERE member_id = '{globals()['curr_user_id']}'"
    elif option == 2:
        new_metric_value = input('Enter the metric\'s updated value: ')
        query = f"UPDATE Health_Metrics SET metric_value = '{new_metric_value}' WHERE member_id = '{globals()['curr_user_id']}'"
    elif option == 3:
        return
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not complete fitness goal update')

# function that inserts a new personal training session record into the the Personal_Sessions table
def add_personal_session(trainer_id, session_date, start_time, end_time, exercise_routine):
    query = f"INSERT INTO Personal_Sessions (member_id, trainer_id, session_date, start_time, end_time, exercise_routine) VALUES ({int(globals()['curr_user_id'])}, {int(trainer_id)}, '{session_date}', '{start_time}', '{end_time}', '{exercise_routine}')"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not schedule new personal training session')

def reschedule_personal_session():
    display_personal_sessions()

    query_session = input("Please enter the ID of the personal trianing session you'd like to reschedule: ")

    new_time = input("Please enter the new time that you'd like to reschedule your personal training session to (HH:MM:SS): ")
    new_duration = input("Please enter, in minutes, the duration you'd like this rescheduled personal training session to be: ")

    end_time = datetime.strptime(str(new_time), '%H:%M:%S')
    end_time = end_time + timedelta(minutes=int(new_duration))

    cursor.execute(f"SELECT trainer_id FROM Personal_Sessions WHERE session_id = {int(query_session)}")
    trainer_id = cursor.fetchone()[0]

    if (is_trainer_still_available(trainer_id, new_time, end_time)): # if the original trainer is still available, we can keep them as the trainer
        query = f"UPDATE Personal_Sessions SET start_time = '{new_time}', end_time = '{end_time.time()}' WHERE session_id = {int(query_session)}"
    else:
        if not display_available_trainers(new_time, end_time, new_duration):
            return
    
        new_trainer = input("Since your original trainer is not available for the updated time, please enter the ID of a new trainer for your personal training session:")
        query = f"UPDATE Personal_Sessions SET trainer_id = {int(new_trainer)}, start_time = '{new_time}', end_time = '{end_time.time()}' WHERE session_id = {int(query_session)}"

    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not reschedule the specified personal training session')

def delete_personal_session():
    display_personal_sessions()

    delete_session = input("Please enter the ID of the personal training session you'd like to cancel")
    query = f"DELETE FROM Personal_Sessions WHERE session_id = {int(delete_session)}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Unable to cancel the specified personal training session')

# function that allows Members to schedule a new personal training session with a trainer
def schedule_personal_session():
    start_time = input("What time are you looking to book your training session for? (HH:MM:SS): ")
    duration = input("How long, in minutes, would you like to schedule this training session for?: ")

    end_time = datetime.strptime(start_time, '%H:%M:%S')
    end_time = end_time + timedelta(minutes=int(duration))

    if not display_available_trainers(start_time, end_time, duration):
        return

    trainer_choice = input("Enter the ID of the trainer you wish to schedule with: ")
    exercise_routine = input("What exercice routine do you want to focus on today?: ")

    add_personal_session(trainer_choice, date.today(), start_time, end_time, exercise_routine)

def add_group_fitness_class():
    start_time = input("What time are you looking to create this group fitness class for? (HH:MM:SS): ")
    duration = input("How long, in minutes, would you like this group fitness class to be?: ")

    end_time = datetime.strptime(start_time, '%H:%M:%S')
    end_time = end_time + timedelta(minutes=int(duration))

    if not display_available_trainers(start_time, end_time, duration):
        return
    
    trainer_choice = input("Enter the ID of the trainer you wish to assign to this group fitness class: ")
    workout_type = input("What type of workout will this group fitness class consist of?: ")
    class_description = input("Add a short description regarding the details of this group fitness class: ")
    room_id = input("Enter the ID of the Room in which you want to book this class for: ")
    room_capacity = input("What is the room's capacity?: ")

    query = f"INSERT INTO Group_Fitness_Classes (class_date, start_time, end_time, trainer_id, workout_type, class_description, room_id, room_capacity, admin_id) VALUES ('{date.today()}', '{start_time}', '{end_time.time()}', {int(trainer_choice)}, '{workout_type}', '{class_description}', {int(room_id)}, {int(room_capacity)}, {globals()['curr_user_id']})"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not create new group fitness class')

def update_group_fitness_class():
    query = f"SELECT * FROM Group_Fitness_Classes"
    cursor.execute(query)

    classes = cursor.fetchall()
    print("Here are all the currently scheduled group fitness classes for today: \n")

    for c in classes:
        display_group_class(c)

    desired_class = input("Enter the ID of the group fitness class for which you want to update its information: ")

    print('What would you like to update?\n'
                  '1 - Start time\n'
                  '2 - Class duration\n'
                  '3 - Assigned trainer\n'
                  '4 - Class workout type\n'
                  '5 - Class description\n'
                  '6 - Class room location'
                  '7 - Cancel\n')
    option = int(input())
    if option == 1:
        new_start_time = input("Please enter an updated class start time (HH:MM:SS)")
        query = f"UPDATE Group_Fitness_Classes SET start_time = '{new_start_time}' WHERE class_id = {int(desired_class)}"
    elif option == 2:
        new_duration = input("Please enter, in minutes, an updated class duration: ")

        cursor.execute(f"SELECT start_time FROM Group_Fitness_Sessions WHERE class_id = {int(desired_class)}")
        temp_start_time = cursor.fetchone()[0]
        end_time = datetime.strptime(temp_start_time, '%H:%M:%S')
        end_time = end_time + timedelta(minutes=int(new_duration))
        
        query = f"UPDATE Group_Fitness_Classes SET end_time = '{end_time.time()}' WHERE class_id = {int(desired_class)}"
    elif option == 3:
        cursor.execute(f"SELECT start_time, end_time FROM Group_Fitness_Classes WHERE class_id = {int(desired_class)}")
        start, end = cursor.fetchone()
        print(f"Start: {start}")
        print(f"End: {end}")
        end_time = datetime.strptime(str(end), '%H:%M:%S')
        if not display_available_trainers(start, end_time):
            print("ERROR: Unable to update the currently assigned trainer for this group fitness class")
            return 

        new_trainer = input("Please enter the ID of the new trainer you'd like to assign to this group fitness class: ")
        query = f"UPDATE Group_Fitness_Classes SET trainer_id = {int(new_trainer)} WHERE class_id = {int(desired_class)}"
    elif option == 4:
        new_workout_type = input("Please enter an updated workout type for this group fitness class: ")
        query = f"UPDATE Group_Fitness_Classes SET workout_type = '{new_workout_type}' WHERE class_id = {int(desired_class)}"
    elif option == 5:
        new_description = input("Please enter an updated description for this group fitness class: ")
        query = f"UPDATE Group_Fitness_Classes SET class_description = '{new_description}' WHERE class_id = {int(desired_class)}"
    elif option == 6:
        new_room = input("Enter the ID of the new room you'd like this class to be booked for: ")
        new_capacity = input("Enter the new capacity of the updated room: ")
        query = f"UPDATE Group_Fitness_Classes SET room_id = {int(new_room)}, room_capacity = {int(new_capacity)} WHERE class_id = {int(desired_class)}"  
    elif option == 7:
        return

    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not update group fitness class information')

def delete_group_fitness_class():
    query = f"SELECT * FROM Group_Fitness_Classes"
    cursor.execute(query)

    classes = cursor.fetchall()
    print("Here are all the currently scheduled group fitness classes for today: \n")

    for c in classes:
        display_group_class(c)

    delete_class = input("Please enter the ID of the group fitness class you'd like to cancel: ")

    cursor.execute(f"SELECT COUNT(*) FROM EnrollsIn WHERE class_id = {int(delete_class)}")
    curr_enrollment = cursor.fetchone()[0]

    if (curr_enrollment > 0):
        print(f"ERROR: Unable to cancel the selected group fitness class because there are {curr_enrollment} Members already committed to attending!")
        return

    query = f"DELETE FROM Group_Fitness_Classes WHERE class_id = {int(delete_class)}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print(f"ERROR: Could not delete the group fitness class with ID {delete_class}")

def enroll_in_group_class():
    query = f"SELECT * FROM Group_Fitness_Classes"
    cursor.execute(query)

    classes = cursor.fetchall()
    print("Here are all the currently scheduled group fitness classes for today: \n")

    for c in classes:
        display_group_class(c)

    desired_class = input("Enter the ID of the group fitness class you want to schedule: ")

    cursor.execute(f"SELECT COUNT(*) FROM EnrollsIn WHERE class_id = {int(desired_class)}")
    curr_enrollment = cursor.fetchone()[0]

    cursor.execute(f"SELECT room_capacity FROM Group_Fitness_Classes WHERE class_id = {int(desired_class)}")
    room_cap = cursor.fetchone()[0]
    
    if curr_enrollment+1 > room_cap:
        print('ERROR: Could not enroll in new group fitness class because its room is at capacity')
        return

    query = f"INSERT INTO EnrollsIn (member_id, class_id) VALUES ({globals()['curr_user_id']}, {int(desired_class)})"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not enroll in new group fitness class')

def add_bill():
    print("What type of bill are we creating? \n- MEMBERSHIP\n- PERSONAL SESSION\n- CREDIT")
    bill_type = input("Please enter the appropriate bill type: ")
    bill_member_id = input("Enter the ID of the member this bill is being created for: ")
    bill_amount = input("What is the amount (positive for debit, negative for credit) of this bill?: ")

    query = f"INSERT INTO Bills (admin_id, member_id, bill_type, bill_amount, bill_paid) VALUES ({globals()['curr_user_id']}, {int(bill_member_id)}, '{bill_type}', {bill_amount}, 'false')"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not add new bill')

def process_bill(user):
    fname, lname = user.split()
    cursor.execute(f"SELECT member_id FROM Members WHERE first_name = '{fname}' AND last_name = '{lname}'")
    member_id = cursor.fetchone()[0]

    query = f"SELECT * FROM Bills WHERE member_id = {member_id}"
    cursor.execute(query)

    bills = cursor.fetchall()
    print(f"Here is a list of all the bills corresponding to Member {fname} {lname}:\n")
    for bill in bills:
        display_bill(bill)

    query_bill = input("Please enter the ID of the bill you want to process: ")
    query = f"UPDATE Bills SET bill_paid = 'true' WHERE bill_id = {int(query_bill)}"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('\nERROR: Could not process bill')

def general_prompt(user_type):
    if user_type == 'USER':
        user_prompt()
    elif user_type == 'TRAINER':
        trainer_prompt()
    else:
        admin_prompt()
    return

def user_prompt():
    while 1:
        print(f"Welcome, Member {globals()['curr_user_name']}! Please select one of the below options:\n"
              '1 - View Personal Information\n'
              '2 - View Personal Dashboard\n'
              '3 - Update Personal Information\n'
              '4 - Update Fitness Goals\n'
              '5 - Update Health Metrics\n'
              '6 - Schedule a personal training session/group fitness class\n'
              '7 - Logout\n')
        option = int(input())

        if option == 1:
            display_user_info()
        elif option == 2:
            display_dashboard()
        elif option == 3:
            update_personal_information()
        elif option == 4:
            manage_fitness_goal()
        elif option == 5:
            manage_health_metric()
        elif option == 6:
            manage_schedule()
        elif option == 7:
            return

        print('\n----------------------------------------------------------------------------\n')
        
def trainer_prompt():
    while 1:
        print(f"Welcome, Trainer {globals()['curr_user_name']}! Please select one of the below options:\n"
              '1 - Personal Schedule Management\n'
              '2 - View Member Profile\n'
              '3 - Logout\n')
        option = int(input())
            
        if option == 1:
            update_availability()
        elif option == 2:
            query_user = input("Enter the full name of the member whose profile you want to view: ")
            view_member_profile(query_user)
        elif option == 3:
            return

        print('\n----------------------------------------------------------------------------\n')

def admin_prompt():
    while 1:
        print(f"Welcome, Admin {globals()['curr_user_name']}! Please select one of the below options:\n"
              '1 - Room Booking Management\n'
              '2 - Equipment Maintenance Monitoring\n'
              '3 - Class Schedule Updating\n'
              '4 - Billing and Payment Processing\n'
              '5 - Logout\n')
        option = int(input())

        if option == 1:
            manage_rooms()
        elif option == 2:
            manage_equipment_maintenance()
        elif option == 3:
            manage_class_schedule()
        elif option == 4:
            manage_billing()
        elif option == 5:
            return

        print('\n----------------------------------------------------------------------------\n')

# Q1 - function that retrieves and displays all records from the students table
def getAllStudents():
    query = 'SELECT * FROM students'
    cursor.execute(query)

    rows = cursor.fetchall()
    print("(student_id, first_name, last_name, email, enrollment_date)")
    for row in rows:
        print(row)

# Q2 - function that inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    query = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')"
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not insert new student record into students table')

# Q3 - function that updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    query = f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id}"
    try:
        cursor.execute(query)
        conn.commit()
    except psycopg2.errors.UniqueViolation as e:
        print(f'ERROR! Could not complete email update: {e}')
    except:
        print('ERROR: Could not complete email update')

# Q4 - function that deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    query = f'DELETE FROM students WHERE student_id = {student_id}'
    try:
        cursor.execute(query)
        conn.commit()
    except:
        print('ERROR: Could not delete student\'s record from the students table')

def run():
    while 1:
        print('Welcome to Step-Up Fitness! Please select one of the below options:\n'
              '1 - New User Registration\n'
              '2 - Returning User Login\n'
              '3 - Trainer Login\n'
              '4 - Admin Login\n'
              '5 - Exit\n')
        option = int(input())

        if option == 1:
            attributes = ['username', 'password', 'email', 'phone number', 'first name', 'last name', 'home #', 'street name', 'postal code']
            for i in range(len(attributes)):
                attributes[i] = input(f"Enter a {attributes[i]}: ")
            register_user(attributes[0], attributes[1], attributes[2], attributes[3], date.today(), attributes[4], attributes[5], attributes[6], attributes[7], attributes[8])
        elif option == 2:
            username = input("Username: ")
            password = input("Password: ")

            if authenticate_user(username, password):
                globals()['curr_user_type'] = 'USER'
                general_prompt('USER')
        elif option == 3:
            username = input("Username: ")
            password = input("Password: ")

            if authenticate_trainer(username, password):
                globals()['curr_user_type'] = 'TRAINER'
                general_prompt('TRAINER')
        elif option == 4:
            username = input("Username: ")
            password = input("Password: ")

            if authenticate_admin(username, password):
                globals()['curr_user_type'] = 'ADMIN'
                general_prompt('ADMIN')
        elif option == 5:
            break

        print('\n----------------------------------------------------------------------------\n')

# establish connection to database
try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
except psycopg2.OperationalError as e:
    print(f'Error: {e}')
    exit(1) # if we cannot even connect to the database, there's no point in proceeding with the rest of the application until the user fixes the connection parameters

# create a cursor from the connection
cursor = conn.cursor()

# main program execution
run()

# close the cursor and connection to the database
cursor.close()
conn.close()