class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def parenthesis(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                parenthesis(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                parenthesis(openN, closeN + 1)
                stack.pop()

        parenthesis(0, 0)
        return res
