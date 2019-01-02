import datetime
import random

TOTAL_TIME = 5 * 60

class Game:
    def __init__(self):
        self._right = 0
        self._wrong = 0

    def run(self):
        self._start = datetime.datetime.now()
        try:
            while not self.time_up():
                self.ask_question()

            print("Slut på tid!")
        except KeyboardInterrupt as e:
            print("")
            print("Avbrutet efter ", datetime.datetime.now() - self._start)
            
        print("")
        self.print_stats()

    def time_up(self):
        time = datetime.datetime.now() - self._start
        return time.total_seconds() > TOTAL_TIME

    def ask_question(self):
        first = random.randint(0, 9)
        second = random.randint(0, 9) % (10 - first)
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

    def print_stats(self):
        print("Rätt:", self._right)
        print("Fel:", self._wrong)
        print("Totalt:", self._right + self._wrong)

if __name__ == "__main__":
    game = Game()
    game.run()