letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


letters_to_point = dict(zip(letters, points))



letters_to_point[" "] = 0 

# print(letters_to_point)


# score a word

def score_word(word):
  point_total = 0
  for elt in word.upper():
    point_total += letters_to_point[elt]
  return point_total


# print(score_word("BROWNIE"))


# score a game

player_to_words = {"player1":["BLUE","TENNIS","EXIT"],
                   "wordNerd" :["EARTH","EYES","MACHINE"],
                   "Lexi Con" : ["ERASER","BELLY","HUSKY"],
                   "Prof Reader" : ["ZAP","COMA","PERIOD"]}
  


player_to_points  = { }


for item in player_to_words:
  player_points = 0
  for data in player_to_words[item]:
    player_points += score_word(data)
  player_to_points[item] = player_points

print(player_to_points)
  














