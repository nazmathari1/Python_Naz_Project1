def alphabet(x):
    if x > 9:
     print("Wrong!")
    elif x < 1:
        print("Wrong!")
    else:
        print("Right!")
        print("End")
        x = 10
    return x

def main():
  x = 5
  x = alphabet(x)
  print (x)
  x = 101 % x
  print ("This is the reminder", x)
  if x is 1:
    print("correct - will try more complex math now :)")
    y = input("enter please")
    result = int(y) + x + 0.5
    print ("This is the result", result)
    result = math.ceil(result)
    print ("Again :)", result)
  else:
    print("something is wrong")

import math
if __name__ == "__main__":
   main()
