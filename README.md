# **Data** **S**cience **S**hortcuts

This time I *really* got tired of rewriting the same old data analysis functions again.

For now on I'll write them in this package.

MIT License

# # Install

Choose one:

- Download and install:

    `$ git clone https://gitlab.com/hbrandao/data-science-shortcuts.git`

    `$ cd datass/`

    `$ pip3 install -e .`

- Install from Pypi:

    `pip3 install datass`

- Install a specific version:

    `pip3 install datass==0.0.1` # or another version

# # Usage

Example:

> import datass

> import pandas as pd

> df = pd.read_csv('some-file.csv')

> #### # find null values
> datass.dataframe.inspection._isnull(df)

> #### # run value counts
> datass.dataframe.inspection._value_counts()(df)

> #### # run describe
> datass.dataframe.inspection._describe(df)

# # Other

- [Packaged using this guide](https://packaging.python.org/tutorials/packaging-projects/)