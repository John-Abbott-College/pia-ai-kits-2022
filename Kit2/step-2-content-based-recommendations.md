# Step 2 : Content Based Recommendations

{% code overflow="wrap" fullWidth="true" %}
```python
products= pd.DataFrame(product_info, columns=['product_id','product_name','ingredients','highlights'])
products.head(5)
products.shape
```
{% endcode %}

`products` is a new DataFrame. Using `pd.DataFrame` constructor, it contains only the specified `'product_id',` `'product_name'`, `'ingredients'`, and `'highlights'` columns of the original `product_info` DataFrame.

<figure><img src=".gitbook/assets/Screenshot 2023-11-04 124818.png" alt=""><figcaption></figcaption></figure>

{% code fullWidth="true" %}
```python
# Removing products with missing highlights values
products = products.dropna(subset=['highlights']) 
products.shape
```
{% endcode %}

`.dropna()` is a function to remove any missing values (NaN) from the DataFrame. In this case, the parameter `subset=['highlights']` is used to specify to look only at the ‘highlights’ column.

The `.shape()` method prints a [tuple](https://www.w3schools.com/python/python_tuples.asp) representing the row and column count of the DataFrame.

{% code overflow="wrap" fullWidth="true" %}
```python
# Resetting the index of the DataFrame. The drop parameter is used to avoid the old index being added as a column when the index is reset.
products = products.reset_index(drop=True)

# Constructing a series from a dictionary with data indices and index product_name
indices = pd.Series(products.index, index=products['product_name'])

```
{% endcode %}

`.reset_index()` function resets the indices in the products DataFrame. The `drop=True` parameter is used to avoid adding the old index as a new column in the DataFrame.



{% hint style="info" %}
#### <mark style="color:blue;">Example</mark>

If this is the data we have in the products DataFrame:
{% endhint %}

<div align="left" data-full-width="false"><figure><img src=".gitbook/assets/Screenshot 2023-11-04 125449.png" alt="" width="302"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The DataFrame products would appear as follows after the execution of `products = products.reset_index(drop=True)`:
{% endhint %}

<div align="left"><figure><img src=".gitbook/assets/Screenshot 2023-11-04 125541.png" alt="" width="301"><figcaption></figcaption></figure></div>

{% hint style="info" %}
`pd.Series()` creates a one-dimensional array object called a **Series** in pandas. In other words, <mark style="color:yellow;">Series is basically a single column</mark> of a DataFrame.

`products.index` is the data that is input into the Series. `indices=products['product_name']` specifies that the `product_name` values will be used as indexes in the Series.

The output of the indices Series created with `indices = pd.Series(products.index, index=products['product_name'])` would be as follows:
{% endhint %}

<div align="left"><figure><img src=".gitbook/assets/Screenshot 2023-11-04 135144.png" alt="" width="156"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Note how indices and product names swapped columns. As such, the code i`ndices['Face Serum']` will returns <mark style="color:yellow;">1</mark>.
{% endhint %}

***

### Feature extraction from product highlights

We will use the built-in `TfidfVectorizer` class in `scikit-learn` library, used for machine learning, that produces the [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) matrix.

This code transforms text input into a numerical format using a technique known as **TF-IDF** (Term Frequency-Inverse Document Frequency). In **NLP** (Natural Language Processing) , this approach is used to prepare data for machine learning algorithms.

{% code fullWidth="true" %}
```python
# Importing the necessary classes
from sklearn.feature_extraction.text import TfidfVectorizer

# Creating an instance of TF-IDF vectorizer Object.
vectorizer = TfidfVectorizer()

# Extracting the values from the highlights column as our corpus
texts = products.highlights.values

# Creating the matrix
tfidf_matrix = vectorizer.fit_transform(texts)

# Displaying the shape of tfidf_matrix
tfidf_matrix.shape

```
{% endcode %}

Import the `TfidfVectorizer` class from `sklearn.feature_extraction.text`.&#x20;

{% hint style="info" %}
You can learn more about sklearn.feature\_extraction.text.TfidfVectorizer and other APIs [here](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
{% endhint %}

Create an instance of `TfidfVectorizer()` class in the vectorizer object.

Then, `products.highlights.values` extracts the text from the highlights column and stores it in the variabletexts.

`fit_transform()` method returns a matrix with the columns corresponding to the words in the texts and the rows the number of products. Each cell in the TF-IDF matrix is the weight of that word in that document. It reflects how significant a certain word is to highlights among other words.

{% hint style="info" %}
#### <mark style="color:blue;">Example</mark>&#x20;

Let’s imagine our products DataFrame looks as follows:
{% endhint %}

```python
products = pd.DataFrame({
    'product_name': ['Perfume A', 'Perfume B', 'Perfume C'],
    'highlights': [
        'Unisex/ Genderless Scent',
        'Layerable Scent',
        'Warm &Spicy Scent'
    ]
})
```

{% hint style="info" %}
Shape of TF-IDF matrix will be $$(3, 6)$$, as the products DataFrame has 3 products and 6 unique words in the highlights. Thus, the matrix will have 3 rows and 6 columns.

The data with its weight will look like this:
{% endhint %}

<figure><img src=".gitbook/assets/Screenshot 2023-11-04 142049.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
For more information on TF-IDF check [here](https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/).

Here is another way of simplifying the visualisation of the flow of this code block:
{% endhint %}

<figure><img src=".gitbook/assets/Screenshot 2023-11-04 142458.png" alt=""><figcaption></figcaption></figure>

***

### Calculating Cosine Similarity

{% hint style="info" %}
#### <mark style="color:blue;">What is Cosine Similarity?</mark>

Simply put, Cosine similarity provides a means to determine the similarity between two items.

This is achieved by calculating the cosine of the angle formed between two vectors (think of two arrows pointing in directions but starting from the same point). The closer the cosine value is to 1 the angle and therefore the greater the similarity between those two items.

* If both vectors are identical their cosine value would be 1 since they have an angle of 0 degrees.
* If both vectors are completely dissimilar their cosine value would be 0 indicating that they are at an angle (90 degrees) to each other.

This method is common in text analysis where words or documents are transformed into lists of values (vectors). These vectors can then be compared to establish their degree of similarity or closeness.
{% endhint %}

```python
# Importing linear_kernel
from sklearn.metrics.pairwise import linear_kernel

# Computing the cosine similarity matrix
cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

```

Let’s look for similarities, between two products!

First, we import the `linear_kernel` function from the `sklearn.metrics.pairwise` library.

Next, for each pair of documents in the `tfidf_matrix`, we calculate their cosine similarity.

By running the `tfidf_matrix` function, we are comparing _each product_ with _every product_. As a result, each <mark style="color:yellow;">cell in the output</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">**cosine\_similarity**</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">represents the cosine similarity between two products</mark> and both rows and columns of the matrix correspond to the number of products, in the `tfidf_matrix`.

{% hint style="info" %}
#### <mark style="color:blue;">Example</mark>

Continuing with products from the previous example:
{% endhint %}

{% code title="Reminder of the products:" %}
```python
products = pd.DataFrame({
    'product_name': ['Perfume A', 'Perfume B', 'Perfume C'],
    'highlights': [
        'Unisex/ Genderless Scent',
        'Layerable Scent',
        'Warm &Spicy Scent'
    ]
})
```
{% endcode %}

{% hint style="info" %}
By running `cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)` we can measure the similarity between all product pairs by based on their descriptions. This measure of similarity goes beyond mere word overlap as it takes into account the frequency and importance of words within the collection of product descriptions (corpus). The resulting matrix of cosine similarity allows us to identify products that share text indicating a connection or shared content characteristics..

Considering this was the tfidf\_matrix we got in the previous example:
{% endhint %}

<figure><img src=".gitbook/assets/Screenshot 2023-11-04 142049.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
The visual table of the 2D array from `cosine_similarit`y will look as such:
{% endhint %}

<figure><img src=".gitbook/assets/Screenshot 2023-11-04 153317.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Values can be in the range from 0 to 1, with 1 being completely similar, to 0 having no similarities whatsoever.



Let’s analyze this table:

* <mark style="color:red;">Perfume A</mark> shows a cosine similarity score of **1.0** against itself which is expected since any vector has a cosine similarity of **1** with itself (the angle is 0 degrees). Same goes for <mark style="color:green;">Perfume B</mark> against <mark style="color:green;">Perfume B</mark> and <mark style="color:purple;">Perfume C</mark> against <mark style="color:purple;">Perfume C</mark>.
* <mark style="color:red;">Perfume A</mark> and <mark style="color:green;">Perfume B</mark> have a cosine similarity of **0.408** suggesting that they share some characteristics while also having some differences.
* <mark style="color:red;">Perfume A</mark> and <mark style="color:purple;">Perfume C</mark> have a cosine similarity of **0.189** indicating they differ more than they resemble each other in terms of the characteristics.
* <mark style="color:green;">Perfume B</mark> and <mark style="color:purple;">Perfume C</mark> have a cosine similarity of **0.0** implying no resemblance at all. In vector space this would signify that they are orthogonal to each other (at a 90 degree angle).
{% endhint %}

***

### get\_recommendations function

{% code fullWidth="true" %}
```python
# Function that takes in product name as input returns most similar products
def get_recommendations(product_name, cosine_sim=cosine_similarity):
    # Getting the index of the product that matches the name
    idx = indices[product_name]

    # Getting the pairwise similarity scores of all products with that product
    sim_scores = list(enumerate(cosine_similarity[idx]))

    # Sorting the products based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Getting the scores of the 10 most similar products
    sim_scores = sim_scores[1:11]

    # Getting the product indices
    product_indices = [i[0] for i in sim_scores]

    # Returning the top 10 most similar products
    return products['product_name'].iloc[product_indices]

```
{% endcode %}

`def` is used to define the function `get_recommendations()` that takes two parameters. `product_name` is the name of the product which we use to generate recommendations for and `cosine_sim` is the matrix that contains the cosine similarity of each product. If no `cosine_sim` matrix is provided, it uses the `cosine_similarity`, matrix we computed in the previous step, by default.

```python
 idx = indices[product_name]
```

idx represents the index of the product\_name that is retrieved from the indices series.

```python
  sim_scores = list(enumerate(cosine_similarity[idx]))
```

`sim_scores` contains the list of tuples that consists of an index (representing a product\_name) and a similarity score that indicates how similar that product is to the input product (pairwise cosine similarity scores).

```python
  sim_scores = sim_scores[1:11]
```

We take only the first ten products, indices 1 to 11. The first index is the input product itself, so it is omitted. The last index is non-inclusive.

```python
  product_indices = [i[0] for i in sim_scores]
```

This iterates over each element $$i$$ of the list `sim_scores`. For each element it takes the first element `[0]` and stores it in `product_indices`.

```python
  return products['product_name'].iloc[product_indices]
```

`product_indices` is used to select the corresponding product name from the `products` DataFrame.

The `iloc` function is used to index the DataFrame by integer location as found in `product_indices`. The function then returns these product names as the top 10 most similar products to the given product.

{% hint style="info" %}
#### <mark style="color:blue;">Example</mark>
{% endhint %}

```python
get_recommendations('Perfume A', cosine_similarity)
```

{% hint style="info" %}
First, we would find the index, for <mark style="color:red;">Perfume A</mark> , which is typically would be **0**.

Next, we retrieve the similarity scores from the matrix for <mark style="color:red;">Perfume A</mark>. From the table generated above the scores are **\[1.0, 0.408 0.189]**.

Them, we arrange these scores in descending order ignoring the first value since it represents <mark style="color:red;">Perfume A</mark>'s similarity with itself.

Considering there are two products both would be returned as recommendations. However, <mark style="color:green;">Perfume B</mark> would be listed first because it has a similarity score of **0.408** compared to <mark style="color:purple;">Perfume C</mark>'s score of **0.189**. In a case with more products, only the first 10 products will be returned.
{% endhint %}
