import pandas as pd
def solve(string):
    """
    returns a series object with word count as values and words as the indices.
    """
    # store the frequency of the strings in a series
    
    ## First convert split the sentence using split() to divide on space
    df = string.split()
    
    ## Convert the values in Series() datatype 
    df = pd.Series(df)
    
    ## Countring the frequency    
    freq = df.value_counts()
    
    ## Storing the value based on the index
    res = freq.sort_index()
    
    return res


"""
You're working on collecting the text data for a Natural Language Processing(NLP) project. You come up with the idea of storing the unique words (case-sensitive) with their frequency in a pandas series object.

You are given the raw data in form of a string, Write a function which can take a string as an input and return the unique words and the corresponding frequency in form of a Pandas Series object. The indices of the series should be the unique words and the values should be the frequency of those unique words.

Note that:

String contains no special character.
Always a Non-empty string.
Case sensitive i.e. He and he should be treated as two different word tokens.
Series returned is expected to be sorted by sort_index()for sorting all the words.

Input Format
Number of testcases
String with space separated words. (basically a sentence)
Output Format
space separated words in first line.
space separated values in the second line.
Sample Input
1
How much wood would a woodchuck chuck if a woodchuck could chuck wood
Sample Output

How          1
a            2
chuck        2
could        1
if           1
much         1
wood         2
woodchuck    2
would        1

Note:

Google about sort_index() to understand how the function works.


"""

string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
solve(string)
