class sequences(object):

    def __init__(self,s1=None,s2=None,substitution_number=None,deletion_number=None):
        self.setsequence1(s1)
        self.setsequence2(s2)
        self.setsubstitution_number(substitution_number)
        self.setdeletion_number(deletion_number)

    def setsequence1(self, sequence):
        self.__sequence1 = '-' + sequence

    def setsequence2(self, sequence):
        self.__sequence2 = '-' + sequence

    def getsequence1(self):
        return self.__sequence1

    def getsequence2(self):
        return self.__sequence2

    def setsubstitution_number(self, substitution_number):
        self.__substitution_number = substitution_number

    def setdeletion_number(self, deletion_number):
        self.__deletion_number = deletion_number

    def getsubstitution_number(self):
        return self.__substitution_number

    def getdeletion_number(self):
        return self.__deletion_number

