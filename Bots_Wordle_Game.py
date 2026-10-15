from Wordle_Game import Wordle
import string
game = Wordle()

class Visuals():
    def run_game(): #runs the actual wordle game.
        game = Wordle()
        runner = Runner()
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
            inputs = runner.main(data, guesses, guessed) #calls for the bot to input a word.
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



class Runner():
    def main(self, datas, guesses, guesseds):
        inputed = Inputs()
        data = datas
        guess_num = guesses
        guessed = guesseds

        change_f = 28 + guess_num
        change_wl = 35 + guess_num
        change_un = 42 + guess_num

        if guess_num > 1:
            wl, f, un = inputed.get_result(data[guess_num], guess_num, guessed[guess_num]) #calls the get_result function so it can start making a guess

            wl = "".join(str(num) for num in wl) #all of this updates the text file so that it can store information between guesses
            f = "".join(str(num) for num in f)
            un = "".join(str(num) for num in un)

            with open("Bots_Data", "r") as file:
                lines = file.readlines()
            lines[change_f] = f + "\n"
            lines[change_wl] = wl + "\n"
            lines[change_un] = un + "\n"

            with open("Bots_Data", "w") as file:
                file.writelines(lines)


            next_guess = inputed.create_input()
            return next_guess
        else:
            initial_guess = inputed.initial(data, guessed)
            return initial_guess

        inputed.change_file(guessed, data)


class Inputs():
    
    def get_result(self, info, guess_num, guessed_1):
        data = info
        guessed = guessed_1
        row = guess_num
        wrong_location = [0, 0, 0, 0, 0]
        found = [0, 0, 0, 0, 0]
        unknown = [0, 0, 0, 0, 0]
        
        for index in range(5):#sorts the guess to see what letters were correct and which ones it has to move.
            if data[index] == 1:
                found[index] = guessed[index]
            elif data[index] == 2:
                wrong_location[index] = guessed[index]
            elif data[index] == 0:
                unknown[index] = guessed[index]

        return wrong_location, found, unknown #returns the letters 





    def create_input(self):
        all_words = game.bank()
        new_word = [None, None, None, None, None]

        with open("Bots_Data", "r") as file:
            lines = file.readlines()

        for i in range(1, 6):
            record = lines[28 + i].strip()
            record = list(record)
            for j in range(len(record)):
                if record[j] != "0":
                    new_word[j] = record[j]

        all_words = [
            word for word in all_words
            if all(new_word[j] is None or word[j] == new_word[j] for j in range(5))
        ]

        for k in range(1, 6):
            record_y = lines[35 + k].strip()#editing this for yellow letters.

            for l in range(len(record_y)):
                char = record_y[l]
                if char != "0":
                    all_words = [
                        word for word in all_words
                        if char in word and word[l] != char
                    ]

        
        for m in range(1, 6):
            record_n = lines[42 + m].strip()#editing this for yellow letters.

            for n in range(len(record_n)):
                char_n = record_n[n]
                if char_n != "0":
                    all_words = [
                        word for word in all_words
                        if char_n not in word
                    ]
        if all_words:
            return list(all_words[0])
        else:
            return ["0", "0", "0", "0", "0", ]
        

         
    

    def initial(self, datas, guesseds ):
        data = datas
        guessed = guesseds
        all_words = game.bank()
        bank = []
        alpha = list(string.ascii_lowercase)
        with open("Bots_Data", "r") as file:
            lines = file.readline()
        letters = lines.split(",")
        letters = [int(x) for x in letters]
        for i in range(8):
            largest = max(letters)
            locate = letters.index(largest)
            bank.append(alpha[locate])
            letters[locate] = -1

        count = 0
        for j in range(5):
            if bank[j] in "aeiouy":
                count += 1

        if count == 4:
            bank[4], bank[6] = bank[6], bank[4]
        elif count == 5:
            bank[5], bank[7] = bank[7], bank[5]


        for idx in range(5):
            char = bank[idx]
            all_words = [
                word for word in all_words
                if char in word
            ]
        
        return bank




    def change_file(self, guesseds, datas):
        
        guessed = guesseds[1]
        data = datas[1]
        bank = []
        send_back = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        alpha = list(string.ascii_lowercase)

        with open("Bots_Data", "r") as file:
            lines = file.readline()
        letters = [int(x) for x in lines.split(",") if x.strip()]

        for i in range(5):
            if data[i] == 1:
                letter = guessed[i].lower()
                if letter in alpha:
                    let_index = alpha.index(letter)
                    letters[let_index] += 1
                    send_back[let_index] +=1
        
        with open("Bots_Data", "w", encoding='utf-8') as file:
            string_to_write = ",".join(map(str, send_back))
            file.write(string_to_write)






        


Visuals.run_game()