#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#grades calc

Class = ""
Grade = input("How much did you get?")
Grade=float(Grade)
if Grade>=70:
    Class = "First"
elif Grade >= 60:
    Class = "Upper second"
elif Grade >= 50:
    Class = "Lower second"
else: Class = "Fail"

print(Class)


#%
total=float(input("Total:"))

for i in range(100):
    total_perc=Grade*total/100

print(total_perc)

