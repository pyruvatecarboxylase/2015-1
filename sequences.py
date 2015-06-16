class sequences(object):

    def __init__(self,s1=None,s2=None):
        self.setsequence1(s1)
        self.setsequence2(s2)

    def setsequence1(self, sequence):
        self.__sequence1 = '-' + sequence

    def setsequence2(self, sequence):
        self.__sequence2 = '-' + sequence

    def getsequence1(self):
        return self.__sequence1

    def getsequence2(self):
        return self.__sequence2