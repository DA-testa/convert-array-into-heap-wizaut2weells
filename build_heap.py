# python3
def build_heap(data):
    n = len(data)
    swaps = []
    
    def heapify(i):
        nonlocal swaps
        largest = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        
        if left_child < n and data[left_child] > data[largest]:
            largest = left_child
            
        if right_child < n and data[right_child] > data[largest]:
            largest = right_child
            
        if largest != i:
            swaps.append((i, largest))
            data[i], data[largest] = data[largest], data[i]
            heapify(largest)
    
    # Build heap
    for i in range(n//2, -1, -1):
        heapify(i)
    
    return swaps



def main():
    input_method=input("I or F")
    if "I" in input_method:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_method:
        file_name = input()
        with open (file_name, 'r'):
            n = int(file_name.readline())
            data = list(map(int, file_name.readline().split()))
    else:
        print("Wrong input")
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
