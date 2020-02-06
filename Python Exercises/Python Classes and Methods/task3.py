#Mission:test task1 and task2

#task3 begins:

#import 2 tasks that we can use StringClass and StringListClass methods
from task1 import StringClass
from task2 import StringListClass

if __name__ == "__main__":

    print("Testing String Class begins")

    # 1.Is new String equal to String 'tester'
    string1 = str(input("please enter a string: "))
    obj1 = StringClass(string1)
    print("1. Test Is new String equal to String you entered")
    string2 = str(input("please enter a contrastive string: "))
    obj2 = StringClass(string2)
    test1 = print("Is new String equal to String 'tester?':", obj1.__eq__(obj2))

    # 2. test how many target letters in string
    print("2. Test how many target letters in string")
    question3=input("enter a letter for frequency")
    print("the number of target character is：", obj1.frequency(question3))
    print("Are there 3 ",question3,"'s in bananas?")
    if obj1.frequency(question3)==3:
        print(True)
    else:
        print(False)

    # 3.test search: if any target letters in string
    print("3.Test search: if any target letters in string")
    question4=input("please enter a letter for search")
    print("Does this letter in string?")
    print(obj1.search(question4))

    # 4.test replace new letter to target letter
    print("4. Test replace new letter to target letter")
    string3=input("please enter target letter")
    string4=input("please enter new letter")
    obj1.replace(string3,string4)
    print("after replace, the output is: ",obj1)
    #owing to we changed string value, so we changed back
    obj1.replace(string4,string3)
    print("Because we will test other methods later, the original value changed back is: ",obj1)

    # 5.test 'uppercase' method: turn string to uppercase
    print("5. test 'uppercase' method: turn string to uppercase")
    obj1.uppercase()
    print("does uppercase turn bananas to BANANAS?")
    obj3=StringClass("BANANAS")
    if obj1 == obj3:
        print(True)
    else:
        print(False)

    # 6.test 'lowercase' method turn string to lowercase
    print("5. Test 'lowercase' method turn string to lowercase")
    obj1.lowercase()
    print("Does lowercase turn BANANAS to bananas?")
    obj4=StringClass("bananas")
    if obj1==obj4:
        print(True)
    else:
        print(False)

    #7.test tokenise
    print("7. Test tokenise")
    print("The string after tokenise is: ",obj1.tokenise(input("please enter a delimiter that you want to tokenise")))

    print("Testing task 1 finish")

    print("***")

    print("Testing StringListClass begins")

    #1.Test initialisation of list
    size = int(input("please enter a number for fixing size of list"))
    task2_obj1=StringListClass(size)
    print("Is new string list length 0? ")
    if task2_obj1.__len__()==0:
        print(True)
    else:
        print(False)

    print("1. Test initialisation of list: ")
    print("Are the items in str_list objects?")
    print(isinstance(task2_obj1,StringListClass))

    #2.Test addition
    print("2. Test addition")
    question1=input("Would you like to add value to a list? T/F")
    while True:
        if question1== "T":
            task2_obj1.add(StringClass(input("please enter a value")))
            question1 = input("Would you like to add more value to a list? T/F")
        elif question1=="F":
            break
        else:
            question1 = input("Error typed! please re-enter: T/F")
    print("the list after entering value is:")
    print(task2_obj1)
    print("the size of list is still: ",size,", and the number of objects in the list is: ",task2_obj1.__len__())

    #3.Test remove method
    print("3. Test remove")
    question2=input("Would you like to remove value from a list? T/F")
    while True:
        if question2== "T":
            task2_obj1.remove(StringClass(input("please enter a value")))
            question2 = input("Would you like to remove more value from a list? T/F")
        elif question2=="F":
            break
        else:
            question2 = input("Error typed! please re-enter: T/F")
    print("the list after removing value is:")
    print(task2_obj1)
    print("the list size is still: ",size,", while the number of objects in the list is: ",task2_obj1.__len__())


    #4. Test Sort. I do not create any new list so that the input of sort is based on the list after 'remove' method.
    print("4. Test sort")
    task2_obj1.sort()
    print("the list after sorting is:")
    print(task2_obj1)

    #5.Test Search
    print("5.1 Test search")
    question6=input("please enter a value which you want to search:")
    print("Does this value in the list? ",task2_obj1.search(StringClass(question6)))

    #test Does search fail to find 'f' in list?
    print("5.2 New Test: Does search fail to find 'f' in list?")
    size = int(input("please enter a number for fix size of list"))
    task2_obj2 = StringListClass(size)
    question5=input("Would you like to add value to a list? T/F")
    while True:
        if question5== "T":
            task2_obj2.add(StringClass(input("please enter a value")))
            question5 = input("Would you like to add more value to a list? T/F")
        elif question5=="F":
            break
        else:
            question5 = input("Error typed! please re-enter: T/F")
    print("the list after entering value is:")
    print(task2_obj2)
    task2_obj2.sort()
    question7 = input("please enter a value which you want to search:")
    print("Does this value in the list? ",task2_obj2.search(StringClass(question7)))
          
          
    print("task2 testing finished!")
