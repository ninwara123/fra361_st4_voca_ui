from tkinter.constants import TRUE



# def g(xx,yy):
#     y = ""
#     for i in range(len(xx)):
#         for y in range(len(xx)):
#             if ord(xx[i])<=ord(xx[y]):
#                 y = xx[i]
#             else:

# g("abcd","bdca")
def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if ord(list[idx])>ord(list[idx+1]):
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
# list = [19,2,31,45,6,11,121,27]
list = "afgth"
bubblesort(list)
print(list)
sorted