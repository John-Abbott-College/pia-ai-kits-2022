# Part 1 - Popular-based recommendations

1. Open SQL Server Management Studio and Create a new Database with name Sephora
2. Download and install the Microsoft Access Database Engine at this [link](https://www.microsoft.com/en-us/download/confirmation.aspx?id=13255).
3. Download and install the Microsoft Server Native Client at this [link](https://www.microsoft.com/en-us/download/details.aspx?id=50402).
4. Right Click on the Sephora Database > Select Tasks > Import Data
5. In **Choose a Data Source** window
   * In the Data Source dropdown list select Microsoft Excel
   * Browse and select the path to the product\_inf.xlsx file
   * Keep the rest of the options unchanged
   * Select Next
6. In **Choose a Destination** window
   * In the Destination dropdown list select SQL Server Native Client > Next
   * Keep the rest of the options unchanged
   * Select Next
7. In **Specify Table Copy or Query** window
   * Keep the default options unchanged
   * Select Next
8. In **Select Source Tables and Views** window
   * Change the name of the table in destination to \[dbo].\[product]
   * Select Next
9. In the **Review Data Type Mapping** window
   * Keep the default options unchanged
   * Select Next
10. In **Save and Run Package** window
    * Keep the default options unchanged
    * Select Next
11. In **Complete Wizard** window
    * Select Finish
12. Verify the table has been created and data has been imported.&#x20;

***

To provide users with popular based recommendations we will write queries that display:

1.  The top ten most popular items. Order Items by decreasing value of popularity.

    We will use a metric to identify how popular a product is. This metric takes into consideration

    * The rating, R, of a product that is in the rating column of the product table
    * The number of reviews, NR, the product received that is in the reviews column of the product table
    * The average rating, AR, of all the products
    * The minimum votes, MV, required to be listed in the popular items (we will use 95th percentile as our cutoff). In other words, for a product to be popular, it must have more ratings than at least 90% of the products in the list. To find this value we will execute the below query&#x20;

{% code overflow="wrap" fullWidth="true" %}
```sql

select distinct percentile_cont(0.90)withingroup(orderby reviews)over ()as MV 
from product

```
{% endcode %}

2. The top ten most loved products. Display the product name, the brand name and the loves count. Order the results from most loved to least loved.
3. All Clean Makeup products under 13$ ordered by price in increasing order
4. The top ten clean products with the highest rating ordered by rating highest to lowest
5. Display all new Sephora exclusive limited edition products. Order by product id from highest to the lowest.
