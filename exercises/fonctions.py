def hello(name,age):
    return "Hello, my name is  {} and I am {} years old".format(name,age)

result = hello("serge",18)
print(result)


def add(a,b):
    return a+b


def redraw(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "impossible division"
    else:
        return a/b


def get_size(array):
    somme = 0
    for x in array:
        somme = somme + 1
    return somme


def fact(number):
    x = 1
    out = 1
    while x >= 1 and x <= number:
         out = x * out
         x += 1
    return out


def array_right_move(steps,array):
    step = 0
    while step < steps:
        last = array[-1]
        i = len(array)-2
        while i >= 0:
            array[i+1] = array[i]
            i = i-1
        array[0] = last
        step += 1
    return array


def palindrome(word):
    i = 0
    j = len(word) -1
    while i < j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def search(array,number):
    for x in array:
        if x == number:
            return True
        else :
            return False



def search(array,number):
    i = 0
    j = len(array)
    while i != j:
        if array[i] == number:
            return True
        else:
            i+=1
    return False


def search_optimize(array,number,l,h):
    if h < l:
        return False
    mid = (l+h)//2
    if array[mid] == number:
        return True
    elif array[mid] > number:
        return search_optimize(array,number,l,mid)
    else:
        return search_optimize(array,number,mid+1,h)


l = [1,2,3,5]
# y = 4
# result = search(l,y)
# print(result)

# print(search_optimize(l,2,0,len(l)-1))

def array_left_move(steps,array):
    step = 0
    while step < steps:
        first = array[0]
        i = 1
        while i < len(array):
            array[i-1] = array[i]
            i = i+1
        array[-1] = first
        step += 1
    return array

def end_zero(array):
    array.sort()
    zeros = 0
    for x in array:
        if x == 0:
            zeros += 1
        else:
            break
    return array_left_move(zeros,array)

def parity_sort(array):
    for x in array:
        if x%2 == 0:
            temp = x
            array.remove(x)
            array.insert(0,temp)
        else:
            temp = x
            array.remove(x)
            array.insert(-1, temp)
    return array

# print(parity_sort([3,1,2,4]))

def amstrong(number):
    temp_number = number
    som = 0
    while number > 0:
        digit = number%10
        som += digit**3
        number = number//10
    if som == temp_number:
        return True
    return False


def fibunacci1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    first = 1
    second = 1
    terme = 0

    for x in range(3,n+1):
        terme = first + second
        first = second
        second = terme

    return terme

def fibunacci2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return  fibunacci2(n-1) + fibunacci1(n-2)


print(fibunacci2(18))