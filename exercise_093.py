if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
        
    def fn(number, list_number):
        if number not in range(2,11):
            return
        
        for item in list_number:
            if item not in range(-100, 101):
                return
                
        list_number = sorted(list(set(list_number)))
            
        return list_number[-2]
            
            
    print(fn(n,arr))