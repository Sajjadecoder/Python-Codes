class QuizClass:
    #PRIVATE Questions:ARRAY [0:19] OF QuestionClass
    #PRIVATE numberofquestions : INTEGER
    def __init__(self):
        self.__numberofquestions = 0

    def AddQuestion(self,questionobj):
            if self.__numberofquestions < 20:
                self.__Questions[self.__numberofquestions] = questionobj
                self.__numberofquestions += 1
                return True
            return False
QuizClass = FirstQuiz()
Question1 = QuestionClass("What is 100/5","20",1)
FirstQuiz.AddQuestion(Question1)