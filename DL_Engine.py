
OPERATIONS = ['and', 'or', 'implies']
QUANTIFIES = ['exist', 'forAll']
INDIVIDUALS = []
CONCEPTS = []
#FUNCTIONS = []
ROLES = []

for i in range(97, 109):
    ROLES.append(str(chr(i)))  # lowercase letters m to z

for i in range(109, 123):
    INDIVIDUALS.append(str(chr(i)))  # lowercase letters a to l

# for i in range(65, 77):
#     FUNCTIONS.append(str(chr(i)))  # uppercase letters

for i in range(65, 91):
    CONCEPTS.append(str(chr(i)))  # uppercase letters

class Node:
    def __init__(self, name=None):
        self.name = name
        self.negation=False

class Concept(Node):
    def __init__(self,  name=None, a=None):
        super().__init__(name)
        self.individual = a

    def equals(self, obj):
        return self.name==obj.name and self.individual ==obj.individual

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))
    def copy(self):
        temp = Concept()
        temp.negation=self.negation
        temp.name = self.name
        temp.individual = self.individual
        return temp


class Role(Node):
    def __init__(self, name=None, a=None, b=None):
        super().__init__(name)
        self.individual_pre = a
        self.individual_post= b

    def equals(self, obj):
        return self.name==obj.name and self.individual_pre ==obj.individual_pre and self.individual_post == obj.name

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))

    def copy(self):
        temp = Role()
        temp.negation=self.negation
        temp.name = self.name
        temp.individual_pre = self.individual_pre
        temp.individual_post = self.individual_post
        return temp

class Sentence:
    def __init__(self):
        self.body = []
        self.operations = []
        self.individual = None

    def copy(self):
        temp = Sentence()
        for i in self.body:
            temp.body.append(i.copy())

        for i in self.operations:
            temp.body.append(i)
        temp.individual = self.individual
        return temp

class Role_Concept(Node):
    def __init__(self, a):
        super().__init__()
        self.quntify = ''#exist or forAll
        self.role = None
        self.concept = None # can be Concept or Role_Concept
        self.individual = a


    def equals(self, obj):
        return self.concept.equals(obj.concept) and self.individual == obj.individual and self.role.equals(obj.role) and self.quntify ==obj.quntify

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))

    def copy(self):
        temp = Role_Concept
        temp.negation=self.negation
        temp.name = self.name
        temp.quntify = self.quntify
        temp.individual = self.individual
        temp.role = self.role.copy()
        temp.concept = self.concept.copy()
        return temp




