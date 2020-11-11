from pyswip import Prolog,registerForeign

factsDic={}
def verify(Question):
    if Question in factsDic:
        if factsDic[Question]=='y':
            return 1
        if factsDic[Question]=='n':
            return 0
    else:
        print('Does the animal has the attribute :',Question,'(y/n)?')
        Response = input()
        if Response == 'y':
            factsDic[Question]='y'
            return 1
        else:
            factsDic[Question]='n'
            return 0
verify.arity=1        

registerForeign(verify)
prolog = Prolog()
prolog.consult('animalPy.pl')
for soln in prolog.query("hypothesize(X)"):
    print("This animal is:",soln["X"])