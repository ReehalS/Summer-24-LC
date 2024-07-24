# 65ms (30.87%), 16.74MB (25.69)

# Could improve by not doing 2 loops. Instead it could be done in one loop. (todo)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote) > len(magazine)):
            return  False

        dictionary = {}

        for letter in magazine:
            if letter in dictionary:
                current = dictionary[letter]
                dictionary[letter] = current+1
            else:
                dictionary[letter] = 1

        print(dictionary)
            
        for letter in ransomNote:
            if letter in dictionary:
                current = dictionary[letter]
                dictionary[letter] = current -1
                if current-1 < 0:
                    return False
            else:
                return False

        return True
