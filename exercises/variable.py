# def array_right_move(steps,array):
#     step = 0
#     while step < steps:
#         last = array[-1]
#         i = len(array)-2
#         while i >= 0:
#             array[i+1] = array[i]
#             i = i-1
#         array[0] = last
#         step += 1
#     return array


# array = [1,2,3]
# steps = 2
# step = 0
# while step < steps:
#     last = array[-1]
#     i = len(array)-2
#     while i >= 0:
#         array[i+1] = array[i]
#         i = i-1
#     array[0] = last
#     step += 1
#
#
# print(array)

def table(n):
    for i in range(1,13):
        s = n * i
        print("{} * {} = {}".format(n,i,n*i))


table(5)
