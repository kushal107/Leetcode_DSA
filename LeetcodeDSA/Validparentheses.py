s = "(){}[]"

stack = []
#mydict = {"}":"{", ")":"(", "]":"["}
mydict = {"{":"}", "(":")", "[":"]"}

for paren in s:
    if paren in mydict:
         stack.append(paren)
    else:
        if not stack or  paren != mydict[stack.pop()]:
            print(False)
            quit() 
        
    
print(True)
print(queue)