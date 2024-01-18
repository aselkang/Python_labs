def count_letters(text):
    letters = {
    }
    for i in text:
        if i.isalpha():
            i = i.lower()
            if i in letters.keys():
                letters[i] += 1
            else:
                letters[i] = 1
    return letters

def calculate_frequency(letters):
    k = 0
    for i in letters.values():
        k += i
    for i in letters.keys():
        letters[i] = round(letters[i]/k, 2)
    return letters

letters = count_letters('АБабВввАежз')
print(letters)
print(calculate_frequency(letters))