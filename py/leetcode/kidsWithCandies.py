
def kidsWithCandies(candies, extraCandies: int) :
    maxi =max(candies)
    ans=[]
    for i in  range (len(candies)):
        if (candies[i]+extraCandies) >= maxi :
            ans.append(True)
        else : 
            ans.append(False)
    return ans
    

print(kidsWithCandies(
[2,3,5,1,3],
3))