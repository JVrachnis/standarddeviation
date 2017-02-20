from statistics import pstdev
numbers = sorted(map(float,input().split(",")))[2:-2]
print(numbers)
if len(numbers)>=1:
    print(pstdev(numbers))
else:
    print("pos 8a bri tin tipiki apoklisi xoris ta 2 megista kai elaxista ligotero 5 ari8moun ?")
