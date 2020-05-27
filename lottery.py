import random;

#陣列中產生不重複的數字寫到
def gen_random_array(array):
  for i in range(1,len(array)+1):
    #print("index = ", i-1)
    while True:
      array[i-1] = random.randint(1,80)    
      for j in range(1,i+1):
        if array[i-1] == array[j-1]:
          break
      if (j == i):
          break
    #print("index",i-1, " = ",array[i-1])
  print(array)

