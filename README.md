# taxcalc

A tax calculator script that I use for estimating federal withholding
throughout the year.

I have verified that it returns accurate results on MY past year returns,
however, do not expect it to be accurate on your own return. There is
absolutely zero warranty provided. Use with caution.

## Notice

## Usage

Copy `data_example.py` to a new file, e.g. `data_2022.py`. Replace the
numbers with your own, then change the imports in `tax.py` to:

```
from laws_<year> import *
from data_<year> import *
```

Then just run `tax.py`.

WARNING: `tax.py` is only compatible with the format of `data_example.py`
from the same revision. If the format of `data_example.py` changes (e.g.
by adding or removing variables), you must repeat these steps using the
new format. Failure to do so may result in undefined variable errors or
incorrect results.

## License

AGPLv3
