#A =[1,3,6,6,3,1]
#A =[2,5,8,9,1]
#A = 'animaljamina'
A = 'animaljjamina'
#A = 'animalamina'
#A = 'animallaminate'

def palindome(A):
    for i in range(len(A)//2):
        print(A[i], A[-1-i])
        if A[i] != A [-1-i]:
            return False
    return True

print(palindome(A))

