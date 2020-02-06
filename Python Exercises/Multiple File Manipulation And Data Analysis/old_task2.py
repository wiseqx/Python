#task2 

#create a StringListClass class
from assignment2_task1 import StringClass
class StringListClass:
           
        #create a fixed size list and see whether the size is greater than 0
        def __init__(self, size):
            assert size > 0, "size must be >0"
            self.str_list = [None] * size
            self.count = 0
            self.left=0
            self.size = size
        
        #check whether the objects in the list equals to the size
        def is_full(self):
            return self.count == self.size

        #is_empty checks whether the number of objects equals 0. It will return True if the list is empty and return False if otherwise
        def is_empty(self):
            return self.count == 0

        #add new StringClass objects at the end of collection in the list
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
        def binary_search_recursive(self, target_item):
            while True:
                if self.left > self.count:
                    return False
                # find the middle position
                self.mid = (self.left + self.count) // 2
                # check if the target is equal to the middle item
                if self.str_list[self.mid] == target_item:
                    return True
                if self.str_list[self.mid] > target_item:
                    # lower half to be considered
                    self.count = self.mid - 1
                else:
                    # upper half to be considered
                    self.left = self.mid + 1
                # the target is not found, then re-call the method again
                return StringListClass.binary_search_recursive(self, target_item)

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

        def binary_search_recursive(self, target_item):
            while True:
                if self.left > self.count:
                    return False
                # find the middle position
                self.mid = (self.left + self.count) // 2
                # check if the target is equal to the middle item
                if self.str_list[self.mid] == target_item:
                    return True
                if self.str_list[self.mid] > target_item:
                    # lower half to be considered
                    self.count = self.mid - 1
                else:
                    # upper half to be considered
                    self.left = self.mid + 1
                # the target is not found, then re-call the method again
                return StringListClass.binary_search_recursive(self, target_item)

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
