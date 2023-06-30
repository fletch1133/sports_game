#Nth Finonacci

# def getNthFib(n):
#     if n == 1:
#         return 0
#     if n <= 3:
#         return 1
    
#     return getNthFib(n-1) + getNthFib(n-2) 


def getNthFib(n, calculated = {1:0, 2:1, 3:1}):

    if n in calculated:
        return calculated[n]
    
    calculated[n] = getNthFib(n-1, calculated) + getNthFib(n-2, calculated) 
    
    return calculated[n] 



#Python program to print prime #'s between 100 and 200

for num in range(100, 200):
    if all(num % i != 0 for i in range (2, num)):
        print(num)


#write a sort function to sort elements in a list

l = [23, 45, 69, 74, 4, 11, 27]
l.sort(reverse = False)

print(l)


#write a sorting function without using the list sort function(descending order)

data_list = [33, 54, 65, 98, 112, 237, 4, 9, 44]
new_list = []

while data_list:
    minimum = data_list[0] #arbitrary number in list
    for x in data_list:
        if x > minimum:
            minimum = x
    new_list.append(minimum)

    data_list.remove(minimum)

print(new_list)


#write python program to print fibonacci series

def R(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return R(n-1) + R(n-2)
    
for i in range(0,26):
    print(R(i))


#print a list in reverse
wo = [3, 15, 4, 442, 25, 70, 38, 19]

def rev(l):
    return l[::-1]

reversed_wo = rev(wo)
print(reversed_wo)


#check if string is a palindrome or not


def isPalindrome(s):
    # use predefined func. to reverse to string print(s)
    rev = ''.join(reversed(s))

    #check if both string are = or !=
    if (s == rev):
        return True
    return False

print(isPalindrome('madam'))
print(isPalindrome('joystick'))


#write program to print set of duplicates

c = [1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7, 1]
print(set([x for x in c if c.count(x) > 1]))


#program to print number of words in a sentence

u = "I hope you have a great trip next fall!"
print(len(u.split()))


# Given an array of n elements, write a func. to give each element
# x in an array

def search(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
        
        print('It is not going to be in this list')

x = [1, 2, 3, 3, 4, 4, 5, 6, 1]

print(search(x,10)) 


#write program to implement binary search

def binary_serach(array, target):
    lower = 0
    upper = len(array)
    
    while lower < upper:     # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        
        if target == val:
            return x
        elif target > val:
            if lower == x:   #these two lines r actual lines
                break        # u r looking for
            lower = x
        elif target < val:
            upper = x

print(binary_serach([1,2,3,4,5],5))



