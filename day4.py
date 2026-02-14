n=int(input("enter no of scores"))
scores=[0]*n

D=2

for i in range(n):
    m=int(input("enter score"))
    scores[i]=scores[i]+m

low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]

icount=0
rcount=0
validcount=0

for i in range(n):
    if (scores[i] < 0):
        icount += 1
    elif(scores[i]>=0):
        validcount+=1
        if(0<=scores[i]<=30):
            low_risk.append(scores[i])
        elif(31<=scores[i]<=60):
            medium_risk.append(scores[i])
        elif(61<=scores[i]<=100):
            high_risk.append(scores[i])
        else:
            critical_risk.append(scores[i])

print("Register Digit(D):",D)
print("Before Personalized Filtering:")
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)

if(D%2==0):
    rcount=len(low_risk)
    low_risk=[]
else:
    rcount=len(critical_risk)
    critical_risk=[]

print("After Personalized Filtering:")
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)

print("Total valid entries:",validcount)
print("Ignored entries:",icount)
print("Removed Due to Personalization:",rcount)