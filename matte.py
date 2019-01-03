import datetime
import random

TOTAL_TIME = 5 * 60

class Level:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __repr__(self):
        return "{} - {}".format(self.min, self.max)

LEVELS = {
    "1": Level(0, 5),
    "2": Level(0, 10),
    "3": Level(0, 20),
}

class Game:

    def __init__(self):
        self._right = 0
        self._wrong = 0

    def run(self):

        self._level = self.select_level()
        self._numbers = self.generate_numbers()
        print("Antal unika: ", len(self._numbers))

        try:
            self._start = datetime.datetime.now()
            while not self.time_is_up():
                self.ask_question()

            print("Slut på tid!")
        except KeyboardInterrupt as e:
            print("")
            print("Avbrutet efter ", datetime.datetime.now() - self._start)
            
        print("")
        print("Rätt:", self._right)
        print("Fel:", self._wrong)
        print("Totalt:", self._right + self._wrong)

    def time_is_up(self):
        time = datetime.datetime.now() - self._start
        return time.total_seconds() > TOTAL_TIME

    def ask_question(self):
        rand = random.randint(0, len(self._numbers) - 1)

        first = self._numbers[rand][0]
        second = self._numbers[rand][1]
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

    def select_level(self):
        print("Nivåer:")
        for name, level in LEVELS.items(): 
            print("{}: {}".format(name, level))
        print("")
        level = input("Välj nivå: ")

        while level not in LEVELS:
            print("Den nivån finns inte, välj en annan!")
            level = input("Välj nivå: ")

        return LEVELS[level]

    def generate_numbers(self):
        numbers = []
        for i in range(0, self._level.max + 1):
            for j in range(self._level.min, self._level.max - self._level.min - i + 1):
                numbers.append((i, j))
        return numbers

if __name__ == "__main__":
    game = Game()
    game.run()