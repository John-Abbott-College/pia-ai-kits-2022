# Teaching Guide for Intro to Recommender systems: Ethical Consumer Choices

### Purpose <a href="#toc1563877551" id="toc1563877551"></a>

This document is meant to act as a teaching guide for kit 2’s activity _Intro to Recommender systems: Ethical Consumer Choices_ (follow the link to access the student version of the activity).

In this activity students will clean and manipulate data to generate three types of product recommendations. Students will generate popular-based recommendations by writing SQL (Structured Query Language) queries on SSMS (SQL Server Management Studio). Students will also generate Content-based and Collaborate filtering recommendations using pandas, numpy, sklearn, and surprise libraries on a Kaggle notebook.

### Target Audience <a href="#toc213657394" id="toc213657394"></a>

The activity has been designed for CEGEP students who are in their second year of a computer science program.

### Prerequisite skills & hardware components required <a href="#toc143897835" id="toc143897835"></a>

To complete this activity, the following is required:

**Equipment & Software**

* [Kaggle Account](https://www.kaggle.com/account/login?phase=startRegisterTab\&returnUrl=%2F)

**Prerequisite Knowledge**

* Intermediate SQL knowledge

### Learning objectives <a href="#toc143897836" id="toc143897836"></a>

By completing this activity, students will be able to:

1. Describe the different types of recommender systems
2. Generate a product recommender system
3. Identify issues related to recommender systems
4. Evaluate the implications of a recommender system based on the principles of ethical AI

### Activity Breakdown <a href="#toc874405034" id="toc874405034"></a>

This activity includes comprehensive, step-by-step instructions for constructing a simple recommender system. Throughout the activity, students are reminded about the importance of developing AI in an ethical manner. Like this guide, the student version of the activity is available on gitbook as well as in MS Word format.



<table data-header-hidden data-full-width="true"><thead><tr><th width="183"></th><th width="194"></th><th width="455"></th><th></th></tr></thead><tbody><tr><td><strong>Section</strong></td><td><strong>Sub-Section</strong></td><td><strong>Description / Objectives</strong></td><td><strong>Length</strong></td></tr><tr><td>What are Recommender Systems?</td><td></td><td>Introduces learners to the concept of a recommender system, engages students in reflection and discussion on what recommendations systems are and how they might have interacted with them</td><td>20 mins.</td></tr><tr><td>How are Recommender Systems Used?</td><td></td><td>Introduces learners to the main areas in which recommender systems are used and examples of companies in these areas that use them</td><td>5 mins.</td></tr><tr><td>Types of Recommender Systems</td><td><ol><li>Popular-based<br></li></ol></td><td>Defines popular-based recommender system, provides an example of this type of recommender system, and discusses its advantages and disadvantages</td><td>5 mins.</td></tr><tr><td></td><td><ol start="2"><li>Content-based</li></ol></td><td>Defines content-based recommender system, provides an example of this type of recommender system, and discusses its advantages and disadvantages</td><td>5 mins.</td></tr><tr><td></td><td><ol start="3"><li>Collaborative filtering</li></ol></td><td>Defines collaborative filtering recommender system, breaking this category down into its two main types – memory-based and model-based – presenting examples, advantages, and disadvantages for both types</td><td>10 mins.</td></tr><tr><td></td><td><ol start="4"><li>Hybrid</li></ol></td><td>Defines hybrid-based recommender system and discusses the advantages and disadvantages of this approach</td><td>3 mins.</td></tr><tr><td>Building a Recommender System</td><td>Data</td><td>Presents the dataset students will use to build their recommender system, describing its main components and defining terms used in the dataset</td><td>5 mins.</td></tr><tr><td></td><td>Part 1 – Popular-based recommendations</td><td>Creates Popular based recommendations using SQL.</td><td></td></tr><tr><td></td><td>Part 2 – Content-based and Collaborative filtering recommendations on notebook</td><td>Creates Content-based and collaborative filtering recommendations using using pandas, numpy, sklearn, and surprise libraries on a Kaggle notebook.</td><td></td></tr><tr><td>Issues with Recommender Systems</td><td></td><td>Introduces learners to the issues related to recommender systems, provides a description and example of each major issue</td><td>10 mins.</td></tr><tr><td>The Ethics of Recommender Systems</td><td>Principles for Creating Ethical AI</td><td>Describes principles for creating ethical AI and challenges related to using recommender systems for the promotion of ethical consumption</td><td>15 mins.</td></tr><tr><td></td><td>Groupwork: Balancing Animal Rights and Traditional Practices in Recommender Systems</td><td>Learners engage in a group exercise in which they must improve a fictional recommender system, taking into account the needs of the system’s diverse stakeholders</td><td>45 mins.</td></tr></tbody></table>

### Teacher Guide Navigation <a href="#toc1604080072" id="toc1604080072"></a>

It is highly recommended to complete the activity at least once to be familiar with the content before attempting to guide students through it. There are a few sections with special preparation notes. This must be read and completed before teaching the section. In cases where there are no specific preparation notes provided, simply reviewing the section’s material before teaching is sufficient.



The teaching notes are organized in a _do, say, and ask_ format.

* _Do_ prompts include actions for the teacher to do themself.
* _Ask_ prompts include questions that the teacher needs to ask students.
* _Say_ prompts include content that is meant to be presented by the teacher to students.
  * In some of these prompts, content from the learn more sections of the student guide, which is optional for students to read, have been included. Some of these prompts include additional material sourced from the learn more sections of the student guide, which is optional for students to read. This inclusion serves to offer supplementary content for teachers to reference and discuss when students require further clarification.
