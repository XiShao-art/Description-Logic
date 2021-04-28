from random import choice, randint
from DL_Engine import *
def ABox_copy( ABox):
    temp=[]
    for i in ABox:
        temp.append(i.copy())
    return temp

def getRandomIndividual():
    return choice(INDIVIDUALS) + str(randint(0, 90))

def ifContains(ABox, item):
    for ele in ABox:
        if type(ele) == type(item):

            if ele.equals(item) and ele.negation==item.negation:
                return True
    return False

def negate( item):
    v = item.copy()
    v.negation = not item.negation
    return v

def ABox_printer(ABox):
    for i in ABox:
        print(str(i))
    print('------------------------')

def noExistOtherPair(ABox, item: Role_Concept):
    role = item.role
    concept = item.concept
    for i in range(len(ABox)):
        if type(ABox[i])==Role and role.name==ABox[i].name and ABox[i].individual_pre==item.individual:
            temp_concept = concept.copy()
            temp_concept.individual = ABox[i].individual_post
            for j in range(len(ABox)):
                if ABox[j].equals(temp_concept):
                    return False
    return True

def getDicOfRoleConecpt(ABox,individual,role_, concept_):
    role_name=role_.name
    concept_name = concept_.name
    dictionary = {}
    for item in ABox:
        if type(item)==Role and item.name == role_name and item.individual_pre==individual:
            post_individual=item.individual_post
            for concept_item in ABox:
                if type(concept_item) == Concept and concept_item.name == concept_name and concept_item.individual == post_individual and (concept_.negation== concept_item.negation):
                    dictionary[post_individual] = []
                    dictionary[post_individual].append(item)
                    dictionary[post_individual].append(concept_item)
    return dictionary

def testAllNotEqual(notEqualDic,individual_list):
    for i in range(len(individual_list)-1):
        for j in range(i+1,len(individual_list)):
           # print(individual_list[i],notEqualDic[individual_list[j]])
            if individual_list[j]not in notEqualDic.dictionary.keys() or individual_list[i] not in notEqualDic.dictionary[individual_list[j]]:
                return False
    return True

def backTrack(keys,individual_list:list, start,number,notEqualDic, flag):
    if len(individual_list)==number:
       # print (testAllNotEqual(notEqualDic,individual_list), notEqualDic , individual_list)
        flag = flag or testAllNotEqual(notEqualDic,individual_list)
    for i in range(start,len(keys)):
        individual_list.append(keys[i])
        flag = flag or backTrack(keys, individual_list, i+1,number,notEqualDic, flag)
        individual_list.pop()
    return flag

def satisfy_number( number, dicOfRoleConecpt:dict, notEqualDic):
    keys = list(dicOfRoleConecpt.keys())
    if len(keys)<number:
        return False
    else:
        return backTrack(keys,individual_list=[], start=0,number=number,notEqualDic=notEqualDic, flag=False)


def generateNumberRoles(ABox, role_concept, individual):
    notEqualDic = None
    for item in ABox:
        if type(item) == NotEqualDic:
            notEqualDic = item
            break
    individuals = []
    for i in range(role_concept.number):
        individuals.append(getRandomIndividual())

    for i in range(role_concept.number):
        ABox.append(Role(role_concept.role.name,individual,individuals[i]))
        ABox.append(Concept(role_concept.concept.name, individuals[i]))
        notEqualDic.dictionary[individuals[i]]=[]
        for j in range(role_concept.number):
            if i!=j:
                notEqualDic.dictionary[individuals[i]].append(individuals[j])

    return ABox





def changeIndividual(ABox,originIn,newIn):
    for item in ABox:
        if type(item)==Role:
            if item.individual_pre==originIn:
                item.individual_pre=newIn
            if item.individual_post==originIn:
                item.individual_post=newIn

        if item.individual==originIn:
            item.individual=newIn

    return ABox

def B(start, list_, keys):
    for i in range(start,len(keys)):
        print(list_)
        list_.append(keys[i])
        B(i+1, list_, keys)
        list_.pop()
if __name__ == "__main__":
    notEqual = {}
    notEqual['a']=['b','c']
    notEqual['b'] = ['a', 'c']
    notEqual['c'] = ['a', 'b']
    keys = ['a','b','c','d','5','ad']
    print(backTrack(keys,[], 0,2,notEqual, False))