from utils import *


def subtituteOperation(op, TBox, key):
    if op.left!=None and op.right!=None:

        if op.left.signatureEquals(key):
            ifNegate = op.left.negation
            temp=TBox[key].copy()
            temp.individual = op.left.individual
            op.left =temp
            if ifNegate:
                op.left = negate(op.left)
        elif type(op.left) == Role_Concept:

            subtituteRole_Concept(op.left, TBox, key)
        else:
            subtituteOperation(op.left, TBox, key)
        if op.right.signatureEquals(key):
            ifNegate = op.right.negation
            temp=TBox[key].copy()
            temp.individual = op.right.individual
            op.right =temp
            if ifNegate:
                op.right = negate(op.right)
        elif type(op.right) == Role_Concept:

            subtituteRole_Concept(op.right, TBox, key)
        else:
            subtituteOperation(op.right, TBox, key)
def iteNegateOperation(op):
    if op.left!=None and op.right!=None:

        if type(op.left)==Operation and op.left.negation:
            op.left = negate(op.left)
            iteNegateOperation(op.left)
        elif type(op.right)==Operation and op.right.negation:
            op.right = negate(op.right)
            iteNegateOperation(op.right)

        elif type(op.left)==Role_Concept and op.left.negation:
            op.left = negate(op.left)
            iteNegateRole_Concept(op.left)
        elif type(op.right)==Role_Concept and op.right.negation:
            op.right = negate(op.right)
            iteNegateRole_Concept(op.right)



def iteNegateRole_Concept(role_Concept):
    if type(role_Concept.concept)==Operation and role_Concept.concept.negation:
        role_Concept.concept = negate(role_Concept.concept)
        iteNegateOperation(role_Concept)
    elif type(role_Concept.concept)==Role_Concept and role_Concept.concept.negation:
        role_Concept.concept = negate(role_Concept.concept)
        iteNegateRole_Concept(role_Concept)



def subtituteRole_Concept(role_Concept, TBox, key):
    if type(role_Concept.concept)==Concept:
      #  print(role_Concept.concept, key, role_Concept.concept.signatureEquals(key))
        if role_Concept.concept.signatureEquals(key):
            ifNegate = role_Concept.concept.negation
            temp=TBox[key].copy()
            temp.individual = role_Concept.concept.individual
            role_Concept.concept =temp
            if ifNegate:
                role_Concept.concept = negate(role_Concept.concept)
    elif type(role_Concept.concept) == Operation:
        subtituteOperation(role_Concept.concept, TBox, key)

    elif type(role_Concept.concept) == Role_Concept:

        subtituteRole_Concept(role_Concept.concept, TBox, key)




def expension(TBox, ABox):
    for item in range(len(ABox)):

        for key in TBox.keys():
            if ABox[item].signatureEquals(key):
                ifNegation = ABox[item].negation
                temp_new = TBox[key].copy()
                print(key, temp_new)
                temp_new.individual = ABox[item].individual
                ABox[item]= temp_new
              #  ABox_printer(ABox)
                if ifNegation:
                    ABox[item]=negate(ABox[item])

            elif type(ABox[item])==Operation:
                subtituteOperation(ABox[item], TBox, key)

            elif type(ABox[item])==Role_Concept:
                subtituteRole_Concept(ABox[item], TBox, key)

    return ABox

def toNNF(ABox):
    for item in range(len(ABox)):
       # print(ABox[item])
        if ABox[item].negation:
            ABox[item].negation=False
            ABox[item]=negate(ABox[item])
        elif type(ABox[item]) == Operation:
            iteNegateOperation(ABox[item])

        elif type(ABox[item]) == Role_Concept:
            iteNegateRole_Concept(ABox[item])

    return ABox

def preprocess(TBox, ABox):
    #加入top
    for i in ABox:
        if type(i)==Role:
            top = Concept('top',i.individual_pre)
            if not ifContains(ABox,top):
                ABox.append(top)

            top = Concept('top', i.individual_post)
            if not ifContains(ABox, top):
                ABox.append(top)
        elif i.individual!='':
            top = Concept('top', i.individual)
            if not ifContains(ABox, top):
                ABox.append(top)

    #用TBox 替换

    ABox = expension(TBox, ABox)


    #弄成NNF形式
    ABox = toNNF(ABox)
    #ABox_printer(ABox)

    return ABox


