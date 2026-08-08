class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for Str in strs:
            encodedStr += f"{str(len(Str))}#"
            encodedStr += Str

        return encodedStr

    def decode(self, s: str) -> List[str]:
        strList = list()
        index = 0

        while index < len(s):
            decodedStr = ""
            numStr = ""

            while s[index] != "#":
                numStr += s[index]
                index += 1

            index += 1
            strLn = int(numStr)

            while strLn > 0:
                decodedStr += s[index]
                index += 1
                strLn -= 1

            strList.append(decodedStr)

        return strList
