# Coin Change Problem
# Given an amount 'tot' and a list of coin values [vi, v2...vk]
# this program outputs the number of different ways in which exact
# change can be obtained. 
#Input Format:
# 10  4
# 2 3 5 6 
# In the above example, the first line states that the total amount
#is 10 cents and the number of types of coins is 4. 
# The second line lists the allowed coin values i.e 2,3,5 & 6cents.



def totnum(tot,coinvals) :
    # sort coinvals to be ascending
    coinvals.sort()
    
    numvals = len(coinvals)
    
    # Check : If the list is empty 
    if numvals == 0:  
        return 0
        
    numways = [[0 for i in range(tot+1)] for j in range(numvals)]
    
    #Initialize first row
    
    for j in range(tot+1)[1:] :
        if j%coinvals[0] == 0 :
            numways[0][j] = 1
            
    # Calculate the (numvals, tot+1) 2d array. For a given [i][j] index
    # the list numways stores the number of distinct ways change can be 
    # produced.
    
    for i in range(numvals)[1:] :
        for j in range(tot+1)[1:] :
            if j < coinvals[i] :
                numways[i][j] = numways[i-1][j]
            elif j-coinvals[i] == 0:
                numways[i][j] = numways[i-1][j] + 1
            else :
                numways[i][j] = numways[i-1][j] + numways[i][j-coinvals[i]]
        
    #output
    print numways[-1][-1]
    
    
def main():
    
    line1 = raw_input()  # contains tot & no. of coin-types
    line2 = raw_input()  # coin values
    

    listline1 = line1.split()
    listline2 = line2.split()
    
    total = int(listline1[0])
    coinvalues = [int(i) for i in listline2]
    
    totnum(total,coinvalues)
    
if __name__ == '__main__':
    main()
    

            
                
                
             
    
    
    
   
       
           
           
        
