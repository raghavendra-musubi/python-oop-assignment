
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

    def __init__(self, full_name, age, gender, email, phone, roll_num, hours_worked, hourly_wage):
        super.__init__(self, full_name, age, gender, email, phone, roll_num)
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage

    def calculate_pay(self):
        return self.hourly_wage * self.hours_worked

# class for school students
class Student(SchoolMember):

    def __init__(self, full_name, age, gender, email, phone, roll_num, score):
        super.__init__(self, full_name, age, gender, email, phone, roll_num)
        self.score = score #score out of 10

    def is_pass(self):
        if self.score > 7:
            return True
        else:
            return False

# class for teachers in the school
class Teacher(SchoolMember):

    def __init__(self, full_name, age, gender, email, phone, roll_num, weekly_salary, weeks_worked):
        super.__init__(self, full_name, age, gender, email, phone, roll_num)
        self.weekly_salary = weekly_salary
        self.weeks_worked = weeks_worked

    def total_salary(self):
        return self.weekly_salary * self.weeks_worked
