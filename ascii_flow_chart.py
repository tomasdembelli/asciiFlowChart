"""This module draws flawcharts with ASCII characters."""


class Item():
    """Provide shared methods and attributes for creating flowchart 
    items.
    
    Define boundaries which will override user input:
    max_X -- the maximum width of an item (default 150 chars)
    max_Y -- the maximum height of an item (default 20 chars)
    max_padding_X -- the maximum padding on X axis (default 20 chars)
    max_padding_Y -- the maximum padding on Y axis (default 4 chars)
    """

    max_X = 150
    max_y = 20
    max_padding_X = 20
    max_padding_Y = 4
    
    def __init__(self, x=10, y=5, padding_X=0, padding_Y=0, character_X=' ', 
            character_Y=' ', character_Fill=' ', character_Joint=' ', 
            text=' '):
        """Initiate an item.
        
        Keyword arquments:
        x -- the length (default 10 or long enough to wrap wrap the text)
        y -- the height (default 5 or long enough to wrap the text)
        padding_X -- default 0
        padding_Y -- default 0
        character_X -- character for the horizantal sides (default space)
        character_Y -- character for the vertical sides (default space)
        character_Fill -- character filling the item (default space)
        character_Joint -- character used at corners (default space)
        text -- the text presented in the item
        """

        # Remove tabs from the text and split it into multiple lines.
        self.text = text.replace('\t', '').split('\n')    

        # Enforce the maximum boundaries for padding.
        self.padding_X = min(abs(int(padding_X)), Item.max_padding_X)
        self.padding_Y = min(abs(int(padding_Y)), Item.max_padding_Y)

        # Define the minimum boundaries to ensure that
        # the size is big enough to wrap the text.
        self.borders = 2    # The number of berders on each axises.
        self.longest_text = max(list(map(len, self.text)))
        self.min_X = self.longest_text + self.borders + 2*self.padding_X  
        self.min_Y = len(self.text) + self.borders + 2*self.padding_Y

        # Enforce the maximum and minimum boundaries.
        self.x = min(max(abs(int(x)), self.min_X), Item.max_X)
        self.y = min(max(abs(int(y)), self.min_Y), Item.max_y)  

        # Ensure that only one string character is accepted.
        self.character_X = str(character_X)[0]
        self.character_Y = str(character_Y)[0]
        self.character_Fill = str(character_Fill)[0]
        self.character_Joint = str(character_Joint)[0]
        
        # The matrix will be created at specific object initiation.
        self.item_Matrix = []    
    
    def draw(self):
        """Join the elements of matrix and return a single string."""
        return '\n'.join(map(''.join, self.item_Matrix))


class ItemRectangle(Item):
    """Create a rectangle object with optional text in it."""
    
    def __init__(self, x=10, y=5, padding_X=3, padding_Y=1, character_X='-', 
            character_Y='|', character_Fill=' ', character_Joint='+', 
            text=' '):
        """Initiate a rectangular item.
        
        Keyword arquments:
        x -- the length (default 10 or long enough to wrap the text)
        y -- the height (default 5 or long enough to wrap the text)
        padding_X -- default 3
        padding_Y -- default 1
        character_X -- character for the horizantal sides (default -)
        character_Y -- character for the vertical sides (default |)
        character_Fill -- character filling inside item (default space)
        character_Joint -- character used at corners (default +)
        text -- the text presented in the item
        """

        super().__init__(x, y, padding_X, padding_Y, character_X, 
            character_Y, character_Fill, character_Joint, text)

        # Create the matrix with X, Y and filling characters.
        self.item_Matrix = [[self.character_Y if i in [0, self.x-1] else 
            self.character_Fill if j not in [0, self.y-1] else 
            self.character_X for i in range(self.x)] for j in range(self.y)]

        # Insert the joint characters to the corners.
        for (q, w) in [(0, 0), (0, -1), (-1, 0), (-1, -1)]: 
            self.item_Matrix[q][w] = self.character_Joint

        # Ad text into the matrix.
        for idx, txt in enumerate(self.text):

            # Ensure the text is not longer than the item can hold.
            txt = txt[: self.x - self.borders - 2*self.padding_X]   

            # Calculate the gab between the end of text and the border.
            gap_Fill = self.x - self.padding_X - self.borders - len(txt)

            # Insert one line of text each time.
            self.item_Matrix[self.padding_Y + 1 + idx] = (    
                [self.character_Y] + self.padding_X*[character_Fill] 
                + list(txt) + gap_Fill*[character_Fill] 
                + [self.character_Y])