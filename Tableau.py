
from utils import *

def ifComplete(ABox, thre):
    if len(ABox) >= thre:
        #print(len(ABox), thre)
        return True
    for index in range(len(ABox)):
        # 第一二种情况
        if type(ABox[index]) is Operation:

            if ABox[index].name == 'and':
                temp_senetnce = ABox[index].left.copy()
                temp_senetnce.individual = ABox[index].individual
                temp_top = ABox[index].right.copy()
                temp_top.individual = ABox[index].individual
                ifchange = False
                if not ifContains(ABox, temp_senetnce):

                    ifchange = True
                if not ifContains(ABox, temp_top):

                    ifchange = True
                if ifchange:
                    return False
            # 第二种情况
            elif ABox[index].name == 'or':
                temp_senetnce = ABox[index].left.copy()
                temp_senetnce.individual = ABox[index].individual
                temp_top = ABox[index].right.copy()
                temp_top.individual = ABox[index].individual

                # print( ( ifContains(ABox,temp_senetnce)) , ( ifContains(ABox,temp_top)))
                if (not ifContains(ABox, temp_senetnce)) and (not ifContains(ABox, temp_top)):
                    return False


            # 0个 有问题
            else:
                print('sentence len zero error')
                exit(1)


        # 第三种情况
        elif type(ABox[index]) is Role_Concept:
            if ABox[index].quntify == 'exist' and noExistOtherPair(ABox, ABox[index]):
                return False

            # 第四种情况
            elif ABox[index].quntify == 'forAll':
                for index_2 in range(len(ABox)):
                    if type(ABox[index_2]) is Role:
                        # 存在forAll a 和 role(a, x)

                        role = ABox[index_2]
                        temp_concept = ABox[index].concept.copy()
                        temp_concept.individual = role.individual_post
                        # print(str(temp_concept),' temp_concept')
                        if role.individual_pre == ABox[index].individual and role.name == ABox[
                            index].role.name and not ifContains(ABox, temp_concept):
                            # print(1)
                            return False
            elif ABox[index].quntify == 'greater':
                dicOfRoleConecpt = getDicOfRoleConecpt(ABox, ABox[index].individual, ABox[index].role,
                                                       ABox[index].concept)

                notEqualDic = None
                for item in ABox:
                    if type(item) == NotEqualDic:
                        notEqualDic = item
                        break
                if notEqualDic == None or not satisfy_number(ABox[index].number, dicOfRoleConecpt, notEqualDic):
                    return False

            elif ABox[index].quntify == 'less':
                dicOfRoleConecpt = getDicOfRoleConecpt(ABox, ABox[index].individual, ABox[index].role,
                                                       ABox[index].concept)
                notEqualDic = None
                for item in ABox:
                    if type(item) == NotEqualDic:
                        notEqualDic = item
                        break

                # ABox contains n+1 pair
                if len(dicOfRoleConecpt.keys()) >= ABox[index].number + 1:
                    if notEqualDic == None:
                        return False
                    else:
                        # 如果存在不相等 但是没有

                        if not satisfy_number(ABox[index].number + 1, dicOfRoleConecpt, notEqualDic):
                            return False
    return True

def ifOpen(ABox, thre):
    #print(1)
    if len(ABox) >= thre:
      #  print(len(ABox))
        return False
    if len(ABox) < 2:
        return True
    else:
        #自己不等于自己
        notEqualDic = None
        for item in ABox:
            if type(item) == NotEqualDic:
                notEqualDic = item
                break
        for item in ABox:
            # 有小于等于但是超过这么多
            if type(item)==Role_Concept and item.quntify=='less':
                dicOfRoleConecpt = getDicOfRoleConecpt(ABox, item.individual, item.role,
                                                       item.concept)
                #print( satisfy_number(item.number + 1, dicOfRoleConecpt, notEqualDic))
                if  satisfy_number(item.number + 1, dicOfRoleConecpt, notEqualDic):
                    return False

        for key in list(notEqualDic.dictionary.keys()):
            if key in notEqualDic.dictionary[key]:
                return False

        for i in range(len(ABox) - 1):


            for j in range(i + 1, len(ABox)):
                if type(ABox[i]) == type(ABox[j]) and type(ABox[i])!=Operation:
                    # 有对立的断言
                    if ABox[i].equalsButNegationOppsite(ABox[j]):
                        return False






    return True


def Tableau(ABox,  flag=False,thre=100):
    ABox_printer(ABox)
    if ifComplete(ABox, thre):


        return flag or ifOpen(ABox, thre)
    else:
        for index in range(len(ABox)):
            # 第一二种情况
            if type(ABox[index]) is Operation:
                # # sentence 只有一个就把他分离出来
                # if len(ABox[index].body) == 1:
                #     ABox[index].body[0].individual = ABox[index].individual
                #     ABox[index] = ABox[index].body[0]
                # # 大于一个
                # elif len(ABox[index].body) > 1:
                    # 第一种情况
                if ABox[index].name == 'and':
                    temp_senetnce = ABox[index].left.copy()
                    temp_senetnce.individual = ABox[index].individual
                    temp_top = ABox[index].right.copy()
                    temp_top.individual = ABox[index].individual
                    ifchange = False
                    if not ifContains(ABox, temp_senetnce):
                        ABox.append(temp_senetnce)
                        ifchange = True
                    if not ifContains(ABox, temp_top):
                        ABox.append(temp_top)
                        ifchange = True
                    if ifchange:
                        flag = flag or Tableau(ABox, flag)
                        break
                # 第二种情况
                elif ABox[index].name == 'or':
                    temp_senetnce = ABox[index].left.copy()
                    temp_senetnce.individual = ABox[index].individual
                    temp_top = ABox[index].right.copy()
                    temp_top.individual = ABox[index].individual

                    #print( ( ifContains(ABox,temp_senetnce)) , ( ifContains(ABox,temp_top)))
                    if (not ifContains(ABox,temp_senetnce)) and (not ifContains(ABox,temp_top)):
                        ABox.append(temp_senetnce)
                        ABox2 = ABox_copy(ABox)
                        ABox2.append(temp_top)
                        flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)
                        break


                # 0个 有问题
                else:
                    print('sentence len zero error')
                    exit(1)


            # 第三种情况
            elif type(ABox[index]) is Role_Concept:
                if ABox[index].quntify == 'exist' and noExistOtherPair(ABox, ABox[index]):
                    individual = getRandomIndividual()
                    temp_role = ABox[index].role.copy()
                    #for role
                    temp_role.individual_pre = ABox[index].individual
                    temp_role.individual_post= individual

                    #for concept
                    temp_concept = ABox[index].concept.copy()
                    temp_concept.individual = individual

                    ABox.append(temp_concept)
                    ABox.append(temp_role)
                    flag = flag or Tableau(ABox, flag)
                    break

                # 第四种情况
                elif ABox[index].quntify == 'forAll':
                    for index_2 in range(len(ABox)):
                        if type(ABox[index_2]) is Role:
                            # 存在forAll a 和 role(a, x)

                            role = ABox[index_2]
                            temp_concept = ABox[index].concept.copy()
                            temp_concept.individual = role.individual_post
                            #print(str(temp_concept),' temp_concept')
                            if role.individual_pre == ABox[index].individual and role.name == ABox[index].role.name and not ifContains(ABox, temp_concept):
                                #print(1)
                                ABox.append(temp_concept)

                                flag = flag or Tableau(ABox, flag)

                                break
                #大于等于
                elif ABox[index].quntify == 'greater':
                    dicOfRoleConecpt = getDicOfRoleConecpt(ABox,ABox[index].individual,ABox[index].role, ABox[index].concept)

                    notEqualDic = None
                    for item in ABox:
                        if type(item) == NotEqualDic:
                            notEqualDic=item
                            break
                    if notEqualDic == None or not satisfy_number(ABox[index].number, dicOfRoleConecpt, notEqualDic):
                        ABox = generateNumberRoles(ABox,ABox[index],  ABox[index].individual)#true or false
                        flag = flag or Tableau(ABox, flag)

                elif ABox[index].quntify == 'less':
                    dicOfRoleConecpt = getDicOfRoleConecpt(ABox,ABox[index].individual,ABox[index].role, ABox[index].concept)
                    notEqualDic = None
                    for item in ABox:
                        if type(item) == NotEqualDic:
                            notEqualDic = item
                            break

                    #ABox contains n+1 pair
                    if len(dicOfRoleConecpt.keys())>=ABox[index].number+1:
                        if notEqualDic ==None:
                            #如果不存在不相等
                            keys = list(dicOfRoleConecpt.keys())
                            for i in range(len(keys)-1):
                                for j in range(i+1,len(keys)):
                                    ABox2 = ABox.copy()
                                    ABox = changeIndividual(ABox,keys[i],keys[j])
                                    ABox2 = changeIndividual(ABox2, keys[j],keys[i])
                                    flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)
                        else:
                            #如果存在不相等 但是没有
                            if not satisfy_number( ABox[index].number+1, dicOfRoleConecpt, notEqualDic):
                                keys = list(dicOfRoleConecpt.keys())
                                for i in range(len(keys) - 1):
                                    for j in range(i+1, len(keys)):
                                        if keys[j] not in notEqualDic.dictionary.keys() or keys[i] not in notEqualDic.dictionary[keys[j]]:
                                            #print(keys[i],keys[j], list(dicOfRoleConecpt.keys()),*dicOfRoleConecpt[keys[j]])
                                            ABox2 = ABox_copy(ABox)
                                            ABox = changeIndividual(ABox, keys[i], keys[j])
                                            ABox2 = changeIndividual(ABox2,  keys[j],keys[i])
                                            # ABox_printer(ABox)
                                            # ABox_printer(ABox2)
                                            flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)



    return flag

if __name__ == '__main__':
    # #∀r.∀s.A ⊓ ∃r.∀s.B ⊓ ∀r.∃s.C ⊓ ∀r.∀s.(-A ⊔ -B ⊔ -C)
    # ABox = [NotEqualDic()]
    # A = Concept('A','')
    # B = Concept('B', '')
    # C = Concept('C', '')
    # r = Role('r','', '')
    # s = Role('s', '', '')
    # op_and1 = Operation('and')
    # op_or1 = Operation('or')
    #
    # op_or1.left = negate(A)
    # op_or1.right = Operation('or')
    # op_or1.right.left=negate(B)
    # op_or1.right.right = negate(C)
    #
    #
    # rc1_2 = Role_Concept('', 'forAll', s.copy(), A.copy())
    # rc1   = Role_Concept('', 'forAll', r.copy(), rc1_2.copy())
    #
    # rc2_2 = Role_Concept('', 'forAll', s.copy(), B.copy())
    # rc2 = Role_Concept('', 'exist', r.copy(), rc2_2.copy())
    #
    # rc3_2 = Role_Concept('', 'exist', s.copy(), C.copy())
    # rc3 = Role_Concept('', 'forAll', r.copy(), rc3_2.copy())
    #
    # rc4_2 = Role_Concept('', 'forAll', s.copy(), op_or1.copy())
    # rc4_2.copy()
    # rc4 = Role_Concept('', 'forAll', r.copy(), rc4_2.copy())
    #
    # op_and1.left = rc1
    # op_and1.right = Operation('and')
    # op_and1.right.left = rc2
    # op_and1.right.right = Operation('and')
    # op_and1.right.right.left = rc3
    # op_and1.right.right.right =rc4
    # op_and1.individual ='a'
    # ABox.append(op_and1)



    # #∀s.C(a), s(a,b), -C(b)
    # rc1 = Role_Concept('a')
    # rc1.role = Role('s',None, None)
    # rc1.concept = Concept('C', None)
    # rc1.individual = 'a'
    # rc1.quntify = 'forAll'
    #
    # role_s = Role('s','a','b')
    # concept_c = Concept('C', 'b')
    # concept_c.negation=True
    # ABox = [rc1, role_s, concept_c]
    #ABox=[]

    #r(a,b1),r(a,b2),r(a,b3), C(b1),C(b2),C(b3), <=4.r.C(a), allnotequal(b1,b2,b3)
    ABox = [NotEqualDic()]
    ABox[0].dictionary['b1'] = ['b2' ]
    ABox[0].dictionary['b2'] = ['b1', 'b3']
    ABox[0].dictionary['b3'] = ['b2']
    r1 = Role('r', 'a', 'b1')
    r2 = Role('r', 'a', 'b2')
    r3 = Role('r', 'a', 'b3')
    C1 = Concept('C', 'b1')
    C2 = Concept('C', 'b2')
    C3 = Concept('C', 'b3')
    rc1 = Role_Concept('a','less')
    rc1.role = Role('r','','')
    rc1.concept = Concept('C', '')
    rc1.number=1
    ABox.append(r1)
    ABox.append(r2)
    ABox.append(r3)
    ABox.append(C1)
    ABox.append(C2)
    ABox.append(C3)
    ABox.append(rc1)

    # r(a,b1),r(a,b2),r(a,b3), C(b1),C(b2),C(b3), <=4.r.C(a),>=5.r.C(a), allnotequal(b1,b2,b3)
    ABox = [NotEqualDic()]
    #ABox[0].dictionary['b1'] = ['b1']
    # ABox[0].dictionary['b2'] = ['b1', 'b3']
    # ABox[0].dictionary['b3'] = ['b2']
    r1 = Role('r', 'a', 'b1')
    r2 = Role('r', 'a', 'b2')
    r3 = Role('r', 'a', 'b3')
    C1 = Concept('C', 'b1')
    C2 = Concept('C', 'b2')
    C3 = Concept('C', 'b3')
    rc1 = Role_Concept('a', 'less')
    rc1.role = Role('r', '', '')
    rc1.concept = Concept('C', '')
    rc1.number = 4

    rc2 = Role_Concept('a', 'greater')
    rc2.role = Role('r', '', '')
    rc2.concept = Concept('C', '')
    rc2.number = 4

    ABox.append(r1)
    ABox.append(r2)
    ABox.append(r3)
    ABox.append(C1)
    ABox.append(C2)
    ABox.append(C3)
    ABox.append(rc1)
    ABox.append(rc2)

    print(Tableau(ABox))

