class Solution:
# example ["cat", "hello", ""]
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
    
    #example 3#cat5#hello
    def decode(self, s: str) -> List[str]:
        strArr = []
        i = 0
        length = ""
        while i < len(s):
            
            if s[i] != "#":
                length += s[i]
            elif s[i] == "#":
                word = s[i+1:i+1+int(length)]
                strArr.append(word)
                i += int(length)
                length = ""
            i+=1
        return strArr
