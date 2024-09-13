#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#C-score calc lv 6
totgrades1=0
totgrades2=0
totgrades3=0


def best5(grades):
    credvol=15*5
    mark=grades*credvol
    return mark

def best3(grades):
    credvol=15*3
    mark=grades*credvol
    return mark

def best1(grades):
    credvol=15*1
    mark=grades*credvol
    return mark

for total in range(6):
    grades=int(input("best 90 credits in level 6:"))
    total+=1
    best5(grades)
    totgrades1+=best5(grades)
    if total>6:
        break
        
for total in range(10):
    grades=int(input("remaining lv 6 and 5:"))
    total+=1
    best3(grades)
    totgrades2+=best3(grades)
    if total>10:
        break
        
for total in range(8):
    grades=int(input("all lv 4"))
    total+=1
    best1(grades)
    totgrades3+=best1(grades)
    if total>8:
        break
        
        
c_score=(totgrades1+totgrades2+totgrades3)/1020

print(c_score)
        

