#Mission: Working with Basic data analysis

#task2 begins:
#importing glob to return and recursive cleaned files alongside the filenames
import glob
#import numpy helping to draw graph
import numpy as np
#import pands to represent the statistics as a tabular format
import pandas as pd
#import matplotlib to plot graphs
import matplotlib.pyplot as plt

#make a class called statistic
class Statistic:
    
    #call the path to glob.glob for matching all of cleaned files which saved in disk
    def __init__(self,path,filename):
        self.tem_files=glob.glob(path)
        #init a filename which we can distinguish TD file and SLI file
        self.filename=filename
        self.count=0
        #num as the glob sorted in arbitrary order, the first file is file-10
        self.num=10
        self.len_total = 0
        self.unique_total=0
        self.rep_total=0
        self.ret_total=0
        self.error_total=0
        self.pau_total=0

    #this method is used to return the average of number of statements which can help to draw average plot
    def count_length(self):
        #making a statement dictionary in order to draw statistic plot easily by using pandas
        self.length_dic = {}
        #making a list for containg the number of statements that each children made
        statement = []
        for txt in self.tem_files:
            #open and read the file one by one
            with open(txt, 'r') as file:
                #read the entire content of a file and return as a string
                read = file.read()
                length = 0
                #split by space and return a list
                line_tokens = read.split(" ")
                #giving each file a name for distinguish TD file and SLI file
                if self.count == 0:
                    name = self.filename+ str(self.num) + "_cleaned"
                if self.count > 0:
                    name = self.filename + str(self.count) + "_cleaned"
                self.count += 1
                #finding delimiters that stop by '.' or '?' or '!'
                for each in line_tokens:
                    if (each == "." or each == "?" or each == "!"):
                        length += 1
                        #if exists, add key and value to dictionary
                        self.length_dic[name] = length
                #append number of statements for each child in one file to list
                statement.append(length)
            self.len_total+=length
        #counting the average of statements children made in one cleaned file, and keep one decimal
        length_mean=round(self.len_total/10,1)
        #append to list
        statement.append(length_mean)
        #add key and value to dictionary
        self.length_dic['average']=length_mean
        #trasnfer list to tuple that we can easily to draw with pandas
        self.statement = tuple(statement)
        return length_mean

    #this method is used to return the average of number of unique word which can help to draw average plot
    def count_unique(self):
        # assert self.count is greater than 9. if does, re-count from 0
        if self.count > 9:
            self.count = 0
        # making a unique word dictionary in order to draw statistic plot easily by using pandas
        self.unique_dic = {}
        # making a list for containg the number of unique words that each children made
        unique_list = []
        for txt in self.tem_files:
            # open and read the file one by one
            with open(txt, 'r') as file:
                # read the entire content of a file and return as a string
                read = file.read()
                # split by space and return a list
                line_tokens = read.split(" ")
                if self.count == 0:
                    name = self.filename + str(self.num) + "_cleaned"
                if self.count > 0:
                    name = self.filename + str(self.count) + "_cleaned"
                self.count += 1
                unique_count_list=[]
                for each in line_tokens:
                    #turn words to lowercase
                    each=each.lower()
                    #strip \n
                    if each.startswith("\n"):
                        each=each.strip("\n")
                        #append to list
                        unique_count_list.append(each)
                    else:
                        unique_count_list.append(each)
                #in oder to make word unique by using set function
                unique_set=set(unique_count_list)
                #count unique words including punctuations
                unique=len(unique_set)
                #make the set into list
                unique_count_list2=list(unique_set)
                for item in unique_count_list2:
                    #extract punctuation which stands for other meanings
                    if (item=="[/]" or item=="[//]" or item=="[*]" or item=="(.)"or item=="(..)"or item=="(...)"or item=="!"or item=="?"or item=="." or item ==";" or item==":" or item=="," or item==""):
                        unique-=1
                #  add key and value to dictionary
                self.unique_dic[name] = unique
                # append number of unique words for each child in one file to list
                unique_list.append(unique)
            self.unique_total += unique
        # counting the average of statements children made in one cleaned file, and keep one decimal
        unique_mean = round(self.unique_total / 10, 1)
        unique_list.append(unique_mean)
        self.unique_dic['average'] = unique_mean
        # trasnfer list to tuple that we can easily to draw with pandas
        self.unique_word = tuple(unique_list)
        return unique_mean

    #this method is used to return the average of number of repetitions which help to draw average plot
    def count_rep(self):
        #assert self.count is greater than 9. if does, re-count from 0
        if self.count > 9:
            self.count = 0
        #making a repetition of certain word dictionary in order to draw statistic plot easily by using pandas
        self.rep_dic = {}
        #making a list for containg the number of repetitions for certain word that each children made
        reptition=[]
        for txt in self.tem_files:
            #open and read the file one by one
            with open(txt, 'r') as file:
                #read the entire content of a file and return as a string
                read = file.read()
                rep = 0
                #split by space and return a list
                line_tokens = read.split(" ")
                #giving each file a name
                if self.count == 0:
                    name = self.filename+ str(self.num) + "_cleaned"
                if self.count > 0:
                    name = self.filename + str(self.count) + "_cleaned"
                self.count += 1
                #finding whether '[/]' exists
                for each in line_tokens:
                    if each == "[/]":
                        rep += 1
                        #if exists, add key and value to dictionary
                        self.rep_dic[name] = rep
                #append number of repetitions for each child in one file to list
                reptition.append(rep)     
            self.rep_total +=rep
        #counting the average of statements children made in one cleaned file, and keep one decimal
        rep_mean=round(self.rep_total/10,1)
        #append to list
        reptition.append(rep_mean)
        self.rep_dic['average']=rep_mean
        #trasnfer list to tuple that we can easily to draw with pandas
        self.repetitions=tuple(reptition)
        return rep_mean

    #this method is used to return the average of number of retracings which help to draw average plot
    def count_retrace(self):
        #assert self.count is greater than 9. if does, re-count from 0
        if self.count > 9:
            self.count = 0
        #making a retracing dictionary in order to draw statistic plot easily by using pandas
        self.ret_dic = {}
        #making a list for containg the number of retracing that each children made
        ret_list=[]
        for txt in self.tem_files:
            #open and read the file one by one
            with open(txt, 'r') as file:
                #read the entire content of a file and return as a string
                read = file.read()
                ret = 0
                #split by space and return a list
                line_tokens = read.split(" ")
                #giving each file a name for distinguish TD file and SLI file
                if self.count == 0:
                    name = self.filename + str(self.num) + "_cleaned"
                if self.count > 0:
                    name = self.filename+ str(self.count) + "_cleaned"
                self.count += 1
                #finding whether '[//]' exists
                for each in line_tokens:
                    if each == "[//]":
                        ret += 1
                        #if exists, add key and value to dictionary
                        self.ret_dic[name] = ret
                #append number of rectracing for each child in one file to list
                ret_list.append(ret)
            self.ret_total+=ret
        #counting the average of statements children made in one cleaned file, and keep one decimal
        ret_mean=round(self.ret_total/10,1)
        #append to list
        ret_list.append(ret_mean)
        self.ret_dic['average']=ret_mean
        #trasnfer list to tuple that we can easily to draw with pandas
        self.retracing=tuple(ret_list)
        return ret_mean

    #this method is used to return the average of number of errors which help to draw average plot
    def count_error(self):
        #assert self.count is greater than 9. if does, re-count from 0
        if self.count > 9:
            self.count = 0
        #making an error dictionary in order to draw statistic plot easily by using pandas
        self.error_dic = {}
        #making a list for containg the number of grammatical errors that each children made
        error_list=[]
        for txt in self.tem_files:
            #open and read the file one by one
            with open(txt, 'r') as file:
                #read the entire content of a file and return as a string
                read = file.read()
                error = 0
                #split by space and return a list
                line_tokens = read.split(" ")
                #giving each file a name for distinguish TD file and SLI file
                if self.count == 0:
                    name = self.filename + str(self.num) + "_cleaned"
                if self.count > 0:
                    name = self.filename+ str(self.count) + "_cleaned"
                self.count += 1
                #finding whether '[*]' exists
                for each in line_tokens:
                    if each == "[*]":
                        error += 1
                        #if exists, add key and value to dictionary
                        self.error_dic[name] = error
                #append number of errors for each child in one file to list
                error_list.append(error)
            self.error_total+=error
        #counting the average of statements children made in one cleaned file, and keep one decimal
        error_mean=round(self.error_total/10,1)
        #append to list
        error_list.append(error_mean)
        self.error_dic['average']=error_mean
        #trasnfer list to tuple that we can easily to draw with pandas
        self.errors=tuple(error_list)
        return error_mean

    #this method is used to return the average of number of pauses which help to draw average plot
    def count_pause(self):
        #assert self.count is greater than 9. if does, re-count from 0
        if self.count > 9:
            self.count = 0
        #making a pause dictionary in order to draw statistic plot easily by using pandas
        self.pause_dic = {}
        #making a list for containg the number of pauses that each children made
        pause_list=[]
        for txt in self.tem_files:
            #open and read the file one by one
            with open(txt, 'r') as file:
                #read the entire content of a file and return as a string
                read = file.read()
                pause = 0
                #split by space and return a list
                line_tokens = read.split(" ")
                if self.count == 0:
                    name = self.filename + str(self.num) + "_cleaned"
                if self.count > 0:
                    name = self.filename+ str(self.count) + "_cleaned"
                self.count += 1
                #finding whether (.) or (..) or (...) exists
                for each in line_tokens:
                    if (each == "(.)" or each == "(..)" or each == "(...)"):
                        pause += 1
                        #if exists, add key and value to dictionary
                        self.pause_dic[name] = pause
                #append number of pauses for each child in one file to list
                pause_list.append(pause)
            self.pau_total+=pause
        #counting the average of statements children made in one cleaned file, and keep one decimal
        pause_mean=round(self.pau_total/10,1)
        #append to list
        pause_list.append(pause_mean)
        self.pause_dic['average']=pause_mean
        #trasnfer list to tuple that we can easily to draw with pandas
        self.pauses=tuple(pause_list)
        return pause_mean


    def chart(self):
        #plot a graph for statistic using pandas
        df = pd.DataFrame({'statements': self.length_dic,
                           'unique words': self.unique_dic,
                           'repetitions': self.rep_dic,
                           'retracing': self.ret_dic,
                           'errors': self.error_dic,
                           'pauses': self.pause_dic})
        #convert NUN to 0 
        df = df.fillna(0)
        return df
    
    def barchart(self):
        #there are 11 bars that needed to draw
        N=11
        #rename each statistics
        statement=self.statement
        unique_word=self.unique_word
        repetitions=self.repetitions
        retracing=self.retracing
        errors=self.errors
        pauses=self.pauses
        
        #create a subplot
        fig, ax=plt.subplots()
        index=np.arange(N)
        #setting bar_with and opacity
        bar_width=0.3
        opacity=0.4
        
        #set up each arguments for each bar 
        rects1=plt.bar(index,statement,bar_width/2,alpha=opacity,color='r',label='statement')
        rects2=plt.bar(index+bar_width/2,unique_word,bar_width/2,alpha=opacity,color='b',label='unique_words')
        rects3=plt.bar(index+bar_width,repetitions,bar_width/2,alpha=opacity,color='y',label='repetitions')
        rects4=plt.bar(index+bar_width*1.5,retracing,bar_width/2,alpha=opacity,color='g',label='retracing')
        rects5=plt.bar(index+bar_width*2,errors,bar_width/2,alpha=opacity,color='c',label='errors')
        rects6=plt.bar(index+bar_width*2.5,pauses,bar_width/2,alpha=opacity,color='m',label='pauses')

        #change the y-axis label
        plt.ylabel('stats')
        #change bar chart title
        plt.title('Stats for file '+ self.filename)
        #set up the width of x-axis and change the label
        plt.xticks(index+bar_width,('file10', 'file1', 'file2', 'file3', 'file4','file5', 'file6', 'file7', 'file8', 'file9','average'))
        #change y-axis limit
        plt.ylim(0,230)
        
        #automatically fetches the legend handles and their associated labels
        plt.legend()
        
        #automatically adjusts subplot params 
        plt.tight_layout()
        #show the plot
        plt.show()
        
    
if __name__ == "__main__":
    #call object with methods for TD children
    obj1 = Statistic(r"C:\Users\*.txt", 'SLI')
    length1=obj1.count_length()
    unique1=obj1.count_unique()
    rep1=obj1.count_rep()
    retrace1=obj1.count_retrace()
    error1=obj1.count_error()
    pause1=obj1.count_pause()
    print(obj1.chart())
    obj1.barchart()
    #call object with methods for SDL children
    obj2 = Statistic(r"C:\Users\*.txt", 'TD')
    length2=obj2.count_length()
    unique2=obj2.count_unique()
    rep2=obj2.count_rep()
    retrace2=obj2.count_retrace()
    error2=obj2.count_error()
    pause2=obj2.count_pause()
    print(obj2.chart())
    obj2.barchart()

    #Now we combine the average of unique words gengerated by two groups into one tuple
    length_list=[]
    length_list.append(length1)
    length_list.append(length2)
    length=tuple(length_list)
    #Now we combine the average of unique words gengerated by two groups into one tuple
    unique_list=[]
    unique_list.append(unique1)
    unique_list.append(unique2)
    unique=tuple(unique_list)
    #Now we combine the average of repetition words gengerated by two groups into one tuple
    rep_list=[]
    rep_list.append(rep1)
    rep_list.append(rep2)
    rep=tuple(rep_list)
    #Now we combine the average of rectracing gengerated by two groups into a tuple
    ret_list=[]
    ret_list.append(retrace1)
    ret_list.append(retrace2)  
    retrace=tuple(ret_list)
    #Now we combine the average of errors gengerated by two groups into a tuple
    error_list=[]
    error_list.append(error1)
    error_list.append(error2)
    error=tuple(error_list)
    #Now we combine the average of pauses gengerated by two groups into a tuple
    pause_list=[]
    pause_list.append(pause1)
    pause_list.append(pause2)
    pause=tuple(pause_list)
    
    #Now we plot a graph for average of each gengerated in two groups
    #2 bars
    N=2
    #gengerate subplots
    fig, ax=plt.subplots()
    index=np.arange(N)
    bar_width=0.3

    opacity=0.4
    
    #set up each arguments for each bar 
    rects1=plt.bar(index,length,bar_width/2,alpha=opacity,color='r',label='statement')
    rects2=plt.bar(index+bar_width/2,unique,bar_width/2,alpha=opacity,color='b',label='unique_words')
    rects3=plt.bar(index+bar_width,rep,bar_width/2,alpha=opacity,color='y',label='repetitions')
    rects4=plt.bar(index+bar_width*1.5,retrace,bar_width/2,alpha=opacity,color='g',label='retracing')
    rects5=plt.bar(index+bar_width*2,error,bar_width/2,alpha=opacity,color='c',label='errors')
    rects6=plt.bar(index+bar_width*2.5,pause,bar_width/2,alpha=opacity,color='m',label='pauses')
    
    #gengrate labels, titles, x-axis label and y-axis limit
    plt.ylabel('stats')
    plt.title('Average Stats')
    plt.xticks(index+bar_width,('TD', 'SLI'))
    plt.ylim(0,170)
    #fetches the legend handles and their associated labels
    plt.legend()
    #adjusts subplot params 
    plt.tight_layout()
    #show the plot
    plt.show()