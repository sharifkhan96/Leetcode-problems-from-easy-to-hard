from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue1 = deque()
        self.running_sum = 0

    def next(self, val: int) -> float:
        self.queue1.append(val)
        self.running_sum += val

        if len(self.queue1) > self.size:
            removed = self.queue1.popleft()
            self.running_sum -= removed

        return self.running_sum / len(self.queue1)



# time comp: O(1)
# space comp: O(n)


class main():
    size = 3
    
    obj1 = MovingAverage(size)
    print(obj1.next(1))
    print(obj1.next(10))
    print(obj1.next(3))
    print(obj1.next(5))




if __name__ == "__main__":
    main()