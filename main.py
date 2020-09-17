#Author: Sarthak Singh sxs6666@psu.edu
#Collaborator:Joshua Chang jvc6690@psu.edu
# Section: 012R
# Breakout: 5

def sum_n(n):
  if n <= 0:
    return 0
  else:
    return n + sum_n(n -1)

def print_n(s,n):
  if n <= 0:
    return 
  else:
    print(s)
    print_n(s,n-1)



def run():
  number = int(input("Enter an int: "))
  print(f"sum is {sum_n(number)}.")
  word = input("Enter a string: ")
  print_n(word, number)

if __name__ == "__main__":
  run()