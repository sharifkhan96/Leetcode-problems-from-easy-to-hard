class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        
        # total_time = 0
        # target_tickets = tickets[k]

        # for i in range(len(tickets)):
        #     if i <= k:
        #         total_time += min(tickets[i], target_tickets)
        #     else:
        #         total_time += min(tickets[i], target_tickets - 1)

        # return total_time
    


        
        # brute force version:
        time = 0
        while True:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return time
                if tickets[i] == 0:
                    continue
                    
                if tickets[i] >= 1:
                    tickets[i] -= 1
                    time+=1
            
        return time
        # o(M*N)

def main():
    st = Solution()
    tickets = [2,3,2]
    k = 2
    print(st.timeRequiredToBuy(tickets, k))

if __name__ == "__main__":
    main()
