age = int(input("Enter your age : "))
if(age >=10 and age <=16):
  ans = input("Are you a student of the lab? : ").lower()
  if(ans == "yes"):
    print("You must be smart! ")
  else:
    print("You should join the lab! ")
elif(age < 10 or age >16 and age <20 ):
  print("That's the good age!")
else:
  print("You are a teenager!")