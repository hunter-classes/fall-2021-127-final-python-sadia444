
------------------- Question 1 ----------------
## if the integers are increasing in order, then it will return 'True'. If it is not increasing in order, then it will return 'False'


def is_Increasing(integers):
  if integers[0]<integers[1]<integers[2]<integers[3]:
    return True
  else:
    return False


def tests():
  print(is_Increasing(2,3,4))
  print(is_Increasing(4,3,2))

def main():
  tests()

if __name__ == '__main__':
  main()




------------------- Question 2 ----------------
## will take a list of integers and will remove the comma, and then combine them

def num_convert(integers):
  for i in integer:
    i = str(i)
  combine = int(" ".join(i))
  return combine


def tests():
  print(1,2,3)

def main():
  tests()

if __name__ == '__main__':
  main()





------------------- Question 3 ----------------
## puts a binary number into the function and reutrns an ineger

def bin_convert("number"):
  conversion = []
  binary = str("number")
  
  for x in binary:
    if x = 1:
      conversion = coversion + x*x
    return conversion 




def tests():
  print(bin_convert(1))
  print(bin_convert(10))
  print(bin_convert(11))
  print(bin_convert(100))
def main():
  tests()

if __name__ == '__main__':
  main()










