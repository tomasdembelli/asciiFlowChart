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
