INSERT INTO Members (member_username, member_password, email, join_date, first_name, last_name, home_number, street, postal_code) VALUES
('member1', 'member1', 'steven.hua@carleton.ca', '2024-04-10', 'Steven', 'Hua', '123', 'Ironside Court', 'K2K1LC'),
('member2', 'member2', 'pallav.wadhwa@carleton.ca', '2024-04-01', 'Pallav', 'Wadhwa', '11', 'Michelin Street', 'K2E3C2'),
('member3', 'member3', 'clint.galvez@carleton.ca', '2024-04-05', 'Clint', 'Galvez', '24', 'Parkway Street', 'K1L4Y2'),
('member4', 'member4', 'justin.ly@carleton.ca', '2024-04-05', 'Justin', 'Ly', '19', 'Cedarview Drive', 'K2K4C2'),
('member5', 'member5', 'rodney.raven@carleton.ca', '2024-03-12', 'Rodney', 'Raven', '123', 'Colonel By Drive', 'K3W2C4');

INSERT INTO Phone (member_id, phone_number) VALUES
(1, '6137953598'),
(1, '6139093305'),
(2, '6136572384'),
(3, '6138887465'),
(3, '4379872543'),
(4, '6139874567'),
(5, '6131238576');

INSERT INTO Trainers (trainer_username, trainer_password, first_name, last_name, start_availability, end_availability) VALUES
('trainer1', 'trainer1', 'Damien', 'Hood', '07:00:00', '15:00:00'),
('trainer2', 'trainer2', 'Dawei', 'Zhang', '12:00:00', '15:30:00'),
('trainer3', 'trainer3', 'Evan', 'Pierce', '09:00:00', '12:00:00'),
('trainer4', 'trainer4', 'Fatemeh', 'Banaeizadeh', '09:00:00', '17:00:00'),
('trainer5', 'trainer5', 'Matia', 'Raspopovic', '09:00:00', '17:00:00'),
('trainer6', 'trainer6', 'Michelle', 'Murphy', '09:00:00', '17:00:00'),
('trainer7', 'trainer7', 'Mihai', 'Sirbu', '09:00:00', '17:00:00'),
('trainer8', 'trainer8', 'Mohumed', 'Dahir', '09:00:00', '17:00:00'),
('trainer9', 'trainer9', 'Raymond', 'Chan', '09:00:00', '17:00:00'),
('trainer10', 'trainer10', 'Rhythm', 'Shah', '09:00:00', '17:00:00'),
('trainer11', 'trainer11', 'Shubh', 'Patel', '09:00:00', '17:00:00'),
('trainer12', 'trainer12', 'Henry', 'Vo', '09:00:00', '17:00:00'),
('trainer13', 'trainer13', 'Victor', 'Litzanov', '09:00:00', '17:00:00'),
('trainer14', 'trainer14', 'Vikrant', 'Kumar', '09:00:00', '17:00:00'),
('trainer15', 'trainer15', 'Raha', 'Rashid', '09:00:00', '17:00:00'),
('trainer16', 'trainer16 ', 'Gabe', 'Martell', '09:00:00', '17:00:00');

INSERT INTO Admin_Staff (admin_username, admin_password, first_name, last_name) VALUES
('admin1', 'admin1', 'Ahmed', 'El-Roby'),
('admin2', 'admin2', 'Abdelghny', 'Orogat');

INSERT INTO Group_Fitness_Classes (class_date, start_time, end_time, trainer_id, workout_type, class_description, room_id, room_capacity, admin_id) VALUES
('2024-04-13', '09:30:00', '10:30:00', 1, 'CARDIO', 'Intensive 60 minute, full-body cardio group session', 1, 2, 1),
('2024-04-13', '10:00:00', '10:30:00', 2, 'CORE', '30 minute HIIT workout, focusing on building core abdominal strength', 2, 35, 2),
('2024-04-13', '13:00', '14:00:00', 5, 'LOWER BODY', '60 minute lower boy workout', 3, 15, 2);

INSERT INTO Maintenance_Equipment (maintenance_summary, equipment_name, last_serviced_date, next_service_date) VALUES
('Perform annual servicing of chest press machine', 'Chest Press', '2023-04-13', '2024-04-13'),
('Perform annual servicing of smith machine', 'Smith Machine 1', '2024-04-01', '2025-04-01'),
('Fix broken hinge on bench', 'Bench 1', '2024-04-01', '2025-04-01');

INSERT INTO Fitness_Goals (member_id, goal_type, goal_description, goal_value, goal_achieved) VALUES
(1, 'WEIGHT', 'Decrease body weight to 170lbs', '170', false),
(1, 'RUNNING PACE', 'Run 3km in under 30 minutes', '30', false),
(1, 'CYCLING', 'Cycle 500km this week', '500', false);

INSERT INTO Health_Metrics (member_id, metric_type, metric_value) VALUES
(1, 'HEART RATE', '60bpm'),
(1, 'HEIGHT', '180cm'),
(1, 'WEIGHT', '170lbs'),
(1, 'BLOOD TYPE', 'O-'),
(1, 'CHOLESTEROL LEVEL', '150mg/dL');

INSERT INTO Personal_Sessions (member_id, trainer_id, session_date, start_time, end_time, exercise_routine) VALUES
(1, 1, '2024-04-13', '10:00:00', '11:00:00', 'LEG TONING'),
(1, 1, '2024-04-13', '15:30:00', '16:30:00', 'MUSCLE STRETCHING'),
(2, 2, '2024-04-13', '13:00:00', '14:00:00', 'BICEP GROWTH');

INSERT INTO EnrollsIn (member_id, class_id) VALUES 
(1, 1),
(1, 2),
(2, 1);