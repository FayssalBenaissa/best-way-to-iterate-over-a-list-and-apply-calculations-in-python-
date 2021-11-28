import numpy as np
#----------------------simple for loop--------------------------------
array = list(range(5))


result = []
for x in array :
    if x%2 == 0:
        result.append(0)
    else:
        result.append(1)
print("for loop : ",result)

#--------------------------lsit comprehension----------------------------

lsit_comprehension = [0 if x%2 == 0 else 1 for x in array]
print("lsit comprehension :",lsit_comprehension)

#-------------------------map-----------------------------

mp = map(lambda x: 0 if x%2 == 0 else 1 , array )
print("map : " ,list(mp))

#----------------------------numpy vectorize--------------------------

fnc = np.vectorize(lambda x: 0 if x%2 == 0 else 1)
npvec = fnc(array)
print("numpy vectorize : ", list(npvec))