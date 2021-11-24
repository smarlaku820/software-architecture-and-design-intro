# Every software component (class, method or even a function) should have one and only one reason to change. 

# Reasons for change:
# 1.Change in the student id format
# 2.Change in the student name format
# 3.Change in the database backend,as adviced by the technical team.
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

    def save_student_info(self):
        # connect to a student db
        # persist the information inside the db.
        pass