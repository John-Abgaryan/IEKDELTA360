print "hello world," , "its amazing"
num1 = int(input("give the first number "))
num2 = int(input("give the second number "))
res=0
suma=0
while res==0:
      eq=int(input("select equation               |1 for + | 2 for - | 3 for * | 4 for / |"))
      if eq==1:
            suma=num1+num2
            res=1
      elif eq==2:
            suma=num1-num2
            res=1
      elif eq==3:
            suma=num1*num2
            res=1
      elif eq==4:
            suma=num1/num2
            res=1
      else:
            print "error, try again"

print "the sum is = ",suma
