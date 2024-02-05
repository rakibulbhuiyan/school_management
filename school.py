import json
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
                        value = input(f'Enter {userType}"s information for this feild,,Kindly enter stop to turminate {key}: ')
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
        # filter_final_list=[i for i in final if i] 
        file=open('data.json')
        data=json.load(file)
        return len(data[0]['hr']), len(data[1]['teacher']), len(data[2]['student'])
    
    def add_record(self):    
        while True:
            userType = input('Enter the user type:(or press stop to terminate :').lower()
            if userType =='stop':
                break
            else:
                input_no = int(input(f'How many {userType}s info you want to record? : ')) 
                record_list = self.__record(userType, input_no)
                print(record_list)        
                if userType=='hr':
                    file=open('data.json')
                    previaous_data=json.load(file)
                    previaous_data[0]['hr'].append(record_list)
                    file1=open('data.json','w')
                    new_data=str(previaous_data).replace("'",'"')
                    file1.write(new_data)
                    
                    # self.final[0].append(record_list)   
                elif userType=='teacher':
                    file=open('data.json')
                    previaous_data=json.load(file)
                    previaous_data[1]['teacher'].append(record_list)
                    file1=open('data.json','w')
                    new_data=str(previaous_data).replace("'",'"')
                    file1.write(new_data)
                              
                elif userType=='student':
                    file=open('data.json')
                    previaous_data=json.load(file)
                    previaous_data[2]['student'].append(record_list)
                    file1=open('data.json','w')
                    new_data=str(previaous_data).replace("'",'"')
                    file1.write(new_data)            
                else:
                    print('Invalid user name')
            return True
        # filter_final_list=[i for i in final if i] 
       

        