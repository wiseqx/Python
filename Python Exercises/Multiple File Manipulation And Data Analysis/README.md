# File Manipulation And Basic Data Analysis

## 1. Brief & Synopsis
This practice is going to manipulate data from multiple text files, and to conduct some basic
 data analysis using Python external packages, as well as to practice on implementing recursive
 solutions.
 

## 2. Instructions

### Task1: Handling with File Contents and Preprocessing
The first task, all the transcripts of the dataset given are read in Python script, both the SLI and TD groups.
Then a number of pre-processing tasks are conducted to extract only the relevant contents or texts needed for
analysis in the subsequent task(i.e.Task 2). Upon completing the pre-processing tasks, each of the cleaned
transcript are saved as an output file. This would be a more efficient approach whenever we need to
manipulate the cleaned dataset without having to repeat the pre-processing task.

The data are required for processing and analysis is the
narative produced by the children, which are the statements (or lines) indicated by the label of "*CHI:" in the
transcripts. The first step is that, for each original transcript, extract only the statements which are prefixed or
begin with "*CHI:". (Note that there are some statements that extend to the next line, which should be
taken into account.)

The next step is to perform a set of pre-processing or filtering tasks. We want to remove certain words (generally
referred as tokens) in each statement that have the CHAT symbols as either prefixes or suffixes, but retaining
certain symbols and words for analysis in Task 2. For this part of the implementation, we consider split
each statement into a list of words or tokens before beginning with the filering process.

Below is a list of symbols that we filter off from each of the child statements extracted:
* Remove those words that have prefixes of '&' and '+'
* Remove those words that have eithert '[' as prefix or ']' as suffx but retain these three symbols: [//], 
[/]，and [*]
* Retain those words that have either '<' as prefix or '>' as suffix but these two symbols should be removed.
* Retain those words that have either '(' as prefix or ')' as suffix but these two symbols should also be removed.



### Task2: Working with Basic Data Analysis

In this second task, we are going to perform some basic data analysis by using some of the external Python
packages(such as NumPy, SciPy, Pandas, and Matplotlib). The main task is to produce a number of statistic
the two groups of children transcripts. The statistics might serve as good indicators for distinguishing between
children with SLI and the typically developed children.

Amongst the statistics of each child that we are interested in are the following:

* Length of the transcript-indicated by the number of statements
* Size of the vocabulary -indicated by the number of unique words
* Number of repetition for certain words or phrases-indicated by the CHAT symbol[/]
* Number of retracing for certain words or phrases-indicated by the CHAT symbol[//]
* Number of grammatical errors made-indicated by the CHAT symbol [*]
* Number of pauses made-indicated by the CHAT symbols(.)(..)(...)

(Note: Given that the length of each child transcript is indicated by the number of statements, the end of each
statement can be determined based on the pronunciation marks of either a full stop '.', a question mark '?', or
an exclamation mark '!'.)



### Task3: Expermenting with Recursion
The final task is to assess on the understanding of the fundamental concepts of recursion. 
We are required to implement two searching algorithms for the two classes by producing a recursive
solution(old_task1 and old_task2). For the search method defined in each of the two classes, we turn it into a recursive
method. Our methods(as well the classes) are tested again to ensure that the overall functionality is
maintained. Define and run a "unit test" in Python for each of the recursive search methods.







