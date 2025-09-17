def age_check(base_age=49):
   print("Welcome to my Capstone Project Python script!")
   user_age = input("I'm 49 years old. Please tell me your age: ")
   
   age = int(user_age)
   if age > base_age:
       print("Hey, you're older than me!  Way to go, old-timer!")
   elif age < base_age:
       print("Hey, you're younger than me!  That's pretty cool!")
   else:
       print("Hey, you are 49 years old.  Just like me!")
       
   print("Thank you for telling me your age.  Talk to you again soon.")
    
age_check()
