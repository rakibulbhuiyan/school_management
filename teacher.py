from rules import Rules
from school import School

class Teacher(Rules):

    def __init__(self, data) -> None:        
        self.__teacher_data = data
        self.teacher_name = data["name"]
        self.teacher_contact_info = data["contact_info"]
        self.teacher_subjects = data["subjects"]

    def individualRules(self):
        rules = """
Professional Conduct:

Demonstrate professionalism in interactions with students, parents, colleagues, and administrators.
Uphold ethical standards and maintain the trust of the school community.
Curriculum and Lesson Planning:

Align lesson plans with curriculum standards and educational objectives.
Provide a well-organized and engaging learning experience for students.
Classroom Management:

Establish clear and consistent expectations for behavior in the classroom.
Implement effective classroom management strategies to create a positive learning environment.
"""





    

