# dragon_fractal

Toy implementation of the popular Dragon Fractal, as seen in paperback editions of Michael Crichton's Jurassic Park.

To use:

```python
from dragon_fractal.DragonFractal import DragonFractal
f = DragonFractal()

f.step() # one iteration forward
f.plot() # see current state in popup matplotlib.pyplot window
```

## Requirements

- numpy
- matplotlib