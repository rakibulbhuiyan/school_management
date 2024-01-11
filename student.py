from rules import Rules

class Student(Rules):
    def __init__(self, data) -> None: 
        self.student_data = data

    def individualRules(self):
        rules = """
Treat teachers, staff, and fellow students with courtesy and respect.
Avoid disruptive behavior that interferes with the learning of others.
Punctuality and Attendance:

Arrive on time for classes and other scheduled activities.
Attend classes regularly and notify the school if absent.
Uniform and Dress Code:

Adhere to the school's dress code and uniform policy.
Maintain personal hygiene and grooming standards.
Classroom Behavior:

Follow classroom rules and guidelines set by teachers.
Participate actively in class discussions and activities.
Homework and Assignments:

Complete and submit homework and assignments on time.
Seek help from teachers when needed to understand and complete assignments.
"""