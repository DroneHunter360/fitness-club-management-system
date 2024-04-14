# Health and Fitness Club Management System

Steven Hua\
101224771\
COMP 3005

### Overview
This application is a CLI-based program built with Python, Psycopg2, and PosstgreSQL. The application simulates a health and fitness club management system, catering to different users such as
members, trainers, and administrative staff. Different users have different operations they can perform; for example, members can schedule personal training sessions and administrative staff can 
create group fitness classes and add them to the overall class schedule. 

### File Structure
- The application itself lies in `main.py`
- The related ER model and relational schema are located in `Diagrams`
- The related database initialization scripts are located in `SQL`

### How to run the application
- Execute the ddl.sql script to initialize the database with all the related tables
- Execute the dml.sql script to populate the database with initial sample data

### Functionality
#### Member Functions
- User Registration
- Profile Management
- Personal Dashboard Display
- Schedule Management (schedule personal training sessions or enroll in group fitness classes)

#### Trainer Functions
- Schedule Management (setting availability)
- Member Profile Viewing (searching and viewing members by name)

### Administrative Staff Functions
- Room Booking Management
- Equipment Maintenance Monitoring
- Class Schedule Updating
- Billing and Payment Processing


