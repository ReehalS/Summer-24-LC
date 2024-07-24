# 59ms (92.44%), 16.68MB (58.65%)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        visited = set()
        sClr = image[sr][sc]

        self.depthFirstSearch(image,sr,sc,sClr,color,visited)

        return image

    def depthFirstSearch(self,image: List[List[int]], sr: int, sc: int, sClr: int, dClr:int, visited: set)->None:
        if(sr <0) or (sc<0) or (sr >= len(image)) or (sc >=len(image[0])) or (image[sr][sc]!= sClr) or (sr,sc) in visited:
            return
        
        visited.add((sr,sc))
        image[sr][sc] = dClr

        self.depthFirstSearch(image, sr-1, sc, sClr, dClr, visited)
        self.depthFirstSearch(image, sr+1, sc, sClr, dClr, visited)
        self.depthFirstSearch(image, sr, sc+1, sClr, dClr, visited)
        self.depthFirstSearch(image, sr, sc-1, sClr, dClr, visited)