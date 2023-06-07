# Part 3: Control Buzzer from Browser

## Overview

1. [Revise Sketch](part-3-control-buzzer-from-browser.md#revise-sketch)&#x20;
2. [IDE Setup](part-3-control-buzzer-from-browser.md#ide-setup-instructions)&#x20;
3. [Circuit Setup Instructions](part-3-control-buzzer-from-browser.md#circuit-setup-instructions) &#x20;
4. [Sketch Setup Instructions](part-3-control-buzzer-from-browser.md#sketch-setup-instructions)&#x20;

## Revise Sketch&#x20;

### Step 1

Add code in the `gotResults(err, results)` function so that the data variable is set to a different value depending on the label of the result.&#x20;

Example: If classification is open, set it to `1`. If classification is closed, set it to `2`… &#x20;

{% hint style="info" %}
These values will be read from the microcontroller in the next step and perform some action.
{% endhint %}

### Step 2

Send the data out the serial port by calling `writeToStream` function and passing `data` as an argument. &#x20;

{% hint style="info" %}
To debug your code and see what is being printed on the console, select the arrow at the bottom right corner as shown below. Print the data value on the console for debugging using `console.log(data);`&#x20;
{% endhint %}

<figure><img src="../.gitbook/assets/Step 3 - pic 1.png" alt=""><figcaption></figcaption></figure>

<div data-full-width="true">

<figure><img src="../.gitbook/assets/line.png" alt=""><figcaption></figcaption></figure>

</div>

## IDE Setup Instructions&#x20;

### Step 1

Download and install the latest version of the Arduino IDE at this[ ](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE)[link](https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE). &#x20;

### Step 2

Go to Tools > Boards > Board Manager in the IDE &#x20;

Type "pico" in the search box and select the Arduino Mbed OS RP2040 Boards by Arduino and install it. &#x20;

<figure><img src="../.gitbook/assets/Step 3 - IDE Setup.png" alt=""><figcaption></figcaption></figure>

### Step 3

Go to Tools > Board > Arduino Mbed OS RP2040 Boards > Raspberry Pi Pico. &#x20;

### Step 4

Connect the micro-USB cable to the Pico and then plug the USB cable into the computer. &#x20;

### Step 5

Go to Tools > Port > Select Port &#x20;

<div data-full-width="true">

<figure><img src="../.gitbook/assets/line.png" alt=""><figcaption></figcaption></figure>

</div>

## Circuit Setup Instructions&#x20;

### Step 1

Place the microcontroller on a breadboard. &#x20;

### Step 2

Connect the + leg of the buzzer to GP5 pin and its negative leg to the ground (8th pin right under GP5 pin). &#x20;

<figure><img src="../.gitbook/assets/pinout.png" alt=""><figcaption></figcaption></figure>

### Step 3

To validate that your circuit is working, open the Arduino IDE. &#x20;

### Step 4

Create a new Sketch and add the below code to it.   &#x20;

```
const int buzzer = 5;
 
void setup() {  
  pinMode(buzzer, OUTPUT);  
}  
void loop() {  
  // put your main code here, to run repeatedly:  
  digitalWrite(buzzer, HIGH);  
  delay(1000); // Wait for 1000 millisecond(s)  
  digitalWrite(buzzer, LOW);  
  delay(1000); // Wait for 1000 millisecond(s)  
}  
```

### Step 6

Go to Tools > Board > Arduino Mbed OS RP2040 Boards > Raspberry Pi Pico. &#x20;

### Step 7

Go to Tools > Port > Select Port &#x20;

### Step 8

Upload the code, if the buzzer is beeping your connections are valid. &#x20;

<div data-full-width="true">

<figure><img src="../.gitbook/assets/line.png" alt=""><figcaption></figcaption></figure>

</div>

## Sketch Setup Instructions&#x20;

In these steps, you will modify the code to make the microcontroller read prediction values, sent by the sketch running on the browser, from the serial port and turn on the buzzer to alert the driver. &#x20;

### Step 1

In `setup()`, start a serial monitor at a data rate of `9600` bits per second by adding this line of code `Serial.begin(9600);` &#x20;

### Step 2

In `Loop()`, Check if the number of bytes available for reading from the serial port is greater than zero by calling method `Serial.available()`. &#x20;

### Step 3

If there are bytes, read the data by calling `Serial.parseInt()` and place it in an integer variable. &#x20;

### Step 4

Based on the read value, turn ON or OFF the buzzer. &#x20;

### Step 5

Test if your sketch is working by using the Serial Monitor of the Arduino IDE. Send the expected integer to your device and see if it reacts.&#x20;

Go to Tools > Serial Monitor

