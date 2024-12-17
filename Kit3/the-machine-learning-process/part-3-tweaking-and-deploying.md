# Part 3: Tweaking & Deploying

## **Model optimization**

<table data-header-hidden><thead><tr><th width="162"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 20 minutes to complete the steps.</td></tr></tbody></table>

&#x20;

## **Deploying the model**

<table data-header-hidden><thead><tr><th width="165"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 30 minutes to complete the steps.</td></tr></tbody></table>

&#x20;

## **Use the model to control other hardware**

<table data-header-hidden><thead><tr><th width="164"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 40 minutes to complete the steps.</td></tr><tr><td><strong>Do</strong></td><td><p>[If students are unable to create the Python script from scratch, then give them the following starter code] </p><pre class="language-python" data-overflow="wrap"><code class="lang-python">pythonCopy codefrom gpiozero import LED
import time

SLEEP_TIME = 0.5  # in seconds

class Room:

    def __init__(self):
        self._led = LED(22)
        # add other actuators here
        
        print("Room initialized")
        
    def on(self):
        self._led.on()
        # turn on other actuators here
        
    def off(self):
        self._led.on()
        # turn off other actuators here

def main():

    # Change main to save energy if the room is empty

    room = Room()
    room.on()
    
    while True:
        sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()
</code></pre></td></tr></tbody></table>

&#x20;
