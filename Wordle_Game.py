import random
class Wordle():


    def board(self):
        word = list(self.getWord())
        print(word)
        guess = self.getInput()
        end_result = [ 0, 0, 0, 0, 0]
        for i in range(5):
            if guess[i] == word[i]:
                end_result[i] = " 1"
            elif guess[i] in word:
                end_result[i] = " 2"
                        

        return end_result


    def getWord(self):
        word_bank = ["about", "above", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alike", "alive", "allow", "alone", "along", "alter", "amber", "among", "anger", "angle", "angry", "apart", "apple", "apply", "apron", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "audio", "audit", "avoid", "award", "aware", "awful", "bacon", "badge", "bagel", "baker", "balsa", "banjo", "bared", "barge", "baron", "basal", "basic", "basis", "baste", "batch", "bathe", "baths", "baton", "batty", "beach", "beads", "beady", "beaks", "beams", "beamy", "beans", "beard", "bears", "beast", "beats", "beech", "beefs", "beefy", "beeps", "beers", "beery", "beets", "befit", "began", "begat", "beget", "begin", "begot", "begun", "beige", "being", "belay", "belch", "belie", "belle", "bells", "belly", "below", "belts", "bench", "bends", "bendy", "beret", "berry", "berth", "beryl", "beset", "bests", "betel", "bevel", "bible", "bided", "bides", "bidet", "bight", "bigot", "bijou", "biked", "biker", "bikes", "bilge", "bills", "billy", "binge", "bingo", "biome", "biped", "birch", "birds", "birth", "bison", "bitch", "biter", "bites", "bitsy", "bitty", "blabs", "black", "blade", "blame", "bland", "blank", "blare", "blast", "blaze", "bleak", "blear", "bleat", "bleed", "bleep", "blend", "bless", "blest", "blind", "blink", "blips", "bliss", "blitz", "bloat", "blobs", "block", "blocs", "blogs", "bloke", "blond", "blood", "bloom", "bloop", "blots", "blown", "blows", "blowy", "blued", "blues", "bluff", "blunt", "blurb", "blurs", "blurt", "blush", "board", "boast", "boats", "bobby", "boded", "bodes", "bodge", "bogey", "bogus", "boils", "boily", "boldy", "boles", "bolls", "bolts", "bombs", "bonds", "boned", "bones", "boney", "bongo", "bongs", "bonny", "bonus", "boobs", "booby", "booed", "books", "booky", "booms", "boomy", "boons", "boors", "boost", "booth", "boots", "booty", "booze", "boozy", "borax", "bored", "bores", "boric", "borne", "boron", "bosom", "boson", "bossy", "bosun", "botch", "botel", "bothy", "botox", "bound", "bount", "bourn", "bouts", "boved", "bovid", "bowed", "bowel", "bower", "bowie", "bowls", "bowse", "boxed", "boxen", "boxer", "boxes", "boyar", "boyla", "boyos", "bozos", "brace", "brach", "bract", "brads", "braes", "brags", "braid", "brail", "brain", "brake", "braky", "bramp", "brand", "brane", "brank", "brans", "brant", "brash", "brass", "brast", "bratp", "brats", "brava", "brave", "bravo", "brawl", "brawn", "braws", "braxy", "brays", "braza", "braze", "bread", "break", "bream", "brede", "breed", "brees", "breid", "breis", "breme", "brens", "brent", "brera", "brere", "bress", "brest", "breve", "brews", "brial", "briar", "bribe", "brick", "bride", "brief", "brier", "bries", "briggs", "brigs", "brike", "brikk", "brill", "brims", "brine", "bring", "brink", "brins", "briny", "brios", "brise", "brisk", "briss", "brist", "brith", "brits", "britt", "briza", "broad", "broch", "brock", "brods", "brogh", "brogs", "broil", "broke", "broma", "brome", "bromo", "bronc", "bronx", "brood", "brook", "brool", "broom", "broon", "broos", "brose", "brosy", "broth", "brown", "brows", "brugh", "bruin", "bruit", "brule", "brume", "brung", "brunt", "brush", "brusk", "brust", "brute", "bruts", "bruvs", "buans", "buart", "bubal", "bubas", "bubba", "bubble", "bubby", "bubus", "bucca", "bucco", "buccy", "buchu", "bucko", "bucks", "bucku", "bucky", "budas", "buddy", "buded", "budes", "budge", "budis", "budos", "buena", "bueno", "buffa", "buffe", "buffi", "buffo", "buffs", "buffy", "bufos", "bufty", "bugan", "buggy", "bugle", "bugly", "buhrs", "buiks", "build", "built", "buist", "bukes", "bulbs", "bulge", "bulgy", "bulks", "bulky", "bulla", "bulls", "bully", "bulse", "bumbo", "bumfs", "bumph", "bumps", "bumpy", "bunch", "bunco", "bunds", "bundt", "bungs", "bungy", "bunia", "bunje", "bunjy", "bunks", "bunns", "bunny", "bunts", "bunty", "bunya", "buoys", "buppy", "buran", "buras", "burbs", "burcm", "burds", "bured", "buren", "buret", "burgh", "burgs", "burin", "burka", "burke", "burks", "burls", "burly", "burns", "burnt", "buroo", "burps", "burqa", "burro", "burrs", "burry", "bursa", "burse", "burst", "busby", "bused", "buses", "bushy", "busks", "busky", "bussu", "busti", "busts", "busty", "butch", "buteo", "butes", "butle", "butoh", "butte", "butts", "butty", "butut", "butyl", "buxom", "buyer", "buyin", "buzes", "buzzu", "buzzy", "bwana", "bwazi", "byded", "bydes", "byked", "bykes", "bylaw", "bynam", "byres", "byrls", "byssi", "bytes", "byway", "cabin", "cable", "camel", "canal", "candy", "canon", "cargo", "carol", "carry", "carve", "cases", "catch", "cause", "cedar", "chain", "chair", "chalk", "champ", "chant", "chaos", "charm", "chart", "chase", "cheap", "cheat", "check", "cheek", "cheer", "chess", "chest", "chick", "chief", "child", "chill", "china", "chips", "choir", "chose", "chuck", "chunk", "churn", "cigar", "circa", "civic", "civil", "claim", "clash", "clasp", "class", "clean", "clear", "clerk", "click", "cliff", "climb", "cling", "clock", "close", "cloth", "cloud", "clown", "coach", "coast", "color", "comet", "comic", "comma", "coral", "corps", "costs", "couch", "cough", "could", "count", "coupe", "court", "cover", "covet", "craft", "crane", "crank", "crash", "crass", "crate", "crave", "crawl", "craze", "crazy", "creak", "cream", "creed", "creek", "creep", "crepe", "crept", "crest", "cried", "cries", "crime", "crimp", "crisp", "croak", "crock", "crone", "crony", "crook", "cross", "croup", "crowd", "crown", "crude", "cruel", "crumb", "crush", "crust", "crypt"]
        num = random.randint(1,len(word_bank))
        return word_bank[num]
        
    
    def output(self):
        guesses = 1
        data = {
            1: [0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0],
            3: [0, 0, 0, 0, 0],
            4: [0, 0, 0, 0, 0],
            5: [0, 0, 0, 0, 0]
        }
        
        while guesses < 6 and ([1, 1, 1, 1, 1,] not in data.values()):
            data[guesses] = self.board()
        
            if [1, 1, 1, 1, 1,] in data.values() == False:
                print("You have run out of Guesses!")
                return data
            else:
                print(f"You completed the Wordle in {guesses} trys!")
                return data

        

    def getInput(self):
        while True:
            guess = input("Enter a 5 letter word: ")
            if len(guess) != 5:
                print('Guess must be 5 letters long')
                break
            else:
                return list(guess)
        
game = Wordle()
data = game.output()
print(data)
