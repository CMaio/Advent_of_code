import re

class Cube():
    redC = 12
    greenC = 13
    blueC = 14

    def inputTransform(nameFile):
        f = open("./Day 2/Part1/"+nameFile, "r")
        inputArray = f.read().split('\n')
        inputTreated = []

        for line in inputArray:
            lineResult = line.split(":")
            gameID =re.findall("\d+",lineResult[0])
            games = lineResult[1].split(';')
            turns = []
            for game in games:
                turnsGame = game.split(',')
                turns.append(turnsGame)

            inputTreated.append([gameID[0],turns])
        f.close()
        return inputTreated
    
    def checkAcceptedGames(input):
        games = []
        for turns in input:
            redMin = 0
            blueMin = 0
            greenMin = 0
            for turn in turns[1]:
                for dices in turn:
                    dice = dices.split()
                    diceNumber = int(dice[0])
                    if dice[1] == "red": 
                        redMin = diceNumber if diceNumber>redMin else redMin
                    elif dice[1] == "green":
                        blueMin = diceNumber if diceNumber>blueMin else blueMin
                    elif dice[1] == "blue":
                        greenMin = diceNumber if diceNumber>greenMin else greenMin
            turnSum = redMin * blueMin * greenMin
            games.append(turnSum)

        return games


    def solution(nameFile):
        input = Cube.inputTransform(nameFile)
        games = Cube.checkAcceptedGames(input)
        sumUp = 0
        for game in games:
            sumUp += game

        return sumUp


        

if __name__ == "__main__":
    solution = Cube.solution("input.txt")
    print("The elf needs to know the games where is possible to play with only 12 red cubes, 13 green cubes, and 14 blue cubes")
    print("And the sum of the power of every game for the solution of Day 2: Cube Conundrum is: " , solution)