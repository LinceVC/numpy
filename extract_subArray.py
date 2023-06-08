import numpy as np


def extract_subarray(arr):
    '''
    INPUT: arr -> 2D array
    
    OUPUT: result -> 2D array
    '''
    
    ### STEP1: Get the rows (2nd  to 4th row)
    
    arr = np.array(arr)
    print(arr)
    row_array = arr[1:4,:]
    print(row_array)
    
    #### STEP 2: Get the last 3 cols from the row array
    
    cols_array = row_array[:,-3:]
    print(cols_array)
    
    #### STEP3: Reverse the rows in cols array
    
    #use negative step to retrieve rows or columns in reverse
    #arr[end:start:-1] will extract columns from end to start+1
    result = cols_array[::-1,:]
    

    return result


arr = [[ 0,  1,  2,  3],  
 [ 4,  5,  6,  7],   
 [ 8,  9, 10, 11],   
 [12, 13, 14, 15],   
 [16, 17, 18, 19]]

extract_subarray(arr)
