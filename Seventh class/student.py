# attribiute/variable, functions


class student:

    stu_name= ""
    stu_dept= ""

    def get_stu_info(self):
       return self.stu_name+"+self.stu_dept"


#create object

student = student()
student.stu_name ="joy"
student.stu_dept = "swe"
print(student.get_stu_info())
