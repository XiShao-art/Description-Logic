# Description-Logic
assignment2 for CS213

1.  Implement a decision procedure for deciding consistency of an ABox in the description logic ALCQ (i.e., for the description logic ALC extended with qualified number restrictions). Input should consist of an ABox and a TBox, the output should be true or false (it is not necessary to specify a model should the ABox be consistent)
2. Implement a decision procedure for deciding subsumption in the description logic ALCQ. 
3. Use your implementation to proof that the following subsumptions are valid with respect to the empty TBox
   - ∀r.∀s.A ⊓ ∃r.∀s.B ⊓ ∀r.∃s.C ⊑ ∃r.∃s.(A ⊓ B ⊓ C)
   - ∀r.∀s.A ⊓ (∃r.∀s.¬A ⊔ ∀r.∃s.B) ⊑ ∀r.∃s.(A ⊓ B) ⊔ ∃r.∀s.¬B
4.  Given the TBox T = {P arentW ithM ax2Children ≡≤ 2HasChild.⊤}, use your implementation to determine if the following ABox is consistent with respect to T
   - HasChild(joe, ann)
   - HasChild(joe, eva)
   - HasChild(joe, mary)
   - ParentWithMax2Children(joe)