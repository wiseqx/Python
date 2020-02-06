#Mission: There are 2 missions in task2. One is required to segment the input text into individual sentences, the other is to count total number of tokenise which are segmented by sentences.

#task 2 begin:
#1.segment sentences begin:

#the process is similar with task 1 except for 1 step below
num_of_delimiters=0
output_string=""
while num_of_delimiters<5:
    input_delimiter=input("Enter a line: ") 
    for items in input_delimiter:        
        if num_of_delimiters==5:
            break
        if num_of_delimiters<5:
            output_string += items                   
            if (items=="." or items== "?" or items=="!"):
                num_of_delimiters +=1
                #here, add "\n" at end of a delimiter, which is used to indicate a new line in a string.
                output_string=output_string+"\n"
    if num_of_delimiters<5:
        print("Total number of delimiters found: ", num_of_delimiters)
print(output_string)

#2.segment tokens begin:
#token shoule be in type of list because it can be splited later
token_list=[]

#replace "\n" with none in case there is a "\n" before each punctuation
output_string=output_string.replace("\n","")
#add a space before every punctuations so we can split later
output_string=output_string.replace(".", " .")
output_string=output_string.replace("?", " ?")
output_string=output_string.replace("!", " !")
output_string=output_string.replace(",", " ,")
output_string=output_string.replace(";", " ;")

#split ouput by space
token_list=output_string.split(" ")
#count total number of tokens
count_tokens=len(token_list)
print("Total number of tokens:",count_tokens)
