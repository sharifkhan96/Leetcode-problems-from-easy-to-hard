class Classdog:
    def evenSquare(self, array1: list) -> list:
        if array1 is None:
            return None
        
        array_new = []

        for i in range(len(array1)):
            
            element = array1[i]
            if i % 2 == 0:
                element *= element
            array_new.append(element) 
        return array_new


    def evenSquareInPlace(self, array1: list) -> list:
        if array1 is None:
            return None
        
        length = len(array1)

        for i in range(len(array1)):
            if i % 2 == 0:
                array1[i] *= array1[i]
            
        return array1
            


def main():
    array = [9, -2, -9, 11, 56, -12, -3]
    obj1 = Classdog()

    # result = obj1.evenSquare(array)
    # print(result)
    result2 = obj1.evenSquareInPlace(array)
    print(result2)

if __name__ == "__main__":
    main()