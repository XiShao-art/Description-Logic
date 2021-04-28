
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
    def __init__(self, name=' '):
        self.name = name
        self.negation=False
        self.left = None
        self.right= None
        self.individual=''

class Concept(Node):
    def __init__(self,  name=' ', a=' '):
        super().__init__(name)
        self.individual = a

    def equals(self, obj):
        return type(obj)== Concept and self.name==obj.name and self.individual ==obj.individual

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))
    def copy(self):
        temp = Concept()
        temp.negation=self.negation
        temp.name = self.name
        temp.individual = self.individual
        return temp

    def __str__(self):
        str_ = ''
        if self.negation:
            str_ = '-'

        str_+=self.name+'('+self.individual+') '
        return str_


class Role(Node):
    def __init__(self, name=' ', a=' ', b=' '):
        super().__init__(name)
        self.individual_pre = a
        self.individual_post= b

    def equals(self, obj):
        return type(obj)== Role and self.name==obj.name and self.individual_pre ==obj.individual_pre and self.individual_post == obj.individual_post

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))

    def copy(self):
        temp = Role()
        temp.negation=self.negation
        temp.name = self.name
        temp.individual_pre = self.individual_pre
        temp.individual_post = self.individual_post
        return temp
    def __str__(self):
        str_ = ''
        str_+=self.name+'('+self.individual_pre+','+self.individual_post+') '
        return str_

# class Sentence(Node):
#     def __init__(self):
#         super().__init__()
#         self.body = []
#         self.operations = []
#         self.individual = ' '
#
#     def copy(self):
#         temp = Sentence()
#         for i in self.body:
#             temp.body.append(i.copy())
#
#         for i in self.operations:
#             temp.operations.append(i)
#         temp.individual = self.individual
#         return temp
#     def __str__(self):
#         str_=''
#         for i in range(len(self.operations)):
#             str_+=str(self.body[i])+' '+self.operations[i]+' '
#         str_+=str(self.body[-1])
#         str_ = str_+'('+str(self.individual)+') '
#         return str_
#     def equals(self, obj):
#         if not type(obj)== Sentence:
#             return False
#         flag = True
#         if len(obj.body)!=len(self.body):
#             return False
#         else:
#             for i in range(len(obj.operations)):
#                 flag = flag and obj.operations[i]==(self.operations[i]) and(obj.body[i].equals(self.body[i]))
#         flag = flag and obj.body[-1].equals(self.body[-1])
#         return   flag


class Role_Concept(Node):
    def __init__(self, a, quntify,role=None, concept = None ):
        super().__init__()
        self.quntify = quntify#exist or forAll
        self.role = role
        self.concept = concept # can be Concept or Role_Concept
        self.individual = a
        self.number = 0


    def equals(self, obj):
        return type(obj)== Role_Concept and self.concept.equals(obj.concept) and self.individual == obj.individual and self.role.equals(obj.role) and self.quntify ==obj.quntify

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))

    def copy(self):
        temp = Role_Concept(None, None)
        temp.negation=self.negation
        temp.name = self.name
        temp.quntify = self.quntify
        temp.individual = self.individual
        temp.role = self.role.copy()
        temp.concept = self.concept.copy()
        return temp

    def __str__(self):
        str_ = self.quntify+'.'+self.role.name+' '+str(self.concept)+str(self.individual)+' '
        return str_


class Operation(Node):
    def __init__(self,name):
        super().__init__()
        self.individual = ''
        self.name = name

    def copy(self):
        temp = Operation(self.name)
        temp.individual = self.individual
        if self.left!=None:
            temp.left=self.left.copy()
        if self.right!=None:
            temp.right=self.right.copy()
        return temp

    def equals(self, obj):
        if type(obj)==Operation:
            if self.left != None and self.right != None and self.left != None and self.right != None:
                return self.name==obj.name and self.left.equals(obj.left) and self.right.equals(obj.right)
            else :
                return self.name==obj.name
        else:
            return False

    def __str__(self):
        return 'op_'+self.name+'('+str(self.left)+','+str(self.right)+')'+'['+self.individual+']'

class QualifyNumber(Node):
    def __init__(self,name, qualify):
        super().__init__()
        self.qualify =qualify
        self.individual = ''
        self.name = name


class NotEqualDic(Node):
    def __init__(self):
        super().__init__()
        self.dictionary = {}
    def copy(self):
        temp = NotEqualDic()
        temp.dictionary = {}
        for key in self.dictionary.keys():
            temp.dictionary[key]=self.dictionary[key].copy()
        return temp

    def equals(self, obj):
        pass

    def __str__(self):
        return str(self.dictionary)




if __name__ =='__main__':
    a = {}
    a['a']=[]
    a['a'].append('b')
    a['b'] = []
    a['b'].append('c')
    print( list(a.keys())[0])