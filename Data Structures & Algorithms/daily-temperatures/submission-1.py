class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stackIndex = list(list())
        resultArr = list()


        for index , temperature in enumerate(reversed(temperatures)) :
            currDif = 0
            while stackIndex :
                currNum = stackIndex[-1]
                if currNum[0] > temperature :
                    currDif = index - currNum[1]
                    break
                stackIndex.pop()
                
            resultArr.append(currDif)   
            stackIndex.append((temperature , index))

        resultArr.reverse()     

        return resultArr