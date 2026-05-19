class Solution:

    def is_number(self, token) :
        try :
            float(token)
            return True

        except ValueError :
            return False


    def evalRPN(self, tokens: List[str]) -> int:
        Rpn = []

        for token in tokens :
            if self.is_number(token):
                Rpn.append(int(token))

            elif token == "+":
                firstDigit = Rpn.pop(-1)
                secondDigit = Rpn.pop(-1)

                result = firstDigit + secondDigit 
                Rpn.append(result)

            elif token == "-":
                firstDigit = Rpn.pop(-1)
                secondDigit = Rpn.pop(-1)

                result = secondDigit - firstDigit
                Rpn.append(result)

            elif token == "*":
                firstDigit = Rpn.pop(-1)
                secondDigit = Rpn.pop(-1)

                result = firstDigit * secondDigit 
                Rpn.append(result)

            elif token == "/":
                firstDigit = Rpn.pop(-1)
                secondDigit = Rpn.pop(-1)

                result = secondDigit / firstDigit
                Rpn.append(int(result))


        return Rpn[-1]

            