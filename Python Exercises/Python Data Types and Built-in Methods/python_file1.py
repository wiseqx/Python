#mission: Task 1 requires that user input whatever the number of sentences are but need to output total of 5 delimiters. Each delimiter either be stop at "." or "?" or "!". 

#task 1 begin:

#set initital number of delimiters is 0
num_of_delimiters=0

#set initial output string is none
output_string=""

#use "while loop" for checking if the total number of delimiters are over or less than 5.
while num_of_delimiters<5: 
    input_delimiter=input("Enter a line: ") 
    #use "for loop" as iteration, allows a code block to be repeated many times.
    for items in input_delimiter:
        #If program find that input reach 5 delimiters, the program should stop excuate.
        if num_of_delimiters==5: 
            break
        #if program find input is less than 5 delimiters, each items of input will be added to output_string list.
        if num_of_delimiters<5: 
            output_string += items  
            #count quantity of input delimiters when meet required puctuation below.
            if (items=="." or items== "?" or items=="!"):
                num_of_delimiters+=1
    #after execute "for loop", program check whether the delimiters is less than 5 and print quantity. 
    if num_of_delimiters<5:
        print("Total number of delimiters found: ", num_of_delimiters)
        
print(output_string)
