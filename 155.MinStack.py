class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

        

def main():
    st = MinStack()
    st.push(3)
    st.push(5)
    st.push(2)
    print(st.getMin())  # 2
    st.pop()
    print(st.getMin())  # 3

if __name__ == "__main__":
    main()
