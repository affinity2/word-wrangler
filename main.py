from random import randint

with open('words.txt', 'r') as file:
    content = file.read()
all_words = content.split()

def get_new_chain():
    word_chain = []
    start = all_words[randint(0, len(all_words) - 1)]
    temp = start
    possible_words = []
    for i in range(35):
        used_words.append(temp)
        word_chain.append(temp)
        possible_words = get_possible_words(temp)
        temp = possible_words[randint(0, len(possible_words) - 1)]
    return word_chain

def get_possible_words(input):
    words_list = []
    for i in range(len(all_words) - 1):
        if check_changes(all_words[i], input) and not all_words[i] in used_words and not input == all_words[i]:
            words_list.append(all_words[i])
    return words_list

def check_changes(new, original):
    changes = 0
    for j in range(4):
        if new[j] != original[j]:
            changes = changes + 1
    if changes >= 2:
        return False
    else:
        return True

def is_valid(input, current):
    try:
        float(input)
        return False
    except ValueError:
        if len(input) == 4 and check_changes(input, current) and input in all_words:
            return True
        else:
            return False

def get_input():
    while True:
        user_input = str(input()).lower()
        if is_valid(user_input, current):
            return user_input
        elif user_input == "help!":
            print(f"Here's a list with words you can use: {get_possible_words(current)}")
        else:
            print('Invalid input, please try again')
        
test1, test2, test3 = 'yell', 'rest', 'test'
min, max = 0, len(all_words)
not_valid = False
used_words = []
words_used = []

new_chain = get_new_chain()
current = new_chain[0]
used_words = []

print(f'You are starting at: "{new_chain[0]}"')
print(f'Change one letter at a time until your word becomes: "{new_chain[len(new_chain) - 1]}". Good luck!')
print(f'If you feel stuck, type "help!"')

while not current == new_chain[len(new_chain) - 1]:
    current = get_input()
    words_used.append(current)
    print(f'Your word is now "{current}"')

print(f'Congratulations! You used {len(words_used)} words! Thanks for playing!')
