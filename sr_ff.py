# FUNCTION FOR AND GATE
def AND(a,b,c):
    return a&b&c
# FUNCTION FOR OR GATE
def OR(a,b):
    return a|b
# FUNCTION FOR NOT GATE
def NOT(z):
    return ~z+2
# FUNCTION FOR NOR GATE
def NOR(a,b):
    return NOT(OR(a,b))

S = int(input("Enter value of S = "))
R = int(input("Enter value of R = "))
Qp = int(input("Enter value of Previous Output = "))


o1 = AND(R,1,1)
o2 = AND(S,1,1)


if(o1 == o2 == 1):
    print("value of Next Output is = Intermediate")
else:
    o3 = NOR(o2,Qp)
    Qn = NOR(o1,o3)

    print("value of Next Output is = ",Qn)

