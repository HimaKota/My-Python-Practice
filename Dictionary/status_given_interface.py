# Write a python program to find status of a given interface
# S.no	Interface		  IP		   Status		
# 1	    Ethernet0		1.1.1.1			 up
# 2	    Ethernet1		2.2.2.2			 down
# 3 	Serial0			3.3.3.3			 up
# 4	    Serial1			4.4.4.4			 up

eth = {                                                                  #Dictionary
        'Interface':['Ethernet0','Ethernet1','Serial0','Serial1'],
        'IP':['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4'],
        'status':['up','down','up','up']
       }

for key in eth.keys():
        print("\t",key,end="\t")
print()
print("------------------------------------------------------------")
x=1
for i in range(0,len(eth['Interface'])):
    print(x,"|     ",eth['Interface'][i],'\t',"   |   ",eth['IP'][i],'\t',"|   ",eth['status'][i])     
    x=x+1                                                                                      
print() 

user_input= input("Enter the interface ")
for i in range(0,len(eth['Interface'])):
    if(eth['Interface'][i] == user_input):
        print("Status of ",user_input," - ",eth['status'][i])
        break
print()