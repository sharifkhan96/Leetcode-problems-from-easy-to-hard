class TwoSum:
    '''
    def __init__(self):
        self.list1 = []
        

    def add(self, number: int) -> None:
        self.list1.append(number)
        return self.list1

    def find(self, value: int) -> bool:
        self.list1.sort()
        for i in range(len(self.list1)):
            for j in range(i+1, len(self.list1)):
                if self.list1[i] + self.list1[j] == value:
                    return True
        return False
    
# time comp: O(n^2)
# space compl: O(n)
       '''
    
    '''
    
    # two pointer soluiton
    class TwoSum:
    def __init__(self):
        self.list1 = []

    def add(self, number: int) -> None:
        self.list1.append(number)

    def find(self, value: int) -> bool:
        nums = sorted(self.list1)

        l, r = 0, len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]

            if s == value:
                return True
            elif s < value:
                l += 1    # increase sum
            else:
                r -= 1    # decrease sum

        return False
    
    '''

    # a more faster solution
    def __init__(self):
        self.map1 = {}

    def add(self, number: int) -> None:
        if number in self.map1:
            self.map1[number] += 1
        else:
            self.map1[number] = 1

    def find(self, value: int) -> bool:
        for num in self.map1:
            target = value - num

            if target in self.map1 and target != num:
                return True
            
            if target == num and self.map1[num] >= 2:
                return True
            
        return False
    
    # time comp: O(n log n)
    # space comp: O(n) 

class main():
# Your TwoSum object will be instantiated and called as such:
    obj = TwoSum()
    print(obj.add(3))
    print(obj.add(1))
    print(obj.add(5))

    param_2 = obj.find(4)
    print(param_2)
    param_3 = obj.find(7)
    print(param_3)

if __name__ == "__main__":
    main()