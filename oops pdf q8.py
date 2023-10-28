# Write your code here :-)
class employee:
    def __init__(self, idp, namep, addressp, dob):
        self.__employeeid = idp
        self.__name = namep
        self.__address = addressp
        self.__dateofbirth = dob

    def getemployeeid(self):
        return self.__employeeid

    def setemployeeid(self, newid):
        self.__employeeid = newid


class salaryemployee(employee):
    def __init__(
        self, idp, namep, addressp, dob, monthlypaymentp, hours, holiday, pensionp
    ):
        super().__init__(self, idp, namep, addressp, dob)
        self.__monthlypayment = monthlypaymentp
        self.__hoursthismonth = hours
        self.__publicholiday = holiday
        self.__pension = pensionp

    def setpension(self, newpension):
        if newpension == True or newpension == False:
            self.__pension = newpension
            return True
        else:
            return False

    def getmonthlypayment(self):
        return self.__monthlypayment

    def gethoursthismonth(self):
        return self.__hoursthismonth

    def getpublicholiday(self):
        return self.__publicholiday


def calculatemonthlysalary(salaryemployee):
    totalbonuspayment = 0
    pubholidaybonus = 0
    pensioncut = 0
    hoursworked = 0
    payment = salaryemployee.getmonthlypayment()
    pubholiday = salaryemployee.getpublicholiday()
    pensionpayment = salaryemployee.getpension()
    hoursworked = salaryemployee.gethoursthismonth()
    if pubholiday == True:
        pubholidaybonus = 0.03 * payment
    if pensionpayment == True:
        pensioncut = 0.04 * payment
    if hoursworked >= 160:
        hoursbonus = 0.05 * payment
    totalbonuspayment = payment + pubholidaybonus + hoursbonus
    print("bonus payment ", str(totalbonuspayment))
    print("pension payment ", str(pensioncut))
    revisedmonthlypayment = (payment + pubholidaybonus + hoursbonus) - pensioncut
    return revisedmonthlypayment
