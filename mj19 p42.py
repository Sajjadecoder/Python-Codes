class ExaminationPaper():
    def __init__(self,centreNo,candidateNo):
        self.__FinalMark = 0
        self.__Grade = "Fail"
        self.__PaperID = centreNo + candidateNo
    def GetGrade(self):
        return self.__Grade
    def GetPaperID(self):
        return self.__PaperID
    def GetFinalMark(self):
        return self.__FinalMark
    def SetFinalMark(self,Mark):
        if int(Mark) >= 0 and int(Mark) <=90:
            self.__FinalMark = Mark
            return True
        else:
            print("enter valid marks")
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
    centre = input("enter a centre number ")
    cand = input("enter a candidate number ")
    Mark = int(input("enter marks "))
    ThisPaper = ExaminationPaper(centre,cand)
    ThisPaper.SetFinalMark(Mark)
    ThisPaper.SetGrade(80,70,55)
    print (ThisPaper.GetGrade())

Main()