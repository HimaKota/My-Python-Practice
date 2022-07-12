# add a new entry to above database
eth= {                                                                  #Dictionary
        'Interface':['Ethernet0','Ethernet1','Serial0','Serial1'],
        'IP':['1.1.1.1','2.2.2.2','3.3.3.3','4.4.4.4'],
        'status':['up','down','up','up']
     }
eth['Active Since']=['4h','1h:15m','2h','3h:20m'] 

for key in eth.keys():
        print("\t",key,end="\t")
print()
print("------------------------------------------------------------------------------") 
 #Print the new dictionary in table format
for i in range(0,len(eth['IP'])):                                      
    print(i+1,"| ",eth['Interface'][i],'\t',"   |   ",eth['IP'][i],'\t',"|   ",eth['status'][i],'\t',"|   ",eth['Active Since'][i])      #Printing_rows
  
