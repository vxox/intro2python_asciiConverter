#ASCII NAME PRINTER PROGRAM
""" 
The purpose of this program is to print my (Paul King) 
name allongside its associated BIN number and HEX value. 

"""
#SETS MY NAME AS ENTERED WORD
entered_word=input("Please enter any word:")
#PRINTS TOP HEADER LINE, WITH FORMATTING BASED ON h1.length values
print(f"{'LETTER':<7} {'Binary Value':<15} {'Decimal Value':<15}")

#start loop over the word in entered_word
for char in entered_word:
#for (num of char's) in entered_word [aka, execute X times where X = len(entered_word){entered_word.length}] 
    ascii_value = ord(char)
    #set var ascii_value to the ord() value, aka ASCII value or Decimal Value
    binary_value = format(ascii_value, '08b')
    #take ascii_value and format it into a binary number, which is denoted by 08b
    #08b tells the computer to 
        #1. (0 Rule) tells computer to fill blank spaces with 0. 
        #2. (8 Rule) tells computer to max out the format with 8 characters
        #3. (b Rule) tells computer to format the number in binary

    print(f"{char:<7} {binary_value:<15} {ascii_value:<15}")
    #prints once at the end of processing each letter. Once the program reaches the end of the string looping, the program will exit. 