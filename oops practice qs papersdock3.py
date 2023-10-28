class Lesson:
    # PRIVATE LessonType : string
    # PRIVATE Instructor : string

    def __init__(self, LessonTypeP, InstructorP):
        self.__LessonType = LessonTypeP
        self.__Instructor = InstructorP

    def GetLessonType(self):
        return self.__LessonType

    def GetInstructor(self):
        return self.__Instructor

    def SetLessonType(self, ltype):
        self.__LessonType = ltype

    def SetInstructor(self, ins):
        self.__Instructor = ins

    def GetFee(self, skill):
        if skill == "B":
            fee = 45
            return fee
        elif skill == "I":
            fee = 50
            return fee
        elif skill == "A":
            fee = 55
            return fee
        else:
            return -1


# Main program
LessonArray = []
for i in range(9):
    LessonArray.append(" ")
NewLesson = "Improve your serve"
NewInstructor = "David"
Lesson2 = Lesson(NewLesson, NewInstructor)
LessonArray[2] = Lesson2
print(LessonArray[2].GetLessonType())
print(LessonArray[2].GetInstructor())
