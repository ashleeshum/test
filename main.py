# define a list of numbers
list_numbers = [2,5,1,6,7,89,100,10]

for number in list_numbers:
  print("{}^2 = {}".format(number,number*number))
  if number%2 == 0:
      print("{} is even".format(number))
  else:
    print("{} is odd".format(number))