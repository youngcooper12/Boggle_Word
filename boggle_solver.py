class tree():
    def_init_(self, letter = None):
    self.letter = letter
    self.children = {}
    self.leaf = false

   #adding a word, letter by letter
   def add(self, word):
       if len(word):
           letter = word[0]
           word = word[1:]
        else:
            self.leaf = True
            return self
    #add word lettter by letter
    def search(self,letter):
        if letter not in self.children:
            return None
        return self.children[letter]             

#need to complete
