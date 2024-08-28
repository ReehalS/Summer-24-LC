# 565ms (92.88%), 22.96MB (60.57%)

# idea: calculate the distances, store the distances in a list, and distance+index in another list
# then sort distances list, and then append all points with distance less than or equal to kth distance to the pointsList
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        distAndIndices=[]
        for i in range(0,len(points)):
            dist= sqrt(points[i][0]*points[i][0]+points[i][1]*points[i][1])
            distances.append(dist)
            distAndIndices.append([dist,i])
        distances.sort()
        pointsList=[]
        for j in range(0,len(distAndIndices)):
            if(distAndIndices[j][0]<=distances[k-1]):
                pointsList.append(points[distAndIndices[j][1]])
        return pointsList