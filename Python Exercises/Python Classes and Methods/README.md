# Building User-Defined Python Classes and Methods
## Brief & Synopsis
This practice is going to implement methods for each class with our own algorithms without utilizing
 any of the built-in functions provided by Python. The data stored in these data types are
 organised in the array-based structure.

### Task 1:The String Class
The first task requirs to implement a number of user-defined methods that are
useful for processing or manipulating strings(data in textual form). Although Python has provided a good
collection of string methods, the purpose of this first task is to assess programming knowledge 
in developing algorithms for handling strings.
This task is to create a Python class that contains a collection of methods defined for manipulating strings. An
attribute or instance variable is required for this String class to represent each individual string data. It should be
stored in an array-based structure. For the purpose of this task, the instance variables are defined by using
a Python list to represent each string data. (With this implementalion, we are assuming that each characterin a
string is represented as one element in the Python list.)


The following is a list of methods that can be applied on the strings represented by this String class. Each of them should
be implemented. 

1. \__init__(self, str_value): This is the constructor method that is required for creating string objects
from this String class. It takes the Python string(str_value) as an argument and assigns it to an instance
variable defined by a Python list as mentioned above.

2. search(self, target_char): This method checks whether a specific character(target char) exists
within the string. So long as the character exists in the string (i.e.once you have found its first occurrence), return
a True value；otherwise a False value. The "linear search" algorithm should be used.

3. frequency(self, target_char): This method performs in the similar way as the search method, except
that it returns the number of occurrences of the specific character(target_char) in the string.

4. replace(self, target_char, new_char): This method will search for the specilic character 
(target_char) within the string and replace allits occurrences with a new character(new_char).

5. lowercase(se1f): This method converts or normalises the string into lower cases. No arguments are required for 
this method.(Note that do not use the built-in lower() method provided by Python.)

6. uppercase(se1f): Similar to the lowercase method,this method converts the string into upper cases
(Again, do not use the built-in upper() method provided by Python.)

7. tokenise(self, the_delimiter): This method tokenises or splits the string based on a specific
character,referred as the delimiter(the_delimiter).The delimiter could be a space character " " or a
pronunciation mark "," .This method will return a list of tokens(sub-strings) where each of the tokens can be
represented as either an individual Python list or an object of this String class.

8. \__eq__(self, other): This is one of the overloaded methods in Python that enables us to check for
equality. Here, we want to compare whether the data represented by the argument other is the same as the data
represented in the current string object referred by se1f. (Make sure that the argument
other is an object of this String class before attempt to compare the contents of the two objects.)

9. \__str__(self): This is another overloaded method that is useful for formating the output of the string data
represented in this String class. Re-build the instance variable (str_data) into a Python string and return it.


### Task 2:The StringList Class

In the second task, we implement another class that is responsible for handling a collection of
strings, which is essentially a List abstract data type(ADT) that we have discussed. For the purpose of this task,
we are (again) using the Python list to represent the string collection as an array-based structure. This means that
each element in the Python list is holding an object from the String class defined in Task 1. As such, we need to
define a Python list as the instance variable (or attribute) for this StringList class that we are going to implement.
We implement each of the following methods for this StringList class. 

1. \__init__(self, size): This is the constructor method that is required for constructing an initial empty list
which wil hold a collection of objects from the String class. You may name this instance variable as 
str_list. Given that we are adopting an array-based structure for the implementation, you should decide on an
initial size for the collection, as indicated by the argument size.

2. add(self, new item): This method will add a new item which is a StringClass object to the collectior
represented in this StringList class(str_list).For the purpose of this task, the new item should just be added to
the end of the collection. (Note that duplication of an existing item is allowed here; and do not 
use the bult-in append() method provided by Python.)

3. remove(self, target item): This method will remove all the occurrences of the specific item(as
indicated by target_item) from the string collection represented in this StringList class(str_list).

4. sort(self): This method sorts items in the string collection (str_list)in an ascending order. You may
choose to implement one of the three basic sorting algorithms namely "bubble sort",
"selection sort", and "insertion sort". (Note that for the implementation of this method, you will have to include
additional overloaded methods to the implementation of the String class in Task 1, such as \__lt__, \__le__, 
\__gt__, or__ge__, which depends on the sorting algorithm that is going to implement.)

5. search(self, target_item):The method is for searching for a specific item (target_item) in the string
collection(str_list). Again, so long as an occurrence of the target item is encountered, return a True value;
otherwise a False value. For the implementation of this method, "binary search" algorithm should be used. 
(Note that the assumption here is that the string collection(str_list) has been sorted before this method can be 
applied to perform the search.)

6. \__le__(self): This is another overloaded method that is commonly implement to return the number of 
items in the collection. (Again, do not use the built-in 1en()method provided by Python.)

7. \__str__(self): This is again the overloaded method that is useful for formatting the output of the string
collection represented in this StringList class. Construct a Python string which organises each item from the string
collection(str_list) as a separate line in the output.


### Task 3：Creating Instances

Task 3 assessed on how to make use of the two user-defined classes implemented in the first two tasks(Task 1 and Task 2).

The task here is to construct a Python program for creating instances or objects of each class by importing the
two classes. "All" the methods defined for each class are applied on the coresponding objects to
test the implementation for each of the methods. 

## How to run?
We use Jupyter Notebook to test task 3 here.


#### 1. Testing:
In order to test assignmen2_task3, you now start entering the Python code: “%run assignment2_task3” in the first line. To execute this single line of Python code, press “shift” plus “enter” simultaneously in your keyboard or just click on the “run” button


Now input a string “bananas” as our first object of this class.


###### 1.1 Is new string equal to string ‘tester’:
‘tester’ is what we input as “bananas” above, now it is time to put another object for comparing with the original string, and see if there are equal.  This step if for testing ‘__eq__’ method.





