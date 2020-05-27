
from lottery import gen_random_array
#from lottery2 import gen_random_array2

array = ["0"] * 80
counter = ["0"] * 255

gen_random_array(array)
#gen_random_array2(array,counter)

prize_num = ["3", "5", "5", "5", "2",
            "8", "5", "2", "3", "3", 
            "3", "2", "10", "3", "3", 
            "3", "5", "2", "3", "3","2"]

offset = 0
for i in range(0,len(prize_num)):
  size = int(prize_num[i],base = 10)
  #print(type(offset),type(size))
  end= offset+size
  #print(offset,end,size)
  array2 = array[offset:end]
  print('p{i} = {array2}'.format(i=i,array2=array2))
  offset = offset + size
  #print('p{i} = array2{array2}'.format(i=i, array2=array2)
  #offset = offset + size

'''
p1 = array[:3]
print("p1=",p1)
p2 = array[0:3]
print("p2=",p2)

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
