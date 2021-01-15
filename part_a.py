
# parent class for all school members
class SchoolMember:
    
    def __init__(self, full_name, age, gender, email, phone, roll_num):
        self.full_name = full_name
        self.age = age
        self.gender = gender 
        self.email = email
        self.phone = phone
        self.roll_num = roll_num

# class for general staff in school
class Staff(SchoolMember):

    def __init__(self, full_name, age, gender, email, phone, roll_num, role, hours_worked, hourly_wage):
        SchoolMember.__init__(self, full_name, age, gender, email, phone, roll_num)
        self.role = role
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage

    def calculate_pay(self):
        return self.hourly_wage * self.hours_worked

# class for school students
class Student(SchoolMember):

    def __init__(self, full_name, age, gender, email, phone, roll_num, level, test_score):
        SchoolMember.__init__(self, full_name, age, gender, email, phone, roll_num)
        self.level = level
        self.test_score = test_score #score out of 10

    def is_pass(self):
        if self.test_score > 7:
            return True
        else:
            return False

# class for teachers in the school
class Teacher(SchoolMember):

    def __init__(self, full_name, age, gender, email, phone, roll_num, subject, weekly_salary, weeks_worked):
        SchoolMember.__init__(self, full_name, age, gender, email, phone, roll_num)
        self.subject = subject
        self.weekly_salary = weekly_salary
        self.weeks_worked = weeks_worked

    def total_salary(self):
        return self.weekly_salary * self.weeks_worked


# Some test cases
print("-----------------")
librarian = Staff('Miss Aruna', 38, 'F', 'aruna@school.edu', '+5543245', 0, 'Librarian' , 40, 20)
print('Name of Staff: ', librarian.full_name)
print('Role: ', librarian.role)
print('Total Pay: ',librarian.calculate_pay())

print("-----------------")
web_dev_student = Student('Luzitu', 40, 'M', 'luzitu@school.edu', '+8744783', 1, 'Sophomore', 5)
print('Name of Student: ', web_dev_student.full_name)
print('Level: ', web_dev_student.level)
print('Student passes?: ',web_dev_student.is_pass) 

print("-----------------")
python_teacher = Teacher('Samarth', 25, 'M', 'samarth@techis.io','+523451', 2, 'Python', 1200, 4)
print('Name of Teacher: ', python_teacher.full_name )
print('Subject taught: ', python_teacher.subject)
print('Total Salary: ', python_teacher.total_salary())




