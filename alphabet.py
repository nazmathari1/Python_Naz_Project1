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
if __name__ == "__main__":
   main()
