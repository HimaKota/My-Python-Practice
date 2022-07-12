# Python program to read file word by word

def word_by_word(fname):
    with open(fname,'r') as file:    
        # reading each line    
        for line in file:    
            # reading each word        
            for word in line.split():    
                # displaying the words           
                print(word)
word_by_word('File Handling\samplefile.txt')