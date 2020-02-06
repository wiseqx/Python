#Mission:create a Python class that contains a collection of methods. String data should be stored in a fixed-size list.

#task2 begins:

#create StringListClass class
class StringListClass:
           
        #create fixed size list and exam whether the size is greater than 0
        def __init__(self, size):
            assert size > 0, "size must be >0"
            self.str_list = [None] * size
            self.count = 0
            self.size = size
        
        #is_full checks the objects in list equal to size
        def is_full(self):
            return self.count == self.size

        #is_empty checks the number of objects equals 0, returns True if list is empty and False if otherwise
        def is_empty(self):
            return self.count == 0

        #add new StringClass objects at end of collection in list
        def add(self, new_item): 
            #check if the list is full
            assert not self.is_full(), "cannot add to a full list"
            self.str_list[self.count]=new_item
            #self.count indicated the next position to be added
            self.count+=1

        #removing an existing item at a specific position 'index'
        #assuming the index is valid: index >= 0 and index < self.count
        def remove(self, target_item):
            assert not self.is_empty(), "cannot remove an empty list"
            count_remove = 0
            #find the position of item which intended to delete
            for i in range(self.count):
                #'=='operator is called from assignment_task1 under '__eq__' method
                if self.str_list[i] == target_item:
                    index = i
                    #shift all of items after the item to be deleted one position to left
                    for num in range(index, self.count - 1):
                        self.str_list[num] = self.str_list[num + 1]
                    #make the last postion becomes None so that reduce duplicate
                    self.str_list[self.size - 1 - count_remove] = None
                    count_remove += 1
                    self.count -= 1

        # sorts using Bubble sort in an ascending order 
        def sort(self):
            # perform n-1 iterations on the entire list
            for passnum in range(self.count - 1, 0, -1):
                # for each iteration, move the largest item to the end
                for i in range(passnum):
                    # '>' operator below will be called in assignment2_task1 under '__gt__' method
                    if self.str_list[i] > self.str_list[i + 1]:
                        # swap if two adjacent items are out of order
                        temp = self.str_list[i]
                        self.str_list[i] = self.str_list[i + 1]
                        self.str_list[i + 1] = temp

        
        #search method is based on the sort method
        #returns True if an item exists in the list or False otherwise
        def search(self, target_item):
            # indicate the start and the end of the list to be considered
            low_num = 0
            high_num = self.count - 1
            
            # repeatedly divide the list into two halves once the target item is not found
            while not (low_num - 1) == high_num:
                # find the middle position
                mid_num = (low_num + high_num) // 2
                
                # check if the target is equal to the middle item
                #'=='operator is called from assignment_task1 under '__eq__' method
                if self.str_list[mid_num] == target_item:
                    return True
                # check if the target is less than the middle item
                # '>' operator below will be called in assignment2_task1 under' __gt__' method
                elif self.str_list[mid_num] > target_item:
                    high_num = mid_num - 1  #lower half to be considered
                # the target is greater than the middle item
                else:
                    low_num = mid_num + 1  #upper half to be considered 
                    
            # the list cannot be divided further and the target is not found
            return False

        #return number of items in the list
        def __len__(self):
            return self.count

        #output string from memory address into real value
        def __str__(self):
            output = ""
            #iterate items of list before the first None item
            for char in range(0,self.count):
                #traslate memory address to real value
                for item in self.str_list[char].str_data:
                    output += item
                #organise each item from string collection as a separate line
                output += "\n"
            return output