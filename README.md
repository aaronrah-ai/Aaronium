# Aaronium

Aaronium is a Python mathematics engine based on Aaron Craig Sinanan's book.

It encodes:
- arithmetic as repeated addition
- custom number systems (binary / ternary / quaternary / quinary)
- roots and the special 9th-root-of-10 style thinking
- logarithms and the phi / ln(5) / log10(41.5) golden region
- Taylor & Maclaurin series
- differentiation and partial differentiation
- geometric series like 1.111...
- golden sample and golden mistake expressions
- Newton-style iterative solvers
- a basic acceleration expression model

## Example

```python
import aaronium as ar

print(ar.root_of_ten(9))
print(ar.phi_region_triplet())

print(ar.golden_sample(0))

from aaronium import series_tools
print(series_tools.infinite_geometric(1, sp.Rational(1,10)))  # 1.111...
```
