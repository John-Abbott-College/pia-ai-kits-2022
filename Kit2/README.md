# Step 1: Loading Data

## Loading product data

**Importing necessary libraries**

This code is in Python and below we are importing two libraries to provide us with extra functionality beyond what is available in the core programming language.

{% code overflow="wrap" fullWidth="true" %}
```python
# Importing necessary libraries
import pandas as pd
import numpy as np
# Loading in products data
product\_info = pd.read\_csv("/kaggle/input/sephora-products-and-skincare-reviews/product\_info.csv")product\_info.info(verbose=True)
```
{% endcode %}

```python
import pandas as pd
```

[**pandas**](https://pandas.pydata.org/docs/index.html) is a data manipulation and analysis library. It is particularly used for data structures and numerical manipulation. We are specifying that from now on, we will be typing a shorthand `pd` anytime we use `pandas`.

```python
import numpy as np
```

[**numpy**](https://numpy.org/) is a popular library that has extra functionality to work with arrays and matrices. We are also specifying that we will be using the shorthand `np` anytime we use `numpy`.

{% code overflow="wrap" %}
```python
product_info = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/product_info.csv")
```
{% endcode %}

This line uses `read_csv` from the pandas library to read a specified CSV file. The location of the file is specified in quotes. The file is then loaded into the variable `product_info` of type [**DataFrame**](https://www.w3schools.com/python/pandas/pandas_dataframes.asp)**.**

{% hint style="info" %}
**What’s a DataFrame?**

&#x20;

A DataFrame is a _data structure_ that organizes data into a 2-dimensional table of rows and columns, much like a spreadsheet \[1].


{% endhint %}

**info()** is a method that provides a concise summary of the data stored in the `product_info` variable. The `verbose` parameter is set to `True` to provide full information on all columns.

### Loading the reviews data and merging DataFrames

{% code fullWidth="true" %}
```python
# Loading in reviews data

df1 = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/reviews_0_250.csv", low_memory=False)
df2 = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/reviews_250_500.csv", low_memory=False)
df3 = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/reviews_500_750.csv", low_memory=False)
df4 = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/reviews_750_1000.csv", low_memory=False)
df5 = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/reviews_1000_1500.csv", low_memory=False)
df6 = pd.read_csv("/kaggle/input/sephora-products-and-skincare-reviews/reviews_1500_end.csv", low_memory=False)

# Combining the dfs
reviews = pd.concat([df1,df2,df3,df4,df5,df6])
reviews.info()

```
{% endcode %}

```python
dfX = pd.read_csv("path", low_memory=False)
```

The `df1` to `df6`  variables contain chunks of one big product-information data set. The files are loaded with the argument `low_memory=False` to prevent pandas from saving memory by guessing `product_info` types which can lead to errors such as:

* **Data Loss** : Some data might be lost if pandas misinterprets the data type. For example, if a column contains both numbers and strings, pandas might interpret this column as numeric and replace string values with NaN.
* **Incorrect Data Types** : Pandas might interpret a column of strings as floating point numbers, or vice versa. This can lead to unexpected behavior when you attempt to manipulate the data later.
* **Performance issues** : If pandas guesses a less memory-intensive data type than the actual one, it may need to upcast that data type later when it encounters a value that doesn't fit. This can slow down the data loading process significantly.
* **Misleading Statistics:** If numeric data is interpreted as strings, methods like mean, min, max, etc., will produce incorrect results or may not work at all.

```python
reviews = pd.concat([df1,df2,df3,df4,df5,df6])
reviews.info()
```

The `reviews` DataFrame will store all the loaded data chunks that are merged using `concat()`**.**

`.info()` is a method to print the summary of the `reviews` DataFrame.

#### Detect missing values.

{% code fullWidth="true" %}
```python
num_missing = product_info.isna().sum()
num_missing
```
{% endcode %}

We are looking for any missing or unavailable (NaN) values in the `product_info` DataFrame.

`product_info.isna()` returns a boolean value (True or False) after looping over all the rows in the DataFrame. If any missing or unavailable values are detected it returns `True` , otherwise it returns `False`.

`.sum()` function adds True as 1 and False as 0 for each column and gives us the total.

`num_missing` variable is an array (pandas Series) where the index represents the column of the `product_info` DataFrame and the value in each index is the number of missing values in that column.

