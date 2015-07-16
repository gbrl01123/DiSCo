class Question:
    """A question, its responses, and metadata"""
    def __init__(self, rowList = None):
        if (rowList is None):
            self.primarySubject = ""
            self.secondarySubject = ""
            self.family = ""
            self.difficulty = -1
            self.question = ""
            self.correctResponseIndex = -1
            self.responses = []
        else:
            self.primarySubject = rowList[0]
            self.secondarySubject = rowList[1]
            self.family = rowList[2]
            self.difficulty = rowList[3]
            self.question = rowList[4]
            self.correctResponseIndex = rowList[5]
            self.responses = rowList[6:]

    def stringRepresentation (self):
        listOut = [
            self.primarySubject,
            self.secondarySubject,
            self.family,
            str(self.difficulty),
            self.question,
            str(self.correctResponseIndex),
            str("\n".join(self.responses))
        ]
        return ("\n" .join(listOut))