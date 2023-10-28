#DECLARE StackPointer: INTEGER
#DECLARE StackData[0:9] OF Integer
global StackData
global StackPointer
StackData = [0]*10
StackPointer = 0

def outputall():
    global StackData
    global StackPointer
    for x in range(10):
        print(StackData[x])
    print (StackPointer)
def Push(value):
    global StackData
    global StackPointer
    if StackPointer > 9:
        return False
    else:
        StackData[StackPointer] = value
        StackPointer += 1
        return True
def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        value = StackData[StackPointer]
        StackData[StackPointer] = ""
        return int(value)

#Q2
class QuestionClass():
    #PRIVATE Question : STRING
    #PRIVATE Answer : STRING
    #PRIVATE DIfficulty : INTEGER
    def __init__(self,QuestionP,AnswerP,DifficultyP):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Difficulty = DifficultyP
    def GetQuestion(self):
        return self.__Question
    def GetDifficulty(self):
        return self.__Difficulty
    def GetAnswer(self):
        return self.__Answer

class QuizClass():
    # PRIVATE Questions:ARRAY [0:19] OF QuestionClass
    # PRIVATE NumberOfQuestions:INTEGER
    def __init__(self):
        self.__NumberOfQuestions = 0
        self.__Questions = [QuestionClass("","",0)]*20

    def AddQuestion(self,questionobject):
        if self.__NumberOfQuestions <20:
            self.__Questions[self.__NumberOfQuestions] = questionobject
            self.__NumberOfQuestions += 1
            return True
        else:
            return False
FirstQuiz = QuizClass()


Q = "What is 100/5"
A = "20"
D = "1"
Question1 = QuestionClass(Q,A,D)

x = FirstQuiz.AddQuestion(Question1)

#DECLARE numData[0:9] OF INTEGER
numData = [10,4,23,45,12,8,21,11,3,1]
def BubbleSort():
    global numData
    boundary = len(numData)-1
    noswaps = False
    while noswaps == False:
        noswaps = True
        for x in range(boundary):
            if numData[x]>numData[x+1]:
                temp = numData[x]
                numData[x] = numData[x+1]
                numData[x + 1] = temp
                noswaps = False
        boundary = boundary-1
BubbleSort()
print(numData)
def EvenNumber(numData):
    evencount = 0
    for x in range(len(numData)):
        if (numData[x] % 2) == 0:
            evencount +=1
    return evencount

print(EvenNumber(numData))
