class Solution1:
    def CheckIfNandItsDoubleExist(self, array1: list[int]) -> bool:
        # if i != j and i < 0 and j > len(array1):
        #     return False
        
        # if array1[i] == 2 * array1[j]:
        #     return True
        
        # return False


        for i in range(len(array1)):
            for j in range(len(array1)):
                if i != j and array1[i] == 2 * array1[j]:
                    return True
        return False


def main():
    #arr = [10,2,5,3]
    arr = [3,1,7,11]
    print(arr)
    # i = int(input("enter i index: "))
    # j = int(input("enter j index: "))
    print("Lets see if i index is doubled the j index... ")
    obj1 = Solution1()
    decision = obj1.CheckIfNandItsDoubleExist(arr)
    if decision:
        print(decision)
    else:
        print(decision)


if __name__ == "__main__":
    main()