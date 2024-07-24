// Done after learning Kotlin for my DSA class

// 205ms (52.97%) 38.26MB (34.60%)


class Solution {
    fun isPalindrome(s: String): Boolean {
        var forwardIndex=0
        var backwardIndex=s.length-1
        for(i in 0 until (s.length-(s.length%2))/2){
            if(!(s[forwardIndex].isDigit() || s[forwardIndex].isLetter())){
                while(!(s[forwardIndex].isDigit() || s[forwardIndex].isLetter())){
                    if(forwardIndex+1 <s.length){
                        forwardIndex++
                    }else{
                        return true
                    }
                    
                }
            }
            if(!(s[backwardIndex].isDigit() || s[backwardIndex].isLetter())){
                while(!(s[backwardIndex].isDigit() || s[backwardIndex].isLetter())){
                    if(backwardIndex-1 >= 0){
                        backwardIndex--
                    }else{
                        return true
                    }
                }
            }
            
            
            if((s[backwardIndex].isDigit() && s[forwardIndex].isDigit())&& s[backwardIndex]== s[forwardIndex]){

                if(forwardIndex+1 <s.length){
                        forwardIndex++
                    }else{
                        return true
                    }
                if(backwardIndex-1 >= 0){
                        backwardIndex--
                    }else{
                        return true
                    }
            } 
            else if((s[backwardIndex].isLetter() && s[forwardIndex].isLetter())&& s[backwardIndex].lowercase()==s[forwardIndex].lowercase()){
                if(forwardIndex+1 <s.length){
                        forwardIndex++
                    }else{
                        return true
                    }
                if(backwardIndex-1 >= 0){
                        backwardIndex--
                    }else{
                        return true
                    }
            }
            else{
                return false
            }
            
        }
        return true
    }
}