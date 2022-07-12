# print first word from a string in python
def print_first_word():    
        words = "All good things come to those who wait"
        print(words.split().pop(0))
    #to print the last word use pop(-1)
print_first_word()