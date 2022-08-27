##Loops
#for loop useful to loop each item in the list

ranks = [1,2,3]
for rank in ranks:
    print("Ranks in order {}".format(rank))

#range() is built in py fucntion used to get range of integer
for num in range(1,11):
    print("num {}".format(num))

#while
temp_f =40
while temp_f > 32:
    print(" the water is {} degress".format(temp_f))
    temp_f -= 1

#Loop Controls
# Break - end the loop. go to the next statement in the program(outside of loop)
# Continue - skips current part of the loop. moves to the next part of the loop
# Pass - skips any part of the loop where "pass" appears. best used for testing code.

#while
temp_f =40
while temp_f > 32:
    print(" the water is {} degress".format(temp_f))
    temp_f -= 1
    if temp_f == 35:
        break

for num in range(1,11):
    if num == 7:
        print("num {} skipped".format(num))
        continue
    print(num)

for num in range(1,11):
    if num == 3:
        pass
    else:
        print(num)

