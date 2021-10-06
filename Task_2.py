class ReadFile:
    def __init__(self, file_name):
        file = open(file_name)
        self.readfile = file.read()
    def characters(self):
        return len(self.readfile)
    def words(self):
        return len(self.readfile.split())
    def sentences(self):
        count = 1
        for i in ['!', '?', '...', '. ']:
            count += self.readfile.count(i)
        return count
test = ReadFile('aboba.txt')
print(test.characters())
print(test.words())
print(test.sentences())