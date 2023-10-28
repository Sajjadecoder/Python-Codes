class ExaminationPaper():
    def __init__(self,CentreNum,CandidateNum):
        self.__FinalMark = 0
        self.__Grade = "Fail"
        self.__PaperID = CentreNum + CandidateNum

    def GetFinalMark(self):
        return self.__FinalMark
    def GetGrade(self):
        return self.__Grade
    def GetPaperID(self):
        return self.__PaperID
    def SetFinalMark(self,Mark):
        if Mark >=0 and Mark <= 90:
            self.__FinalMark = Mark
            return True
        else:
            return False
    def SetGrade(self,DistMark,MeritMark,PassMark):
        if self.__FinalMark >= DistMark:
            self.__Grade = "Distinction"
        elif self.__FinalMark >= MeritMark:
            self.__Grade = "Merit"
        elif self.__FinalMark >= PassMark:
            self.__Grade = "Pass"
        else:
            self.__Grade = "Fail"
def Main():
    centre = input("enter centre number: ")
    candidate = input("enter candidate number: ")
    thismark = int(input("enter the marks: "))
    ThisPaper = ExaminationPaper(centre,candidate)
    isvalid = ThisPaper.SetFinalMark(thismark)
    if isvalid == True:
        ThisPaper.SetGrade(80,70,55)
        print(ThisPaper.GetGrade())
    else:
        print("invalid marks entered")
Main()