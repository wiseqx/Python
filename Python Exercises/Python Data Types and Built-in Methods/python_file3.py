#Mission: ayalysis.

#task 3 begin:
#the following process is based on task1 and task 2. 
#here comes the output strings based on task 1
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
                num_of_delimiters+=1

#here comes token list and number of tokens progrom based on task 2
token_list=[]
output_string=output_string.replace(".", " .")
output_string=output_string.replace("?", " ?")
output_string=output_string.replace("!", " !")
output_string=output_string.replace(",", " ,")
output_string=output_string.replace(";", " ;")
token_list=output_string.split()
count_tokens=len(token_list)

#1.count words and letters
#count words
words_list=[]
punc_list=[",",".","?","!",";"]
#use "for loop" as iteration that excuate every word in token_list.
for word in token_list:
    #every word of token_list which is not in punc_list will be cumulatively adding to words_list.
    if word not in punc_list:
        words_list.append(word)
#count the number of words by using List len() function
words_count=len(words_list)
print("The total number of words are:",words_count)

#count letters(characters)
chars_list=[]
char_list="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
##use "for loop" as iteration that excuate every characters in output_string.
for char in output_string:
    #every characters in output_string which is also in char_list will be adding to words_list.
    if char in char_list:
        chars_list.append(char)
#count the number of characters by using List len() function
chars_count=len(chars_list)
print("The total number of letters are:",chars_count)

#2.count unique words
#change a string within list into lowercase
new_words_list=[element.lower() for element in words_list]
#identify the unqiue words by using set data type
unqiue_words_set=set(new_words_list)
unqiue_words_count=len(unqiue_words_set)
print("The total number of unique words are:",unqiue_words_count)


#3.count the number of words that begin with an uppercase letter
uppercase_count=0
uppercase_list="ABCDEFGHIJKLMNOPQRSTUVWQYZ"
#use "for loop" as iteration that check each item in word_list.
for uppercase in words_list:
    #the step below indicate whether each item in word_list index at 0 is Capital letter.
    if uppercase[0] in uppercase_list:
        uppercase_count+=1
print("The total number of words that begin with an uppercase letter:",uppercase_count)

#4.count number of different punctuation marks
#create a List of 5 0's representing the count of the 5 punctuations in punc_list.
count=[0]*5
#use "for loop" to check every character in output_string 
for character in output_string:
    #check the character if it is not in alphabetic characters and not space and not numbers, then count
    if not character.isalpha() and character.strip()!='' and not character.isdigit():
        #List quanatity of corresponding puntucation in punc_list for every delimiters
        count[punc_list.index(character.lower())]+=1
        
print("The total number of different punctuation marks are as follow:")
i=0
#use "while loop" repeatedly executes every punctuation in punc_list.
while i<len(punc_list):
    #print punctuation with corresponding quantity by required format.
    s='Punctuation mark %s has count equal to %s'
    print(s% (punc_list[i], count[i]))
    i+=1

#5.count number of words that are numbers
words_number=0
#use "for loop" that checks every words in output_string meet the if statement.
for number in token_list:
    #The method isnumeric() checks whether the token_list consists of numeric characters. 
    if number.isnumeric():
        words_number+=1
print("The total number of words that are numbers:",words_number)
