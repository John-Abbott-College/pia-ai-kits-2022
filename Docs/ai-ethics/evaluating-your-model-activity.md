# Evaluate Your Model \[Activity]

Now that you've built your model, let's evaluate it!&#x20;

Evaluating AI models is not just about how accurate its predictions are. Anyone involved in the development or deployment of AI technologies must be mindful of the impact they can have. As we learned earlier, AI technologies have the potential to cause harm. To avoid doing harm, AI must be developed and deployed with ethical principles in mind.&#x20;

## Principles for Ethical AI

While there is no universal set of guidelines or regulations governing AI, a consensus is beginning to emerge around the importance of the following principles: **responsibility, fairness, transparency, and freedom** (Jobin et al., 2019).&#x20;

<table data-header-hidden><thead><tr><th width="173">Principle</th><th>Description</th></tr></thead><tbody><tr><td><strong>Responsibility</strong></td><td><p>Encompasses the accountability and conscientiousness required from individuals and organizations involved in the development, deployment, and use of artificial intelligence systems. (Bertani-Okland, 2019; William, A, 2019 <a href="https://cdn2.hubspot.net/hubfs/4015851/Fate%20In%20AI.pdf">Ref</a>) </p><p> </p><p><strong>Example: Self-driving cars</strong></p><p>Responsibility issues with self-driving cars revolve around determining who is responsible in the event of accidents or incidents involving autonomous vehicles (<a href="https://montrealethics.ai/the-ethical-considerations-of-self-driving-cars/">Ref</a>). Unlike traditional human-driven cars, where liability typically rests with the driver, the introduction of AI systems in self-driving cars complicates this matter (<a href="https://montrealethics.ai/the-ethical-considerations-of-self-driving-cars/">Ref</a>). <a href="https://www.theguardian.com/technology/2022/dec/22/tesla-crash-full-self-driving-mode-san-francisco">Here</a> is just one of many incidents involving self-driving cars.</p></td></tr><tr><td><strong>Fairness</strong></td><td><p>Encompasses the pursuit of equitable and impartial treatment of individuals and groups throughout the development, deployment, and utilization of AI systems (Bertani-Okland, 2019).</p><p> </p><p><strong>Example: AI decides who gets healthcare</strong><br>A healthcare algorithm used in US hospitals exhibited favoritism towards white patients over black patients (<a href="https://datatron.com/real-life-examples-of-discriminating-artificial-intelligence/">Ref</a>). This disparity arose due to the algorithm's training on historical data related to healthcare spending, which mirrored the long-standing wealth and income inequalities between black and white patients (<a href="https://datatron.com/real-life-examples-of-discriminating-artificial-intelligence/">Ref</a>). Although the bias in this particular algorithm was identified and rectified, the incident points to the potential for discrimination and unfairness in AI algorithms (<a href="https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism">Ref</a>).</p></td></tr><tr><td><strong>Transparency</strong></td><td><p>Refers to the degree to which AI systems' inner workings, decision-making processes, and underlying data are open, understandable, and accessible to users, stakeholders, and the general public (Bertani-Okland, 2019; William, A, 2019 <a href="https://cdn2.hubspot.net/hubfs/4015851/Fate%20In%20AI.pdf">Ref</a>).</p><p> </p><p><strong>Example: AI decides who gets hired</strong></p><p>Many AI algorithms used in hiring processes are complex and opaque, making it difficult to understand how decisions are reached (<a href="https://www.computerworld.com/article/3691819/legislation-to-rein-in-ais-use-in-hiring-grows.html">Ref</a>). This lack of transparency raises concerns about accountability and the potential for discriminatory outcomes (<a href="https://www.theregister.com/2016/10/17/hr_sw_for_job_applicants_lacking/">Ref</a>). Candidates and even hiring managers may struggle to comprehend why an AI system made a particular decision, leading to decreased trust and increased skepticism (<a href="https://www.computerworld.com/article/3691819/legislation-to-rein-in-ais-use-in-hiring-grows.html">Ref</a>).</p></td></tr><tr><td><strong>Freedom</strong></td><td><p>Refers to the protection and preservation of individual autonomy, privacy, and agency in the face of AI systems (Jobin et al., 2019).</p><p> </p><p><strong>Example: Clearview AI</strong></p><p>Clearview AI is a controversial facial recognition technology company that has amassed a vast database of billions of facial images, scraped without consent from online platforms (<a href="https://incidentdatabase.ai/cite/267/#r1847">Ref</a>). Their technology enables constant monitoring and tracking, eroding personal freedom and privacy (<a href="https://www.makeuseof.com/what-is-clearview-ai/">Ref</a>). It allows entities like law enforcement and private companies to identify individuals without their knowledge or consent, undermining control over personal information and anonymity (<a href="https://www.nytimes.com/2020/01/18/technology/clearview-privacy-facial-recognition.html">Ref</a>). Concerns arise from potential false identifications and wrongful arrests, impacting due process and individual freedoms (<a href="https://www.makeuseof.com/what-is-clearview-ai/">Ref</a>).</p></td></tr></tbody></table>

<details>

<summary>Learn More - AI Ethical Principle Details &#x26; Challenges With Making AI More Ethical</summary>

### AI Ethical Principle Details

#### Responsibility &#x20;

* Responsibility means recognizing and accepting responsibility for the actions and consequences arising from the use of AI systems ([Ref](https://www.fatml.org/resources/principles-for-accountable-algorithms)). This involves being answerable for the decisions made, the data used, and the outcomes produced by AI technologies ([Ref](https://www.fatml.org/resources/principles-for-accountable-algorithms)).
* There is ongoing debate surrounding ethical principles in AI due to the absence of definitive guidelines, with particular emphasis on the contentious issue of assigning responsibility for the outcomes of AI (Jobin et al., 2019).
* Various stakeholders have been identified as responsible and liable for the actions and choices of AI, including AI developers, designers, institutions, and the industry (Jobin et al., 2019). Additionally, there is disagreement regarding whether AI should be held accountable in a manner resembling human accountability, or if humans should always bear the ultimate responsibility for technological artifacts (Jobin et al., 2019)

#### Fairness &#x20;

* To promote fairness in AI systems, it is crucial to address biases inherent in both the data employed for training AI systems and the systems themselves (Jobin et al., 2019).&#x20;
* By attempting to mitigate these biases, AI applications can be prevented from yielding unjust or discriminatory consequences that hinge on factors like race, gender, ethnicity, or socioeconomic status. ([Ref](https://www.fatml.org/resources/principles-for-accountable-algorithms)).&#x20;

#### Transparency &#x20;

* Transparency, in the context of AI ethics, refers to the degree to which AI systems' inner workings, decision-making processes, and underlying data are open, understandable, and accessible to users, stakeholders, and the general public (Bertani-Okland, 2019; Lutge et al., 2021; & William, A, 2019 [Ref](https://cdn2.hubspot.net/hubfs/4015851/Fate%20In%20AI.pdf)). &#x20;
  * It involves ensuring that AI systems are not overly opaque or "black-boxed," but instead promote clarity and accountability by providing explanations, justifications, and insights into how they operate, how they arrive at decisions, and how they handle and process data (Shaw, 2019; [Ref](https://sites.google.com/view/introduction-to-fate-in-ai/module/fate-awareness?authuser=0)). &#x20;
* Efforts to enhance transparency involve endeavors aimed at improving explainability, auditability, or other forms of communication and disclosure (Jobin et al., 2019) &#x20;
  * **Explainability** pertains to the assurance that decisions made by AI systems, along with the data influencing those decisions, can be clarified to end-users and other relevant parties using language that is not overly technical ([Ref](https://www.fatml.org/resources/principles-for-accountable-algorithms)). &#x20;
  * **Auditability** encompasses the provision of opportunities for external third parties to comprehensively understand, thoroughly investigate, and critically assess AI systems ([Ref](https://www.fatml.org/resources/principles-for-accountable-algorithms)). Auditability can be supported through permissive terms of use, detailed documentation, and disclosure of information that enables monitoring, checking, and criticism. ([Ref](https://www.fatml.org/resources/principles-for-accountable-algorithms)) &#x20;

#### Freedom &#x20;

* To properly safeguard freedom in the face of AI systems, it is essential to ensure that AI technologies do not unduly limit or infringe upon the fundamental rights and freedoms of individuals (Jobin et al., 2019).&#x20;
* To be free, individuals must have:&#x20;
  * Ability to make informed choices (Jobin et al., 2019).
  * Control over their personal data (Jobin et al., 2019).
  * Protection against unwarranted surveillance (Jobin et al., 2019).
  * Protection against manipulation by AI systems (Jobin et al., 2019).

### Challenges With Making AI More Ethical

By acknowledging the potential biases and ethical considerations associated with AI, we can strive to develop AI systems that are fair, accountable, and uphold ethical standards, while promoting inclusivity. However, achieving these goals can be challenging due to the **complexity of AI systems**, which often involve numerous variables that make comprehensive understanding difficult (Shaw, 2019). &#x20;

It is important to note that there is no one set of rules that have been agreed upon to guide the development and deployment of ethical AI (Borenstein et al., 2021; Shaw, 2019). **Ethical questions in AI are still subject to ongoing debates and discussions that are expected to persist for years to come** (Borenstein et al., 2021). Despite these challenges, it is essential to make continuous efforts in creating more ethical AI systems.&#x20;

</details>

## Evaluate Your Model&#x20;

### Activity Overview

#### Aim

* Evaluate the accuracy of your model&#x20;
* Consider the ethical implications of using your model in a real-life scenario&#x20;
* Think of ways to mitigate any potential harm your model could cause&#x20;

#### Instructions&#x20;

1. Split into groups (4-6 people)&#x20;
2. Assign the following roles within your group: **leader, notetaker, timekeeper,** and **presenter**&#x20;
3. Read the scenario&#x20;
4. Reflect on the accuracy of your model
5. Evaluate your model with respect to the scenario and the ethical principle (**responsibility, fairness, transparency,** or **freedom**) your teacher assigned to your group
6. Share your results with the rest of the class

## **Scenario**&#x20;

Your model has gained widespread attention due to its potential to revolutionize the **delivery industry** by significantly reducing the number of accidents caused by driver negligence or fatigue. Delivery companies across the country are eager to adopt your technology, believing it will enhance road safety and improve the efficiency of their operations.

To help you imagine this scenario, review the video below that promotes a real-life DDD system called **Driveri** which is currently being used by Amazon to monitor their delivery drivers.&#x20;

{% embed url="https://www.youtube.com/watch?v=W2F-3oq7nDI" %}

## Evaluation

### Accuracy

Reflect on the accuracy of the model you created.

* <mark style="color:purple;">Were there instances where your model made accurate predictions. Why do you think it worked? Share your responses</mark> [here](https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz\_iRQ/viewer?f=4). &#x20;
* <mark style="color:purple;">Were there instances where your model made inaccurate predictions. Why do you think it did not work? Share your responses</mark> [here](https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz\_iRQ/viewer?f=5). &#x20;

### Ethics

Consider the broader implications of putting your model on the market. Reflect on the ethical implications involved in deploying such a technology and how ethical principles can be upheld while the benefits of your innovation are maximized.

Answer the questions related to the ethical principle your group has been assigned and **be ready to share them with your class.**&#x20;

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Responsibility</strong></td><td><ol><li><mark style="color:purple;">Consider a scenario where a driver becomes heavily reliant on a DDD system and, unfortunately, encounters a false negative instance when the system fails to alert them when they doze off, resulting in an accident. Who bears responsibility for this situation?</mark></li><li><mark style="color:purple;">What unintended consequences could arise from the implementation of the system? How can these unintended consequences be identified, evaluated, and mitigated?</mark></li><li><mark style="color:purple;">What responsibilities do the developers of the system have towards ensuring its accuracy and reliability?</mark></li></ol><p>Share your responses <a href="https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz_iRQ/viewer?f=6">here.</a></p></td><td></td></tr><tr><td><strong>Fairness</strong></td><td><ol><li><mark style="color:purple;">How can you ensure that the system treats all drivers fairly and equally?</mark> </li><li><mark style="color:purple;">What are the potential risks of the system inadvertently discriminating against certain individuals or groups?</mark> </li><li><mark style="color:purple;">Are there any specific metrics or performance criteria that might inadvertently discriminate against certain drivers? How can you proactively identify and address these risks to ensure fair treatment of all drivers?</mark></li></ol><p>Share your responses <a href="https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz_iRQ/viewer?f=7">here.</a></p></td><td></td></tr><tr><td><strong>Transparency</strong></td><td><ol><li><mark style="color:purple;">How can you make the decision-making process of the model transparent to both drivers and the general public?</mark> </li><li><mark style="color:purple;">What mechanisms or explanations can be provided to ensure that the system's judgments are understandable and explainable?</mark> </li><li><mark style="color:purple;">How can you ensure transparency in how the data collected by the model is utilized? What measures can be implemented to inform drivers about the types of data being collected, how it will be used, and how long it will be retained?</mark></li></ol><p>Share your responses <a href="https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz_iRQ/viewer?f=8">here.</a></p></td><td></td></tr><tr><td><strong>Freedom</strong></td><td><ol><li><mark style="color:purple;">How can DDD systems strike a balance between ensuring road safety and preserving the freedom and autonomy of drivers?</mark> </li><li><mark style="color:purple;">Should drivers have the freedom to opt out of the system? What are the ethical considerations surrounding opt-out options, particularly in the context of safety and accountability?</mark> </li><li><mark style="color:purple;">How might constant monitoring by a distraction detection system affect drivers' well-being, job satisfaction, and sense of control? How can driver input and feedback be integrated into the system to enhance their sense of autonomy and control?</mark> </li></ol><p>Share your responses <a href="https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz_iRQ/viewer?f=9">here.</a></p></td><td></td></tr></tbody></table>

<details>

<summary>Learn More - DDD System Accuracy Issues &#x26; Potential Solutions</summary>

DDD systems encounter numerous challenges that limit their accuracy.

### Common Accuracy Issues&#x20;

DDD systems encounter accuracy challenges due to several factors. One reason is the limited variation in frame sequences for the classes of interest, such as looking forward, looking left, or looking right (Chai et al., 2023). Unlike different human activities like jumping or squatting, the variation in head movements is minimal, while other features, such as appearance and clothing, vary significantly across different drivers (Chai et al., 2023).

A lack of variation in the training classes can make predictions less accurate, especially for people of darker skin colors (Albadawi, Takruri, & Award, 2022). This is an example of overfitting, which is a concerning machine learning behaviour that can lead to discrimination as it makes the model more biased toward certain groups over others (Lopez et al., 2022).&#x20;

When a model is trained on a small range of frame sequences, it may be more susceptible to overfitting (Chai et al., 2023). Overfitting occurs when the model memorizes specific patterns or noise in the training data instead of learning the underlying generalizable features (Lopez et al., 2022). This can result in the model making biased predictions based on irrelevant or spurious correlations present in the limited data, reinforcing discriminatory biases and perpetuating unfair outcomes (Lopez et al., 2022).&#x20;

### Translating DDD Systems from Simulations to Real-Life

DDD systems are typically developed and tested in simulated environments, posing significant challenges when translating them for real-life applications (Albadawi, Takruri, & Award, 2022).&#x20;

<img src="../.gitbook/assets/driving simulator (from Ahangari et al., 2020.png" alt="Driving Simulator" data-size="original"><img src="../.gitbook/assets/distracted-driving netradyne.webp" alt="Netradyne Driver Simulator " data-size="original">

While simulated environments allow for control over intervening variables, these variables can reduce a system’s accuracy when it is put to work in the real world (Tango & Botta, 2013). Some **intervening variables** that can interfere with a system’s performance include:&#x20;

* Illumination variation (Addanki et al., 2020; Albadawi, Takuri, & Award, 2022)
* Background variation (Albadawi, Takruri, & Award, 2022)
* Movements such as swallowing, blinking, or touching one’s face ([Ref](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9482962/))&#x20;
* Features that cover the mouth or eyes such as a beard, mustache, and sunglasses (Albadawi, Takruri, & Award, 2022)&#x20;

Given the impact of these variables, recalibration of the system becomes essential when a new driver assumes control (Badgujar & Selmokar, 2023). Neglecting to recalibrate the system can introduce biases and lead to inaccurate indications of distracted driving (Badgujar & Selmokar, 2023).

### Issues with Amazon's Drivers

Concerns have been raised regarding **privacy**, with drivers describing the cameras as **intrusive** and akin to a **punishment** system ([Ref](https://www.cnbc.com/2021/02/03/amazon-using-ai-equipped-cameras-in-delivery-vans.html)).

The use of AI monitoring raises accuracy and fairness concerns, as AI struggles to comprehend human behavior nuances and anomalies, potentially leading to errors in **judgment** ([Ref](https://www.cnbc.com/2021/02/03/amazon-using-ai-equipped-cameras-in-delivery-vans.html)).

Furthermore, the refined AI capabilities may exert increasing pressure on drivers to conform their behavior, movements, and appearance to satisfy the demands of the **surveillance** AI system ([Ref](https://www.aclu.org/news/privacy-technology/amazon-drivers-placed-under-robot-surveillance-microscope)). For instance, if caught yawning, drivers are instructed to pull over for a minimum of 15 minutes, with non-compliance possibly resulting in a call from their supervisor ([Ref](https://www.cnbc.com/2021/02/03/amazon-using-ai-equipped-cameras-in-delivery-vans.html)).&#x20;

### Potential Solutions&#x20;

To address some of these challenges, it is essential to collect more diverse data (Sharara et al., 2023). If the training data does not adequately represent the diversity of real-world driving scenarios and driver behaviors, the model may struggle to make accurate predictions for underrepresented groups or specific situations (Misra et al., 2022; Sharara et al., 2023). If the training data predominantly consists of drivers of a specific gender, age group, or ethnicity, the model may not generalize well to diverse populations and exhibit biased predictions (Babusi, 2020). This can lead to discriminatory outcomes, where certain groups are unfairly targeted or disadvantaged (Babusi, 2020).\[KI1] \[KI2]&#x20;

&#x20;

However, it is important to note, that the training phase machine learning systems undergo cannot encompass all possible real-world examples (Bossman, 2016). These systems can be vulnerable to deception in ways that humans wouldn't be (Bossman, 2016). To ensure the desired performance and prevent misuse, it is crucial to carefully monitor and safeguard AI systems as they become integral to various aspects of our lives, such as labor, security, and efficiency (Bossman, 2016).

</details>

## Improve your model&#x20;

There are several approaches researchers are taking to mitigate or minimize bias in AI systems, such as: &#x20;

* Ensuring a balance in the training data employed to develop AI models ([Ref;](https://docs.google.com/document/d/1i\_\_XQcSVF1BfHCFWRZ3GkLaqWde0RVxyz2o85xBMMJw/edit) Albadawi, Takruri, & Award, 2022; Liu et al., 2016) &#x20;
* establishing open datasets ([Ref;](https://docs.google.com/document/d/1i\_\_XQcSVF1BfHCFWRZ3GkLaqWde0RVxyz2o85xBMMJw/edit) Sharara et al., 2023)&#x20;

Think about how you can minimize bias and improve your model. Share your ideas [here](https://jamboard.google.com/d/1hl8j9C71M-c26si500VDR7DIiD7zUTTF6JQb1cz\_iRQ/viewer?f=10). &#x20;
