INDIVIDUALS = []
for i in range(97, 123):
    INDIVIDUALS.append(str(chr(i)))  # lowercase letters a to l


class Node:
    def __init__(self, name=''):
        self.name = name
        self.negation=False
        self.left = None
        self.right= None
        self.individual=''

class Concept(Node):
    def __init__(self, name='', individual='', negation = False):
        super().__init__(name)
        self.individual = individual
        self.negation = negation
    def signatureEquals(self,obj):
        return type(obj) == Concept and self.name == obj.name

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
    def totalEquals(self, obj):
        return self.equals(obj) and self.negation ==obj.negation


class Role(Node):
    def __init__(self, name='', individual_pre='', individual_post=''):
        super().__init__(name)
        self.individual_pre = individual_pre
        self.individual_post= individual_post

    def signatureEquals(self, obj):
        return type(
            obj) == Role and self.name == obj.name

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
    def totalEquals(self, obj):
        return self.equals(obj) and self.negation ==obj.negation


class Role_Concept(Node):
    def __init__(self, individual='', quntify='', role=None, concept = None,negation=False, number=0):
        super().__init__()
        self.quntify = quntify#exist or forAll
        self.role = role
        self.concept = concept # can be Concept or Role_Concept
        self.individual = individual
        self.number = number
        self.negation = negation


    def signatureEquals(self, obj):
        return type(obj)== Role_Concept and self.concept.signatureEquals(obj.concept)  and self.role.signatureEquals(obj.role) and self.quntify ==obj.quntify and self.number == obj.number

    def equals(self, obj):
        return type(obj)== Role_Concept and self.concept.equals(obj.concept) and self.individual == obj.individual and self.role.equals(obj.role) and self.quntify ==obj.quntify and self.number == obj.number

    def totalEquals(self, obj):
        return type(obj)== Role_Concept and self.concept.totalEquals(obj.concept) and self.individual == obj.individual and self.role.totalEquals(obj.role) and self.quntify ==obj.quntify and self.number == obj.number

    def equalsButNegationOppsite(self, obj):
        return self.equals(obj) and (self.negation == (not obj.negation))

    def copy(self):
        temp = Role_Concept()
        temp.negation=self.negation
        temp.name = self.name
        temp.quntify = self.quntify
        temp.individual = self.individual
        temp.role = self.role.copy()
        temp.concept = self.concept.copy()
        temp.number = self.number
        return temp

    def __str__(self):
        str_ = self.quntify+str(self.number)+'.'+self.role.name+' '+str(self.concept)+str(self.individual)+' '
        return str_


class Operation(Node):
    def __init__(self,name,left=None, right=None, negation=False):
        super().__init__()
        self.individual = ''
        self.name = name
        self.left = left
        self.right = right
        self.negation = negation

    def copy(self):
        temp = Operation(self.name)
        temp.individual = self.individual
        if self.left!=None:
            temp.left=self.left.copy()
        if self.right!=None:
            temp.right=self.right.copy()
        return temp

    def signatureEquals(self, obj):
        if type(obj)==Operation:
            if self.left != None and self.right != None and self.left != None and self.right != None:
                return self.name==obj.name and self.left.signatureEquals(obj.left) and self.right.signatureEquals(obj.right)
            else :
                return self.name==obj.name
        else:
            return False

    def equals(self, obj):
        if type(obj)==Operation:
            if self.left != None and self.right != None and self.left != None and self.right != None:
                return self.name==obj.name and self.left.equals(obj.left) and self.right.equals(obj.right) and self.individual==obj.individual
            else :
                return self.name==obj.name
        else:
            return False
    def totalEquals(self, obj):
        if type(obj) == Operation:
            if self.left != None and self.right != None and self.left != None and self.right != None:
                return self.name == obj.name and self.left.totalEquals(obj.left) and self.right.totalEquals(
                    obj.right) and self.individual == obj.individual
            else:
                return self.name == obj.name
        else:
            return False

    def __str__(self):
        return 'op_'+self.name+'('+str(self.left)+','+str(self.right)+')'+'['+self.individual+']'



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
        return False

    def signatureEquals(self, obj):
        return False

    def __str__(self):
        return str(self.dictionary)
    def totalEquals(self, obj):
        return self.equals(obj) and self.negation ==obj.negation




if __name__ =='__main__':
    a = {}
    a['a']=[]
    a['a'].append('b')
    a['b'] = []
    a['b'].append('c')
    print( list(a.keys())[0])