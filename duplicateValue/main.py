def find_duplicates(arr1, arr2):
  arr3=sorted(arr1+arr2)
  print(arr3)
  arr4=[]
  for i in range(0,len(arr3)-1):
      if arr3[i] == arr3[i+1]:
          arr4.append(arr3[i])
  return arr4