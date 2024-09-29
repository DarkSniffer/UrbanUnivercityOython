import os
import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for char in string.punctuation:
                    text = text.replace(char, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                positions[file_name] = words.index(word) + 1
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        for file_name, words in self.get_all_words().items():
            counts[file_name] = words.count(word)
        return counts

# Create test_file.txt if it doesn't exist
if not os.path.exists('test_file.txt'):
    with open('test_file.txt', 'w') as file:
        file.write("It's a text for task. Найти везде, используйте его для самопроверки. Успехов в решении задачи! text text text")

# Testing the class
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))