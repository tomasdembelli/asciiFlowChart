class Item():
    """Provide shared methods and attributes for creating flowchart items.
    
    Define padding and maximum allowed item size."""
    spacingX = 3
    spacingY = 2
    max_X = 150
    max_y = 20
    
    def __init__(self, x=10, y=5, character_X='-', character_Y='|', character_Fill=' ', character_Joint='+', text=''):
        """Initiate an item.
        
        Keyword arquments:
        x -- the length (default 10)
        y -- the height (default 5)
        character_X -- the character constructing the horizantal sides (default -)
        character_Y -- the character constructing the vertical sides (default |)
        character_Fill -- the character filling inside the item (default space)
        character_Joint -- the character used at corners (default +)
        text -- the text presented in the item
        """
        self.text = text.split('\n')
        self.min_X = max(list(map(len, self.text))) + 2 + 2*Item.spacingX    #2 for borders
        self.x = min(max(abs(int(x)), self.min_X), Item.max_X)
        self.min_Y = 2*Item.spacingY + 2 + len(self.text)
        self.y = min(max(abs(int(y)), self.min_Y), Item.max_y)    
        self.character_X = str(character_X)[0]
        self.character_Y = str(character_Y)[0]
        self.character_Fill = ' ' if str(character_Fill) == '' else str(character_Fill)[0]
        self.character_Joint = str(character_Joint)[0]
    
    def draw(self):
        """Join the elements of matrix and return a single string."""
        return '\n'.join(map(''.join, self.item_Matrix))


class ItemRectangle(Item):
    """Create a rectangle object with optional text in it."""
    
    def __init__(self, x=10, y=5, character_X='-', character_Y='|', character_Fill=' ', character_Joint='+', text=''):
        """Construct a matrix defining the initiated rectangular item."""
        super().__init__(x, y, character_X, character_Y, character_Fill, character_Joint, text)
        self.item_Matrix = [[self.character_Y if i in [0, self.x-1] else self.character_Fill if j not in [0, self.y-1] else self.character_X for i in range(self.x)] for j in range(self.y)]
        for (q, w) in [(0,0), (0, -1), (-1, 0), (-1, -1)]: self.item_Matrix[q][w] = self.character_Joint
        # adding text to the item
        if self.text != ['']:
            for idx, val in enumerate(self.text):
                val = val[:self.x - 2 - 2*ItemRectangle.spacingX]    #slice the text not to exceed max_X
                gap_Fill = self.x - ItemRectangle.spacingX - 2 - len(val)    #2 is for the borders
                self.item_Matrix[ItemRectangle.spacingY + 1 + idx] = [self.character_Y] + ItemRectangle.spacingX*[character_Fill] + list(val) + gap_Fill*[character_Fill] + [self.character_Y]