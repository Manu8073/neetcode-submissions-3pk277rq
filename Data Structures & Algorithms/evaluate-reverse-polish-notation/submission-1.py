class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for ch in tokens:
            if ch not in "+-*/":
                st.append(int(ch))
            else:
                op2=st.pop()
                op1=st.pop()
                if ch=='+':
                    st.append(op1 + op2)
                elif ch=='-':
                    st.append(op1 - op2)
                elif ch=='*':
                    st.append(op1 * op2)
                elif ch=='/':
                    st.append(int(op1 / op2))
        return st.pop()