# To complete this exercise, create an ER diagram based on what you've learned and the following qualities:
#A course has an attribute of department name
#A course has an attribute of course number
#A course has an attribute of a  start date
#A course has an attribute of whether it is open for  enrollment or closed
#A course has two other attributes of your choosing

import datetime

class Course:

    deptName = "CSE"
    courseNumber = 680
    startDate = datetime.datetime.now()
    enrollment = "open"
    location = "Houston"

compscience = Course()
print(compscience.deptName, compscience.courseNumber, compscience.startDate, compscience.enrollment, compscience.location)
