#Write a python program to count how many ethernet interfaces are there
# S.no	Interface		  IP		   Status		
# 1	    Ethernet0		1.1.1.1			 up
# 2	    Ethernet1		2.2.2.2			 down
# 3 	Serial0			3.3.3.3			 up
# 4	    Serial1			4.4.4.4			 up

eth= {                                                                  #Dictionary
        'Interface':['Ethernet0','Ethernet1','Serial0','Serial1'],
        'IP':['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4'],
        'status':['up','down','up','up']
    }
#To print the number of Interface's available in the dictionary
c=len(eth['Interface'])                                                 
print("Number of Interface's in the dictionary - ",c)