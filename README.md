
![](etc/img/apple-touch-icon.png)

## [**Data** **S**cience **S**hortcuts - DataSS](https://htbrandao.github.io/datass/)


# About:

This time I *really* got tired of rewriting the same old data analysis functions again.

For now on I'll write them in this package.

MIT License.

# Installation ([PyPI](https://pypi.org/project/datass/)):

Download and install:

```bash
git clone https://gitlab.com/htbrandao/datass.git

cd datass/

pip3 install -e .
```

or, install from PyPI:

```bash
pip3 install datass
```

or, install a specific version:

```bash
pip3 install datass==0.0.1
```

# Usage:

Example:

```python
import datass

import pandas as pd

df = pd.read_csv('some-file.csv')

# find null values
datass.dataframe.inspection._isnull(df)

# run value counts
datass.dataframe.inspection._value_counts()(df)

# run describe
datass.dataframe.inspection._describe(df)
```

# Other:

- Documentation created using [Sphinx](https://www.sphinx-doc.org/en/master/)
- Packaged using this [guide](https://packaging.python.org/tutorials/packaging-projects/)
- Bootstrap [theme](https://startbootstrap.com/theme/freelancer)

# TODO & FIXME:

    1 - keep on coding the actual module
    1.1 - update docs
    1.2 - fix proj page not fowarding to docs
    1.3 - improve 404.md
    2 - YOLO
