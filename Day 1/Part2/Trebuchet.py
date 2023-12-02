import re

class Trebuchet():

    def inputTransform(nameFile):
        f = open(nameFile, "r")
        inputArray = f.read().split('\n')
        f.close()
        return inputArray
    
    def translateWordIntoNum(wordTranslate):
        words= ["one","two","three","four","five","six","seven","eight","nine","zero"]
        nums= [1,2,3,4,5,6,7,8,9,0]

        number =nums[words.index(wordTranslate)] if wordTranslate in words else wordTranslate
        return number
    
    def processWord(word):
        
        numbers = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))")
        matches = [match.group(1) for match in numbers.finditer(word)]
        print("word",word)
        print("words", matches)
        print("numbers",Trebuchet.translateWordIntoNum(matches[0]),Trebuchet.translateWordIntoNum(matches[len(matches)-1]))
        return int(f"{Trebuchet.translateWordIntoNum(matches[0])}{Trebuchet.translateWordIntoNum(matches[len(matches)-1])}")
    
    def processData(input):
        numbersFoundInWords = []
        for word in input:
            numbersFoundInWords.append(Trebuchet.processWord(word))
        return numbersFoundInWords

    def solution(nameFile):
        input = Trebuchet.inputTransform(nameFile)
        numbersPerWord = Trebuchet.processData(input)
        result = 0
        for num in numbersPerWord:
            result += num

        return result

if __name__ == "__main__":
    solution = Trebuchet.solution("input.txt")

    print("The solution for the Day 1: Trebuchet?! part2 is: " , solution)