import re

class Trebuchet():

    def inputTransform(nameFile):
        f = open("./Day 1/Part1/"+nameFile, "r")
        inputArray = f.read().split('\n')
        f.close()
        return inputArray
    
    def processWord(word):
        numbers = re.findall("\d", word)
        return int(f"{numbers[0]}{numbers[len(numbers)-1]}")
    
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
    print("Write the name of the file you want to process: ")

    solution = Trebuchet.solution("input.txt")

    print("The solution for the Day 1: Trebuchet?! is: " , solution)