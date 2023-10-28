class Member:
    # PRIVATE MemberName, MemberID : string
    # PRIVATE SubscriptionPaid : boolean
    def __init__(self):
        self.__MemberName = ""
        self.__MemberID = ""
        self.__SubscriptionPaid = False

    def SetMemberName(self, MemberNameP):
        self.__MemberName = MemberNameP

    def SetMemberID(self, MemberIDP):
        self.__MemberID = MemberIDP

    def SetSubscriptionPaid(self, Paid):
        self.__SubscriptionPaid = Paid

class JuniorMember(Member):
    # PRIVATE DateOfBirth : String
    def __init__(self):
        super().__init__()
        self.__DateOfBirth = ""


    def SetDateOfBirth(self , dob):
        self.__DateOfBirth = dob

    def SetMemberName(self,MemberNameP):
        super().SetMemberName(MemberNameP)
    def SetMemberID(self , MemberIDP):
        super().SetMemberID(MemberIDP)
    def SetSubscriptionPaid(self,Paid):
        super().SetSubscriptionPaid(Paid)

NewMember = JuniorMember()
NewMember.SetMemberID("1247")
NewMember.SetSubscriptionPaid(True)
NewMember.SetDateOfBirth("11/07/2004")

NewMember.SetMemberName("Ahmed")

