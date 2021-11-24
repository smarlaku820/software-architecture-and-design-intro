# Every software component (class, method or even a function) should have one and only one reason to change. 

# Loose coupling between handling students and student operations.
# Reason for change:
# 1. Change student details
class Student:
    def __init__(self):
        pass

    def get_student_id(self):
        # get the student id
        pass

    def set_student_id(self):
        # set the student id
        pass

    def get_student_address(self):
        # working with the student address
        pass

# Reason for change:
# 1. Change in the backend database.
class StudentRepository:
    def __init__(self):
        pass

    def save_student_info(self, student):
        # connect to a student db
        # persist the information inside the db.
        pass