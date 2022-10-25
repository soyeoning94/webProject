#함수
def add_func(n1,n2):
    return n1+n2
def dob_func(n1,n2):
    return n1**n2
#전역
num1, num2, result=100,200,0
num3=3
#메인
result=add_func(num1,num2)
print(num1,"+",num2,"=",result)

result=dob_func(num1,num3)
print(num1,"^",num3,"=",result)
