# Part 1 – Popular-based recommendations

**Teaching Notes**

<table data-header-hidden><thead><tr><th width="139"></th><th></th></tr></thead><tbody><tr><td>Ask</td><td>Students to complete steps 1 to 12 <a href="https://app.gitbook.com/s/NzKApfSfEwdEjEg8yyOv/building-a-recommender-system/part-1-popular-based-recommendations">here</a>.</td></tr><tr><td>Do</td><td>Give students 45 minutes to complete the steps in this part.</td></tr><tr><td>Ask</td><td>Students if they have any questions.</td></tr><tr><td>Ask</td><td>Students to complete step 1.</td></tr><tr><td>Do</td><td><p></p><p>Provide this solution to students if needed:</p><p> </p><p>The popularity value is calculated using the formula below</p><p>Popularity = [Equation]</p><pre class="language-sql" data-overflow="wrap"><code class="lang-sql"><strong>DECLARE @AR AS FLOAT
</strong>SELECT @AR=AVG(rating) from product;
PRINT @AR
 
DECLARE @MV AS INT 
select @MV= MV from (select percentile_cont(0.90) within group(order by reviews) over () as MV from product) as t;
PRINT @MV;
 
select top 10 product_name + ' by '+ brand_name,  rating as R, reviews as NR, ((reviews / (reviews + @MV)) * rating) + ((@MV / (reviews + @MV)) * @AR) popularity from product order by popularity desc;
</code></pre><p></p><p> </p></td></tr><tr><td>Ask</td><td>Students to complete step 2.</td></tr><tr><td>Do</td><td><p> </p><p>Provide this solution to students if needed:</p><pre class="language-sql" data-overflow="wrap"><code class="lang-sql">select product_name + ' by '+ brand_name, loves_count from product order by loves_count desc
</code></pre><p> </p></td></tr><tr><td>Ask</td><td>Students to complete step 3.</td></tr><tr><td>Do</td><td><p> </p><p>Provide this solution to students if needed:</p><p> </p><pre class="language-sql" data-overflow="wrap"><code class="lang-sql">select  product_name + ' by '+ brand_name, loves_count from product where price_usd &#x3C; 13 and primary_category = 'Makeup' and highlights like '%clean%' order by price asc;  
</code></pre><p> </p></td></tr><tr><td>Ask</td><td>Students to complete step 4.</td></tr><tr><td>Do</td><td><p> </p><p>Provide this solution to students if needed:</p><p> </p><pre class="language-sql" data-overflow="wrap"><code class="lang-sql">select top 10 product_name + ' by '+ brand_name from product where highlights like '%clean%' order by rating desc;  
</code></pre><p> </p></td></tr><tr><td>Ask</td><td>Students to complete step 5.</td></tr><tr><td>Do</td><td><p> </p><p>Provide this solution to students if needed:</p><p> </p><pre class="language-sql" data-overflow="wrap"><code class="lang-sql">select * from product where new=1 and sephora_exclusive=1 and limited_edition=1 order by product_id desc
</code></pre><p> </p></td></tr></tbody></table>

