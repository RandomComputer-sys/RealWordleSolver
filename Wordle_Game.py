import random
class Wordle():


    def board(self, ran_word, inputss):#checks how close the guess was to the answer and returns a 1 for in the right place and a 2 for in the word but wrong spot.
        word = ran_word
        inputs = inputss
        print(word)
        guess = inputs
        while guess == 0:
            guess = inputs
        print(guess)
        x = word.copy()
        end_result = [ "0", "0", "0", "0", "0"]
        for i in range(len(x)):
            if guess[i] == x[i]:
                x[i] = "0"
                end_result[i] = "1"
        
        for j in range(len(x)):
            if guess[j] in x:
                match_index = x.index(guess[j])
                x[match_index] = "0"
                end_result[j] =  "2"
                        
        
        return end_result


    def getWord(self): #700 word wordbank
        word_bank = ["about", "above", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", 
    "agree", "ahead", "alarm", "album", "alert", "alike", "alive", "allot", "allow", "alone", 
    "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena", 
    "argue", "arise", "array", "arrow", "aside", "asset", "audio", "audit", "avoid", "award", 
    "aware", "awful", "badly", "baker", "bases", "basic", "basis", "beach", "beard", "beast", 
    "begin", "being", "below", "bench", "berry", "bible", "birth", "black", "blade", "blame", 
    "blank", "blast", "blend", "blind", "block", "blood", "board", "boast", "bonus", "boost", 
    "bound", "brain", "brake", "brand", "brave", "bread", "break", "breed", "brick", "bride", 
    "brief", "bring", "broad", "broke", "brown", "brush", "build", "built", "buyer", "cable", 
    "camel", "campa", "canal", "candy", "canon", "cargo", "carol", "carry", "carve", "cases", 
    "catch", "cater", "cause", "cedar", "chain", "chair", "chalk", "champ", "chant", "chaos", 
    "charm", "chart", "chase", "cheap", "cheat", "check", "cheek", "cheer", "chess", "chest", 
    "chick", "chief", "child", "chili", "chill", "china", "chips", "choir", "chose", "chuck", 
    "chunk", "churn", "cigar", "civic", "civil", "claim", "clash", "clasp", "class", "clean", 
    "clear", "clerk", "click", "cliff", "climb", "cling", "clock", "clone", "close", "cloth", 
    "cloud", "clown", "clump", "coach", "coast", "cobra", "cocoa", "colon", "color", "comet", 
    "comic", "comma", "conch", "coney", "coral", "couch", "cough", "could", "count", "coupe", 
    "court", "cover", "covet", "crack", "craft", "cramp", "crane", "crank", "crash", "crass", 
    "crate", "crave", "crawl", "crazy", "cream", "creed", "creek", "creep", "creme", "crepe", 
    "cress", "crest", "crewz", "cried", "crier", "crime", "crimp", "crisp", "crock", "crook", 
    "cross", "crowd", "crown", "crude", "cruel", "crumb", "crush", "crust", "crypt", 
    "cubic", "cuffs", "cumin", "cupid", "curry", "curse", "curve", "cycle", "cynic", "daddy", 
    "daily", "dairy", "daisy", "dance", "dandy", "dated", "datum", "dawns", "dazed", "dealt", 
    "deary", "death", "debar", "debit", "debug", "debut", "decal", "decay", "decor", "decoy", 
    "decry", "defer", "deity", "delay", "delta", "demon", "demur", "denim", "dense", "depot", 
    "depth", "derby", "detox", "deuce", "devil", "diary", "diced", "dicey", "digit", "diner", 
    "dingo", "dingy", "dinky", "diode", "dirge", "dirty", "disco", "ditch", "ditto", "ditty", 
    "divan", "diver", "divot", "divvy", "dizzy", "dodge", "dodgy", "doers", "dogma", "doing", 
    "doily", "doles", "dolls", "dolly", "dolor", "dolts", "donor", "donut", "dooms", "doors", 
    "doozy", "doped", "dopey", "dorks", "dorky", "dorms", "dosed", "doses", "doted", "dotes", 
    "doubt", "dough", "douse", "doves", "dowdy", "dowel", "dower", "downs", "downy", "dowry", 
    "dowse", "doyen", "dozed", "dozen", "dozer", "dozes", "drabs", "drack", "drags", "drain", 
    "drake", "drama", "drams", "drank", "drape", "drats", "drawl", "drawn", "draws", "drays", 
    "dread", "dream", "drear", "dregs", "dress", "dried", "drier", "dries", "drift", "drill", 
    "drily", "drink", "drips", "drive", "droid", "droll", "drone", "drool", "droop", "drops", 
    "dross", "drove", "drown", "drubs", "drugs", "druid", "drums", "drunk", "drupe", "dryad", 
    "dryer", "dryly", "duals", "ducal", "ducat", "duces", "duchy", "ducks", "ducky", "ducts", 
    "duddy", "dudes", "duels", "duets", "duffs", "duffy", "dukes", "dulls", "dully", "dulse", 
    "dumas", "dumbo", "dummy", "dumps", "dumpy", "dunce", "dunes", "dungs", "dungy", "dunks", 
    "dunno", "duomo", "duped", "duper", "dupes", "duple", "duppy", "dural", "durst", 
    "durum", "dusks", "dusky", "dusts", "dusty", "dutch", "duvet", "dwarf", "dweeb", "dwell", 
    "dwelt", "dyads", "dyers", "dying", "dykes", "dynes", "eager", "eagle", "eared", "earls", 
    "early", "earns", "earth", "eased", "easel", "eases", "easts", "eaten", "eater", "eaves", 
    "ebbed", "ebony", "ebook", "echos", "eclat", "edema", "edged", "edger", "edges", "edict", 
    "edify", "edits", "eerie", "egged", "egret", "egypt", "eider", "eight", "eject", "eking", 
    "eland", "elate", "elbow", "elder", "elect", "elegy", "elfin", "elide", "elite", "elope", 
    "elude", "elven", "elves", "embed", "ember", "emcee", "emend", "emery", "emirs", "emits", 
    "emmet", "emoji", "emory", "empty", "enact", "endow", "endue", "enema", "enemy", "enjoy", 
    "ennui", "enoki", "enrol", "ensue", "enter", "entry", "envoy", "eosin", "epics", "epoch", 
    "epoxy", "equal", "equip", "erase", "erect", "ergot", "erica", "erode", "erred", "error", 
    "erupt", "esker", "essay", "esses", "ester", "estop", "ether", "ethic", "ethos", "ethyl", 
    "etude", "evade", "evens", "event", "evert", "every", "evict", "evils", "evite", "evoke", 
    "exact", "exalt", "exams", "excel", "exert", "exile", "exist", "exits", "expel", 
    "expos", "extol", "extra", "exude", "exult", "exurb", "eying", "eyrie", "fable", "faced", 
    "facer", "faces", "facet", "facia", "facie", "facto", "facts", "faddy", "faded", "fader", 
    "fades", "fados", "faery", "faffs", "faggy", "fagin", "fagot", "fails", "faint", "fairs", 
    "fairy", "faith", "faked", "faker", "fakes", "fakir", "falco", "falls", "false", "famed", 
    "fames", "fancy", "fanes", "fanga", "fango", "fangs", "fanny", "fanon", "fanos", "fanum", 
    "faqir", "farad", "farce", "fared", "farer", "fares", "farms", "faros", "farts", "fasci", 
    "fasts", "fatal", "fated", "fates", "fatly", "fatsy", "fatso", "fatwa", "fault", "fauna", 
    "fauns", "faurd", "fauts", "fauve", "favor", "favos", "fawns", "fawny", "faxed", "faxes", 
    "fayed", "fayer", "fayne", "fayre", "fazed", "fazes", "feals", "feant", "feare", "fears", 
    "feart", "fease", "feast", "feats", "feaze", "fecal", "feces", "fecks", "fedex", "feebs", 
    "feeds", "feels", "feens", "feers", "feese", "feest", "feets", "feeze", "feign", "feint", 
    "feist", "felid", "fella", "fells", "felly", "felon", "felts", "felty", "femes", "femic", 
    "femme", "femur", "fence", "fends", "fendy", "fenis", "fenks", "fenny", "fents", "feods", 
    "feoff", "feral", "ferer", "feres", "feria", "ferly", "ferme", "ferms", "ferns", "ferny", 
    "ferry", "fesse", "festa", "fests", "festy", "fetal", "fetas", "fetch", "feted", "fetes", 
    "fetor", "fetta", "fetts", "fetus", "fetwa", "feuar", "feuds", "feued", "fever", "fewer", 
    "feyed", "feyer", "feyly", "fezzy", "fiars", "fiats", "fiber", "fibro", "fibby", "fices", 
    "fiche", "fichu", "ficin", "ficos", "ficus", "fides", "fidge", "fidos", "fiefs", "field", 
    "fiend", "fiery", "fifer", "fifes", "fifis", "fifth", "fifty", "figgy", "fight", "figos", 
    "fiked", "fikes", "filar", "filch", "filed", "filer", "files", "filet", "filii", "filks", 
    "fille", "fillo", "fills", "filly", "filme", "films", "filmy", "filos", "filth", "filum", 
    "final", "finca", "finch", "finds", "fined", "finer", "fines", "finis", "finks", "finny", 
    "finos", "fiord", "fiqhs", "fique", "fired", "firer", "fires", "firme", "firms", "firns", 
    "firry", "first", "firth", "fishy", "fists", "fisty", "fitch", "fitly", "fitte", "fitts", 
    "fiver", "fives", "fixed", "fixer", "fixes", "fixit", "fizzy", "gazer", "gecko", "ghost", "giant", "gland", "glove", "grace", "grand", "graph", "grasp", 
    "grass", "grave", "great", "green", "greet", "grief", "grill", "grind", "groan", "gross", 
    "group", "habit", "hairy", "handy", "happy", "hardy", "harsh", "haste", "hasty", "hatch", 
    "haunt", "haven", "havoc", "hazel", "heads", "heard", "heart", "heath", "heavy", "hedge", 
    "hefty", "icing", "ideal", "ideas", "idiom", "idiot", "idled", "idler", "idles", "idols", 
    "idyll", "igloo", "image", "imbue", "impel", "imply", "inane", "inbox", "incur", "index", 
    "indie", "jacks", "jacob", "jaded", "jades", "jaunt", "jazzy", "jeans", "jeeps", "jelly", 
    "jerry", "jests", "jesus", "jeton", "jewel", "jewry", "jiffy", "jihad", "jilts", "jimmy", 
    "jingo", "kails", "kales", "kalif", "kalpa", "kaons", "kapas", "kapok", "kappa", "karma", 
    "kayak", "kebab", "keels", "keeps", "kelps", "kelpy", "kenaf", "kenos", "kenya", 
    "kepis", "labor", "laced", "laces", "lacey", "lacks", "laded", "laden", "lades", "ladle", 
    "lager", "laird", "lairs", "laity", "lakes", "lamas", "lambs", "lamed", "lamer", "lames", 
    "lamps", "macro", "madam", "madly", "mafia", "magic", "magma", "maids", "mails", "maims", 
    "mains", "maize", "major", "maker", "makes", "males", "malts", "malty", "mamma", "mammy", 
    "nadir", "naggy", "naiad", "naifs", "nails", "naive", "naked", "named", "namer", "names", 
    "nanas", "nancy", "nanny", "naomi", "napes", "narco", "narcs", "nardy", "nasal", "nasty", 
    "ocean", "ochre", "octal", "octet", "odder", "oddly", "odeon", "odors", "odour", "offal", 
    "offed", "offer", "often", "ogled", "ogler", "ogles", "ogres", "oiled", "oiler", "olive", 
    "pabby", "paced", "pacer", "pacha", "packs", "pacts", "paddy", "padre", "paean", 
    "pagan", "paged", "pager", "pages", "pails", "pains", "paint", "pairs", "palms", "qadis", 
    "qaids", "qanat", "quack", "quads", "quaff", "quags", "quail", "quake", "quaky", "quale", 
    "qualm", "quant", "quark", "quart", "quash", "quasi", "queen", "queer", "query", "rabbi", 
    "rabid", "raced", "racer", "races", "racks", "radar", "radix", "radon", "rafts", "ragas", 
    "raged", "rages", "raggy", "rails", "rains", "rainy", "raise", "rajah", "rally", "saber", 
    "sable", "sabot", "sabre", "sacks", "sacra", "sadly", "safes", "safer", "sagas", "sager", 
    "sages", "saggy", "sahib", "saiks", "sails", "saint", "saith", "salad", "tabby", "table", 
    "taboo", "tabor", "tacit", "tacks", "tacky", "tacos", "tacts", "taffy", "tails", "taint", 
    "taken", "taker", "takes", "tales", "talks", "talky", "tally", "udder", "udons", "ugali", 
    "uhlan", "uhuru", "uigur", "ulcer", "ulema", "ulnae", "ulnar", "ulnas", "ultra", "umami", 
    "umbel", "umber", "umbra", "umiak", "unbar", "uncle", "uncut", "vacua", "vague", "vagus", 
    "vails", "vales", "valet", "valid", "valor", "value", "valve", "vamps", "vampy", "vanda", 
    "vanes", "vaped", "vaper", "vapes", "vapid", "vapor", "vault", "wafer", "wafts", "waged", 
    "wager", "wages", "wagon", "wahoo", "waifs", "wails", "wains", "waist", "waits", "waive", 
    "waked", "waken", "waker", "wakes", "waldo", "wales", "walks", "xebec", "xenia", "xenic", 
    "xenon", "xeric", "xerox", "xiles", "xints", "xiphs", "xylem", "yacht", "yager", "yages", 
    "yahoo", "yaird", "yakin", "yakka", "yales", "yalta", "yamen", "yamms", "yangs", "yanks", 
    "yapok", "yapon", "yappy", "yards", "yarns", "yawls", "zaire", "zamia", "zanje", "zante", 
    "zanza", "zapan", "zappy", "zarfs", "zaris", "zaxes", "zayin", "zazen", "zeals", "zebra"]
        

    def getInput(self): #gets an input of the correct size
        while True:
            print("Enter a 5 letter word: ")
            guess = input("Enter a 5 letter word: ")
            
            if len(guess) != 5:
                print('Guess must be 5 letters long')
                return 0
            else:
                return list(guess)
