class TwoSum:

    def __init__(self):
        self.list1 = []
        

    def add(self, number: int) -> None:
        self.list1.append(number)
        return self.list1

    def find(self, value: int) -> bool:
        self.list1.sort()
        for i in range(len(self.list1)):
            for j in range(1, len(self.list1)):
                if self.list1[i] + self.list1[j] == value:
                    return True
        return False
    
# time comp: O(n^2)
# space compl: O(n log n)
        

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