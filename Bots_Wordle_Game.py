from Wordle_Game import Wordle
import string
import random

game = Wordle()

class Visuals():
    @staticmethod
    def run_game(): # runs the actual wordle game.
        game = Wordle()
        runner = Runner()
        word = list(game.getWord()) # retrieves random word

        guesses = 1
        data = {i: [0, 0, 0, 0, 0] for i in range(1, 8)}
        guessed = {i: [0, 0, 0, 0, 0] for i in range(1, 8)}
        
        found = [None, None, None, None, None]
        unknown = {}        
        none = []

        game_won = False

        while guesses <= 6:
            print(f"\n--- Guess {guesses} ---")
            print(f"Target word: {word}")

            # Correctly pass all tracking logs to runner.main
            inputs = runner.main(data, guesses, guessed, found, none, unknown)
            guessed[guesses] = inputs
            
            print(f"Bot guessed: {''.join(inputs)}")

            result_score = game.board(word, inputs)
            data[guesses] = result_score

            # Correctly align order of tracking structures
            unknown, none, found = runner.update_log(unknown, none, found, data, guessed, guesses)    

            print(f"Guess {guesses} result score: {data[guesses]}")

            if result_score == [1, 1, 1, 1, 1]:
                game_won = True
                break

            guesses += 1
        
        if game_won:
            print(f"\nYou completed the Wordle in {guesses} trys!")
        else:
            print(f"\nYou have run out of guesses! The word was {''.join(word)}")


class Runner():
    def main(self, datas, guesses, guesseds, fnd, no, uk):
        inputed = Inputs()
        
        if guesses > 1:
            next_words = inputed.create_input(fnd, no, uk)
            
            # FIXED: Grab the FIRST word string from the list, then split into characters
            if isinstance(next_words, list) and len(next_words) > 0:
                return list(next_words[0]) 
            
            return list("salet") # Fallback if no matching words remain
        else:
            initial_guess = list(inputed.initial())
            return initial_guess

        
    def update_log(self, uk, no, fnd, dta, gsd, gsnum):
        found = fnd
        unknown = uk
        none = no
        data = dta
        guessed = gsd
        
        last_guess_idx = gsnum
        unknown_cnt = len(unknown) + 1

        for j in range(5):
            letter = guessed[last_guess_idx][j]
            status = data[last_guess_idx][j]

            if status == 1:
                found[j] = letter

            elif status == 2:
                letter_exists = False
                for key, val in unknown.items():
                    if val[0] == letter:  
                        letter_exists = True
                        break
                
                if not letter_exists:
                    unknown[unknown_cnt] = [letter, status]
                    unknown_cnt += 1

            elif status == 0: 
                if letter not in none:
                    none.append(letter)
                    
        return unknown, none, found


class Inputs():
    def create_input(self, fnd, no, uk):
        all_words = game.bank()  
        found = fnd
        unknown = uk
        none = no

        filtered_words = []
        yellow_letters = [val[0] for val in unknown.values()]

        for word in all_words:  
            keep_word = True
            
            for idx, letter in enumerate(found):
                if letter and letter != 0 and word[idx] != letter:
                    keep_word = False
                    break
            
            if not keep_word:
                continue

            for letter in yellow_letters:
                if letter not in word:
                    keep_word = False
                    break
                    
            if not keep_word:
                continue

            for letter in none:
                if letter in word:
                    if letter in found or letter in yellow_letters:
                        continue
                    keep_word = False
                    break

            if keep_word:
                filtered_words.append(word)

        return filtered_words
        
    def initial(self):
        bank = ["salet", "slate", "crane", "trace", "crate", "stare", "roate", "slant", "raise", "arose", "stale", "scale", "soare", "least", "carte", "dealt", "roast", "scone", "orate", "audio", "adieu", "canoe", "saute", "shale", "clasp"]
        return random.choice(bank)

Visuals.run_game()