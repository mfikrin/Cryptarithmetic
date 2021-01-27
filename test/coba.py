#
# # for i in range(5,0,-1):
# #     print(i)
# #
# # string = "ABC"
# #
# # a = list(string)
# # print(a)
# #
# #
# # # Python program to print all permutations with
# # # duplicates allowed
# #
#
# #
# #
# # Function to print permutations of string
# # This function takes three parameters:
# # 1. String
# # 2. Starting index of the string
# # 3. Ending index of the string.
#
arrNum = [0 for i in range(10)]

for i in range(len(arrNum)):
    arrNum[i] = i

print(list(arrNum))

def toString(List):
    return ''.join(List)

# print(toString(arrNum))

arr = []
def permute(a, l, r):

    if l == r:
        arr.append(toString(a))

        # print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
string = "9567108234"
n = len(string)
a = list(string)
print("-----")
print(a)
print("-----")
permute(a, 0, n - 1)
print(arr)
print(len(arr))
print((arr[0][0]))
arrs = ["S","E","N","D","M","O","R","Y"]
print(arrs)

n = len(arrs)
answer = []
for permute in arr:
    if permute == '9567108234':
        answer.append(permute[0:len(arrs)])
        print("adddaa")
        break
print(answer)
#
#
# # This code is contributed by Bhavya Jain
#
# # Python function to print permutations of a given list
# # def permutation(lst):
# #     # If lst is empty then there are no permutations
# #     if len(lst) == 0:
# #         return []
# #
# #         # If there is only one element in lst then, only
# #     # one permuatation is possible
# #     if len(lst) == 1:
# #         return [lst]
# #
# #         # Find the permutations for lst if there are
# #     # more than 1 characters
# #
# #     l = []  # empty list that will store current permutation
# #
# #     # Iterate the input(lst) and calculate the permutation
# #     for i in range(len(lst)):
# #         m = lst[i]
# #
# #         # Extract lst[i] or m from the list.  remLst is
# #         # remaining list
# #         remLst = lst[:i] + lst[i + 1:]
# #
# #         # Generating all permutations where m is first
# #         # element
# #         for p in permutation(remLst):
# #             l.append([m] + p)
# #     return l
# #
# #
# # # Driver program to test above function
# # arr = []
# # data = list('0123456789')
# # for p in permutation(data):
# #     arr.append(toString(p))
# #
# # print(arr)
# # print(len(arr))
# #
# # for i in arr:
# #     if i == '9567108234':
# #         print("adddaa")
# #         break
