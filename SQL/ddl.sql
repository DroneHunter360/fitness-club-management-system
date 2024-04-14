DROP TABLE IF EXISTS Members CASCADE;
DROP TABLE IF EXISTS Phone;
DROP TABLE IF EXISTS Health_Metrics;
DROP TABLE IF EXISTS Fitness_Goals;

DROP TABLE IF EXISTS Trainers CASCADE;
DROP TABLE IF EXISTS Admin_Staff CASCADE;

DROP TABLE IF EXISTS Group_Fitness_Classes CASCADE;
DROP TABLE IF EXISTS Personal_Sessions;
DROP TABLE IF EXISTS Bills;
DROP TABLE IF EXISTS Maintenance_Equipment CASCADE;

DROP TABLE IF EXISTS EnrollsIn;
DROP TABLE IF EXISTS ResponsibleFor;

-- logically, when you sign up for fitness membership, ALL the below info. is required, thus none of the fields can be null
CREATE TABLE IF NOT EXISTS Members (
	member_id SERIAL PRIMARY KEY,
	member_username VARCHAR(20) UNIQUE NOT NULL,
	member_password VARCHAR(20) NOT NULL,
	email TEXT NOT NULL,
	join_date DATE NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	home_number INTEGER NOT NULL,
	street TEXT NOT NULL,
	postal_code VARCHAR(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS Phone (
	member_id INTEGER NOT NULL,
	phone_number VARCHAR(10) NOT NULL,
	PRIMARY KEY (member_id, phone_number),
	FOREIGN KEY (member_id) REFERENCES Members
);

CREATE TABLE IF NOT EXISTS Health_Metrics (
	member_id INTEGER NOT NULL,
	metric_type VARCHAR(20),
	metric_value VARCHAR(10),
	PRIMARY KEY (member_id, metric_type, metric_value),
	FOREIGN KEY (member_id) REFERENCES Members
);

CREATE TABLE IF NOT EXISTS Fitness_Goals (
	member_id INTEGER NOT NULL, 
	goal_type VARCHAR(20),
	goal_description TEXT,
	goal_value VARCHAR(20),
	goal_achieved BOOLEAN,
	PRIMARY KEY (member_id, goal_type, goal_description, goal_value, goal_achieved),
	FOREIGN KEY (member_id) REFERENCES Members
);

CREATE TABLE IF NOT EXISTS Trainers (
	trainer_id SERIAL PRIMARY KEY,
	trainer_username VARCHAR(20) UNIQUE NOT NULL,
	trainer_password VARCHAR(20) NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	start_availability TIME,
	end_availability TIME
);

CREATE TABLE IF NOT EXISTS Admin_Staff (
	admin_id SERIAL PRIMARY KEY,
	admin_username VARCHAR(20) UNIQUE NOT NULL,
	admin_password VARCHAR(20) NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Group_Fitness_Classes (
	class_id SERIAL PRIMARY KEY,
	class_date DATE,
	start_time TIME,
	end_time TIME,
	trainer_id INTEGER NOT NULL,
	workout_type VARCHAR(20) NOT NULL,
	class_description TEXT NOT NULL,
	room_id INTEGER,
	room_capacity INTEGER,
	admin_id INTEGER NOT NULL,
	FOREIGN KEY (trainer_id) REFERENCES Trainers,
	FOREIGN KEY (admin_id) REFERENCES Admin_Staff
);

CREATE TABLE IF NOT EXISTS Personal_Sessions (
	session_id SERIAL PRIMARY KEY,
	member_id INTEGER NOT NULL,
	trainer_id INTEGER NOT NULL,
	session_date DATE,
	start_time TIME,
	end_time TIME,
	exercise_routine VARCHAR(20),
	FOREIGN KEY (member_id) REFERENCES Members,
	FOREIGN KEY (trainer_id) REFERENCES Trainers
);

CREATE TABLE IF NOT EXISTS Bills (
	bill_id SERIAL PRIMARY KEY,
	admin_id INTEGER NOT NULL,
	member_id INTEGER NOT NULL,
	bill_type VARCHAR(20), -- what the bill is for (ex. personal session, member sign up, etc.)
	bill_amount INTEGER,
	bill_paid BOOLEAN,
	FOREIGN KEY (admin_id) REFERENCES Admin_Staff,
	FOREIGN KEY (member_id) REFERENCES Members
);

CREATE TABLE IF NOT EXISTS Maintenance_Equipment (
	maintenance_id SERIAL PRIMARY KEY,
	maintenance_summary TEXT NOT NULL,
	equipment_id SERIAL,
	equipment_name VARCHAR(20),
	last_serviced_date DATE,
	next_service_date DATE
);

CREATE TABLE IF NOT EXISTS EnrollsIn (
	member_id INTEGER NOT NULL, 
	class_id INTEGER NOT NULL,
	PRIMARY KEY (member_id, class_id),
	FOREIGN KEY (member_id) REFERENCES Members,
	FOREIGN KEY (class_id) REFERENCES Group_Fitness_Classes
);

CREATE TABLE IF NOT EXISTS ResponsibleFor (
	admin_id INTEGER NOT NULL,
	maintenance_id INTEGER NOT NULL, 
	PRIMARY KEY (admin_id, maintenance_id),
	FOREIGN KEY (admin_id) REFERENCES Admin_Staff,
	FOREIGN KEY (maintenance_id) REFERENCES Maintenance_Equipment
);