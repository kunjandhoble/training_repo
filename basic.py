##method def
##class def
##for loops
##file open
##import statetments
##json
##list,dict,tuple

'''
var = 5
str_v= 'string'
d= """ttt"""
float_v = 9.8
print(var)
print("print this")
print(str_v+d)

##invalid
123strre=78
print(123strre)
'''

#declare list, tuple, dict
new_list = [1,2,3,4,'str1','str2',[2,3,4]]
#print(new_list[0])

#print(new_list[-1])

#print(new_list[4][1])

#add two list

#print(new_list+[89,90,98])


#new_list.append(23)
#print(new_list)
#new_list[0] = 45
#print(new_list)

#loop
#try to use negative indexes

#for i in range(2,11):
#    print(i)


#for i in new_list[:3]:
#    print(i)


##    if i ==1:
##        print(i+i)
##    else:
##        print ("Not one")


#tuple
'''
tup = ((1,2),
       ('str1',[23, 4], 67)
       )

print (tup[0])
print(tup[1])
print(tup[1][1][0])

'''


#dictionaries
'''
dc = {'key1':1, 'key2':2}
print(dc.keys())
print(dc.values())
print(dc['key1'])

#for key in dc:
#    print(dc[key])
print("\n\n\n")
for key, val in dc.items():
    print(key, val)

#read about nested dictrionaries and nested loops
#nested_dc = {'nested':{'key1':1, 'key2':2}}
#wap to provide value of key2 using nested loops
'''

f = open("C:\\Users\\Owner\'s\\training_repo\\file.txt", 'r')
print(f)
#print(f.read())
#print(f.readlines())

for line in f.readlines():
    print(line)
















