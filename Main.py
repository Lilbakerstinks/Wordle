import turtle
from time import sleep
from random import choice

WIDTH, HEIGHT = 512, 512
screen = turtle.Screen()
screen.screensize(WIDTH, HEIGHT)

playing = True
def Play():
    
  global playing
  while playing == True:

    turtle.colormode(255)
    screen.bgcolor(150, 150, 150)

    t = turtle.Turtle()
    t.speed(0)
    t.width(5)
    t.hideturtle()

    t2 = turtle.Turtle()
    t2.speed(0)
    t2.width(5)
    t2.hideturtle()

    titleX = -85
    for i in "WORDLE":
      t.pu()
      t.goto(titleX, 200)
      t.pd()
      t.color(255, 255, 255)
      t.write(i, font=("Adobe Garamond Pro Bold", 25, "bold"), move=True)
      if i == "W":
        titleX += 38
      elif i == "O":
        titleX += 30
      elif i == "R":
        titleX += 28
      elif i == "D":
        titleX += 30
      else:
        titleX += 25

    layout = [
      "1", "2", "3", "4", "5",
      "6", "7", "8", "9", "10",
      "11", "12", "13", "14", "15",
      "16", "17", "18", "19", "20",
      "21", "22", "23", "24", "25"
    ]

    locations = [
      [-100, 100],
      [-50, 100],
      [0, 100],
      [50, 100],
      [100, 100],

      [-100, 50],
      [-50, 50],
      [0, 50],
      [50, 50],
      [100, 50],

      [-100, 0],
      [-50, 0],
      [0, 0],
      [50, 0],
      [100, 0],

      [-100, -50],
      [-50, -50],
      [0, -50],
      [50, -50],
      [100, -50],

      [-100, -100],
      [-50, -100],
      [0, -100],
      [50, -100],
      [100, -100]
    ]

    options = ["apple", "about", "pizza", "plane", "guess", "windy", "level", "crane", 'slate', "adieu", "moldy", "coded", "speed", "hello", "media", "token", "other", "which", "their", "there", "first", "would", "these", 
               "click", "price", "state", "email", "world", "music", "after", "video", "where", "books", "links", "years", "order", "items", "group", "under", "games", "could", "great", "hotel", "store", "terms", "right",
               "local", "those", "using", "phone", "forum", "based", "black", "check", "index", "being", "women", "today", "south", "pages", "found", "house", "photo", "power", "while", "three", "total", "place", "think", 
               "north", "posts", "media", "since", "guide", "board", "white", "small", "times", "sites", "hours", "image", "title", "shall", "class", "still", "money", "visit", "tools", "reply", "value", "press", "learn",
               "print", "stock", "point", "sales", "large", "table", "start", "model", "human", "movie", "march", "yahoo", "going", "study", "staff", "again", "april", "never", "users", "topic", "below"
              ]
    ANS = choice(options)
    checker = []
    for i in ANS.upper():
      checker.append(i)

    #print(checker) # <-- Untag if you want to see the chosen answer

    x = -125
    y = 150

    t.speed(0)
    for tag in layout:
      t.color(0, 0, 0)
      t.pu()
      t.goto(x, y)
      t.pd()
      for i in range(4):
        t.fd(50)
        t.rt(90)
      if x < 75:
        x += 50
        y -= 0
      else:
        x = -125
        y -= 50

    global word
    word = ""

    def HasNumber(inputString):
        return any(char.isdigit() for char in inputString)

    def Question():
      global word
      word = str(turtle.textinput("Word", "Enter A 5 Letter Word: "))
      while True:
        if HasNumber(word) == True:
          t2.pu()
          t2.goto(-230, -120)
          t2.pd()
          t2.color(255, 255, 255)
          t2.begin_fill()
          for i in range(2):
            t2.fd(450)
            t2.rt(90)
            t2.fd(80)
            t2.rt(90)
          t2.end_fill()
          t2.pu()
          t2.goto(0, -180)
          t2.pd()
          t2.color(127, 0, 255)
          t2.write("No Numbers Allowed!", font=("Adobe Garamond Pro Bold", 30, "bold"), move=False, align="center")
          sleep(1)
          t2.clear()
          word = str(turtle.textinput("Word", "Enter A 5 Letter Word: "))
        else:
          break

    def addWord(row, pos):
      global word
      
      Question()
      while len(word) != 5:
        if len(word) == 5:
          break
        elif len(word) > 5:
          t2.pu()
          t2.goto(-330, -120)
          t2.pd()
          t2.color(255, 255, 255)
          t2.begin_fill()
          for i in range(2):
            t2.fd(660)
            t2.rt(90)
            t2.fd(80)
            t2.rt(90)
          t2.end_fill()
          t2.pu()
          t2.goto(-325, -180)
          t2.pd()
          t2.color(0, 255, 255)
          t2.write("Your Word Is Too Long! Try Again!", font=("Adobe Garamond Pro Bold", 30, "bold"), move=False)
          sleep(1)
          t2.clear()
          Question()
        elif len(word) < 5:
          t2.pu()
          t2.goto(-330, -120)
          t2.pd()
          t2.color(255, 255, 255)
          t2.begin_fill()
          for i in range(2):
            t2.fd(665)
            t2.rt(90)
            t2.fd(80)
            t2.rt(90)
          t2.end_fill()
          t2.pu()
          t2.goto(-325, -180)
          t2.pd()
          t2.color(255, 0, 255)
          t2.write("Your Word Is Too Short! Try Again!", font=("Adobe Garamond Pro Bold", 30, "bold"), move=False)
          sleep(1)
          t2.clear()
          Question()
        else:
          t2.pu()
          t2.goto(-260, 80)
          t2.pd()
          t2.color(255, 255, 255)
          t2.begin_fill()
          for i in range(2):
            t2.fd(550)
            t2.rt(90)
            t2.fd(80)
            t2.rt(90)
          t2.end_fill()
          t2.pu()
          t2.goto(-245, 0)
          t2.pd()
          t2.color(127, 0, 255)
          t2.write("Error! Try Again!", font=("Adobe Garamond Pro Bold", 50, "bold"), move=False)
          sleep(1)
          t2.clear()
          Question()
      if len(word) == 5:
        loc = row
        pos = pos
        valX = 0
        valY = 1
        for letter in word.upper():
          t.pu()
          t.goto(locations[loc][valX], locations[loc][valY])
          t.pd()
          if letter.upper() in ANS.upper():
            if letter.upper() == checker[pos]:
              t.color(0, 255, 0)
              t.write(letter.upper(), align="center", font=("Adobe Garamond Pro Bold", 30, "bold"))
              loc += 1
              pos += 1
            elif letter.upper() != checker[pos]:
              t.color(255, 255, 0)
              t.write(letter.upper(), align="center", font=("Adobe Garamond Pro Bold", 30, "bold"))
              loc += 1
              pos += 1
            else:
              t.color(0, 0, 0)
              t.write(letter.upper(), align="center", font=("Adobe Garamond Pro Bold", 30, "bold"))
              loc += 1
              pos += 1
          else:
              t.color(0, 0, 0)
              t.write(letter.upper(), align="center", font=("Adobe Garamond Pro Bold", 30, "bold"))
              loc += 1
              pos += 1

    words = 0
    num = 0
    while word.upper() != ANS or words != 5:
      addWord(num, 0)
      num += 5
      words += 1
      if word.upper() == ANS.upper():
        break
      elif words == 5:
        words += 1
        break

    if word.upper() == ANS.upper():
      print("CORRECT!")
      t2.pu()
      t2.goto(-105, -180)
      t2.pd()
      t2.color(0, 255, 0)
      t2.write("CORRECT!", font=("Adobe Garamond Pro Bold", 30, "bold"), move=True)
      t2.hideturtle()
      play = str(turtle.textinput("Another Round", "Play Again? (y / n) "))
      while play != "y" or play != "n":
        if play == "y":
          break
        elif play == "n":
          break
        else:
          t2.pu()
          t2.goto(-265, 80)
          t2.pd()
          t2.color(255, 255, 255)
          t2.begin_fill()
          for i in range(2):
            t2.fd(550)
            t2.rt(90)
            t2.fd(80)
            t2.rt(90)
          t2.end_fill()
          t2.pu()
          t2.goto(-255, 0)
          t2.pd()
          t2.color(127, 0, 255)
          t2.write("Error! Try Again!", font=("Adobe Garamond Pro Bold", 50, "bold"), move=False)
          sleep(1)
          t2.clear()
          play = str(turtle.textinput("Another Round", "Play Again? (y / n) "))
      if play == "y":
        turtle.clearscreen()
        playing = True
      elif play == "n":
        playing = False
        t2.pu()
        t2.goto(-360, 80)
        t2.pd()
        t2.color(0, 0, 0)
        t2.begin_fill()
        for i in range(2):
          t2.fd(780)
          t2.rt(90)
          t2.fd(80)
          t2.rt(90)
        t2.end_fill()
        t2.pu()
        t2.goto(-355, 0)
        t2.pd()
        t2.color(255, 255, 255)
        t2.write("THANKS FOR PLAYING!", font=("Adobe Garamond Pro Bold", 50, "bold"), move=False)
        sleep(2)
        turtle.bye()

    if words == 6:
      t2.pu()
      t2.goto(-220, -180)
      t2.pd()
      t2.color(255, 0, 0)
      t2.write("The Word Was " + ANS.upper() + "!", font=("Adobe Garamond Pro Bold", 30, "bold"), move=True)
      t2.hideturtle()
      play = str(turtle.textinput("Another Round", "Play Again? (y / n) "))
      while play != "y" or play != "n":
        if play == "y":
          break
        elif play == "n":
          break
        else:
          t2.pu()
          t2.goto(-265, 80)
          t2.pd()
          t2.color(255, 255, 255)
          t2.begin_fill()
          for i in range(2):
            t2.fd(550)
            t2.rt(90)
            t2.fd(80)
            t2.rt(90)
          t2.end_fill()
          t2.pu()
          t2.goto(-255, 0)
          t2.pd()
          t2.color(127, 0, 255)
          t2.write("Error! Try Again!", font=("Adobe Garamond Pro Bold", 50, "bold"), move=False)
          sleep(1)
          t2.clear()
          play = str(turtle.textinput("Another Round", "Play Again? (y / n) "))
      if play == "y":
        turtle.clearscreen()
        playing = True
      elif play == "n":
        playing = False
        t2.pu()
        t2.goto(-360, 80)
        t2.pd()
        t2.color(0, 0, 0)
        t2.begin_fill()
        for i in range(2):
          t2.fd(780)
          t2.rt(90)
          t2.fd(80)
          t2.rt(90)
        t2.end_fill()
        t2.pu()
        t2.goto(-355, 0)
        t2.pd()
        t2.color(255, 255, 255)
        t2.write("THANKS FOR PLAYING!", font=("Adobe Garamond Pro Bold", 50, "bold"), move=False)
        sleep(2)
        turtle.bye()

Play()
turtle.mainloop()
