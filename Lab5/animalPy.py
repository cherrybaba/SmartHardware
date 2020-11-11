from pyswip import Prolog,registerForeign

dic={}
def verify(Question):
    if Question in dic:
        if dic[Question]=='y':
            return 1
        if dic[Question]=='n':
            return 0
    else:
        print('Does the animal has the attribute :',Question,'?')
        Response = input()
        if Response == 'y':
            dic[Question]='y'
            return 1
        else:
            dic[Question]='n'
            return 0
verify.arity=1        

registerForeign(verify)
prolog = Prolog()
prolog.consult('animal.pl')
for soln in prolog.query("hypothesize(X)"):
    print("This animal is:",soln["X"])