import random

class GuessNumber:
  def __init__(self, infinite):
    self.infinite = infinite

  def guess(self):
    randomNumber = random.randint(0, 100)
    
    while self.infinite == 1:
      number = int(input("Type a number: "))

      if randomNumber < number:
        print("Lower")
      elif randomNumber > number:
        print("Higher")       
      else:
        print("You won")
        break

def main():
  guessGame = GuessNumber(1)
  guessGame.guess()

if __name__ == "__main__":
  main()
