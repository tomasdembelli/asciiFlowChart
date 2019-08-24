# asciiFlowChart
Draws flow charts with ascii characters.
Similar to [asciiflow](http://asciiflow.com).

#### Examples

Rectangular items can be drawn with `ItemRectangle` class:

```python
from ascii_flow_chart import ItemRectangle

start = ItemRectangle(text = 'START:\n1)This is the first item.\n2)This is the second item.')

print(start.draw())

```

```
+--------------------------------+
|                                |
|                                |
|   START:                       |
|   1)This is the first item.    |
|   2)This is the second item.   |
|                                |
|                                |
+--------------------------------+
```

Arguments can be passed to change the look of the item.

```python
from ascii_flow_chart import ItemRectangle

text="""Keyword arquments:
x -- the length (default 10)
y -- the height (default 5)
padding_X -- default 3
padding -- default 1
character_X -- the character constructing the horizantal sides (default -)
character_Y -- the character constructing the vertical sides (default |)
character_Fill -- the character filling inside the item (default space)
character_Joint -- the character used at corners (default +)
text -- the text presented in the item"""

showArguments = ItemRectangle(text=text, character_Joint='.', character_Fill='.', character_X=' ', character_Y=' ')

print(showArguments.draw())
```

```
.                                                                                .
 ................................................................................ 
 ...Keyword arquments:........................................................... 
 ...x -- the length (default 10 or wrap the text)................................ 
 ...y -- the height (default 5 or wrap the text)................................. 
 ...padding_X -- default 3....................................................... 
 ...padding_Y -- default 1....................................................... 
 ...character_X -- the character constructing the horizantal sides (default -)... 
 ...character_Y -- the character constructing the vertical sides (default |)..... 
 ...character_Fill -- the character filling inside the item (default space)...... 
 ...character_Joint -- the character used at corners (default +)................. 
 ...text -- the text presented in the item....................................... 
 ................................................................................ 
.                                                                                .
```
