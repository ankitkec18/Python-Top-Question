a=20  # Global Variable 
def display():
          b=30  # Local variable 
          print("inside user-defined function :",a)
          print("local variable ",b)
display()
print("inside user-defined function :",a)
print("local variable ",b) # Gives Error 

    