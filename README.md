# randomstring

Create psuedo random strings in python 2.7, with repeatable string sequences.

## Example

```python
from randomstring import RandString

r = RandString()
for x in range(0,5):
   print r.next()

```

## Arguments to RandString

- `Initializer` specify the seed for the random generator.  If not specified then uuid.uuid4() is used
- `NoAmbiguousCharacters` specify whether the string should be constructed from base62 (A-Z, a-z, 0-9) or base56 (removing iloILO).  Default is base56
- `Size` the size of the string to create.  Default is a 10 character string

## Random Number State Management

The `RandString` class manages state between calls to the `random` package functions.  This ensures that in the following example, `r1` and `r3` generate the same string sequence:

```python
from randomstring import RandString

r1 = RandString(Initializer="foo")
r2 = RandString(Initializer="bar")
r3 = RandString(Initializer="foo")

r1_strs = [r1.next() for x in range(0,5)]
r2_strs = [r2.next() for x in range(0,5)]
r3_strs = [r3.next() for x in range(0,5)]

print r1_strs == r3_strs

```

## Licence

This project is released under the MIT license. See [LICENSE](LICENSE) for details.
