# Part 3: Tweaking & Deploying

## A.   Model Optimization <a href="#toc1027834767" id="toc1027834767"></a>

Let’s improve the model by fine-tuning it with the _**EON Tuner**_ feature of Edge Impulse.

The EON Tuner will run several variations of your model in parallel with slightly different parameters. You can then see if any of these variations perform better than the current model.

First, we need to specify a few details about our project.

1. Select the _**EON Tuner**_ page and select the _Target_ parameters on the top-right of the screen.
   1. On the EON Tunner settings page, under _**Dataset category**_, select _**Continuous audio**_.
   2. Make sure _**Target device**_ is set to _**Raspberry Pi 4**_.
   3. Select _**save**_.
   4. Select _**Start EON tuner**_.  &#x20;

You will see multiple models being trained in parallel. <mark style="color:yellow;">This will take several minutes to finish</mark>. You can change pages and come back later ⏱

<figure><img src="../.gitbook/assets/Screenshot 2023-11-04 220750.png" alt=""><figcaption></figcaption></figure>

2. Once the EON Tuner is done, you can inspect the performance of several optimized models.
   * Check the following:
     1. Overall accuracy (top left)
     2. Confusion matrix.
     3. See the Classification section for the overall neural network&#x20;
3. Pick a new optimized model and write down the optimized model’s confusion matrix in the table below:

| _**Optimized training results**_ | Overall accuracy: |       |
| -------------------------------- | ----------------- | ----- |
|                                  | Activity          | Empty |
| Activity                         |                   |       |
| Empty                            |                   |       |

* Click _**Select**_ to replace the current model with the optimized EON model.
  * Confirm that you want to update the primary model.

<figure><img src="../.gitbook/assets/Picture29.svg" alt=""><figcaption></figcaption></figure>

4. We must test the optimized model’s performance against unseen data.
5. Repeat the steps in _**Part 2: Testing the Model**_ _._
   1. Go to the _**Model testing**_ page and select _**Classify all**_**.** This will run your model against the full testing dataset and display it’s performance.
   2. As usual, the testing accuracy is expected to be lower than the training accuracy. &#x20;

<figure><img src="../.gitbook/assets/Screenshot 2023-11-04 221247.png" alt=""><figcaption></figcaption></figure>

6. Write down the model's confusion matrix in the table below:

| _**Optimized testing results**_ | Overall accuracy: |       |
| ------------------------------- | ----------------- | ----- |
|                                 | Activity          | Empty |
| Activity                        |                   |       |
| Empty                           |                   |       |

&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2023-11-04 221325.png" alt=""><figcaption></figcaption></figure>

## B.   Deploying the Model <a href="#deploying_the_model" id="deploying_the_model"></a>

There are two options to deploy the model you just created:

* Build and download for a specific CPU architecture (Linux ARMv7 in the case of the RPi)
* Download the model directly using the Edge Impulse CLI.

We’ll use the second method since it saves a few steps.

7. In your Raspberry Pi, return to the directory `room-occupancy-audio` of the project repository that you cloned in Part 1, step D.
8. Use the Edge Impulse CLI to download the model and start generating predictions (inferences) in real time:
   1. This command will build and download an executable version of the model. It might take a few minutes.
   2.  Select the `seeed-2mic-voicecard` as the microphone and observe the inferences in real time.

       ```bash
        edge-impulse-linux-runner --download modelfile.eim
       ```
9.  Run the model using Python. Now that the model has been downloaded to your machine, run the model using the Edge Impulse Python SDK.

    1. Run `run-inference.py` with the path to the downloaded model and the _**index of the**_ `seeed-2mic-voicecard`_**.**_

    <pre class="language-bash"><code class="lang-bash"><strong> python run-inference.py modelfile.eim 0
    </strong></code></pre>

## C.   Use the model to control other hardware <a href="#use_the_model" id="use_the_model"></a>

You’ve learned how to run the model and generate an inference (prediction) using Python. In this section you will create a new script based on `run-inference.py` to control a hardware actuator (eg.: led, buzzer, relay switch, servo, etc.).

The objective of our model is to accurately turn off lights and lower heating when there is no one in the room. Let’s create a prototype that initially has an LED on and/or a running fan controlled via a relay. The LED and/or the fan will be on as long as the model is detecting the presence of someone in the room. Once the model detects that the room is empty, it will turn the actuators off.

10. Connect the actuator to the Raspberry Pi.
    1. Connect an LED to GPIO22
    2. Alternatively, if you are using a reTerminal, you can use the [onboard LED](https://github.com/Seeed-Studio/Seeed_Python_ReTerminal/blob/main/samples/test_led.py)s.
11. Create a Python script that keeps the actuator on indefinitely (as long as the script isrunning).
12. Modify the script you created by using the code in `run-inference.py` so that the room is “off” if the model detects that the room is empty.
