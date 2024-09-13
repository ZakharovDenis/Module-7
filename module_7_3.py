#from pprint import pprint


class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        j = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, 'r', encoding='utf-8') as file:
            for line in self.file_names:
                punc = file.read().lower()
                for j in line:
                    if j in punc:
                        file = file.replace(j, '')
                j = j + line
            all_words.update({self.file_names: j.split()})

        return all_words

    def find(self, word):
        self.word = word
        result = {}
        n = 3
        world = self.get_all_words()[self.file_names]
        result.update({self.file_names: world.count(word.lower())})
        result.update({self.file_names: n})
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word.lower()) + 4
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
