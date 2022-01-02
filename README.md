# Auto Art Gen with <a href="https://github.com/sepandhaghighi/samila">Samila</a>

Generates random art based on random points on Cartesian coordinate system calculated from random set of mathemtical formulas with random parameter.

## Requirements

```pip install -r requirements.txt```
```python>=3```
```samila>=0.3```

If requirements.txt won't install check <a href="https://github.com/sepandhaghighi/samila#installation">Samila installation</a>

## Usage

Every color, projection and point is randomly selected.

```python3 main.py```

```main.py```
```
if __name__ == '__main__':
    Generate(num_pieces=300)
```

![example-1](examples/218.png?raw=true)
![example-2](examples/271.png?raw=true)
![example-3](examples/300.png?raw=true)

## References
https://github.com/sepandhaghighi/samila <br />
https://github.com/cutterkom/generativeart <br />
