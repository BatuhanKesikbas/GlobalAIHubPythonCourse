# 1ST PART OF THE 2ND DAY'S HOMEWORK.

# For the even numbered length list: for loop removed 1,2 and 3 from Original_list
# and removed 4,5,6 from Copied_list. (Referenced list is [1,2,3,4,5,6].)
# For the odd numbered length list: for loop removed 1,2,3 and 4 from the Original_list
# and removed 4,5,6 and 7 from Copied_list.(Referenced list is [1,2,3,4,5,6,7].)

Original_list=[1,2,3,4,5,6]
# To see the differences between odd number and even numbered length you can add or remove an index.

Copied_list=Original_list.copy()

middle=Original_list.copy() # 'middle' is for the element in the middle, if the length of the Original_list is odd
middle.append(0) # it was out of index range so i needed to add 1 element for each side
middle.insert(0,0)

# I popped the half of the each lists and add them if the list has even length.
if len(Original_list)%2==0:
    for k in range(0, (len(Original_list)) // 2):
        Copied_list.pop()
        Original_list.pop(0)
    print(Original_list+Copied_list)
# To erase the index in the middle, I popped extra 1 index and added the index in the middle as 'middle'.
else:
    for k in range(0, ((len(Original_list)) // 2)+1):
        Copied_list.pop()
        Original_list.pop(0)
        middle.pop(0)
        middle.pop()
    print(Original_list + middle + Copied_list)


# 2ND PART OF THE 2ND DAY'S HOMEWORK.

# I take an input n and numbers between 0 to n+1.
# (because n need to be calculated, so I add +1 to include n, since the last number inside the range does not count)
# If the number can be divided by 2, it means it's even number so I printed the even numbers.

n=int(input("Please enter an one digit integer."))
if n>=10:
    print("Plese rerun and  enter an ONE digit integer.")

else:
    for n in range(0,n+1):
        if n%2==0:
         print(n)

