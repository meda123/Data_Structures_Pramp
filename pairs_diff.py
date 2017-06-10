
#Pairs with specific difference 

"""
Given a list1 of distinct integers and a non-negavite integer k, write a function
findPairsWithGivenDifference that returns a list of all pairs [x, y] in list1, 
such that x-y =k 

>>>findPairsWithGivenDifference([0, -1, -2, 2, 1], k = 1) 
[[0, -1], [-1, -2], [2, 1], [1, 0]]

>>>findPairsWithGivenDifference([1, 7, 5, 3, 32, 17, 12], k = 17)
[]

"""
a = [1, 7, 5, 3, 32, 17, 12]
k = 17 

def findPairsWithGivenDifference(a, k):

    a.sort()
    adder_pairs = []

    first = 0
    last = 1 

    while (last < len(a) and first < len(a)):
        if first != last and a[last] - a[first] == k:
            pairs = [a[last], a[first]]
            adder_pairs.append(pairs)
            last += 1 

        elif (a[last] - a[first]) < k:
            last += 1 

        elif a[last] - a[first] > k:
            first += 1 

    return adder_pairs

### Testing that my code works 

test = findPairsWithGivenDifference(a, k)
print test 