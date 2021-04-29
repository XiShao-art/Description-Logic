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

                            #print(temp_concept,'complete')
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
                for item in ABox:
                    if type(item) == Role and item.name == ABox[index].role.name and item.individual_pre == ABox[
                        index].individual:
                        t1 = ABox[index].concept.copy()
                        t1.individual = item.individual_post
                        t2 = ABox[index].concept.copy()
                        t2.negation = not t1.negation
                        t2.individual = item.individual_post
                        # ABox_printer(ABox)
                        # print(t1,"?????")
                        if (not ifContains(ABox, t1)) and (not ifContains(ABox, t2)):
                            return False
                dicOfRoleConecpt = getDicOfRoleConecpt(ABox, ABox[index].individual, ABox[index].role,
                                                       ABox[index].concept)
                notEqualDic = None
                for item in ABox:
                    if type(item) == NotEqualDic:
                        notEqualDic = item
                        break

                # ABox contains n+1 pair
                if len(dicOfRoleConecpt.keys()) >= ABox[index].number + 1:
                    # if len(notEqualDic.dictionary) == 0:
                    #     return False
                    # else:
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
                if  satisfy_number(item.number + 1, dicOfRoleConecpt, notEqualDic) or item.number<0:
                    return False
            if type(item)==Concept and item.name=='top' and item.negation:
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
   # ABox_printer(ABox)
    if ifComplete(ABox, thre):
        # ABox_printer(ABox)
        # print(ifOpen(ABox, thre))
        # print('******************')


        return flag or ifOpen(ABox, thre)
    else:
        for index in range(len(ABox)):
            # 第一二种情况
            if type(ABox[index]) is Operation:
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

                  #  print( temp_top,ifContains(ABox,temp_top))
                    if (not ifContains(ABox,temp_senetnce)) and (not ifContains(ABox,temp_top)):
                        ABox2 = ABox_copy(ABox)
                        ABox.append(temp_senetnce)

                        ABox2.append(temp_top)

                        flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)
                        break


                # 0个 有问题
                else:
                    print('sentence len zero error')
                    exit(1)


            # 第三种情况
            elif type(ABox[index]) is Role_Concept:


                # 第四种情况
                if ABox[index].quntify == 'forAll':
                    for index_2 in range(len(ABox)):
                        if type(ABox[index_2]) is Role:
                            # 存在forAll a 和 role(a, x)

                            role = ABox[index_2]
                            temp_concept = ABox[index].concept.copy()
                            temp_concept.individual = role.individual_post
                            a=role.individual_pre == ABox[index].individual
                            b=role.name == ABox[index].role.name
                            c=not ifContains(ABox, temp_concept)

                            #print(str(temp_concept),' temp_concept')
                            if role.individual_pre == ABox[index].individual and role.name == ABox[index].role.name and not ifContains(ABox, temp_concept):

                                #print(1)
                                ABox.append(temp_concept)

                                flag = flag or Tableau(ABox, flag)

                                break

                elif ABox[index].quntify == 'less':

                    #如果有r(a,b) 但没有C(b) 或-C(b),就加
                    for item in ABox:
                        if type(item)==Role and item.name == ABox[index].role.name and item.individual_pre == ABox[index].individual:
                            t1 = ABox[index].concept.copy()
                            t1.individual = item.individual_post
                            t2 = ABox[index].concept.copy()
                            t2.negation = not t1.negation
                            t2.individual = item.individual_post
                            # ABox_printer(ABox)
                            # print(t1,"?????")
                            if (not ifContains(ABox,t1)) and (not ifContains(ABox,t2)):
                                print('??????????????')
                                ABox2 = ABox.copy()
                                ABox2.append(t2)
                                ABox.append(t1)

                                flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)
                                break

                    dicOfRoleConecpt = getDicOfRoleConecpt(ABox,ABox[index].individual,ABox[index].role, ABox[index].concept)
                    notEqualDic = None
                    for item in ABox:
                        if type(item) == NotEqualDic:
                            notEqualDic = item
                            break

                    #ABox contains n+1 pair
                    if len(dicOfRoleConecpt.keys())>=ABox[index].number+1:
                        if len(notEqualDic.dictionary)==0:
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
                                           # print(keys[i],keys[j])
                                            ABox2 = ABox_copy(ABox)
                                            ABox = changeIndividual(ABox, keys[i], keys[j])
                                            ABox2 = changeIndividual(ABox2,  keys[j],keys[i])
                                            # ABox_printer(ABox)
                                            # ABox_printer(ABox2)

                                            flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)

                elif ABox[index].quntify == 'exist' and noExistOtherPair(ABox, ABox[index]):
                    individual = getRandomIndividual()
                    top = Concept('top',individual)
                    if not ifContains(ABox, top):
                        ABox.append(top)
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
                # 大于等于
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
    return flag



