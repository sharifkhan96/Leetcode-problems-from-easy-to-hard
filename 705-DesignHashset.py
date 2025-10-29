class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # alist of buckets, each is a list (to handle collisions)

    def hash_function(self, key:int) -> int:
        # simple hash function: sum of character codes modulo the number of buckets
        #return sum(ord(char) for char in value) % self.size
        return key % self.size

    def add(self, key: int):
        # add a key if it's not already present
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def contains(self, key: int):
        # check if a key exists in the set
        index = self.hash_function(key)
        bucket = self.buckets[index]
        return key in bucket

    def remove(self, key: int):
        # remove a key
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def print_set(self):
        # Print all elements in the hash set
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


#time comnp:O(1)
#space comp: O(N)

def main():
    
    obj = SimpleHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))  # True
    print(obj.contains(3))  # False
    obj.add(2)
    obj.remove(2)
    print(obj.contains(2))  # False


if __name__ == "__main__":
    main()