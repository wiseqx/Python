#task1
class Clean:
    
    #open files and write to new files
    def __init__(self,input_file,output_file):
        self.file_original=input_file
        self.file_cleaned=output_file
    
    #programming starts here
    def main(self):
        try:
        # open and read a file
            input_handle = open(self.file_original, 'r')
        # open for exclusive creation
            output_handle = open(self.file_cleaned, 'w')
            
        #check if the file exist
        except IOError:
            print("cannot open files")
        
        #check the run-time error
        except RumtimeError:
            print("some run-time errors")

        else:
            # read the entire content of a file and return a list
            inp = input_handle.readlines()
            # searching for the lines that start with label of "*CHI:"
            output = []
            target_words = "*CHI:\t"
            target_word = "\t"
            target_word2 = "\n"
            extract_word = "%mor"
            for i in range(len(inp)):
                # finding a line start with "*CHI:\t", then append to new list
                if target_words in inp[i]:
                    output.append(inp[i])
                    # finding the statement that extend to next line and in case that finding the next line started with "%mor"
                    if target_word in inp[i + 1] and not extract_word in inp[i + 1]:
                        # append to the new output list
                        output.append(inp[i + 1])
                        # in case the line extending to second line
                        if target_word in inp[i + 2] and not extract_word in inp[i + 2]:
                            output.append(inp[i + 2])

            # remove the item "*CHI:" and make a new list
            new_output = []
            for item in output:
                # find the line which start with word "*CHI:"
                if item.startswith(target_words):
                    # remove "*CHI:"
                    new_item = item.strip("*CHI:")
                    # append to new output list
                    new_output.append(new_item)
                else:
                    new_output.append(item)

            # removing "\t" for each line
            new_new_output = []
            for each in new_output:
                line_split = each.split(target_word)
                # there is an empty item remaining needed to be deleted
                del line_split[0]
                # append each to new list
                for each in line_split:
                    new_new_output.append(each)

            # deal with each line in new output list
            for line in new_new_output:
                # split by space and turn string into list
                line_tokens = line.split(" ")
                new_line_tokens = []

                for word in line_tokens:
                    # retain these three symbols and append to new list
                    if word == "(.)":
                        new_line_tokens.append(word)
                    elif word == "(..)":
                        new_line_tokens.append(word)
                    elif word == "(...)":
                        new_line_tokens.append(word)
                    # in addition to 6 symbols above, we need to extract the following symbols if they exist in file
                    else:
                        # change the string to list
                        word_list = list(word)
                        # retain the other letters except for following 4 symbols
                        word_list = [x for x in word_list if x != "("]
                        word_list = [x for x in word_list if x != ")"]
                        word_list = [x for x in word_list if x != "<"]
                        word_list = [x for x in word_list if x != ">"]
                        # remove "\n" that in case the file has new lines
                        word_list = [x for x in word_list if x != target_word2]
                        # make word list to string sp that we could append each word
                        word_str = ""
                        for each in word_list:
                            word_str += each
                        # append what we get from 'else condition' to list
                        new_line_tokens.append(word_str)

                # if "&" exist, remove that word containing the "&" from each line
                for i in range(len(new_line_tokens) - 1, -1, -1):
                    if "&" in new_line_tokens[i]:
                        del new_line_tokens[i]

                # return index(n) and each item(char) from new_line_tokens list
                for n, char in enumerate(new_line_tokens):
                    letter_list = list(char)
                    # if the first letter of a word is "+", then removing that word
                    if letter_list[0] == "+":
                        del new_line_tokens[n]

                # deal with '[]'
                new_new_line_tokens = []
                for item in new_line_tokens:
                    # retain these three symbol
                    if item == "[//]" or item == "[/]" or item == "[*]":
                        new_new_line_tokens.append(item)
                    else:
                        ##remove those words that have either ']' or '[' as suffix
                        if not "]" in item and not "[" in item:
                            new_new_line_tokens.append(item)

                # change the list to string
                tempstring = ""
                for character in new_new_line_tokens:
                    tempstring += character + " "
                # write a line to file at a time
                tempstring=tempstring+"\n"
                output_handle.write(tempstring)

            #close both files after processing
            input_handle.close()
            output_handle.close()
            
        #checking if it programming exit
        finally:
            print("Exiting program")

if __name__ == "__main__":
    #read and clean TD files
    obj1=Clean('TD-1.txt','TD-1_cleaned.txt')
    obj1.main()
    obj2=Clean('TD-2.txt','TD-2_cleaned.txt')
    obj2.main()
    obj3=Clean('TD-3.txt','TD-3_cleaned.txt')
    obj3.main()
    obj4 = Clean('TD-4.txt', 'TD-4_cleaned.txt')
    obj4.main()
    obj5 = Clean('TD-5.txt', 'TD-5_cleaned.txt')
    obj5.main()
    obj6 = Clean('TD-6.txt', 'TD-6_cleaned.txt')
    obj6.main()
    obj7 = Clean('TD-7.txt', 'TD-7_cleaned.txt')
    obj7.main()
    obj8 = Clean('TD-8.txt', 'TD-8_cleaned.txt')
    obj8.main()
    obj9 = Clean('TD-9.txt', 'TD-9_cleaned.txt')
    obj9.main()
    obj10 = Clean('TD-10.txt', 'TD-10_cleaned.txt')
    obj10.main()
    
    #read and clean SLI files
    obj11 = Clean('SLI-1.txt', 'SLI-1_cleaned.txt')
    obj11.main()
    obj12 = Clean('SLI-2.txt', 'SLI-2_cleaned.txt')
    obj12.main()
    obj13 = Clean('SLI-3.txt', 'SLI-3_cleaned.txt')
    obj13.main()
    obj14 = Clean('SLI-4.txt', 'SLI-4_cleaned.txt')
    obj14.main()
    obj15 = Clean('SLI-5.txt', 'SLI-5_cleaned.txt')
    obj15.main()
    obj16 = Clean('SLI-6.txt', 'SLI-6_cleaned.txt')
    obj16.main()
    obj17 = Clean('SLI-7.txt', 'SLI-7_cleaned.txt')
    obj17.main()
    obj18 = Clean('SLI-8.txt', 'SLI-8_cleaned.txt')
    obj18.main()
    obj19 = Clean('SLI-9.txt', 'SLI-9_cleaned.txt')
    obj19.main()
    obj20 = Clean('SLI-10.txt', 'SLI-10_cleaned.txt')
    obj20.main()