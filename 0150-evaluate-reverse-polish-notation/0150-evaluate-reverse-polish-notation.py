class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st= []
        for token in tokens:
            if token == '+':
                val = int(st.pop()+ st.pop())
                st.append(val)
            elif token == '-':
                val1 = st.pop()
                val2 = st.pop()
                val = int(val2-val1)
                st.append(val)
            elif token == '*':
                val = int(st.pop()*st.pop())
                st.append(val)
            elif token == '/':
                val1 = st.pop()
                val2 = st.pop()
                val = int(float(val2/val1))
                st.append(val)

            else:
                st.append(int(token))
                
        return st[0]