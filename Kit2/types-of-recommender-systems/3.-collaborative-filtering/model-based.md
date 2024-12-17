# Model-based

**Model-based** approaches assume an underlying model that explains the user-item interactions and try to discover it in order to make new predictions  \[[1](https://link.springer.com/referenceworkentry/10.1007/978-0-387-30164-8_705)], \[[29](https://link.springer.com/chapter/10.1007/978-3-319-29659-3_3)]. Data is extracted from the user-item interaction matrix and used to build a model to make recommendations using machine learning or data mining techniques \[[29](https://link.springer.com/chapter/10.1007/978-3-319-29659-3_3)]. The techniques used to build these models include matrix factorization, deep neural networks, and other types of ML algorithms \[[29](https://link.springer.com/chapter/10.1007/978-3-319-29659-3_3)]. Information is extracted from the dataset and used to build a "model" to make recommendations without having to use the complete dataset every time \[[29](https://link.springer.com/chapter/10.1007/978-3-319-29659-3_3)].



<details>

<summary><strong>Learn More – Model-based Collaborative Filtering Approach</strong></summary>

**Advantages:**

* **Scalability** : Model-based algorithms typically produce much smaller models compared to the actual dataset \[[28](https://vitalflux.com/recommender-systems-in-machine-learning-examples/)], \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)]. As a result, even when dealing with very large datasets, the models remain small enough to be efficiently utilized \[[28](https://vitalflux.com/recommender-systems-in-machine-learning-examples/)], \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)].
* **Prediction speed** : Model-based systems also offer faster prediction speeds, especially when compared to memory-based systems \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)]. The time needed to query the model is generally much shorter than the time required to query the entire dataset which leads to quicker predictions \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)].

**Disadvantages:**

* **Complexity** : Model-based CF requires more complex implementation and training compared to memory-based approaches \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)]. Building and fine-tuning models can be more challenging and resource-intensive \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)].
* **Cold start problem** : Model-based CF can still face a cold start problem for new users and items that haven't provided sufficient interaction data for training the model \[[1](https://link.springer.com/referenceworkentry/10.1007/978-0-387-30164-8_705)], \[[14](https://www.analyticssteps.com/blogs/what-are-recommendation-systems-machine-learning)], \[[15](https://zenodo.org/records/5574927)]. Handling the cold start problem requires additional strategies or hybrid approaches  \[[1](https://link.springer.com/referenceworkentry/10.1007/978-0-387-30164-8_705)], \[[14](https://www.analyticssteps.com/blogs/what-are-recommendation-systems-machine-learning)], \[[15](https://zenodo.org/records/5574927)], \[[18](https://www.altexsoft.com/blog/recommender-system-personalization/)], \[[21](https://maddevs.io/blog/recommender-system-using-machine-learning/)].
* **Interpretability** : Model-based CF models are often less interpretable compared to memory-based methods \[[16](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada)]. Understanding the exact reasons behind the recommendations can be more challenging due to the complexity of the models \[[16](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada)].
* **Data requirements** : Model-based CF generally requires a significant amount of data for training, especially when using complex machine learning algorithms \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)], \[[31](https://www.granify.com/blog/10-things-you-need-to-know-about-collaborative-filtering)]. In scenarios with limited data, it can be challenging to build accurate and reliable models \[[30](https://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/modelbased.html)], \[[31](https://www.granify.com/blog/10-things-you-need-to-know-about-collaborative-filtering)].

</details>
