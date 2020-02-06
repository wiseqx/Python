#Mission: Recursion

#import old tasks with altered linear search and binary search
from old_task1 import StringClass
from old_task2 import StringListClass
import unittest


class Testforlinear(unittest.TestCase):
    
    #test if 'a' in string "bananas"
    def testlinear_1(self):
        string1 = "bananas"
        obj1 = StringClass(string1)
        self.assertTrue(obj1.linear_search("a"))
    
    #test if 'f' is not in string "bananas"
    def testlinear_1(self):
        string1 = "bananas"
        obj1 = StringClass(string1)
        self.assertFalse(obj1.linear_search('f'))

class Testforbinary(unittest.TestCase):
    
    #test if "a" is in string 'bananas'
    def testbinary_2(self):
        #set space of list
        task2_obj1 = StringListClass(6)
        #add item to list and should be the same number as number of list in what we set
        task2_obj1.add(StringClass('b'))
        task2_obj1.add(StringClass('a'))
        task2_obj1.add(StringClass('n'))
        task2_obj1.add(StringClass('a'))
        task2_obj1.add(StringClass('n'))
        task2_obj1.add(StringClass('s'))
        #have to do search after sorting
        task2_obj1.sort()
        #test if "a" is in string 'bananas'
        self.assertTrue(task2_obj1.binary_search_recursive(StringClass("a")))
    
    #test if 'f' is not in string "bananas"
    def testbinary_2(self):
        #set space of list
        task2_obj1 = StringListClass(6)
        #add item to list and should be the same number as number of list in what we set
        task2_obj1.add(StringClass('b'))
        task2_obj1.add(StringClass('a'))
        task2_obj1.add(StringClass('n'))
        task2_obj1.add(StringClass('a'))
        task2_obj1.add(StringClass('n'))
        task2_obj1.add(StringClass('s'))
        #have to do search after sorting
        task2_obj1.sort()
        #test if 'f' is not in string "bananas"
        self.assertFalse(task2_obj1.binary_search_recursive(StringClass("f")))
    


if __name__ == "__main__":
    unittest.main()