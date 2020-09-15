###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import string

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    egg_weights = sorted(egg_weights, reverse=True) #ret list sorted descending order
    i = 0 #indexer
    j = 1 #counter
    ship_weight = 0

    while ship_weight != target_weight:
        if egg_weights[i] <= (target_weight-ship_weight): #if biggest egg fits...
            memo.update({egg_weights[i]:j}) #add to dict with counter
            ship_weight += egg_weights[i] #add aboard
            j+=1 #increase egg counter
        else:
            i+=1 #move to next egg
            j=1 #reset egg counter
    
    
    output = [] #formatting from here on...
    for key, value in memo.items():
        output += ['{0} * {1}'.format(value,key)] #creates a list of lists to be formatted into str
    
    output = ' + '.join(output) #join terms 
    output += (" = {0}".format(target_weight)) #add suffix
    output = str(sum(memo.values())) + " ({0})".format(output) #for the sake of matching the OG formatting
    return output #
    
    


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()