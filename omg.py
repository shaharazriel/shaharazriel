def between(lst, a, b):
    # delete pass and fill in your code below
    num = 0
    n = len(lst)
    for i in range(n):
        if lst[i] > a and lst[i] < b:
            num = num + 1
            
    return(num)



### TESTS ###

print("********************")
print("Starting the test:")
    
print("********************")
print("Counting over [1, 2, 3, 4] with a = 0, b = 5")
ans = between([1, 2, 3, 4], 0, 5)
if ans == 4:
    print("CORRECT: Very good, there are 4 elements between a = 0 and b = 5 in [1, 2, 3, 4]")
else:
    print("WRONG: There are 4 elements between a = 0 and b = 5 in [1, 2, 3, 4] but the code returned", ans)

print("********************")
print("Counting over [-5, 20, 13, 0] with a = 200, b = 300")
ans = between([-5, 20, 13, 0], 200, 300)
if ans == 0:
    print("CORRECT: Very good, there are no elements between a = 200 and b = 300 in [-5, 20, 13, 0]")
else:
    print("WRONG: There are no elements between a = 200 and b = 300 in [-5, 20, 13, 0] but the code returned", ans)
    
print("********************")
print("Counting over [-5, 20, 13, 0] with a = -10, b = 5")
ans = between([-5, 20, 13, 0], -10, 5)
if ans == 2:
    print("CORRECT: Very good, there are 2 elements between a = -10 and b = 5 in [-5, 20, 13, 0]")
else:
    print("WRONG: There are 2 elements between a = -10 and b = 5 in [-5, 20, 13, 0] but the code returned", ans)

print("********************")    
print("Tests concluded, add more tests of your own below!")
print("********************")
