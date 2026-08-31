"""
we need to encode and decode strings, we care given a lsit of strings that needs to be encoded as a string, then later decoded back into a list of strigns 

input can contain any valid ascii char 

so initial thoughts we could use the ascii table value (ord) of each char to convert it to a number and then use a characters as the word abd letter delimeter. ex 01E11E32A23E4r42E34A 
where A is the word delimeter and E is the  letter delimeter 
"""

class Solution:
    wordDelim = "A"
    letterDelim = "E"

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        if len(strs) == 0:
            return "nothing"
       
        for s in strs:
            for c in s:
                encodedString = encodedString + str(ord(c)) + self.letterDelim
            encodedString = encodedString + self.wordDelim
        
        # print(f"encodedString : {encodedString}")
        if len(encodedString) > 0 and encodedString[-1] == self.wordDelim:
            encodedString = encodedString[:-1]
        # print(f"encodedString : {encodedString}")
        if len(encodedString) > 0 and encodedString[-1] == self.letterDelim:
            encodedString = encodedString[:-1]
        # print(f"encodedString : {encodedString}")
        return encodedString
    

    def decode(self, s: str) -> List[str]:
        res = []
        if s == "nothing":
            return []
        
        encodedWords = s.split(self.wordDelim)
        print(f"encodedWords : {encodedWords}")
        for encodedWord in encodedWords:
            letters = encodedWord.split(self.letterDelim)
            # print(f"letters : {letters}")
            word = ""
            for letter in letters:
                if letter == "": continue
                # print(f"Letter {letter}")
                word = word + chr(int(letter))
            res.append(word)

        return res