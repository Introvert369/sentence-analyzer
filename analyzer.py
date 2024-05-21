import string

class Check:
    def __init__(self, s):
        s = s.lower()
        for i in string.punctuation:
            s = s.replace(i, " ")

        self.wordlist = s.split()
        self.worddic = {}
        self.ls = []

        for i in self.wordlist:
            if i[0] not in self.ls:
                self.ls.append(i[0])

        self.ls.sort()

        for i in self.ls:
            self.worddic[i[0]] = []

    def start(self):
        for i in self.worddic:
            for j in self.wordlist:
                if j[0] == i:
                    self.worddic[i].append(j)

        for l in self.worddic:
            if len(self.worddic[l]) == 1:
                print("1 word starts with", l+".", "It is", self.worddic[l])
            else:
                print(len(self. worddic[l]), "words start with", l+".", "They are", self.worddic[l])

    def num(self):
        print("Your sentence has", len(self.wordlist), "words")

sent = input("Give a sentence.: ")
check = Check(sent)
check.start()
check.num()