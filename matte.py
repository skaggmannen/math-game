import datetime
import random

class Level:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __repr__(self):
        return "{} - {}".format(self.min, self.max)

class BaseGame:
    def __init__(self):
        self._right = 0
        self._wrong = 0
    
    def run(self, level):
        self._level = level
        self.numbers = self.generate_numbers()
        print("Antal unika: ", len(self.numbers))

        try:
            self._start = datetime.datetime.now()
            while not self.is_done():
                self.ask_question()

            print("Slut!")
        except KeyboardInterrupt as e:
            print("")
            print("Avbrutet!")
            
        print("")
        print("Tid: ", datetime.datetime.now() - self._start)
        print("Rätt:", self._right)
        print("Fel:", self._wrong)
        print("Totalt:", self._right + self._wrong)

    def ask_question(self):
        number = self.select_number()

        first = number[0]
        second = number[1]
        answer = first + second

        guess = input("{} + {} = ".format(first, second))
        try:
            if int(guess) != answer:
                print("Fel! Det ska vara", answer)
                self._wrong += 1
            else:
                print("Rätt!")
                self._right += 1
        except:
            print("Det där var inte en siffra...")
            self._wrong += 1

    def generate_numbers(self):
        numbers = []
        for i in range(0, self._level.max + 1):
            for j in range(self._level.min, self._level.max - self._level.min - i + 1):
                numbers.append((i, j))
        return numbers

    def select_number(self):
        raise NotImplementedError()

    def is_done(self):
        raise NotImplementedError()

class TimedGame(BaseGame):
    name = "På Tid"

    TOTAL_TIME = 5 * 60

    def __init__(self):
        super().__init__()

    def is_done(self):
        time = datetime.datetime.now() - self._start
        return time.total_seconds() > self.TOTAL_TIME

    def select_number(self):
        rand = random.randint(0, len(self.numbers) - 1)
        return self.numbers[rand]

class UniqueGame(BaseGame):
    name = "Alla Tal"

    def __init__(self):
        super().__init__()

    def is_done(self):
        return len(self.numbers) == 0

    def select_number(self):
        rand = random.randint(0, len(self.numbers) - 1)
        return self.numbers.pop(rand)

GAMES = {
    "1": TimedGame,
    "2": UniqueGame,
}

LEVELS = {
    "1": Level(0, 5),
    "2": Level(0, 10),
    "3": Level(0, 20),
}

def select_game():
    print("Spel:")
    for name, game in GAMES.items(): 
        print("{}: {}".format(name, game.name))
    print("")
    
    name = input("Välj spel: ")

    while name not in GAMES:
        print("Det där spelet finns inte!")
        name = input("Välj spel: ")

    return GAMES[name]()

def select_level():
    print("Nivåer:")
    for name, level in LEVELS.items(): 
        print("{}: {}".format(name, level))
    print("")
    name = input("Välj nivå: ")

    while name not in LEVELS:
        print("Den nivån finns inte, välj en annan!")
        name = input("Välj nivå: ")

    return LEVELS[name]

if __name__ == "__main__":
    game = select_game()
    level = select_level()
    game.run(level)