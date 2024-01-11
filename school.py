class School():
    def __init__(self, val) -> None:
        self.val = val
        self.final=[[],[],[]]

    def __record(self, userType : str,  input_no : int):

            self.info_list = []

            for j in range(input_no):

                info = {}

                print(f'\nPlease add a {userType}"s info. Kindly enter stop to turminate.')
                key = input(f'Enter first key: ')

                if key != "":
                    if userType=='hr':
                        add_id=len(self.final[0])
                    if userType=='teacher':
                        add_id=len(self.final[1])
                    if userType=='student':
                        add_id=len(self.final[2])
                    
                    while(key != "stop"):
                        add_id +=1
                        info['id']=add_id
                        value = input(f'Enter {userType}"s information for this feild ->{key}: ')
                        info[key] = value
                        key = input(f'Enter another key: ')

                if userType == 'hr' or userType == 'teacher':
                    salary = int(input('Enter salary: '))
                    info["Salary"] = salary
                    info["Dept"] = userType

                if userType == 'student' :
                    std_class = int(input('Enter class: '))
                    fathername = input('Enter Father"s name: ')
                    info["Class"] = std_class
                    info["Fathers_name"] = fathername
                
                if userType == 'student' or userType == 'teacher':
                    total_subject_no = int(input('Enter total subject no: '))
                    subject_list = []

                    for i in range(total_subject_no):
                        subject_list.append(input('Enter subject name: '))

                    info["Subjects"] = subject_list

                if userType == 'teacher' : 
                    total_class_no = int(input('Enter total class no: '))
                    class_list = []

                    for i in range(total_class_no):
                        class_list.append(input('Enter subject name: '))

                    info["Classes"] = class_list       
                
                self.info_list.append(info)
            return self.info_list  
 
    def total_info(self):    
        while True:
            userType = input('Enter the user type:(or press stop to terminate) :').lower()
            if userType =='stop':
                break
            else:
                input_no = int(input(f'How many {userType}s info you want to record? : ')) 
                record_list = self.__record(userType, input_no)
                print(record_list)
                if userType=='hr':
                    self.final[0].append(record_list)   
                if userType=='teacher':
                    self.final[1].append(record_list) 
                if userType=='student':
                    self.final[2].append(record_list) 
        # filter_final_list=[i for i in final if i] 
        return len(self.final[0]), len(self.final[1]), len(self.final[2])

        