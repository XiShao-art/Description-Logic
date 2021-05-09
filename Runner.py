from Reasoning import *
if __name__ =='__main__':
    # ∀r.∀s.A ⊓ ∃r.∀s.B ⊓ ∀r.∃s.C ⊑ ∃r.∃s.( A ⊓ B ⊓ C)
    TBox = {}  # TBox
    ABox = [NotEqualDic()]  # ABox with unequal relations

    rc1 = Role_Concept(quntify='forAll', role=Role('r'),concept=Role_Concept(quntify='forAll', role=Role('s'), concept=Concept('A')))  # ∀r.∀s.A

    rc2 = Role_Concept(quntify='exist', role=Role('r'),concept=Role_Concept(quntify='forAll', role=Role('s'), concept=Concept('B')))  # ∃r.∀s.B

    rc3 = Role_Concept(quntify='forAll', role=Role('r'),concept=Role_Concept(quntify='exist', role=Role('s'), concept=Concept('C')))  # ∀r.∃s.C

    op1 = Operation('and', left=rc1, right=rc2)  # ∀r.∀s.A ⊓ ∃r.∀s.B

    op2 = Operation('and', left=op1, right=rc3)  # ∀r.∀s.A ⊓ ∃r.∀s.B ⊓ ∀r.∃s.C

    c1 = Concept('A')  # A
    c2 = Concept('B')  # B
    c3 = Concept('C')  # C

    op3 = Operation('and', left=c1, right=c2)  # A ⊓ B
    op4 = Operation('and', left=op3, right=c3)  # A ⊓ B ⊓ C

    rc4 = Role_Concept(quntify='exist', role=Role('r'),concept=Role_Concept(quntify='exist', role=Role('s'), concept=op4))# ∃r.∃s.( A ⊓ B ⊓ C)

    op_containsTo = Operation('containsTo', left=op2, right=rc4)# ∀r.∀s.A ⊓ ∃r.∀s.B ⊓ ∀r.∃s.C ⊑ ∃r.∃s.( A ⊓ B ⊓ C)

    print(subsumptions(TBox, ABox, op_containsTo))  # subsumption
    #################################################################
    # ∀r.∀s.A ⊓ (∃r.∀s.¬A ⊔ ∀r.∃s.B) ⊑ ∀r.∃s.(A ⊓ B) ⊔ ∃r.∀s.¬B
    TBox = {}  # TBox
    ABox = [NotEqualDic()]  # ABox with unequal relations

    rc1 = Role_Concept(quntify='forAll', role=Role('r'),concept=Role_Concept(quntify='forAll', role=Role('s'), concept=Concept('A')))# ∀r.∀s.A

    rc2 = Role_Concept(quntify='exist', role=Role('r'),concept=Role_Concept(quntify='forAll', role=Role('s'), concept=Concept('A', negation=True)))# ∃r.∀s.¬A

    rc3 = Role_Concept(quntify='forAll', role=Role('r'),concept=Role_Concept(quntify='exist', role=Role('s'), concept=Concept('B')))# ∀r.∃s.B

    op1 = Operation('or', left=rc2, right=rc3)# ∃r.∀s.¬A ⊔ ∀r.∃s.B
    op2 = Operation('and', left=rc1, right=op1)# ∀r.∀s.A ⊓ (∃r.∀s.¬A ⊔ ∀r.∃s.B)

    c1 = Concept('A')  # A
    c2 = Concept('B')  # B
    op3 = Operation('and', left=c1, right=c2)  # A ⊓ B

    rc4 = Role_Concept(quntify='forAll', role=Role('r'),concept=Role_Concept(quntify='exist', role=Role('s'), concept=op3))# ∀r.∃s.(A ⊓ B)

    rc5 = Role_Concept(quntify='exist', role=Role('r'),concept=Role_Concept(quntify='forAll', role=Role('s'), concept=Concept('B', negation=True)))# ∃r.∀s.¬B

    op4 = Operation('or', rc4, rc5)# ∀r.∃s.(A ⊓ B) ⊔ ∃r.∀s.¬B

    op_containsTo = Operation('containsTo', left=op2, right=op4)# ∀r.∀s.A ⊓ (∃r.∀s.¬A ⊔ ∀r.∃s.B) ⊑ ∀r.∃s.(A ⊓ B) ⊔ ∃r.∀s.¬B

    print(subsumptions(TBox, ABox, op_containsTo))  # subsumption
################################################
# TBox = {ParentWithMax2Children ≡≤ 2HasChild.⊤};   ABox : HasChild(joe, ann) - HasChild(joe, eva) - HasChild(joe, mary) - ParentWithMax2Children(joe)
    TBox = {Concept('ParentWithMax2Children'):Role_Concept(number=2, quntify='less',role=Role('HasChild'),concept=Concept('top'))}
    ABox = [NotEqualDic()]
    r1 = Role('HasChild', 'joe', 'eva')
    r2 = Role('HasChild', 'joe', 'mary')
    r3 = Role('HasChild', 'joe', 'ann')
    C1 = Concept('ParentWithMax2Children','joe')
    ABox.extend([r1,r2,r3,C1])
    print(consistent(TBox,ABox))
