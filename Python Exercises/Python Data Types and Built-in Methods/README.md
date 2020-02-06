# Python Data Types and Built-in Methods

## 1. Brief & Synopsis
In this practice, I will get to work on various programming constructs of Python, such as
python built-in data types and the methods associated with each of these data types,
program control structures, and the standard input and output. 

## 2. Instructions
This practice will assessed on applying various built-in data types as well as 
utilising the associated methods for the implementation of Python programs that perform
basic processing on texts.

* String data type and its built-in methods
* List data type and its built-in methods
* Tuple data type and its built-in methods
* Dictionary data type and its built-in methods
* Standard input and output
* Selective and iterative control structures

## 3. What are python files about?

### Python_file 1 :Standard Input and Output
Python_file 1 is a basic Python program that will repeatedly prompts the user to input a number
of lines of text. The input process is considered complete whenever the program has 
encountered or detected a total of 5 sentence delimiters, which can either be a full stop
 or period ".", a question mark "?", or an exclamation mark "!".
 
### Python_file 2: Basic Processing of Texts
Python_file2 is going to explore different Python built-in data types, in particular 
the sequences, to organize the input texts from Python file 1. The program is to perform some 
basic processing on the input texts

Extending from the program implemented in Python file 1, the input text are segmented
into individual sentences. The end of each sentence should be denoted by either a full stop
 or period ".", a question mark "?", or an exclamation mark "!". The program tokenises each sentence
 into individual works, where words within a sentence are separated by spaces " ". Any punctuation marks
 such as a comma "," and a semicolon ";" that appear within a sentence should be considered as individal 
 tokens. (Note that the apostrophe "’" should be considered as part of the word that it is attached to.)
 
 The number of tokens or words should be 46 with 41 words and 5 punctuation marks(4 ","s and 1 ".")
 
 The program considers which of the sequence data types in Python is best for organising 
 the segmented sentences and the individual words associated with each sentence for 
 further processing. In particular, it considers how to retrieve a particular sentence or particular
 word from a sentence.

 ### Python_file 3: Basic Analysis of Texts
 Python_file3 is an extension of the program from Python_file2. Upon segmenting the input 
 text (or the paragraph) into sentences and words, the program is extended to perform 
 some simple analysis on the input text.
 
 Python_file3 program performs the following analysis:
 * Count the total number of words and the total number of characters
 * Count the total number of unique words (ignoring the case of letters)
 * Count the number of words that begin with an uppercasee letter (ie.A-Z)
 * Count the number of different punctuation marks
 * Count the number of words that are numbers (ie. Words that consist of digits 0-9)
 
 At the end of program, all the counts on the terminal screen are displayed in an informative 
 way.
 
 ## How to run?
### 1.Running Python using Jupyter Notebook:

Task 1:

In order to test assignment_task1, we can start entering the Python code: “%run python_file1” in the first line. To execute this single line of Python code, press “shift” and “enter” in your keyboard or just click on the “run” button:
![](/images/i_1.png)

Now you see an input that require user to enter a line. We can test whether the program works or not by entering a text.

Firstly, we test a long paragraph which the number of delimiters is over 5. Let's see what the output delimiters would look like. Now we input the Sample input and press “enter” in keyboard:

Sample input: In Newton's day the whole field of nature was practically lying fallow. No fundamental principles were known until the law of gravitation was discovered. This law was behind all the work of Copernicus, Kepler, and Galileo, and what they had done needed interpretation. It was quite natural that the most obvious and mechanical phenomena should first be reduced, and so the Principia was concerned with mechanical principles applied to astronomical problems. To us, who have grown up familiar with the principles and conceptions underlying them, all varieties of mechanical phenomena seem so obvious, that it is difficult for us to understand how any one could be obtuse to them; but the records of Newton's time, and immediately after this, show that they were not so easy of apprehension. It may be remembered that they were not adopted in France till long after Newton's day. In spite of what is thought to be reasonable, it really requires something more than complete demonstration to convince most of us of the truth of an idea, should the truth happen to be of a kind not familiar, or should it chance to be opposed to our more or less well-defined notions of what it is or ought to be.
 ![](/images/i_2.png)

The output shows that a text from input but just 5 total number delimiters. So, the test is successful.

---


Now we test python_file2. Enter the code “%run python_file2” in a new cell and press “enter” and “shift” simultaneously in keyboard. Then an input instruction appears.

![](/images/i_3.png)

Now we enter Sample input 2 below and press “enter” in keyboard.

Sample input 2: This is a test sentence. Is it a test sentence? Yes, it is a test sentence. OK, bye! Well, Hello again.
![](/images/i_4.png)

We can see the output in the figure above. Sentences have been segmented and each sentence starts from newline. Total number of tokens has been counted from sentences. Note that tokens include words and required punctuations (“,”, “;”, “.”, “?”, “!”).


---

Now we test python_file3 by entering the code “%run python_file3” in a new cell and run the program. The figure should be:
![](/images/i_5.png)
Now we enter Sample input 3 below, then press “enter” in the keyboard to see the output.

Sample input 3: There appears to be a definite amount of matter in the visible universe, a definite number of molecules and atoms. How many molecules there are in a cubic inch of air under ordinary pressure has been determined, and is represented approximately by a huge number, something like a thousand million million millions. If one should feel that the number thus obtained was not very accurate, he might reflect that if there were ten times as many it would add but another cipher to a long line of similar ones and would not materially modify it. The point is that there is a definite, computable number. If one will then add to these the number of molecules in the more distant stars and nebule, of which there are visible about 100000000, making such estimate of their individual size as he thinks prudent, the sum of all will give the number of molecules in the visible universe.
![](/images/i_6.png)
