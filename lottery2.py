
import random

#array = ["0"] * 80

#counter = ["0"] * 80

def gen_random_array2(array,counter):
  for i in range(1,len(array)+1):
    #print("index = ", i-1)
    while True:
      n = random.randint(1,len(counter)) # n = 1->
      #print(n)    
      if (int(counter[n-1]) == 0):
          break
    counter[n-1] = "1"
    #print(n,counter[n-1])
    array[i-1] = n
  print(array)