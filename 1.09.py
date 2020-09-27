num1,num2 = input("Enter 2 positive integer").split()

for i in range(int(num1),int(num2),3):
  print(i)
  print(id(i))
  i = "counting " + str(i)
  print(i)
  print(id(i))


