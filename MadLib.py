#MadLib.py
#Name:Nola Nelson
#Date:08/29/2025
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
place1 = input("Enter a place: ")
transportation1 = input("Enter a mode of transportation: ")
activity1 = input("Enter an activity: ")
food1 = input("Enter a food: ")
drink1 = input("Enter a drink: ")
home1 = input("Enter your hometown: ")
  #Print the story with the user supplied words.
print("I am going to "+place1+"!")
print("I am going to take a "+transportation1+" to get there.")
print("While I am at "+place1+", I am going to go "+activity1+".")
print("When I get there I am going to eat "+food1+".")
print("I will probably also get a "+drink1+".")
print("After the day is done, I will head back to "+home1+".")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
