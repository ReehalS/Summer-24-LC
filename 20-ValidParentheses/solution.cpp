// redo this problem

// Time complexity: O(n)
// 4ms (11.94%), 6.61MB (100%)

class Solution {
public:
    bool isValid(string s) {
        
        stack<char> stk;
         for(char c:s){
            if(c== '(' || c=='{' || c== '['){
                stk.push(c);
            }
            else{
                if (stk.empty() || (c == ')' && stk.top() != '(') || (c == '}' && stk.top() != '{') || (c == ']' && stk.top() != '[')) {
                    return false;
                }
                stk.pop();
            }
        }
        return stk.empty();  
    }
};