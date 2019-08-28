"""This module draws flowcharts with ASCII characters."""


class Item():
    """Provide shared methods and attributes for creating a flowchart 
    items.
    
    Define boundaries which will override user input:
    max_X -- the maximum width of an item (default 150 chars)
    max_Y -- the maximum height of an item (default 20 chars)
    max_padding_x -- the maximum padding on X-axis (default 20 chars)
    max_padding_y -- the maximum padding on Y-axis (default 4 chars)
    """

    max_X = 150
    max_y = 20
    max_padding_x = 20
    max_padding_y = 4
    
    def __init__(self, x=10, y=5, padding_x=0, padding_y=0, character_x=' ', 
            character_y=' ', character_fill=' ', character_joint=' ', 
            text=' '):
        """Initiate an item.
        
        Keyword arquments:
        x -- the length (default 10 or long enough to wrap wrap the text)
        y -- the height (default 5 or long enough to wrap the text)
        padding_x -- default 0
        padding_y -- default 0
        character_x -- character for the horizantal sides (default space)
        character_y -- character for the vertical sides (default space)
        character_fill -- character filling the item (default space)
        character_joint -- character used at corners (default space)
        text -- the text presented in the item
        """

        # Remove tabs from the text and split it into multiple lines.
        self.text = text.replace('\t', '').split('\n')    

        # Enforce the maximum boundaries for padding.
        self.padding_x = min(abs(int(padding_x)), Item.max_padding_x)
        self.padding_y = min(abs(int(padding_y)), Item.max_padding_y)

        # Define the minimum boundaries to ensure that
        # the size is big enough to wrap the text.
        self.borders = 2    # The number of berders on each axises.
        self.longest_text = max(list(map(len, self.text)))
        self.min_x = self.longest_text + self.borders + 2*self.padding_x  
        self.min_y = len(self.text) + self.borders + 2*self.padding_y

        # Enforce the maximum and minimum boundaries.
        self.x = min(max(abs(int(x)), self.min_x), Item.max_X)
        self.y = min(max(abs(int(y)), self.min_y), Item.max_y)  

        # Ensure that only one string character is accepted.
        self.character_x = str(character_x)[0]
        self.character_y = str(character_y)[0]
        self.character_fill = str(character_fill)[0]
        self.character_joint = str(character_joint)[0]
        
        # The matrix will be created at specific object initiation.
        self.item_matrix = []    
    
    def draw(self):
        """Join the elements of matrix and return a single string."""
        return '\n'.join(map(''.join, self.item_matrix))


class ItemRectangle(Item):
    """Create a rectangle object with optional text in it."""
    
    def __init__(self, x=10, y=5, padding_x=3, padding_y=1, character_x='-', 
            character_y='|', character_fill=' ', character_joint='+', 
            text=' '):
        """Initiate a rectangular item.
        
        Keyword arquments:
        x -- the length (default 10 or long enough to wrap the text)
        y -- the height (default 5 or long enough to wrap the text)
        padding_x -- default 3
        padding_y -- default 1
        character_x -- character for the horizantal sides (default -)
        character_y -- character for the vertical sides (default |)
        character_fill -- character filling inside item (default space)
        character_joint -- character used at corners (default +)
        text -- the text presented in the item
        """

        super().__init__(x, y, padding_x, padding_y, character_x, 
            character_y, character_fill, character_joint, text)

        # Create the matrix with X, Y and filling characters.
        self.item_matrix = [[self.character_y if i in [0, self.x-1] else 
            self.character_fill if j not in [0, self.y-1] else 
            self.character_x for i in range(self.x)] for j in range(self.y)]

        # Insert the joint characters to the corners.
        for (q, w) in [(0, 0), (0, -1), (-1, 0), (-1, -1)]: 
            self.item_matrix[q][w] = self.character_joint

        # Ad text into the matrix.
        for idx, txt in enumerate(self.text):

            # Ensure the text is not longer than the item can hold.
            txt = txt[: self.x - self.borders - 2*self.padding_x]   

            # Calculate the gab between the end of text and the border.
            gap_Fill = self.x - self.padding_x - self.borders - len(txt)

            # Insert one line of text each time.
            self.item_matrix[self.padding_y + 1 + idx] = (    
                [self.character_y] + self.padding_x*[character_fill] 
                + list(txt) + gap_Fill*[character_fill] 
                + [self.character_y])