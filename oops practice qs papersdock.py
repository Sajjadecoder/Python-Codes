class TreasureChest:
    # PRIVATE question :string
    # PRIVATE answer :string
    # PRIVATE points : integer
    def __init__(self, q, a, p):
        self.question = q
        self.answer = a
        self.points = p

    def getQuestion(self):
        return self.question

    def checkAnswer(self, useranswer):
        if useranswer == self.answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.points)
        elif attempts == 2:
            totalpts = int(self.points // 2)
            return totalpts
        elif attempts == 3 or attempts == 4:
            totalpts = int(self.points // 4)
        else:
            return 0
