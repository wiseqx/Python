#Mission: Changing the linear search by using recursive

#task1 

#make a class called StringClass
class StringClass:
    
    #trasfer string to list and count the length of object
    def __init__(self,str_value):
        self.str_data=list(str_value)
        self.count=0
        self.search_string=[]
        self.search_start_idx=0
        for item in self.str_data:
            self.count+=1
    
    #return the length of the object
    def __len__(self):
        return self.count
    
    #returns ture if item in list is equal to target_char and return false otherwise.
    def linear_search(self, target_char):
        #search first item and then one by one 
        self.search_string=self.str_data[self.search_start_idx:]
        if len(self.search_string)==0:
            #return false if the items can not be divided further
            return False
        else:
            if self.search_string[0]==target_char:
                #if found, reset the number to 0
                self.search_start_idx=0
                #if found, reset back to empty list
                self.search_string=[]
                return True
            else:
                #if not found, index+1
                self.search_start_idx+=1
                self.search_string=self.str_data[self.search_start_idx:]
                #if not found, recursive orrcurs
                return self.linear_search(target_char)
    
    #use for loop to count how many target_char in the list 
    def frequency(self,target_char):
        count_letter = 0
        #check each item in list and see if it equals target character, count plus 1 
        for i in range(self.count):
            if self.str_data[i]==target_char:
                count_letter+=1
        return count_letter
    
    #use for loop to interate search target char
    def replace(self, target_char, new_char):
        for i in range(self.count):
            #use index to find the target char and then replace with the new char
            if self.str_data[i]==target_char:
                self.str_data[i]=new_char
    
    #change all of uppercase to lowercase in the list
    def lowercase(self):
        #first, list all lowercase and uppercase
        self.lower_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.upper_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        #find the total number of characters in the list
        count_char = 0
        for item in self.lower_list:
            count_char+=1      
        #use for loop to interate list
        for num in range(self.count):
            #use for loop to interate lowercase list
            for i in range(count_char):
                #once found the uppercase letter in list, change to lowercase
                if self.str_data[num]==self.upper_list[i]:
                    self.str_data[num]=self.lower_list[i]

    #change all of lowercase to uppercase in list
    def uppercase(self):
        #first, list all lowercase and uppercase
        self.lower_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.upper_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        #find the total number of characters in the list
        count_char = 0
        for item in self.lower_list:
            count_char+=1
        #use for loop to interate list
        for num in range(self.count):
            #use for loop to interate uppercase list
            for i in range(count_char):
                #once found the lowercase letter in list, change to uppercase
                if self.str_data[num]==self.lower_list[i]:
                    self.str_data[num]=self.upper_list[i]

    #tokenise by delimiter
    def tokenise(self,the_delimiter):
        new_list=[]
        new_item=""
        count_num = 0
        #use for loop to interate
        for i in range(self.count):
            #if one of item in list equals delimiter, add all of items from first detectived delimiter and next delimiters to the new_item
            if self.str_data[i]==the_delimiter:
                for n in range(count_num,i):
                    if self.str_data[n]!=" ":
                        new_item+=self.str_data[n]
                count_num=i+1
                #append new_item to new list
                new_list.append(new_item)
                new_item = ""
        #this for loop is to combine the items from last detectived delimiter and the last item of list to new_item
        for index in range(count_num,self.count):
             new_item+=self.str_data[index]
        #then append the new_item above to new_list
        new_list.append(new_item)
        #check if there is an empty item in list at the beginning of list 
        if new_list[-1]=="":
            new_list.pop()
        #check if there is an empty item in list or at the end of list
        if new_list[0]=="":
            new_list.pop(0)
        return new_list
    
    #__eq__ is used to compare a pair of objects whether is equal to each other
    def __eq__(self,other):
        #need to know whther is an instance of this class
        if not isinstance(other,StringClass):
            raise TypeError("error! Should have entered an object!")

        return self.str_data==other.str_data

    def __gt__(self,other):
        #need to know whther a new string is an instance of this class
        if not isinstance(other,StringClass):
            raise TypeError("error! Should have entered an object!")

        #first need to compare a pair of characters at the same position
        for index in range(self.count):
            if ord(self.str_data[index]) < ord(other.str_data[index]):
                return False
            else:
                return True
        
        #then we compare the size
        if self.count > len(other.str_data):
            return True

        return False
    
    #ouput is to return back to a string from a list
    def __str__(self):
        output=""
        for item in self.str_data:
            output+=item
        return output
