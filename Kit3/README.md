# Teaching Guide for Intro to Energy Preservation Using ML: Monitoring Room Occupancy

## Purpose

This document serves as a teaching guide for Kit 3's activity, [Intro to Energy Preservation using ML: Monitoring Room Occupancy](https://app.gitbook.com/o/Cg0gqSeueeUG6DMlpHqI/s/MLbHwJQX5E1Pb36YbQUv/).

In this activity, you will embark on a journey to train an audio classification machine learning model. The goal is to train the model on sound samples to discern whether a room is occupied or vacant, paving the way to potentially lowering energy consumption in buildings by switching off electrical appliances and reducing heating during unoccupied times. The training will occur on the Edge Impulse platform, and deployment will be on a Raspberry Pi computer.

## Room Occupancy Monitors

Exploring ways to enhance energy efficiency in buildings leads us to room occupancy monitoring via ML\[[1](https://www.sciencedirect.com/science/article/pii/S2666546822000441)]\[[2](https://www.frontiersin.org/articles/10.3389/fenrg.2023.1071291/full)]. By understanding occupancy patterns, ML could serve as a precise tool to determine room occupancy\[[1](https://www.sciencedirect.com/science/article/pii/S2666546822000441)]\[[3](https://www.researchgate.net/publication/362644322_Machine_Learning_Deep_Learning_and_Statistical_Analysis_for_forecasting_building_energy_consumption_-A_systematic_review)]. The indoor conditions of a building can then be adjusted based on the predictions from the ML model\[[1](https://www.sciencedirect.com/science/article/pii/S2666546822000441)]\[[4](https://www.sciencedirect.com/science/article/abs/pii/S0378778821007623)]\[[5](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)]. For instance, lights can be turned off when a room is predicted to be vacant\[[4](https://www.sciencedirect.com/science/article/abs/pii/S0378778821007623)]\[[5](https://www.sciencedirect.com/science/article/abs/pii/S1364032121002616)]. Educational buildings stand as prime candidates for this technology given their substantial energy requirements\[[6](https://ieeexplore.ieee.org/document/9377027)]. Utilizing ML-powered room occupancy monitors could significantly trim down energy consumption in educational establishments\[[6](https://ieeexplore.ieee.org/document/9377027)]\[[3](https://www.researchgate.net/publication/362644322_Machine_Learning_Deep_Learning_and_Statistical_Analysis_for_forecasting_building_energy_consumption_-A_systematic_review)].

## Target Audience

The design of this activity aligns with the curriculum of CEGEP students in their third year of a computer science program.

## Requirements

### Equipment & Software

* A Raspberry Pi Model 4 or higher (referred to as Pi) with a 64-bit image and updated software.
* A Raspberry Pi-compatible microphone like the [reSpeaker 2 mic hat](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT.html?queryID=e215cf26fedd60071817a0f39326f0ed\&objectID=306\&indexName=bazaar_retailer_products).
* Necessary software installations include:
  * git
  * python3.9 or newer
  * Pip

### Prerequisite Knowledge

* Operative knowledge of a Raspberry Pi like:
  * Internet connectivity
  * SSH login
  * Command line software installation
  * Program file creation and saving
  * GitHub repository cloning
* Familiarity with Python:
  * Creating, saving, and executing a python script
  * Python package installation and utilization with pip

## Learning Objectives

Upon completion of this activity, students will have the skills to:

1. Navigate through the typical machine learning workflow steps
2. Equip a Raspberry Pi with a microphone to collect audio samples
3. Utilize an online AI service for training, validating, optimizing, and deploying a machine learning model to classify room occupancy status
4. Identify challenges tied to room occupancy monitors
5. Evaluate the implications of a room occupancy monitoring system from an ethical AI standpoint

## Activity Breakdown

This activity encompasses detailed, step-by-step guidelines to construct a basic room occupancy monitor. It underscores the importance of ethical AI development throughout the activity. Similar to this guide, the student version is available on Gitbook and in MS Word format.

For a snapshot of the activity, refer to the tutorial [Recognize sounds from audio](https://docs.edgeimpulse.com/docs/tutorials/audio-classification) or watch the video: [Building an Audio Classifier with Embedded Machine Learning ](https://www.youtube.com/watch?v=ckD3InrSXo0)(24:38)

<table data-full-width="true"><thead><tr><th width="154"></th><th width="182.5">Section</th><th width="353">Description / Objectives</th><th>Length</th></tr></thead><tbody><tr><td><strong>Introduction</strong></td><td>Intro to Kit:</td><td><p>Introduces learners to:</p><ul><li>Activity’s purpose</li><li>Learning objectives</li><li>Prerequisite skills and hardware components needed</li><li>Tips for navigating through the activity</li></ul></td><td>5 mins</td></tr><tr><td></td><td>Neural networks and basic neuron architectures</td><td>Introduces learners to ML concepts related to the activity</td><td>10 mins</td></tr><tr><td></td><td>Common steps involved in training a neural network</td><td>Further exploration of ML concepts pertinent to the activity</td><td>5 mins</td></tr><tr><td><strong>ML in Energy</strong></td><td>Issues in the Energy Sector</td><td>Highlighting issues in the energy sector</td><td>3 mins</td></tr><tr><td></td><td>Using ML to Improve the Energy Sector</td><td>Introducing learners to the potential of ML in improving the energy sector</td><td>3 mins</td></tr><tr><td></td><td>Challenges with Integrating ML in Energy : Privacy</td><td>Exploring privacy issues tied to ML usage in the energy sector with a focus on smart homes</td><td>10 mins</td></tr><tr><td></td><td>Challenges with Integrating ML in Energy : Sustainability</td><td>Introduces learners to the sustainability issues related to using ML in the energy sector and ML’s carbon footprint</td><td>15 mins</td></tr><tr><td><strong>ML in Energy Application: Room Occupancy Monitors</strong></td><td>[Intro Content]</td><td>Introduces learners to room occupancy monitors as an application of ML in Energy</td><td>3 mins</td></tr><tr><td></td><td>Identifying Occupancy: Think-Pair-Share</td><td>Engaging learners in identifying methods to ascertain room occupancy</td><td>30 mins</td></tr><tr><td><strong>The Machine Learning Process</strong></td><td>Part 1: Hardware &#x26; Code Setup</td><td>Guiding learners through software installation and device configuration for audio recording</td><td>45 mins</td></tr><tr><td></td><td>Part 2: Data Collection, Training &#x26; Testing</td><td>Audio sample collection, discarding invalid samples, training a new model, and testing model performance against known data</td><td>90 mins</td></tr><tr><td></td><td>Part 3: Tweaking &#x26; Deploying</td><td>Model tweaking and improvement, re-evaluating model performance, and deploying it on the device</td><td>90 mins</td></tr><tr><td><strong>Evaluating the Ethics of ML</strong></td><td>Accuracy</td><td>Introduces learners to the importance of accuracy in ML</td><td>5 mins</td></tr><tr><td></td><td>Accuracy vs. Sustainability</td><td>Presents learners with the potential tradeoffs between accuracy and sustainability in ML</td><td>5 mins</td></tr><tr><td></td><td>Accuracy vs. Privacy</td><td>Presents learners with the potential tradeoffs between accuracy and privacy in ML</td><td>5 mins</td></tr><tr><td></td><td>Ethical Principles</td><td>Describes accuracy, privacy, and sustainability as principles of creating ethical AI</td><td>3 mins</td></tr><tr><td></td><td>Balancing Accuracy, Privacy, and Sustainability</td><td>Engaging learners in a group exercise to balance accuracy, privacy, and sustainability in a room occupancy monitor within a realistic scenario</td><td>45 mins</td></tr></tbody></table>

## Teacher Guide Navigation

It's highly recommended for teachers to go through the activity at least once to familiarize with the content before guiding students. The teaching notes follow a _do_, _say_, and _ask_ format:

* **Do**: Actions for the teacher.
* **Ask**: Questions for students.
* **Say**: Content to be presented by the teacher to students.
  * Some prompts include content from the 'learn more' sections of the student guide, which are optional reading for students, providing additional material for further clarification when needed.
