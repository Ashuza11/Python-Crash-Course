"""
    M. Ashuza 
    Auguest 15 2022
    Python Crash Course Book chapter 10 Exercises 
"""
# Question 10-8. Cats and Dogs
common_word = input("Give the common word: ")

def commonWords(file_name, word):
    """Find the common word in the file"""
    try:
        with open(file_name) as file_objects:
            content = file_objects.read()
    except FileNotFoundError:
        print(f"File {file_name} does not exist.")
    else:
        common_word = content.count(word.lower())
        print(common_word)
        


file_name = 'common_words.txt'
commonWords(file_name, common_word)