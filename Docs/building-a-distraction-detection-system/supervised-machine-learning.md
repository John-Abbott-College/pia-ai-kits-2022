# Supervised Machine Learning

Having gained an understanding of the complexity involved in measuring the state of distraction, it is now time to construct your own distraction detection model. This will be accomplished using supervised machine learning (SML).

SML uses labeled datasets to train algorithms to classify data or predict outcomes accurately.

| Steps for training an SML model to identify distracted driving                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ol><li>Human experts review visual data of drivers and assess their level of distraction based on the behaviour they display while driving [36].</li></ol> |
| <ol start="2"><li>Labels are created to categorize the different levels of distraction [36].</li></ol>                                                      |
| <ol start="3"><li>These labels are then used as the ‘ground truth’ of distraction that the machine learning model can be based on [36].</li></ol>           |

### Benefits of SML

SML can prove more effective in monitoring drivers for signs of distraction compared to human observation \[37].&#x20;

<table data-header-hidden><thead><tr><th width="187">Benefit</th><th>Description</th></tr></thead><tbody><tr><td><strong>Accuracy</strong></td><td><p>Can make accurate predictions for new, unseen data [38].</p><p> </p><p>Example: <a href="https://www.medicalnewstoday.com/articles/325223">Artificial intelligence better than humans at spotting lung cancer</a></p><p>Example: <a href="https://scitechdaily.com/artificial-intelligence-proves-30-more-accurate-than-humans-at-analyzing-dark-matter/">Artificial Intelligence Proves 30% More Accurate Than Humans at Analyzing Dark Matter</a></p></td></tr><tr><td><strong>Efficiency</strong></td><td><p>Quickly processes and analyzes large amounts of data that is an efficient solution for handling complex and time-consuming tasks [39].</p><p> </p><p>Example: <a href="https://phys.org/news/2023-05-deep-images-deep-sea-coral-reefs.html">Deep learning system can analyze images to protect deep-sea coral reefs much faster than humans</a></p></td></tr><tr><td><strong>Scalability</strong></td><td>Scales well with increased data and computational resources ​[3]​, ​[39]​.</td></tr><tr><td><strong>Adaptability</strong></td><td>Able to adapt and learn from new data, enables continuous improvements to predictive capabilities ​[34]​, ​[40]​.</td></tr><tr><td><strong>Interpretability</strong></td><td>More interpretable compared to other approaches [41].</td></tr><tr><td><strong>Human Guidance</strong></td><td>Humans provide labeled data and guide training process, ensuring model learns from reliable and relevant examples [42].</td></tr></tbody></table>

### Issues with SML

#### Dependency on Human Expertise&#x20;

SML heavily relies on human expertise for labeling, feature selection, and model evaluation ​\[43]​. The quality and reliability of the model are highly dependent on the competence and domain knowledge of the human experts involved ​\[43]​. Inadequate expertise or biased judgments can negatively impact the performance and fairness of the model.

#### Bias & Generalization Issues&#x20;

Since distraction is a subjective experience that varies from person to person, accurately labeling instances of distraction can be challenging \[2]. <mark style="color:red;">This</mark> <mark style="color:red;"></mark><mark style="color:red;">**subjectivity**</mark> <mark style="color:red;"></mark><mark style="color:red;">means that the "ground truths" provided by humans may contain inherent</mark> <mark style="color:red;"></mark><mark style="color:red;">**biases**</mark> <mark style="color:red;"></mark><mark style="color:red;">or</mark> <mark style="color:red;"></mark><mark style="color:red;">**inaccuracies**</mark> <mark style="color:red;"></mark><mark style="color:red;">\[17], \[18].</mark>

When humans label data to train the model, their subjective interpretation of distraction can unintentionally introduce bias ​\[17]​. This bias can manifest in various ways, such as labeling certain instances as distractions while ignoring others, or misclassifying certain states as distractions when they are not ​\[36]​.

If the training data used to teach the model is unrepresentative or contains biased labels, <mark style="color:red;">the model can learn and perpetuate those biases \[17].</mark> As a result, the model's predictions and classifications may be skewed, leading to unfair or discriminatory outcomes when applied in real-world scenarios \[37].

