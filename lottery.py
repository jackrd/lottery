import random;

array = ["0"] * 80

#陣列中產生不重複的數字寫到
def gen_random_array():
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
  #print(array)

gen_random_array()

p1 = array[:3]
print("p1=",p1)
p2 = array[0:3]
print("p2=",p2)
'''
p3 = array[9:]
print("p3=",p3)
p4 = array[:]
print("p4=",p4)
p5 = array[:]
print("p5=",p5)
p6 = array[:]
print("p6=",p6)
p7 = array[:]
print("p7=",p7)
p8 = array[:]
print("p8=",p8)
p9 = array[:]
print("p9=",p9)
p10 = array[:]
print("p10=",p10)
p11 = array[:]
print("p11=",p11)
p12 = array[:]
print("p12=",p12)
p13 = array[:]
print("p13=",p13)
p14 = array[:]
print("p14=",p14)
p15 = array[:]
print("p15=",p15)
p16 = array[:]
print("p16=",p16)
p17 = array[:]
print("p17=",p17)
p18 = array[:]
print("p18=",p18)
p19 = array[:]
print("p19=",p19)
p20 = array[:]
print("p20=",p20)
p21 = array[:]
print("p21=",p21)
'''


'''
for i in range(0,21):
  #print("print(","p",i,"=",",","p",i,")")
  #print("print(\"p1=\",p1)")
  print('p{i} = array[:]'.format(i=i+1))
  print('print("p{i}=",p{i})'.format(i=i+1))
'''  
'''
name = 'Jack'
text = 'world'

print('hello {name}, hello {text}'.format(name=name, text=text))
'''
'''        
int i = 1;
do{
  printf("%d\n", i);
  i = i + 1;
} while(i <= 3);

while True:
    print(i)
    i = i + 1
    if(i > 3):
        break
'''
