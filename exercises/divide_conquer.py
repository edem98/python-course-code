def search2(array,number):
    count = 0
    for x in array:
        if x == number:
            print(count)
            return True
        count += 1
    print(count)
    return False


def search(array,number):
    count = 0
    if number > array[-1]:
        print(count)
        return False
    if number < array[0]:
        print(count)
        return False
    start = 0
    end = len(array)
    while start != end:
        if number > array[(start+end)//2]:
            start = (start+end)//2
        elif number < array[(start+end)//2]:
            end = (start + end) // 2
        else:
            print(count)
            return True
        count += 1
    print(count)
    return False

# print(search([x for x in range(1000)],999))

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(2)
chidl1 = Node(1)
chidl2 = Node(3)
chidl3 = Node(5)
chidl4 = Node(4)

root.left = chidl1
root.right = chidl2
chidl2.right = chidl3
chidl3.left = chidl4


def search3(root,data):
    while root != None:
        if root.data == data:
            return True
        elif root.data > data:
            root = root.left
        else:
            root = root.right
    return False

print(search3(root,5))
