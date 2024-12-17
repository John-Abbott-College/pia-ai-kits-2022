# Evaluating the Ethics of ML

Anyone involved in the development or deployment of ML must be mindful of the impact they can have. As we learned earlier, ML technologies have the potential to cause harm. To avoid doing harm, ML must be developed and deployed with ethical principles in mind. Let’s start off by exploring the principle of accuracy and its importance in reducing harm that can be caused by ML.

## Accuracy <a href="#toc2099554218" id="toc2099554218"></a>

<div align="left"><figure><img src=".gitbook/assets/Picture30.png" alt="" width="99"><figcaption></figcaption></figure></div>

ML in the energy sector is intended to enhance accuracy and improve processes. However, there are instances where ML can introduce inaccuracies in energy systems, which can be highly costly and dangerous \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)].

### Data Quality

ML models are sensitive to data quality \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[23](https://www.mdpi.com/1996-1073/16/8/3309)]. Noisy or incomplete data, outliers, or errors in the data can introduce inaccuracies in the learning process \[[6](https://www.ey.com/en_ca/power-utilities/why-artificial-intelligence-is-a-game-changer-for-renewable-energy)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[23](https://www.mdpi.com/1996-1073/16/8/3309)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. These issues can mislead the model and lead to inaccurate predictions or classifications \[[6](https://www.ey.com/en_ca/power-utilities/why-artificial-intelligence-is-a-game-changer-for-renewable-energy)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[23](https://www.mdpi.com/1996-1073/16/8/3309)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. Using high-quality datasets can help to minimize errors and biases in the model \[[20](https://www.mdpi.com/2673-2688/4/2/22)]. &#x20;

### Dangers of ML Inaccuracy

ML models in the energy sector are responsible for critical decision-making in power generation, distribution, and control systems \[[14](https://www.sciencedirect.com/science/article/pii/S2211467X22002115)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[68](https://www.tojqi.net/index.php/journal/article/download/3305/2242/3638)]. Inaccurate models can lead to disruptions, equipment failures, and accidents \[[23](https://www.mdpi.com/1996-1073/16/8/3309)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. For instance, incorrect energy demand predictions can cause power grid imbalances and component overloads, posing safety risks \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)], \[[69](https://www.semanticscholar.org/paper/Smart-home-energy-strategy-based-on-human-behaviour-Ko-Kim/e52e9c302e8845b660bc15e822e23b6f9b60af67)]. Inaccurate ML systems directly impact field employees' safety, potentially exposing them to hazards during maintenance or high-voltage operations \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)].

### Improving ML Accuracy <a href="#toc744262854" id="toc744262854"></a>

One way to improve a model’s accuracy is to gather more data \[[6](https://www.ey.com/en_ca/power-utilities/why-artificial-intelligence-is-a-game-changer-for-renewable-energy)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[68](https://www.tojqi.net/index.php/journal/article/download/3305/2242/3638)]. More data provides a richer understanding of the complexities of the energy sector, leading to improved accuracy and better-informed decision-making \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[65](https://ieeexplore.ieee.org/document/9377027)]. With a larger dataset, ML models can better identify patterns, correlations, and trends within the energy system, leading to more precise predictions and reliable insights \[[6](https://www.ey.com/en_ca/power-utilities/why-artificial-intelligence-is-a-game-changer-for-renewable-energy)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)], \[[70](https://www.sciencedirect.com/science/article/pii/S2666827022000597)], \[[71](https://towardsdatascience.com/analyzing-power-usage-in-schools-with-machine-learning-ba07f089d547)].

However, the abundance of data can be a double-edged sword. While more data becomes available, there is a risk of including a significant amount of outdated and irrelevant information \[[66](https://www.mdpi.com/1996-1073/12/17/3254)]. This can impact the quality of the data which directly influences the accuracy and reliability of the insights derived from it \[[6](https://www.ey.com/en_ca/power-utilities/why-artificial-intelligence-is-a-game-changer-for-renewable-energy)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)].

Energy companies may find themselves overwhelmed by the sheer volume of data they generate, struggling to effectively manage and utilize it due to its dispersed and disorganized nature \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. So, despite having access to substantial amounts of data, efficiently interpreting this vast and diverse data to extract valuable information for smart decision-making remains a major hurdle for the energy sector \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)].

## Accuracy vs. Sustainability <a href="#toc457610866" id="toc457610866"></a>

![](.gitbook/assets/Picture30.png) VS. ![](<.gitbook/assets/Picture9 (1).png>)

&#x20;

Evaluating ML models is not just about how accurate its predictions are. Sustainability also matters a great deal. However, making a ML model more accurate can lead to reduced sustainability due to the increased resource demands and environmental impact \[[24](https://www.researchgate.net/publication/350071340_Automated_prediction_system_of_household_energy_consumption_in_cities_using_web_crawler_and_optimized_artificial_intelligence)], \[[45](https://dl.acm.org/doi/10.1145/3442188.3445922)], \[[47](https://futurium.ec.europa.eu/en/european-ai-alliance/blog/sustainable-artificial-intelligence-energy-sector?language=es)]. Here are some factors that can contribute to the trade-off between accuracy and sustainability:

Factors that make ML <mark style="color:green;">more accurate</mark>, but <mark style="color:red;">less sustainable</mark>:

* Computational resources: Improving accuracy often involves using more sophisticated and computationally intensive algorithms or larger models \[[25](https://www.mdpi.com/1996-1073/15/12/4427)], \[[48](https://arxiv.org/abs/2212.11738)]. These resource-intensive approaches consume more energy and computational power, making the model less energy-efficient and thus less sustainable \[[45](https://dl.acm.org/doi/10.1145/3442188.3445922)], \[[48](https://arxiv.org/abs/2212.11738)].
* Model Tuning and Optimization: Achieving higher accuracy may involve exhaustive hyperparameter tuning and optimization, which can require multiple training iterations, leading to increased energy consumption \[[45](https://dl.acm.org/doi/10.1145/3442188.3445922)].

{% hint style="info" %}
Note: This is not an exhaustive list, there are other factors that can make ML more accurate but less sustainable.
{% endhint %}

On the other hand, making a ML model more sustainable may lead to a reduction in accuracy due to certain trade-offs involved in optimizing for sustainability \[[72](https://www.forbes.com/sites/esade/2023/03/17/we-need-to-make-machine-learning-sustainable-heres-how/)].

Factors that make ML <mark style="color:red;">less accurate</mark>, but <mark style="color:green;">more sustainable</mark>:

* Feature Engineering: Sustainable models might streamline feature engineering processes, focusing on a subset of relevant features to reduce computation \[[47](https://futurium.ec.europa.eu/en/european-ai-alliance/blog/sustainable-artificial-intelligence-energy-sector?language=es)], \[[73](https://towardsdatascience.com/why-having-many-features-can-hinder-your-models-performance-865369b6b8b1)]. However, this approach may overlook valuable information, impacting accuracy \[[47](https://futurium.ec.europa.eu/en/european-ai-alliance/blog/sustainable-artificial-intelligence-energy-sector?language=es)], \[[73](https://towardsdatascience.com/why-having-many-features-can-hinder-your-models-performance-865369b6b8b1)].
* Regularization and Constraints: Sustainability-conscious ML models might apply regularization techniques or constraints to limit model complexity and resource usage \[[74](https://towardsdatascience.com/regularization-in-machine-learning-76441ddcf99a)] - \[[75](https://www.annualreviews.org/doi/10.1146/annurev-environ-020220-061831)]. While this can improve efficiency, it may also limit the model's ability to fit complex patterns in the data, leading to decreased accuracy \[[74](https://towardsdatascience.com/regularization-in-machine-learning-76441ddcf99a)] - \[[75](https://www.annualreviews.org/doi/10.1146/annurev-environ-020220-061831)].

{% hint style="info" %}
Note: This is not an exhaustive list, there are other factors that can make ML more sustainable but less accurate.
{% endhint %}

To truly make ML more accurate and sustainable, the rebound effect must be taken into consideration \[[46](https://ideas.repec.org/a/nat/natcli/v12y2022i6d10.1038_s41558-022-01377-7.html)]. If the ML process is made more efficient with lower energy, emissions, and monetary costs, people will use it more \[[46](https://ideas.repec.org/a/nat/natcli/v12y2022i6d10.1038_s41558-022-01377-7.html)]. Sometimes by lowering the cost you don’t increase demand \[[46](https://ideas.repec.org/a/nat/natcli/v12y2022i6d10.1038_s41558-022-01377-7.html)]. However, sometimes you can partially or fully negate the benefits that you get from making something more efficient if the demand increases \[[46](https://ideas.repec.org/a/nat/natcli/v12y2022i6d10.1038_s41558-022-01377-7.html)].&#x20;

## Accuracy vs. Privacy <a href="#toc95454732" id="toc95454732"></a>

![](.gitbook/assets/Picture30.png) VS. ![](.gitbook/assets/Picture31.png)

&#x20;

Similar to the relationship between accuracy and sustainability, making ML more accurate can also make it less private. The tradeoff between accuracy and privacy in machine learning arises due to the tension between maximizing predictive performance and protecting sensitive information \[[29](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)]. Here are some factors that can contribute to the trade-off between accuracy and privacy:

Factors that make ML <mark style="color:green;">more accurate</mark>, but <mark style="color:red;">less privacy preserving</mark>:

* Increased data collection: To achieve high accuracy, machine learning models often require large and diverse datasets. However, collecting such data can raise privacy concerns \[[24](https://www.researchgate.net/publication/350071340_Automated_prediction_system_of_household_energy_consumption_in_cities_using_web_crawler_and_optimized_artificial_intelligence)], \[[68](https://www.tojqi.net/index.php/journal/article/download/3305/2242/3638)]. The more data that is collected, the higher the risk of exposing sensitive information about individuals \[[24](https://www.researchgate.net/publication/350071340_Automated_prediction_system_of_household_energy_consumption_in_cities_using_web_crawler_and_optimized_artificial_intelligence)], \[[68](https://www.tojqi.net/index.php/journal/article/download/3305/2242/3638)].
* Data sharing: Improving accuracy may require accessing and sharing more data, including sensitive information, to train the model effectively \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[28](https://dl.acm.org/doi/10.1145/3538637.3539636)], \[[29](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)], \[[43](https://ieeexplore.ieee.org/document/9883030)]. Increased data sharing can raise privacy concerns, as it exposes sensitive details about individuals or organizations \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[28](https://dl.acm.org/doi/10.1145/3538637.3539636)], \[[29](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)], \[[43](https://ieeexplore.ieee.org/document/9883030)].

{% hint style="info" %}
Note: This is not an exhaustive list, there are other factors that can make ML more accurate              but less privacy preserving.
{% endhint %}

Factors that make ML <mark style="color:red;">less accurate</mark>, but <mark style="color:green;">more privacy preserving</mark>:

* Data anonymization: Anonymization techniques are often employed to protect privacy when sharing or using data \[[7](https://www.sciencedirect.com/science/article/pii/S0306261921001409)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)]. However, the process of anonymization can result in a loss of accuracy \[[76](https://www.k2view.com/blog/anonymized-data/)]. When data is heavily anonymized or aggregated, important details may be obscured, limiting the effectiveness of the machine learning models trained on such data \[[7](https://www.sciencedirect.com/science/article/pii/S0306261921001409)], \[[20](https://www.mdpi.com/2673-2688/4/2/22)].
* Noise addition: To preserve privacy, noise or perturbation might be added to the data during training, making it more challenging for the model to distinguish between subtle patterns \[[10](https://www.sciencedirect.com/science/article/pii/S2405959523000644)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)], \[[77](https://www.codingninjas.com/studio/library/noise-injection-in-neural-networks)]. This can result in reduced accuracy compared to models trained on clean data \[[78](https://arxiv.org/abs/1805.08000)].

{% hint style="info" %}
Note: This is not an exhaustive list, there are other factors that can make ML more privacy preserving but less accurate.
{% endhint %}

## Ethical Principles <a href="#toc99787066" id="toc99787066"></a>

For the next sub-activity, we will focus on the principles of **accuracy**, **privacy**, and **sustainability** as they have particular importance in the application of ML in the energy sector. However, it is important to keep in mind that there may still be other ethical issues at play such as unfairness and lack of transparency, including others that have not been outlined here. For now, we will limit our focus to the following:

&#x20;

<table data-header-hidden><thead><tr><th width="261"></th><th width="170.33333333333331" align="center"></th><th></th></tr></thead><tbody><tr><td><img src=".gitbook/assets/Picture30.png" alt=""></td><td align="center"><strong>Accuracy</strong></td><td><p>Involves striving for the highest level of precision and correctness, ensuring reliable and dependable results that align with intended objectives [<a href="https://www.fatml.org/resources/principles-for-accountable-algorithms">79</a>].</p><p> </p></td></tr><tr><td><img src=".gitbook/assets/Picture31.png" alt=""></td><td align="center"><strong>Privacy</strong></td><td><p>Involves safeguarding and respecting the confidentiality of data, emphasizing responsible and secure handling of sensitive information throughout the development and deployment process [<a href="https://www.nature.com/articles/s42256-019-0088-2">80</a>].</p><p> </p></td></tr><tr><td><img src=".gitbook/assets/Picture9 (1).png" alt=""></td><td align="center"><strong>Sustainability</strong></td><td><p>Involves developing systems with a positive and lasting impact on society and the environment, emphasizing responsible resource use to support long-term viability [<a href="https://www.nature.com/articles/s42256-019-0088-2">80</a>].</p><p> </p></td></tr></tbody></table>

&#x20;

<details>

<summary><strong>Learn More – Additional Ethical Principles to Consider</strong></summary>

While there is no universal set of guidelines or regulations governing ML, certain principles have emerged as crucial in developing ethical ML, including **fairness** and **transparency**, to name a few \[[80](https://www.nature.com/articles/s42256-019-0088-2)]. These principles are important when assessing ML’s impact on the energy sector \[[8](https://www.researchgate.net/publication/370580741_AI-Enabled_Energy_Policy_for_a_Sustainable_Future)], \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)]. For instance, ML can create **unfair** outcomes in energy systems \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. ML models learn from historical data, and if the training data is biased, the model will perpetuate that bias in its predictions \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. In the energy sector, historical data may reflect past inequalities or discriminatory practices, leading to biased outcomes \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. If certain groups or communities are underrepresented in the training data, the ML model may not accurately capture their specific needs or energy consumption patterns, resulting in unequal treatment \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)], \[[29](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)].

**Transparency** refers to the clarity and openness in the decision-making process of ML models \[[81](https://medium.com/compendium/https-medium-com-mab-55055-what-is-fatml-and-why-should-you-care-dfb36e51f2f4)], \[[82](https://cdn2.hubspot.net/hubfs/4015851/Fate%20In%20AI.pdf)]. Many ML models can be highly complex and consist of numerous layers and interconnected nodes \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. As these models become more sophisticated, they often become harder to interpret and understand fully \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)], \[[23](https://www.mdpi.com/1996-1073/16/8/3309)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. This lack of transparency can make it difficult to identify and address potential biases and **unfairness** in the model's decision-making process \[[22](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)], \[[25](https://www.mdpi.com/1996-1073/15/12/4427)]. In addition, a lack of transparency can raise **privacy** concerns as individuals may not understand how their data is being used or how the model arrives at its predictions \[[2](https://www.sciencedirect.com/science/article/abs/pii/S0959652621000548)], \[[26](https://www.energyrev.org.uk/media/1985/energyrev_aiandethics_final_202207.pdf)], \[[43](https://ieeexplore.ieee.org/document/9883030)]. These examples demonstrate how the principles intertwine and reinforce each other. It is therefore best practice to assess the ethics of ML holistically \[[26](https://www.energyrev.org.uk/media/1985/energyrev_aiandethics_final_202207.pdf)], \[[29](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)].

</details>
