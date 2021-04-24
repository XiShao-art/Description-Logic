from DL_Engine import *
from utils import *
def ifComplete(ABox):
    for index in range(len(ABox)):
        # 第一二种情况
        if type(ABox[index]) is Sentence:
            return False


        # 第三种情况
        elif type(ABox[index]) is Role_Concept:
            if ABox[index].quntify == 'exist':
                return False
            # 第四种情况
            elif ABox[index].quntify == 'forAll':
                for index_2 in range(len(ABox)):
                    if type(ABox[index_2]) is Role:
                        # 存在forAll a 和 role(a, x)
                        if ABox[index_2].individual == ABox[index].individual:
                            return False
    return True

def ifOpen(ABox):
    if len(ABox) < 2:
        return True
    else:
        for i in range(len(ABox) - 1):
            for j in range(i + 1, len(ABox)):
                if type(ABox[i]) == type(ABox[j]):
                    if ABox[i].equalsButNegationOppsite(ABox[j]):
                        return False
    return True


def Tableau(ABox, flag=False):
    if ifComplete(ABox):
        return flag or ifOpen(ABox)

    else:
        for index in range(len(ABox)):
            # 第一二种情况
            if type(ABox[index]) is Sentence:
                # sentence 只有一个就把他分离出来
                if len(ABox[index].body) == 1:
                    ABox[index].body[0] = ABox[index].individual
                    ABox[index] = ABox[index].body[0]
                # 大于一个
                elif len(ABox[index].body) > 1:
                    # 第一种情况
                    if ABox[index].operations[0] == 'and':
                        temp_senetnce = ABox[index].copy()
                        temp_top = ABox[index].body[0].copy()

                        temp_senetnce.body.pop(0)
                        temp_senetnce.operations.pop(0)
                        ABox[index] = temp_senetnce
                        ABox.append(temp_top)
                        flag = flag or Tableau(ABox, flag)
                        break
                    # 第二种情况
                    elif ABox[index].operations[0] == 'or':
                        temp_senetnce = ABox[index].copy()
                        temp_top = ABox[index].body[0].copy()

                        temp_senetnce.body.pop(0)
                        temp_senetnce.operations.pop(0)
                        ABox[index] = temp_senetnce
                        ABox2 = ABox_copy(ABox)
                        ABox2[index] = temp_top
                        flag = flag or Tableau(ABox, flag) or Tableau(ABox2, flag)

                # 0个 有问题
                else:
                    print('sentence len zero error')
                    exit(1)


            # 第三种情况
            elif type(ABox[index]) is Role_Concept:
                if ABox[index].quntify == 'exist':
                    pass
                # 第四种情况
                elif ABox[index].quntify == 'forAll':
                    for index_2 in range(len(ABox)):
                        if type(ABox[index_2]) is Role:
                            # 存在forAll a 和 role(a, x)
                            if ABox[index_2].individual == ABox[index].individual:
                                return False



