
# yspacepy

## Synopsis

```python
>>> from yspacepy.objects import sun, earth
>>> sun.radius.value
695508.0
>>> sun.radius.unit
Unit("km")
>>> sun.radius.to('au').value
0.004649183820234682
>>> sun.radius.to('au').unit
Unit("AU")
>>> sun.radius
<Quantity 695508. km>
>>> sun.dist('earth')
<Quantity 1.496e+08 km>
```

## Installation

    $ pip install yspacepy

