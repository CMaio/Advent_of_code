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
        acceptedGame = False
        for turns in input:
            acceptedGame = True
            for turn in turns[1]:
                print(turn)
                for dices in turn:
                    dice = dices.split()
                    diceNumber = int(dice[0])
                    if dice[1] == "red" and Cube.redC < diceNumber: 
                        acceptedGame = False
                        print("number ", diceNumber)
                    elif dice[1] == "green" and Cube.greenC < diceNumber:
                        acceptedGame = False
                    elif dice[1] == "blue" and Cube.blueC < diceNumber:
                        acceptedGame = False

            if acceptedGame:
                games.append(int(turns[0]))

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
    print("And the sum of the IDs of those games for the solution of Day 2: Cube Conundrum is: " , solution)