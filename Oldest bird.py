##Given a array of bird names and another array with corresponding ages of the birds, find the name of the oldest bird in the list.

##Input Format:

#Input has two lines.
#First line is the array of bird names (String).
#Second line is the array of ages of the birds (Int).
#Output Format:string

#Sample Input:
#['sparrow', 'peacock', 'parrot', 'owl', 'peacock', 'macaw', 'macaw', 'parrot', 'macaw', 'peacock']  
#[6, 1, 6, 5, 7, 6, 0, 9, 0, 7]

#Sample Output:
##parrot

#Explanation:
#parrot has age 9 which is the max of all the ages in the array; therefore parrot is returned.



import numpy as np
def oldest_bird(birds, age):
    ''' birds[i] consist of the names of the type of ith bird
        age[i] consist of the age of ith bird'''
        
    ## STEP 1: Get the index of maximum age element
    
    max_age_index = np.argmax(age)
    
    
    ## STEP 2: Get the bird with maxium age using the above index
    
    old_bird = birds[max_age_index]
    
    
    return old_bird
    
    
    ## input as below
    birds = ['sparrow', 'peacock', 'parrot', 'owl', 'peacock', 'macaw', 'macaw', 'parrot', 'macaw', 'peacock']  
    age = [6, 1, 6, 5, 7, 6, 0, 9, 0, 7]
    ##calling the function to compute bird with maximum age 
    oldest_bird(birds, age)
