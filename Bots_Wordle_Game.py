from Wordle_Game import Wordle
game = Wordle()

class Visuals():
    def run_game(): #runs the actual wordle game.
        game = Wordle()
        word = list(game.getWord()) #retrieves random word

        guesses = 1
        data = { #stores a 1 for in the right place and 2 for wrong place.
            1: [0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0],
            3: [0, 0, 0, 0, 0],
            4: [0, 0, 0, 0, 0],
            5: [0, 0, 0, 0, 0]
        }
        guessed = { #words that have been guessed
            1: [0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0],
            3: [0, 0, 0, 0, 0],
            4: [0, 0, 0, 0, 0],
            5: [0, 0, 0, 0, 0]
        }
                
        while guesses < 6 and ([1, 1, 1, 1, 1,] not in data.values()):#runs the game for a maximum of 6 turn or until the word is guessed.
            print(word)
            inputs = main.main(data, guesses, guessed) #calls for the bot to input a word.
            guessed[guesses] = inputs #saves the input to guessed
            data[guesses] = game.board(word, inputs)#calls the file that holds the rules to the game to compare and see how the bot did.
            
            
            print(data[guesses])
            guesses += 1
        if [1, 1, 1, 1, 1,] not in data.values():#checks if the bot won or lost
            print("You have run out of Guesses!")
            print(data)
                    
        else:
            print(f"You completed the Wordle in {guesses -1} trys!")
            print(data)

class inputs():
    
    def get_result(self, info, guess_num, guessed_1):
        data = info
        guessed = guessed_1
        row = guess_num
        wrong_location = [0, 0, 0, 0, 0]
        found = [0, 0, 0, 0, 0]
        unknown = [0, 0, 0, 0, 0]
        
        for index in range(5):#sorts the guess to see what letters were correct and which ones it has to move.
            if data[row][index] == 1:
                found[index] = guessed[row][index]
            elif data[row][index] == 2:
                wrong_location[index] = guessed[row][index]
            elif data[row][index] == 0:
                unknown[index] = guessed[row][index]



        return wrong_location, found, unknown #returns the letters 

    def create_input(self):
        pass

    def initial():
        pass

class main():
    def main(self, datas, guesses, guesseds):
        data = datas
        guess_num = guesses
        guessed = guesseds

        change_f = 28 + guess_num
        change_wl = 35 + guess_num
        change_un = 42 + guess_num

        if guess_num > 1:
            wl, f, un = inputs.get_result(data[guess_num], guess_num, guessed[guess_num]) #calls the get_result function so it can start making a guess

            wl = "".join(str(num) for num in wl) #all of this updates the text file so that it can store information between guesses
            f = "".join(str(num) for num in f)
            un = "".join(str(num) for num in un)

            with open("Bots_Data.txt", "r") as file:
                lines = file.readlines()
            lines[change_f] = f + "\n"
            lines[change_wl] = wl + "\n"
            lines[change_un] = un + "\n"

            with open("Bots_Data.txt", "w") as file:
                file.writelines(lines)


            next_guess = inputs.create_input()
        else:
            pass



Visuals.run_game()