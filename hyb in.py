class Person:
    def __init__(self, name):
        self.name = name


    def display_person(self):
        print(f"Name: {self.name}")
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


    def display_student(self):
        print(f"Student ID: {self.student_id}")
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name


    def display_sports_player(self):
        print(f"Sport Name: {self.sport_name}")


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        
        Person.__init__(self, name)
        self.student_id = student_id
        self.sport_name = sport_name
        self.college_name = college_name


    def display_college_student(self):
        print(f"College Name: {self.college_name}")
student = CollegeStudent("supritha", "1SW24EC001", "Cricket", "mrit")
student.display_person()
student.display_student()
student.display_sports_player()
student.display_college_student()
