print("===============================================================")
print("             WELCOME TO SELF INTRODUCTION PROGRAM              ")
print("===============================================================")
name = input("enter your name: ")
print("hi " + name)
age = int(input("enter your age: "))
if age >= 18:
   print("not good age for built curreir you have to think at age of 14 to built your currier")
else:
   print("this is built your currier you are at right path")
while True:
    about_future = input("enter what you want to do in your life: ").strip()
    if about_future != "":
       print("work for your skills soon you achieve your goals")
       break
    else:
       print("want to be a bagger")
while True:
    job = input("enter your job: ").strip()
    if job != "":
        print("good job but you need to work hard")
        break
    else:
     print("died now you are not exist in world")
while True:
    hobby = input("enter your hobby: ").strip()
    if hobby != "gaming":
        print("good hobby but come in vs code")
        break
    else:
       print("not bad but it not make currier")
print("FINAL LINE: " + name + " is a " + str(age) + " year old boy who want to be " + about_future + " and his job is " + job + " and his hobby is " + hobby)