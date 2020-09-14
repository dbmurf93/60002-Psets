###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    print("Loading cows to shuttle...")
    inFile = open(filename, 'r')
    all_cows = inFile.read() #one long str
    cow_list = all_cows.split() #split by whitespace (CLUMSY?)
    
    cow_dict = {}
    for cow in cow_list:
        cow_name, weight = cow.split(',')
        cow_dict.update({cow_name: int(weight)}) 
    
    return cow_dict

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True) #returns list of tuples sorted descending order by weights
    #print(sorted_cows) ##for debugging
    trips = [] 
    cows_mooved = []
    shuttle_wt = 0 #empty shuttle
    
    while len(cows_mooved) != len(sorted_cows): #until theres no cow left behind
        trip = [] #empty heifer register
        shuttle_wt = 0 #empty shuttle 
    
        for cow in sorted_cows: #checks all cows, in sort order
            if cow in cows_mooved: continue #skips for already ferried heifers
        
            if cow[1] <= (limit-shuttle_wt): #if beast will fit
                shuttle_wt += cow[1] #allow beast onboard
                trip.append(cow) #add tuple to ledger
                cows_mooved.append(cow) #add to list
        ##print("Trip:",trip) 
        trips.append(trip)

    return trips
                
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trip_options = []

    for partition in get_partitions(cows.items()):
        ledger = [] #clear trips ledger between  
        
        for trip in partition:
            trip_wt = sum(cow[1] for cow in trip)
            if trip_wt <= limit:
                ledger.append([cow[0] for cow in trip]) #adds list of names to list
                continue
            else: break #next partition but hits next line first...
        
        if len(ledger) == len(partition): #checks if above loop completed vs broke
            trip_options.append(ledger) 

    return trip_options
        
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    all_cows = load_cows('PS1\ps1_cow_data.txt')

    start = time.time()
    greedy_list = greedy_cow_transport(all_cows)
    end = time.time()
    total = end-start
    print (total, 'sec')
    print('Greedy Transport:', greedy_list)
    print('# of trips:', len(greedy_list))

    start = time.time()
    power_list = brute_force_cow_transport(all_cows)
    best = len(all_cows)
    for ledger in power_list:
        if len(ledger) < best:
            best = len(ledger)
            best_trip = ledger
    
    end = time.time()
    total = end-start
    print (total, 'sec')
    print('Best trip:', best_trip)
    print('# of trips:',best)

def main():
    compare_cow_transport_algorithms()

if __name__ == "__main__":
    main()