# Supervised Machine Learning

Having gained an understanding of the complexity involved in measuring the state of distraction, it is now time to construct your own distraction detection model. This will be accomplished using supervised machine learning (SML).

SML uses labeled datasets to train algorithms to classify data or predict outcomes accurately.

| Steps for training an SML model to identify distracted driving                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ol><li>Human experts review visual data of drivers and assess their level of distraction based on the behaviour they display while driving</li></ol> |
| <ol start="2"><li>Labels are created to categorize the different levels of distraction</li></ol>                                                      |
| <ol start="3"><li>These labels are then used as the ‘ground truth’ of distraction that the machine learning model can be based on</li></ol>           |

### Benefits of SML

SML can prove more effective in monitoring drivers for signs of distraction compared to human observation (Shaw, 2019).&#x20;

<table data-header-hidden><thead><tr><th width="187">Benefit</th><th>Description</th></tr></thead><tbody><tr><td><strong>Accuracy</strong></td><td><p>Can make accurate predictions for new, unseen data <a href="https://www.ibm.com/topics/supervised-learning">(IBM, n.d.</a>) [KI1] </p><p> </p><p>Example: <a href="https://www.medicalnewstoday.com/articles/325223">Artificial intelligence better than humans at spotting lung cancer</a></p><p>Example: <a href="https://scitechdaily.com/artificial-intelligence-proves-30-more-accurate-than-humans-at-analyzing-dark-matter/">Artificial Intelligence Proves 30% More Accurate Than Humans at Analyzing Dark Matter</a></p></td></tr><tr><td><strong>Efficiency</strong></td><td><p>Quickly processes and analyzes large amounts of data that is an efficient solution for handling complex and time-consuming tasks (<a href="https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained">Brown, 2021</a>)</p><p> </p><p>Example: <a href="https://phys.org/news/2023-05-deep-images-deep-sea-coral-reefs.html">Deep learning system can analyze images to protect deep-sea coral reefs much faster than humans</a></p></td></tr><tr><td><strong>Scalability</strong></td><td>Scales well with increased data and computational resources (<a href="https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained">Brown, 2021</a>; Sarker, 2021)</td></tr><tr><td><strong>Adaptability</strong></td><td>Able to adapt and learn from new data, enables continuous improvements to predictive capabilities (Aksjonov et al., 2019; Li et al., 2023)</td></tr><tr><td><strong>Interpretability</strong></td><td>More interpretable compared to other approaches (Misra et al., 2022)</td></tr><tr><td><strong>Human Guidance</strong></td><td>Humans provide labeled data and guide training process, ensuring model learns from reliable and relevant examples (<a href="https://www.seldon.io/supervised-vs-unsupervised-learning-explained">Seldon, 2022</a>)</td></tr></tbody></table>

### Issues with SML

#### Dependency on Human Expertise&#x20;

SML heavily relies on human expertise for labeling, feature selection, and model evaluation (Ayyadevara, 2018). The quality and reliability of the model are highly dependent on the competence and domain knowledge of the human experts involved. Inadequate expertise or biased judgments can negatively impact the performance and fairness of the model.

#### Bias & Generalization Issues&#x20;

Since distraction is a subjective experience that varies from person to person, accurately labeling instances of distraction can be challenging. <mark style="color:red;">This</mark> <mark style="color:red;"></mark><mark style="color:red;">**subjectivity**</mark> <mark style="color:red;"></mark><mark style="color:red;">means that the "ground truths" provided by humans may contain inherent</mark> <mark style="color:red;"></mark><mark style="color:red;">**biases**</mark> <mark style="color:red;"></mark><mark style="color:red;">or</mark> <mark style="color:red;"></mark><mark style="color:red;">**inaccuracies**</mark> <mark style="color:red;"></mark><mark style="color:red;">(Bossman, 2016; European Commission, 2018).</mark>

When humans label data to train the model, their subjective interpretation of distraction can unintentionally introduce bias (European Commission, 2018). This bias can manifest in various ways, such as labeling certain instances as distractions while ignoring others, or misclassifying certain states as distractions when they are not (Liu et al., 2016)

If the training data used to teach the model is unrepresentative or contains biased labels, <mark style="color:red;">the model can learn and perpetuate those biases (European Commission, 2018).</mark> As a result, the model's predictions and classifications may be skewed, leading to unfair or discriminatory outcomes when applied in real-world scenarios (Shaw, 2019).

