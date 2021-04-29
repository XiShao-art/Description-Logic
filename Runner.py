from Reasoning import *
if __name__ =='__main__':
    # >=3has.T and  <=1has,Female(a) and <=1has.-Female(a)
    TBox = {}
    ABox = [NotEqualDic()]
    #ABox.append(Role_Concept(number=0, quntify='greater', role=Role('has'), concept=Concept('top'), negation=True))
    rc1 = Role_Concept(number=3, quntify='greater', role=Role('has'), concept=Concept('top'))
    rc2 = Role_Concept(number=1, quntify='less', role=Role('has'), concept=Concept('Female'))
    rc3 = Role_Concept(number=1, quntify='less', role=Role('has'), concept=Concept('Female', negation=True))
    op1 =Operation('and',rc1,rc2)
    op2 = Operation('and', op1, rc3)

    print(satisfication(TBox, ABox, op2))