from rules import Rules
from school import School

class HR(School,Rules): 
    def __init__(self, data) -> None:        
        self.__HR_data = data
        self.hr_name = data["name"]
        # print(self.hr_name[:3])
        super().__init__(3)
        self.totalHR, self.totalTeacher, self.totalStudent = self.total_info()
    
     
    def individualRules(self):
        rules = """
Compliance with Laws and Regulations:

Ensure compliance with local, state, and federal education laws and regulations.
Adhere to school board policies and guidelines.
Student Safety and Well-being:

Prioritize the safety and well-being of students.
Implement and enforce safety protocols, emergency procedures, and health guidelines.
Educational Standards:

Align curriculum and teaching methods with educational standards and objectives.
Monitor and assess academic performance and progress.
"""

    def TeachersalaryCount(self):
        print(self.a)
        return self.totalTeacher * 10000
    
    def HRsalaryCount(self):
        len(self.final[0])
        return self.totalHR * 8000
    
    def StudentFeesCount(self):
        return self.totalStudent * 3000
    
    def __total_revenew(self):
        return self.StudentFeesCount() - (self.TeachersalaryCount() + self.HRsalaryCount()) 

new_HR = {"name": "Sabrina","salary": 8000}
obj_hr = HR(new_HR)
obj_hr.add_record()
