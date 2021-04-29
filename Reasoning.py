from Tableau import  *
from Preprocess import *
def RemoveContains(item):
    if item.left!=None and item.right!=None:
        if item.name =='containsTo':
            item.name='and'
            item.right = negate(item.right)
        else:
            RemoveContains(item.left)
            RemoveContains(item.right)

def subsumptions(TBox, ABox, subsumpt):
    ABox.append(subsumpt)
   # def
    #ABox_printer(ABox)
    for item in ABox:
        if type(item)==Operation:
            RemoveContains(item)
    for item in ABox:
        if type(item)!=NotEqualDic and item.individual=='':
            item.individual = getRandomIndividual()
            top = Concept('top',item.individual)
            if not ifContains(ABox, top):
                ABox.append(top)



    #ABox_printer(ABox)
    ABox = preprocess(TBox, ABox)
    return not Tableau(ABox)

def consistent(TBox, ABox):
    ABox = preprocess(TBox, ABox)
    return Tableau(ABox)

def satisfication(TBox, ABox, satisfy):

    ABox.append(satisfy)
    for item in ABox:
        if type(item) != NotEqualDic and item.individual == '':
            item.individual = getRandomIndividual()
            top = Concept('top', item.individual)
            if not ifContains(ABox, top):
                ABox.append(top)

    # ABox_printer(ABox)
    ABox = preprocess(TBox, ABox)
    return Tableau(ABox)

def instantiation(TBox, ABox, satisfy):
    satisfy.negation=True
    ABox.append(satisfy)
   # ABox_printer(ABox)
    for item in ABox:
        if type(item) == Operation:
            RemoveContains(item)
    for item in ABox:
        if type(item) != NotEqualDic and item.individual == '':
            item.individual = getRandomIndividual()
            top = Concept('top', item.individual)
            if not ifContains(ABox, top):
                ABox.append(top)

    # ABox_printer(ABox)
    ABox = preprocess(TBox, ABox)
    return Tableau(ABox)


