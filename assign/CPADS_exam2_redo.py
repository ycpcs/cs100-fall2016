_author__ = 'djhake2'

# for testing equality in floating point comparisons
DELTA = 0.1

# for setting/testing invalid course name
INVALID_COURSE = "invalid"

# TODO 1: finish the following function so that it accepts assignment grades
# TODO 1: and returns the average of the grades
# TODO 1: make sure to validate each grade (0 <= grade <= 150)
# TODO 1: the function should continue to accept assignment grades until a
# TODO 1: negative grade is entered
# TODO 1: return 0 if no valid grades are entered
def getAssignmentGrades():
    # use these variables in the function
    count = 0
    sum   = 0
    ave   = 0.0
    grade = 0

    # TODO 1: INSERT YOUR CODE HERE




    # return average of assignment grades
    print("Assignment average:", ave, "for", count, "grades")
    return ave


# TODO 2: finish the following the function so that it accepts the specified
# TODO 2: number of exam scores (numExams), drops the lowest exam grade, and returns
# TODO 2: the average of the remaining grades.
# TODO 2: make sure to validate each grade input (0 <= grade <= 115)
# TODO 2: the function should continue to request grades until four valid grades have
# TODO 2: been entered.
def getExamGrades(numExams):
    # use these variable in the function
    sum   = 0
    min   = 115
    ave   = 0.0
    grade = 0
    count = 0

    # TODO 2: INSERT YOUR CODE HERE






    # return the exam average
    print("Exam average:", ave, "for", numExams - 1, "highest grades, dropped", min)
    return ave


# TODO 3: finish the following function so that it calculates the course percentage
# TODO 3: and then assigns the appropriate course grade based on the exam average
# TODO 3: and course percentage.
def getCourseGrade(assignAve, examAve):
    # use these variables in the function
    coursePercent = 0.0
    courseGrade   = 0.0

    # TODO 3: INSERT YOUR CODE HERE






    # return the course grade
    print("Course percentage:", coursePercent, "  Course grade:", courseGrade)
    return courseGrade

# TODO 4: finish the following function so that it accepts the course name from the user
# TODO 4: it should accept 2 course names: CS101 and CS201 (with only that capitalization)
# TODO 4: the function should return the first valid course name the user enters
# TODO 4: give the user a maximum of MAX_ATTEMPTS tries at entering a valid course name
# TODO 4: if the user does not a valid course name within MAX_ATTEMPTS tries, return INVALID_COURSE
def getCourseName():
    # use these variables in the function
    MAX_ATTEMPTS = 3
    attempts     = 0
    name         = INVALID_COURSE

    # TODO 4: INSERT YOUR CODE HERE






    # return the course name
    print("Course name:", name)
    return name


# TODO 5: finish the following function so that it accepts the student ID from the user
# TODO 5: it should accept only valid student ID's (MIN_ID <= studentID <= MAX_ID)
# TODO 5: the function should return the first valid studentID the user enters
# TODO 5: the user can also enter a negative value to exit the function, which will be used by the
# TODO 5: main() routine to determine that the user is done entering grade data and is ready to exit
# TODO 5: DO NOT enforce maximum attempts in this function

def getStudentID():
    # use these variables in the function
    MIN_ID    = 903000000
    MAX_ID    = 903999999
    studentID = 0

    # TODO 5: INSERT YOUR CODE HERE






    # return the student ID
    print("Student ID:", studentID)
    return studentID



# main function for running grading program - called from testMain()
def main():
    # use the variable in main()
    numStudents = 0       # tracks # of students
    courseAve   = 0.0     # average of all course grades
    courseSum   = 0.0     # sum of all course grades
    courseMin   = 4.0     # minimum of all course grades
    courseMax   = 0.0     # maximum of all course grades

    # get the course name from the user
    courseName = getCourseName()

    # if user entered a valid course name, start accepting studentID's and grades
    if courseName != INVALID_COURSE:
        studentID = 0

        # TODO 6: Surround the applicable code below in a loop here so that the user can calculate the
        # TODO 6:    course grades for multiple students in one run of the program
        # TODO 6: also find the minimum, maximum and average COURSE grades and output them after the loop exits
        # TODO 6: the loop should run until the user enters a negative value for the student ID
        # TODO 6: you need to determine how much of the following code to indent under the loop you add

        # if the user did not "quit" (by entering a negative value)
        if studentID > 0:
            # get assignment grades for this student
            assignAve = getAssignmentGrades()

            # get exam grades for this student
            examAve = getExamGrades(4)

            # calculate the course grade for this student
            grade = getCourseGrade(assignAve, examAve)

            # TODO 6: INSERT YOUR CODE HERE to gather course grade statistics
            # TODO 6: stats to keep are course grade sum, min course grade, max course grade









            print("Course:", courseName, "Student ID:", studentID, "  Assign ave:", assignAve, "  Exam ave:", examAve, "  Course grade:", grade)
        else:
            print("Course:", courseName, "Done entering grades")

        # if there were any grades entered
        # output the grade statistics for the course
        if numStudents > 0:
            # TODO 6: INERT YOUR CODE HERE to calculate course grade average





            print("Course:", courseName, "Students:", numStudents, "Course ave:", courseAve, "Course min:", courseMin, "Course max:", courseMax)
        else:
            print("Course:", courseName, "No grades were entered")
    else:
        print("Invalid course")


#############################################################
#         DO NOT MODIFY ANY CODE BEYOND THIS POINT          #
#############################################################

# testing function - calls main() if 'run' is entered,
# otherwise continues in this function to test individual routines
def testMain():
    answer = input("Enter 'run' to run program, anything else to run test cases on the TODO's: ")

    if answer == "run":
        main()
        return

    testTODO = 1
    while (testTODO > 0):
        testTODO = int(input("Enter TODO # to test (<= 0 to exit): "))

        if testTODO == 1:
            actualValue   = getAssignmentGrades()
            expectedValue = float(input("Enter expected assignment average: "))

            if (actualValue >= expectedValue - DELTA) and (actualValue <= expectedValue + DELTA):
                print("TODO 1 test case passed:", actualValue, "=", expectedValue)
            else:
                print("TODO 1 test case failed:", actualValue, "!=", expectedValue)
        elif testTODO == 2:
            actualValue   = getExamGrades(4)
            expectedValue = float(input("Enter expected exam average: "))

            if (actualValue >= expectedValue - DELTA) and (actualValue <= expectedValue + DELTA):
                print("TODO 2 test case passed:", actualValue, "=", expectedValue)
            else:
                print("TODO 2 test case failed:", actualValue, "!=", expectedValue)
        elif testTODO == 3:
            assignAve = float(input("Enter assignment average: "))
            examAve   = float(input("Enter exam average: "))

            actualValue   = getCourseGrade(assignAve, examAve)
            expectedValue = float(input("Enter expected course grade: "))

            if (actualValue >= expectedValue - DELTA) and (actualValue <= expectedValue + DELTA):
                print("TODO 3 test case passed:", actualValue, "=", expectedValue)
            else:
                print("TODO 3 test case failed:", actualValue, "!=", expectedValue)
        elif testTODO == 4:
            actualValue   = getCourseName()
            expectedValue = input("Enter expected course name: ")

            if actualValue == expectedValue:
                print("TODO 4 test case passed:", actualValue, "=", expectedValue)
            else:
                print("TODO 4 test case failed:", actualValue, "!=", expectedValue)
        elif testTODO == 5:
            actualValue   = getStudentID()
            expectedValue = int(input("Enter expected student ID: "))

            if actualValue == expectedValue:
                print("TODO 5 test case passed:", actualValue, "=", expectedValue)
            else:
                print("TODO 5 test case failed:", actualValue, "!=", expectedValue)

        elif testTODO > 5:
            print("Invalid TODO, try again")


testMain()