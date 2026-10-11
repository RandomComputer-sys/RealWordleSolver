from Wordle_Game import Wordle
game = Wordle()
class Visuals():

    game = Wordle()
    word = list(game.getWord())

    guesses = 1
    data = {
        1: [0, 0, 0, 0, 0],
        2: [0, 0, 0, 0, 0],
        3: [0, 0, 0, 0, 0],
        4: [0, 0, 0, 0, 0],
        5: [0, 0, 0, 0, 0]
    }
    guessed = {
        1: [0, 0, 0, 0, 0],
        2: [0, 0, 0, 0, 0],
        3: [0, 0, 0, 0, 0],
        4: [0, 0, 0, 0, 0],
        5: [0, 0, 0, 0, 0]
    }
            
    while guesses < 6 and ([1, 1, 1, 1, 1,] not in data.values()):
        print(word)
        inputs = list(inputs.get_result(data))
        guessed[guesses] = inputs
        data[guesses] = game.board(word, inputs, guesses, guessed)
        
        
        print(data[guesses])
        guesses += 1
    if [1, 1, 1, 1, 1,] not in data.values():
        print("You have run out of Guesses!")
        print(data)
                
    else:
        print(f"You completed the Wordle in {guesses -1} trys!")
        print(data)

class inputs():
    
    def get_result(self, info, guess_num, guessed_1):
        data = info
        guessed = guess_num
        roun = guess_num
        guess = [0, 0, 0, 0, 0]
        found = [0, 0, 0, 0, 0]
        unknown = [0, 0, 0, 0, 0]
        i = 1
        while i < roun:
            for j in data:
                if data[j] == 1:
                    found[j] = 1


        

        


    def create_input(self):
        pass


class outputs():
    pass

inputs.get_result()