# 945 : 기타 자료형 - 자가진단 5

animations = {
    "Pokemon": "Pikachu",
    "Digimon": "Agumon",
    "Yugioh": "Black Magician"
}

word = input()
#print(animations[word])
'''
if word in animations:
    print(animations[word])
else:
    print("I don't know")
'''
print(animations.get(word, "I don't know"))