# 67ms (46.83), 17.16MB (13.70%)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # got this part from StackOverflow, 
        # did not really improve performance as compared to a normal if statement
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,  
        }
        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return ops[oper](op1, op2)
        
        i=0
        while True:
            if(len(tokens)==1):
                return int(tokens[0])
            while((i+1<len(tokens)) and tokens[i] not in("+","-","/","*")):
                i+=1
            a=int(tokens[i-2])
            b=int(tokens[i-1])
            tokens[i-2] = eval_binary_expr(a,tokens[i],b)
            tokens.pop(i-1)
            tokens.pop(i-1)
            i-=2