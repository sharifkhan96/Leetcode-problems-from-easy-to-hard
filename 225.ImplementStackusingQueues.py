from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.queue)-1):
            self.push(self.queue.popleft())

        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        return len(self.queue) == 0


# time and space complexities: O(1) except the po() but it's actually O(N), O(N)

def main():
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    print(obj.push(3))

    print(obj.top())
    print(obj.pop())
    # print(obj.pop()) # this line will dtermine the fate of the empty state of the stack ::)
    print(obj.empty())
    print(obj.top())




if __name__ == "__main__":
    main()