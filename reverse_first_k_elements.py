from collections import deque
class Solution:
    def reverse_first_k_elements(self, k, q):
        q = deque(q)
        stack = []

        for i in range(k):
            stack.append(q.popleft())

        
        while stack:
            q.append(stack.pop())

        
        for i in range(len(q)-k):
            q.append(q.popleft())

        return q



'''
    we are given a list(queue) and we need to reverse the k elements of it using stack
    complexities: O(n)  & O(n) for time and space complexities respectively
'''




def main():
    obj = Solution()
    k = 5
    q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("The left before reversing: ", q)
    print("The left after reversing: ", obj.reverse_first_k_elements(k, q))


if __name__ == "__main__":
    main()