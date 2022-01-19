class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.all_course = []
        self.students = []
        
    def add_course(self, class_name, credit):
        newCourse = Course(class_name,credit)
        self.all_course.append(newCourse)
        return newCourse 
    
    def add_student(self, student):
        student.department_name = self.department_name
        self.students.append(student)

    
    
class Course:
    def __init__(self, class_name, credit):
        self.class_name = class_name
        self.credit = credit
        
    def __str__(self):
        return f"({self.class_name}: {self.credit}학점)"
    
class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.department_name = None
        self.course = []
        
    def enroll(self, class_name):
        self.course.append(class_name)
        
    def __str__(self):
        info = f"""이름 : {self.name} \n학과 : {self.department_name} \n학번 : {self.number} \n수강중인 강좌 : {" ".join(map(str, self.course))}"""
        return info
        
dept = Department("지능로봇공학과")  # 학과이름          
math1 = dept.add_course("미적분학", 3) #교과목 이름, 학점
coding = dept.add_course("정보기술 프로그래밍", 2)  

heo = Student("Heo Ju Young", 2021042042) #학생 이름, 학번
dept.add_student(heo)
heo.enroll(math1)
heo.enroll(coding)
print(heo)