# Issues with DAD Systems

## Accuracy Issues

Driver alertness detection (DAD) systems encounter numerous challenges that limit their accuracy.

<figure><img src="../../.gitbook/assets/missed target right orientation.png" alt="" width="563"><figcaption></figcaption></figure>

### Key points:

* **Lack of variation in training classes** can reduce accuracy, especially for individuals with darker skin colors
* **Overfitting**&#x20;
  * occurs when models memorize noise instead of generalizable features, leading to biased predictions
  * can lead to biased predictions and perpetuate discriminatory outcomes
* More diverse training data is needed to address these issues, but **AI systems still need to be monitored**

<details>

<summary>Learn More</summary>

Driver alertness detection (DAD) systems encounter accuracy challenges due to several factors. One reason is the limited variation in frame sequences for the classes of interest, such as looking forward, looking left, or looking right (Chai et al., 2023). Unlike different human activities like jumping or squatting, the variation in head movements is minimal, while other features, such as appearance and clothing, vary significantly across different drivers (Chai et al., 2023). This can lead to overfitting and poor generalization when using convolution-based models trained and tested on different drivers (Chai et al., 2023). &#x20;

Additionally, unlike traditional human activity classification where multiple frames contribute to determining the action label, in driver monitoring, the label primarily depends on frames towards the end, such as distinguishing between looking left and looking forward (Chai et al., 2023). Moreover, the camera's position can pose an additional challenge by decreasing the visual differences between different classes, such as looking forward and looking left (Chai et al., 2023).  Driver alertness detection (DAD) systems face accuracy challenges due to various factors. One such factor is the limited variation in frame sequences for the classes of interest. For DAD systems that detect alertness based on the driver’s head position, the main classes of interest would include actions such as turning one’s head to the left, right, or downwards. The system could be trained to associate these classes with various levels of alertness. For example, if the driver’s head is turned downwards, they could be looking at their phone and so, this action would be classified as driving unalert.&#x20;

However, unlike different human activities like jumping or squatting, the variation in head movements is minimal, while other features, such as appearance and clothing, vary significantly across different drivers (Chai et al., 2023). A lack of variation in the training classes for DAD systems can make its predictions less accurate, especially for people of darker skin colors (Albadawi, Takruri, & Award, 2022). This is an example of overfitting, which is a concerning machine learning behaviour that can lead to discrimination as it makes the model biased toward certain groups over others.&#x20;

When a model is trained on a small range of frame sequences, it may be more susceptible to overfitting. Overfitting occurs when the model memorizes specific patterns or noise in the training data instead of learning the underlying generalizable features. This can result in the model making biased predictions based on irrelevant or spurious correlations present in the limited data, reinforcing discriminatory biases and perpetuating unfair outcomes.&#x20;

To address some of these challenges, it is essential to collect more diverse data. If the training data does not adequately represent the diversity of real-world driving scenarios and driver behaviors, the model may struggle to make accurate predictions for underrepresented groups or specific situations. If the training data predominantly consists of drivers of a specific gender, age group, or ethnicity, the model may not generalize well to diverse populations and exhibit biased predictions. This can lead to discriminatory outcomes, where certain groups are unfairly targeted or disadvantaged.

However, it is important to note, that the training phase machine learning systems undergo cannot encompass all possible real-world examples (Bossman, 2016). These systems can be vulnerable to deception in ways that humans wouldn't be (Bossman, 2016). To ensure the desired performance and prevent misuse, it is crucial to carefully monitor and safeguard AI systems as they become integral to various aspects of our lives, such as labor, security, and efficiency (Bossman, 2016).

</details>

## Translating DAD Systems from Simulations to Real-Life

<div>

<figure><img src="../../.gitbook/assets/driving simulator (from Ahangari et al., 2020.png" alt="" width="338"><figcaption><p>Driving Simulator</p></figcaption></figure>

 

<figure><img src="../../.gitbook/assets/distracted-driving netradyne.webp" alt="" width="320"><figcaption><p>Netradyne Driver Simulator </p></figcaption></figure>

</div>

DAD systems are typically developed and tested in simulated environments, posing significant challenges when translating them for real-life applications (Albadawi, Takruri, & Award, 2022).&#x20;

While simulated environments allow for control over intervening variables, these variables can reduce a system’s accuracy when it is put to work in the real world. Some **intervening variables** that can interfere with a system’s performance include:&#x20;

* Illumination variation (Addanki et al., 2020; Albadawi, Takuri, & Award, 2022)
* Background variation (Albadawi, Takruri, & Award, 2022)
* Movements such as swallowing, blinking, or touching one’s face ([Ref](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9482962/))&#x20;
* Features that cover the mouth or eyes such as a beard, mustache, and sunglasses (Albadawi, Takruri, & Award, 2022)&#x20;

Given the impact of these variables, recalibration of the system becomes essential when a new driver assumes control. Neglecting to recalibrate the system can introduce biases and lead to inaccurate indications of distracted driving.&#x20;

<details>

<summary>Learn More</summary>

The translation of DAD systems developed in simulated environments to real-life situations presents significant challenges. When a shorter driver takes over, the way their eyes are tracked changes, resulting in prediction errors. The fixed camera position causes the facial features' location in the image to shift, requiring adjustments to track the driver's eye movement. Moreover, recalibration of the system is needed when the driver changes position to ensure accurate tracking of their eye direction. &#x20;

Another issue arises from the need for real-time systems to function continuously under various lighting conditions; accurately account for changes in facial features due to facial expressions; and provide precise predictions for individuals of different ethnicities, genders, ages, and with different styles of eyeglasses (Badgujar & Selmokar, 2023; Chai et al., 2023). Given the impact of these variables, recalibration of the system becomes essential when a new driver assumes control. Neglecting to recalibrate the system can introduce biases and lead to inaccurate indications of distracted driving.&#x20;

</details>
