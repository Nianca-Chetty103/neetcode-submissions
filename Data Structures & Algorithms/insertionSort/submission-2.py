class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result =[]

        for i in range ( len(pairs)):
           key = pairs[i] 
           j = i -1
           
           while j >= 0 and pairs[j].key > key.key:
               pairs[j + 1] = pairs[j]
               j -= 1
               
           pairs[j + 1] = key
           result.append([Pair(p.key, p.value) for p in pairs])

        return result