class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string `s` containing just the characters 
        '(', ')', '{', '}', '[' and ']' is valid.

        A string is valid if:
        1. Open brackets are closed by the same type of brackets.
        2. Open brackets are closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.

        :param s: A string containing parentheses
        :return: True if the string is valid, False otherwise
        """        
        matches = {')': '(', '}': '{', ']': '['}
        stack = []  
        for p in s:
            if p in matches.values():
                stack.append(p)
            elif p in matches:
                if stack and stack[-1] == matches[p]:
                    stack.pop()
                else:
                    return False
        return not stack
        


solution = Solution()

print(solution.isValid(")"))          # False
print(solution.isValid("((("))        # False
print(solution.isValid("()[]{}"))     # True
print(solution.isValid("([{}])"))     # True
print(solution.isValid("{[()]}"))     # True
print(solution.isValid("(([]){})"))   # True
print(solution.isValid("{[(])}"))     # False