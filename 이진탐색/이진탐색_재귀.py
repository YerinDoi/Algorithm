def binary_search(array, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  # 바로 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  
  # 중간점의 값보다 찾는 값이 작은 경우 -> 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  
  # 중간점의 값보다 찾는 값이 큰 경우 -> 오른쪽 확인
  else:
    return binary_search(array, target, mid + 1, end)
  
n, target = 10, 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
  
result = binary_search(array, target, 0, n-1)

print(result + 1)
  