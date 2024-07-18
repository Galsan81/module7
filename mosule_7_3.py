import io
from pprint import pprint
class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name
    def get_all_words(self):
        all_words = {}
        for i in self.file_name:
            with open(i, 'r', encoding='utf-8') as file:
                line = file.read().lower() #readline()?
                for punkt in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(punkt, '')
                slova = line.split()
                all_words[i] = slova
        return all_words
    def find(self, word):
        slovo={}
        b = 0
        slovar = self.get_all_words()
        for k, v in slovar.items():
            for w in v:
                b += 1
                if w == word.lower():
                    break
            slovo[self.file_name] = b
            return slovo
    def count(self, word):
        slovo = {}
        b = 0
        slovar = self.get_all_words()
        for k, v in slovar.items():
            for w in v:

                if w == word.lower():
                    b += 1
            slovo[self.file_name] = b
            return slovo



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего