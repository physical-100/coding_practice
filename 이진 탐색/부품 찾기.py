def binary_search(arr, target,start,end): # 이진 탐색으로 구현
    if start > end:
        return None
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid+1
    return None
N = int(input())
arr = list(map(int,input().split()))
# 리스트 말고 set으로 받을 수 있다.
#계수 정렬을 이용해서 풀때는 입력값으로 가능한 모든 값을 고려해야함
#문제에서 입력 값이 1000000의 범위를 가지기에 1000001의 배열을 선언해야함 
M = int(input())
target_arr = list(map(int,input().split()))
  #이진 탐색은 정렬이 되어 있어야한다
arr.sort()
for i in target_arr:
    if (binary_search(arr,i,0,N-1))!=None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
