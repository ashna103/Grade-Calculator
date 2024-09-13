#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#total grade calc

Class = ""
Grade = input("How much did you get?")
Grade=float(Grade)
#%
total=float(input("Total:"))
for i in range(100):
    total_perc=Grade*total/100
    
Grade2 = input("How much did you get?")
Grade2=float(Grade2)
#%
total2=100-total
for i in range(100):
    total_perc2=Grade2*total2/100
    
T0tal=total_perc+total_perc2

if T0tal>=70:
    Class = "First"
elif T0tal>= 60:
    Class = "Upper second"
elif T0tal>= 50:
    Class = "Lower second"
else: Class = "Fail"



print(T0tal)
print(Class)

