// Done after learning Kotlin for my DSA class

// 168ms (92.28%), 36.46MB (96.06%)


class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if(s.length != t.length){
            return false
        }
        
        var array = IntArray(26)

        for(letter in s){
            var letterIndex = letter -'a'
            array[letterIndex] +=1
        }
        for(letters in t){
            var letterIndex = letters-'a'
            array[letterIndex] -=1
        }
        for(entry in array){
            if(entry != 0){
                return false
            }
        }
        return true
    }
}