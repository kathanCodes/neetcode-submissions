class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackRP = list()

        for token in tokens:
            if token.lstrip('-').isnumeric():
                stackRP.append(int(token))

            else:
                firstNum = stackRP[-1]
                stackRP.pop()

                secondNum = stackRP[-1]
                stackRP.pop()

                resultNum = 0
                if token == "+":
                    resultNum = secondNum + firstNum

                elif token == "-":
                    resultNum = secondNum - firstNum

                elif token == "*":
                    resultNum = secondNum * firstNum

                else:
                    resultNum = int(secondNum / firstNum)

                stackRP.append(resultNum)

            
        return stackRP[-1]
