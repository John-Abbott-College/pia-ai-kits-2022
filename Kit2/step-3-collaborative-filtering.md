# Step 3: Collaborative filtering

Data Cleaning and Filtering

{% code overflow="wrap" fullWidth="true" %}
```python
# Removing products with no values in ratings and reviews columns
product_info = product_info.dropna(subset=['reviews','rating'])

# Getting for every product the number of reviews 
product_stats = reviews.groupby(['product_id'])['product_id'].count().reset_index(name='counts')

# Sorting by count
product_stats.sort_values('counts', ascending=False)

# Calculating cutoff value. The count number where 20% percent of the products have number of reviews less than this number
cutoff= product_stats['counts'].quantile(0.20)

# keeping authors with review counts > cutoffvalue
filtered_products = product_stats.loc[product_stats['counts'] > cutoff]

# Converting to set the product_id column
products_set = filtered_products['product_id'].squeeze()

# Keeping products with product_ids in the above products set
products_subset = product_info.loc[product_info['product_id'].isin(products_set)]

```
{% endcode %}

This code's objective is to generate a filtered list of products, specifically, a list of those that have more reviews. Products with few reviews or missing reviews are filtered out.

```python
product_info = product_info.dropna(subset=['reviews','rating'])
```

We are removing any row in `product_info` DataFrame where `reviews` or `rating` are missing (NaN).

{% code overflow="wrap" %}
```python
product_stats = reviews.groupby(['product_id'])['product_id'].count().reset_index(name='counts')
```
{% endcode %}

We are creating a new DataFrame `product_stats` that counts the number of reviews per product.&#x20;

`groupby()` method groups reviews by their unique `product_id`.&#x20;

`count()` function then calculates the reviews for each unique `product_id.`

`reset_index()` method resets the index of the DataFrame and name the new column as `count` which will hold the count of the reviews per product.

```python
product_stats.sort_values('counts', ascending=False)
```

`product_stats` DataFrame is sorted in descending order by the review count.

```python
cutoff= product_stats['counts'].quantile(0.20)
```

We calculate the cutoff value for the `product_stats` count column which would be at the 20th percentile of the column values.  <mark style="color:yellow;">In other words, 20% of the counts will be less than this cutoff value.</mark>

[quantile()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html) is a statistical operator that would return the value at the set percentage/cutoff.

```python
filtered_products = product_stats.loc[product_stats['counts'] > cutoff]
```

**filtered\_products** will be a new DataFrame storing products from **product\_stats** that have counts above the cutoff value.

`product_stats['counts'] > cutoff` creates a **Boolean Series**. Each value will be either **true**, if the value in the counts column is greater than the value of cutoff, or **false**.

The [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) function is used to access a group of rows and columns by label(s) or  by a boolean array, which is what we use in this case, in the DataFrame. All the rows in `product_stats` where the condition in the square brackets is true will be selected.

```python
products_set = filtered_products['product_id'].squeeze()
```

We take the `product_id` column of the `filtered_products` DataFrame and use the [`squeeze()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.squeeze.html) method to create a `products_set` Series.

{% code overflow="wrap" %}
```python
products_subset = product_info.loc[product_info['product_id'].isin(products_set)]
```
{% endcode %}

We take the `product_info` DataFrame and filter it to only keep the products present in `products_set`.

The `isin` function checks whether each element in `product_id` column of the`product_info` DataFrame is present in the `products_set` Series.

The result is stored in the `products_subset` DataFrame that contains only the top 80% of the review counts (since out cut off was set at 20%).



{% code fullWidth="true" %}
```python
product_info.shape
```
{% endcode %}

This returns a tuple representing the dimensions **(rows, columns)** of the `product_info` DataFrame before filtering.

{% code fullWidth="true" %}
```python
products_subset.shape
```
{% endcode %}

This returns a tuple representing the dimensions **(rows, columns)** of the `products_subset` DataFrame after the filtering.

We can observe how many products were filtered out comparing the first value of the tuples **(rows)**.

***

<pre class="language-python" data-full-width="true"><code class="lang-python"># Getting for every author the number of reviews they made
author_stats = reviews.groupby(['author_id'])['author_id'].count().reset_index(name='counts')
<strong>
</strong><strong># Sorting by count
</strong>author_stats.sort_values('counts', ascending=False)

# Calculating cutoff value
cutoff= author_stats['counts'].quantile(0.95)
<strong>
</strong><strong># keeping authors with review counts > cutoffvalue
</strong>filtered_authors = author_stats.loc[author_stats['counts'] > cutoff]

# Converting to set only the author_id column
authors = filtered_authors['author_id'].squeeze()

# Keeping reviews from the authors in the set
reviews_subset = reviews.loc[reviews['author_id'].isin(authors)]

</code></pre>

We will filter the reviews to only get the top **5%** of the authors based on the review amount by each author.

{% code overflow="wrap" %}
```python
author_stats = reviews.groupby(['author_id'])['author_id'].count().reset_index(name='counts')
```
{% endcode %}

We generate `author_stats` DataFrame that counts the number of reviews each author has written. The `reviews` DataFrame is grouped by `author_id`, then it counts the number of times each `author_id` appears, which equals to the number of reviews made by that specific author. Finally, the indexes are reset using the name `counts` for the new column containing the number of reviews.

```python
author_stats.sort_values('counts', ascending=False)
```

We sort the **author\_stats** DataFrame in descending order based on the count of reviews.

```python
cutoff= author_stats['counts'].quantile(0.95)
```

We sort the `author_stats` DataFrame in descending order based on the count of reviews.

```python
filtered_authors = author_stats.loc[author_stats['counts'] > cutoff]
```

The new `filtered_authors` DataFrame will contain anything above the cutoff value, so the first **5%**.

```python
authors = filtered_authors['author_id'].squeeze()
```

We take the `author_id` column of the f`iltered_author`s DataFrame and turn it into **authors** Series.

```python
reviews_subset = reviews.loc[reviews['author_id'].isin(authors)]
```

`reviews_subset` is the new filtered DataFrame that only includes the reviews written by the authors in the `authors` Series.

{% code fullWidth="true" %}
```python
reviews.shape
```
{% endcode %}

`.shape` gives us a tuple of the reviews DataFrame size **(rows, columns)**.

{% code fullWidth="true" %}
```python
reviews_subset.shape
```
{% endcode %}

We get a tuple of the `reviews_subset` size **(rows, columns)**.

We can observe how many reviews **(rows)** were filtered out.

{% code overflow="wrap" fullWidth="true" %}
```python
# Inner join the 2 DataFrames and place in a results DataFrame, common column names are suffixed by x and y where x is the right DataFrame, and y is the left one
result=products_subset.merge(reviews_subset,  how='inner', on='product_id')

```
{% endcode %}

We take the `products_subset` and [`merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) it with `reviews_subset`. The resulting data is stored in the `result` DataFrame.

`on=` is a parameter to specify the common key to join the DataFrames on. In this case, it will use the column `product_id`.

`how=` is a parameter specifier of the type of merge to be performed. **Inner** means we are performing an `inner join` (only keeping the rows that have the same `product_id` present in both DataFrames).&#x20;

\* **pandas** automatically appends suffixes `_x` and `_y` to make the column names unique. `_x` is appended to the columns from the left DataFrame, and `_y` is appended to the columns from the right DataFrame (eg. rating\_x, rating\_y).

***

### Making Predictions using Surprise library

{% code overflow="wrap" fullWidth="true" %}
```python
from surprise import Reader, Dataset
reader = Reader(rating_scale=(1,5))

# Load Pandas DataFrame into a Surprise Dataset
#load_from_df() method, we will also need a Reader object, and the rating_scale parameter must be specified. The data frame must have three columns, corresponding to the user ids, the item ids, and the ratings in this order. Each row thus corresponds to a given rating.
data = Dataset.load_from_df(result[['author_id', 'product_id', 'rating_y']], reader)

```
{% endcode %}

Here, we will be using the [Surprise](https://surprise.readthedocs.io/en/stable/) library and import [Reader](https://surprise.readthedocs.io/en/stable/reader.html?highlight=reader) class and [Dataset](https://surprise.readthedocs.io/en/stable/dataset.html?highlight=Dataset%20class) module.

```python
reader = Reader(rating_scale=(1,5))
```

We’re initializing a `Reader` object and specifying we want the`rating_scale` to be between 1 and 5. This will be the rating scale used for every item.

{% code overflow="wrap" %}
```python
data = Dataset.load_from_df(result[['author_id', 'product_id', 'rating_y']], reader)
```
{% endcode %}

We load a Dataset object from `results` DataFrame using only `author_id`, `product_id`, and `rating_y` columns.

`Dataset.load_from_df()` is used to specifically upload a pandas DataFrame. It absolutely has to contain user **ids**, **item ids**, and **ratings** in this precise order.

{% code fullWidth="true" %}
```python
# Importing the SVD algorithm from surprise
from surprise import SVD 

# Building a training set
trainset = data.build_full_trainset()

# Creating an instance of SVD
algo = SVD()

# Training the model using the training set:
algo.fit(trainset)

```
{% endcode %}

Here, we will train a recommendation model using **Singular Value Decomposition** (SVD) algorithm.

```python
from surprise import SVD 
```

We import the [SVD](https://surprise.readthedocs.io/en/stable/matrix_factorization.html) class from the Surprise library.

```python
trainset = data.build_full_trainset()
```

We are using the `build_full_trainset()` method from the Dataset class to create a [Trainset](https://surprise.readthedocs.io/en/stable/trainset.html) object using all the user-item ratings in the `data` Dataset.

{% hint style="info" %}
#### <mark style="color:blue;">Example</mark>

Let's assume the `data` Dataset contains ratings for thousands of Sephora products.

<mark style="color:red;">User A</mark> has rated the _"Fenty Beauty Foundation"_ with **5** stars, <mark style="color:purple;">User B</mark> has rated _"Anastasia Beverly Hills Brow Wiz"_ with **4** stars, and so on.&#x20;

`data.build_full_trainset()` will use all the ratings for the trainset and organize the data to maximize the efficiency of the recommender algorithm to learn from.
{% endhint %}

```python
algo = SVD()
```

This creates an instance of the SVD algorithm.

```python
algo.fit(trainset)
```

This is where the model learns from the trainset!

&#x20;When `fit()` is called, the algorithm is learning the best way to map the user-item interactions from `trainset` to the user ratings. By adjusting the internal parameters, it will try to minimize the difference between the predicted and the actual ratings.

{% hint style="info" %}
#### <mark style="color:blue;">Example</mark>

Let’s say, users who rate highly  _"Fenty Beauty Foundation"_ tend to also rate highly _“Creamy Concealer”._ That’s the kind of patterns the `fit()` function is looking for. Based on these patterns, the algorithm will be able to make predictions and recommend for users who have highly rated “Beauty Foundation” the “Creamy Concealer” product.
{% endhint %}

***

{% code fullWidth="true" %}
```python
# Predicting ratings for all pairs (u, i) that are NOT in the training set.
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

```
{% endcode %}

We are using this code to generate a quick list of unknown ratings.

```python
testset = trainset.build_anti_testset()
```

To make a `testset` that contains all user-item pairs that are NOT in the training set, we use the `build_anti_testset()` function from the Trainset class. It pairs each user with products that said <mark style="color:yellow;">user has not rated yet</mark>.

This `testset` is used to create potential new recommendations.

The `testset` will be a list of tuples **(user, item, estimated rating)**.

{% hint style="info" %}
<mark style="color:blue;">**Example**</mark>

Let’s say, a user with the user\_id 12345 has not rated the _“Beauty Foundation”_ yet. Then, this user-product pair will be included in this testset.
{% endhint %}

```python
predictions = algo.test(testset)
```

`test()` method is used to predict ratings of all the pairs in the `testset.`

{% hint style="info" %}
**Example**

We are asking the model `algo`, what will be the rating of the products that each user has not rated yet?&#x20;

Based on the patters it learned during the training, it will make a prediction.&#x20;

It might predict that based on the patterns of user 12345, they would rate the _“Beauty Concealer”_ as **3.8**.
{% endhint %}

***

{% code fullWidth="true" %}
```python
from surprise import accuracy
mse = accuracy.mse(predictions)
rmse = accuracy.rmse(predictions)
```
{% endcode %}

Here, we will evaluate the accuracy of our recommender model.

```python
from surprise import accuracy
```

We import the [accuracy](https://surprise.readthedocs.io/en/stable/accuracy.html) module from Surprise library. It provides tools to compare the accuracy of a recommender system.

```python
mse = accuracy.mse(predictions)
```

**Compute MSE** (Mean Squared Error) is used to measure the accuracy. It is calculated by taking the average of the squared differences between the predicted and the existing ratings. The smaller the MSE, the closer the predictions are to the actual ratings.

```python
rmse = accuracy.rmse(predictions)
```

**Root Mean Squared Error** (RMSE) is another way to measure accuracy. It measures the standard deviation of prediction errors. RMSE is calculated by taking the square root of the RMSE formula. The smaller the MSE, the closer the predictions are to the actual ratings.

{% code fullWidth="true" %}
```python
# Converting to a DataFrame
pred = pd.DataFrame(predictions)
```
{% endcode %}

We convert the [predictions](https://surprise.readthedocs.io/en/stable/predictions_module.html) object to a pandas DataFrame.

The `pred` DataFrame will contain one row for each prediction and the columns will be **uid** (user id), **iid** (item id), **r\_ui** (true rating), **est** (estimated rating), and **details** (may contain additional  information about the prediction).

{% code fullWidth="true" %}
```python
# Function that takes in user_id input and returns most similar products
def get_recommendations_SVD(user_id, pred):
    # Keeping predictions of user user_id
    pred_subset = pred.loc[pred['uid'] == user_id]

    # Sorting based on est
    pred_subset.sort_values(by=['est'],ascending = False)
    
    # Selecting the top 10 products
    product_list = pred_subset.head(10)['iid'].to_list()
    
    # Keeping products with product_ids in the above products set
    recommendations = product_info.loc[product_info['product_id'].isin(product_list)]
    
   return recommendations['product_name']

```
{% endcode %}

```python
def get_recommendations_SVD(user_id, pred):
```

We define the function `get_recommendations_SVD` which takes `user_id` and `pred` as parameters and returns the top 10 recommended products.

```python
pred_subset = pred.loc[pred['uid'] == user_id]
```

The rows where the `user_id` is equal to the `uid` are selected and stored in `pred_subset` DataFrame.

```python
    pred_subset.sort_values(by=['est'],ascending = False)
```

`pred_subset` is sorted in descending order of the `est` (estimated rating) column.

```python
product_list = pred_subset.head(10)['iid'].to_list()
```

`head(10)` selects the first 10 rows and the `iid` ( product\_id) column of these rows is converted to a list `product_list`.

```python
 recommendations = product_info.loc[product_info['product_id'].isin(product_list)]
```

`product_info` DataFrame is compared against `product_list`. All items that are present in the `product_list` are then stored in the `recommendations` DataFrame.

```python
return recommendations['product_name']
```

The function then returns the `product_name` of the items inside the `recommendations` DataFrame.

{% hint style="info" %}
**Example**

Run the function get\_recommendations\_SVD for user with the user\_id 1117898902 and our pred DataFrame.
{% endhint %}

```python
get_recommendations_SVD('1117898902', pred)
```
