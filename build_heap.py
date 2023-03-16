# python3
def build_heap(data):
    n = len(data)
    swaps = []
    
    def heapify(i):
        nonlocal swaps
        largest = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        
        if left_child < n and data[left_child] < data[largest]:
            largest = left_child
            
        if right_child < n and data[right_child] < data[largest]:
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
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in input_method:
        file_name = input()
        if 'a' in file_name:
            return
        with open (f"./tests/{file_name}", 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split(" ")))
    else:
        print("Wrong input")
        return

    assert len(data) == n

    arr = [[] for i in range(n)]
    for i in range(n):
        if data[i]<n:
            arr[data[i]].append(i)
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()