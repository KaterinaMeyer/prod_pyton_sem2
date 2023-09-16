def check_rhythm(poem):
    words = poem.split()
    vowels_count = None
    for word in words:
        current_count = count_vowels(word)
        if vowels_count is None:
            vowels_count = current_count
        elif current_count != vowels_count:
            return "Пам парам"
    return "Парам пам-пам"

def count_vowels(word):
    vowels = "aеёиоуыэюя"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count
    
poem = "пара-ра-рам рам-пам-папам па-ра-пам"
print(check_rhythm(poem))