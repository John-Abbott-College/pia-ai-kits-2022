# Intro

## Welcome to another activity on ethical Machine Learning (ML)!&#x20;

In this activity you will train an audio classification machine learning model. The model will be trained on sound samples to detect whether a room is occupied or empty. This model has the potential to be used to lower energy consumption in buildings by turning off electrical devices and reducing heating when a room is unoccupied. The model will be trained in the [Edge Impulse](https://www.edgeimpulse.com/) platform and deployed to a Raspberry Pi computer.

## Learning Objectives

By completing this activity, you will be able to:

1. Apply steps of a typical machine learning workflow
2. Make a Raspberry Pi equipped with a microphone collect audio samples
3. Use an online AI service to train, validate, optimize and deploy a machine learning model that classifies a room as occupied or empty
4. Identify issues related to room occupancy monitors
5. Evaluate the implications of a room occupancy monitoring system based on the principles of ethical AI

## Requirements <a href="#toc141203020" id="toc141203020"></a>

To complete this activity, the following is required:

### Equipment & Software

* A Raspberry Pi Model 4 or above (referred to as Pi) with a 64-bit image and up to date software.
* A microphone compatible with a Raspberry Pi such as the [reSpeaker 2 mic hat](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT.html?queryID=e215cf26fedd60071817a0f39326f0ed\&objectID=306\&indexName=bazaar_retailer_products).
* Installed software:
  * git
  * python3.9 or above
  * Pip

### Prerequisite Knowledge

* Familiarity operating a Raspberry Pi such as:
  * Connecting to the internet
  * SSH login
  * Installing software using the command line
  * Creating and saving a program file
  * Cloning repositories from GitHub
* Familiarity with Python:
  * Creating, saving and running a python script
  * Installing and using Python packages with pip

## Navigation <a href="#toc141203021" id="toc141203021"></a>

Special notation has been used to make it easier to navigate through each page.

<table data-header-hidden><thead><tr><th width="199"></th><th></th></tr></thead><tbody><tr><td>Learn More</td><td><p><strong>Learn More</strong> sections, which can be found in blue boxes throughout the activity information, contain more in-depth explanations and additional information about the concepts and topics presented in the activity.</p><p> </p><p>PLEASE NOTE: <strong>It is not necessary to read this information</strong>, all activities can be completed without the <strong>Learn Mor</strong>e content. However, it is highly recommended to read the content, especially if you are unfamiliar with the concepts presented.</p></td></tr><tr><td>Key Info</td><td>Content highlighted in <mark style="color:red;">red</mark> represent crucial information and should be given your full attention.</td></tr><tr><td>Reflection Questions</td><td>Questions highlighted in <mark style="color:purple;">purple</mark> are meant to give you a chance to reflect and consider the implications of the information presented.</td></tr></tbody></table>
