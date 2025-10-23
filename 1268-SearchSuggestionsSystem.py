class Solution:
    def suggestedProducts(self, products, searchWord):
        
        # step 1: sort the product list lexicographically
        products.sort()
        result = []
        prefix = ""

        # step 2: for each character typed
        for c in searchWord:
            prefix += c
            suggestions = []

            # step 3: collect up to 3 matching words
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                if len(suggestions) == 3:
                    break

            result.append(suggestions)

        return result

# time comp: O(n log n + n * m
# space comp: 

# :
def main():
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    obj = Solution()
    print(obj.suggestedProducts(products, searchWord))


if __name__ == "__main__":
    main()
