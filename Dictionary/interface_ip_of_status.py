# find interface and IP of all interfaces which are up
# S.no	Interface		  IP		   Status		
# 1	    Ethernet0		1.1.1.1			 up
# 2	    Ethernet1		2.2.2.2			 down
# 3 	Serial0			3.3.3.3			 up
# 4	    Serial1			4.4.4.4			 up

eth= {                                                                  #Dictionary
        'Interface':['Ethernet0','Ethernet1','Serial0','Serial1'],
        'IP':['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4'],
        'status':['up','down','up','down']
     }
for key in eth.keys():
        print("\t",key,end="\t")
print()
print("------------------------------------------------------------")   
x=1
 #printing rows with serial number
for i in range(0,len(eth['Interface'])):
    print(x,"| ",eth['Interface'][i],'\t',"   |   ",eth['IP'][i],'\t',"|   ",eth['status'][i])     
    x=x+1                                                                                      
print() 

print("Status \"up\" having Interfaces and IP's are")   
print("Interface        IP")  
print("---------------------------")   
for i in range(0,len(eth['Interface'])): 
     
    if eth['status'][i]=='up':    #Checking the status is up    
        print(eth['Interface'][i],"----",eth['IP'][i])
        

print()  