from random import randint
import math

a = int( input ("Введите нижнюю границу: "))
b = int( input ("Введите верхнюю границу: "))
c = int( input ("Сколько ты хочешь? "))
 
l = []
l2 = []
l_2 = []
l3 = []
l_3 = []

for i in range(c):
    l.append(randint(a, b))
    
for i in l:    
    l2.append(i**2)

for i in l:    
    l_2.append(pow(i,-2))
    
for i in l:    
    l3.append(i**3)

for i in l:    
    l_3.append(pow(i,-3))

    
print('l = {}\nl2 = {}\nl_2 = {}\nl3 = {}\nl_3 = {}'.format(l, l2, l_2, l3, l_3))

like = str("Y") or str("N")
like = str( input( "Нравится? Y / N "))

while like == str("N"):
    n = float(input("В какую степень? Введите число: ")) 
    
    l_n = []
    
    for i in l:
        l_n.append(pow(i, n))
    
    print(l_n)
    like = str( input( "Доволен? Y / N "))
    
if like == str("Y"):
    print ('l = {}\nl2 = {}\nl_2 = {}\nl3 = {}\nl_3 = {}\nl_n = {}'.format(l, l2, l_2, l3, l_3, l_n))
