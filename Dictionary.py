string="Hello Welcome to Azerbaijan" #deafult string
#create empty dictionary
dict=dict()
#create empty lists
UpperList=[]
LowerList=[]
for i in string:
    #select lower case
    if(i.islower()):
        LowerList.append(i)
        #select upper case
    elif(i.isupper()):
        UpperList.append(i)
#create key and value
dict["UPPER"]=UpperList
dict["LOWER"]=LowerList
print (dict)