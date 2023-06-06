# Measuring Alertness

## Distraction&#x20;

Drivers may become **unalert** due to **distractions** in the driving environment.&#x20;

<div>

<figure><img src="../.gitbook/assets/Male driver drinking hot coffee while driving on road in autumn warm colors.jpeg" alt="" width="375"><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/Woman Traveling By Car Using Smartphone.jpeg" alt="" width="375"><figcaption></figcaption></figure>

</div>

<mark style="color:red;">Distraction is a</mark> <mark style="color:red;"></mark><mark style="color:red;">**complex**</mark> <mark style="color:red;"></mark><mark style="color:red;">state.</mark> Most activities that divert a driver’s attention from the road and the task of driving tend to involve multiple, if not all, types of distraction simultaneously (Ahangari et al., 2020).&#x20;

### Types of Distractions

<table data-card-size="large" data-view="cards" data-full-width="false"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><em><strong>Auditory</strong></em></td><td>Takes <strong>ears</strong> off road</td><td>Ex) listening to radio or passengers talk </td><td><a href="../.gitbook/assets/ear.png">ear.png</a></td></tr><tr><td><em><strong>Visual</strong></em></td><td>Takes <strong>eyes</strong> off road</td><td>Ex) looking at smartphone screen </td><td><a href="../.gitbook/assets/eye.png">eye.png</a></td></tr><tr><td><em><strong>Cognitive</strong></em></td><td>Takes <strong>mind</strong> off road</td><td>Ex) thinking about something other than driving</td><td><a href="../.gitbook/assets/human-brain.png">human-brain.png</a></td></tr><tr><td><em><strong>Biomechanical</strong></em></td><td>Takes <strong>hands</strong> off wheel</td><td>Ex) eating, adjusting dashboard controls</td><td><a href="../.gitbook/assets/open-hands.png">open-hands.png</a></td></tr></tbody></table>

### Distraction is subjective&#x20;

Distraction is a multifaceted state that cannot be fully captured by just one type of data (Vismaya & Saritha, 2020). What distracts one person may not distract another.&#x20;

<div align="center">

<figure><img src="../.gitbook/assets/cognitive.png" alt="" width="128"><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/blank space.png" alt="" width="73"><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/adhd.png" alt="" width="128"><figcaption></figcaption></figure>

</div>

## Data Types

There are four types of data used to study alertness in driving, each type has its **advantages** and **limitations** (Vismaya & Saritha, 2020).&#x20;

{% tabs %}
{% tab title="Behavioural" %}
Visual data depicting position and movement of different body parts of drivers (Shajari et al., 2022)
{% endtab %}

{% tab title="Self-assessment" %}
Data collected from self-report questionnaires or surveys that ask drivers to reflect on their driving behaviour and engagement in distracting activities (Aksjonov et al., 2019)&#x20;
{% endtab %}

{% tab title="Physiological" %}
Data collected through sensors placed on drivers' bodies including heart rate, brain activity, breathing rate, skin temperature, and eye movement (Aksjonov et al., 2019)
{% endtab %}

{% tab title="Performance" %}
Data that are obtained indirectly from the driver by assessing their vehicle-related actions such as brake and steering behaviour (Aksjonov et al., 2019; Shajari et al., 2022)
{% endtab %}
{% endtabs %}

<details>

<summary>Learn More</summary>

Each type of data has its advantages and limitations (Vismaya & Saritha, 2020). For instance, data collected from self-assessment questionnaires can offer valuable insights, but they are based on drivers’ personal opinions and the subjectivity of this measure can lessen its reliability (Shajari et al., 2022). Likewise, physiological data, although valuable to the study of distracted driving, are susceptible to interference from various factors such as drivers’ muscle movements (Shajari et al., 2022).&#x20;

Distraction is a multifaceted state that cannot be fully captured by just one type of data (Vismaya & Saritha, 2020). Most activities that divert a driver’s attention from the road and the task of driving tend to involve multiple, if not all, types of distraction simultaneously (Ahangari et al., 2020). For instance, texting creates concurrent manual, visual, and cognitive distractions (Ahangari et al., 2020). To add to this complexity, the four types of data - performance, physiological, behavioral, and self-assessment - may not always align with each other. For example, a driver may feel fully focused on the road despite exhibiting behavioral signs of distraction. This discrepancy would result in a misalignment between the behavioral data collected from the driver and their self-assessment data. &#x20;

Alternatively, a driver can experience cognitive distraction without it being evident in their driving performance or detectable through physiological measures. This exemplifies the subjective and complex nature of distraction. Current methods lack the capability to fully comprehend and identify the complexities involved. The state of distraction is inherently unique to each person, as what may distract one individual might not have the same effect on another. This subjectivity presents challenges when attempting to study or measure distraction accurately.&#x20;

</details>

## Supervised Machine Learning (SML)

SML models can be used to study alertness in driving.&#x20;

| Steps for training SML model to identify unalert driving                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ol><li>Human experts review visual data of drivers and assess their level of distraction based on the behaviour they display while driving</li></ol> |
| <ol start="2"><li>Labels are created to categorize the different levels of distraction</li></ol>                                                      |
| <ol start="3"><li>These labels are then used as the ‘ground truth’ of distraction that the machine learning model can be based on</li></ol>           |

<details>

<summary>Learn More</summary>

Most studies on distracted driving utilize supervised machine learning (SML) to analyze data (Liu et al, 2016). As part of this process, human experts review visual data of drivers and assess their level of distraction based on the behaviour they display while driving (Liu et al., 2016). Based on this initial review of the data, labels are created to categorize the different levels of distraction (Liu et al., 2016). These labels are then used as the ‘ground truth’ of distraction that the machine learning model can be based on (Liu et al., 2016). This is an example of SML in which models are trained under human supervision ([Ref](https://emeritus.org/blog/artificial-intelligence-and-machine-learning-classification-in-machine-learning/)).&#x20;

</details>

### Benefits of SML

SML can prove more effective in monitoring drivers for signs of distraction compared to human observation.&#x20;

<table data-header-hidden><thead><tr><th width="187">Benefit</th><th>Description</th></tr></thead><tbody><tr><td><strong>Accuracy</strong></td><td>can make accurate predictions for new, unseen data </td></tr><tr><td><strong>Efficiency</strong></td><td>quickly processes &#x26; analyzes large amounts of data, efficient solution for handling complex &#x26; time-consuming tasks</td></tr><tr><td><strong>Scalability</strong></td><td>scales well with increased data &#x26; computational resources </td></tr><tr><td><strong>Adaptability</strong></td><td>able to adapt and learn from new data, enables continuous improvements to predictive capabilities</td></tr><tr><td><strong>Interpretability</strong></td><td>more interpretable compared to other approaches</td></tr><tr><td><strong>Human Guidance</strong></td><td>humans provide labeled data and guide training process, ensuring model learns from reliable and relevant examples</td></tr></tbody></table>

### Issues with SML

#### Dependency on Human Expertise&#x20;

SML heavily relies on human expertise for labeling, feature selection, and model evaluation. The quality and reliability of the model are highly dependent on the competence and domain knowledge of the human experts involved. Inadequate expertise or biased judgments can negatively impact the performance and fairness of the model.

#### Bias & Generalization Issues&#x20;

Since distraction is a subjective experience that varies from person to person, accurately labeling instances of distraction can be challenging. <mark style="color:red;">This</mark> <mark style="color:red;"></mark><mark style="color:red;">**subjectivity**</mark> <mark style="color:red;"></mark><mark style="color:red;">means that the "ground truths" provided by humans may contain inherent</mark> <mark style="color:red;"></mark><mark style="color:red;">**biases**</mark> <mark style="color:red;"></mark><mark style="color:red;">or</mark> <mark style="color:red;"></mark><mark style="color:red;">**inaccuracies**</mark><mark style="color:red;">.</mark>

When humans label data to train the model, their subjective interpretation of distraction can unintentionally introduce bias. This bias can manifest in various ways, such as labeling certain instances as distractions while ignoring others, or misclassifying certain states as distractions when they are not.

If the training data used to teach the model is unrepresentative or contains biased labels, <mark style="color:red;">the model can learn and perpetuate those biases.</mark> As a result, the model's predictions and classifications may be skewed, leading to unfair or discriminatory outcomes when applied in real-world scenarios.
