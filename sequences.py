class sequences(object):
    
    def __init__(self,s1=None,s2=None,substitution_constant=None,add_del_constant=None):
        self.setsequence1(s1)
        self.setsequence2(s2)
        self.setsubstitution_constant(substitution_constant)
        self.setadd_del_constant(add_del_constant)

    def setsequence1(self, sequence):
        self.__sequence1 = '-' + sequence

    def setsequence2(self, sequence):
        self.__sequence2 = '-' + sequence

    def getsequence1(self):
        return self.__sequence1

    def getsequence2(self):
        return self.__sequence2

    def setsubstitution_constant(self, substitution_constant):
        self.__substitution_constant = substitution_constant

    def setadd_del_constant(self, add_del_constant):
        self.__add_del_constant = add_del_constant

    def getsubstitution_constant(self):
        return self.__substitution_constant

    def getadd_del_constant(self):
        return self.__add_del_constant

