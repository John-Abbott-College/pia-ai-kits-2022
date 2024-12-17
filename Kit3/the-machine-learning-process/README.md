# The Machine Learning Process

## Overview <a href="#toc760213027" id="toc760213027"></a>

### Part 1: Hardware & Code Setup

1. Setup the microphone on the Raspberry Pi (Pi)
2. Create an Edge Impulse Account
3. &#x20;Install the Edge Impulse CLI tools and SDK on the Pi
4. Downloading the project’s repository from GitHub

### Part 2: Data Collection, Training & Testing

1. Data collection
2. Split the data for training and testing &#x20;
3. Training inputs & data features &#x20;
4. Data clean-up &#x20;
5. Model design & training &#x20;
6. Evaluating the trained performance &#x20;
7. Testing the model

### Part 3: Tweaking & Deploying

1. Model optimization &#x20;
2. Deploying the model&#x20;
3. Use the model to control other hardware



## Updating Your Software

If you are unsure if your Pi is up to date and has all the required software, run the following commands:

1.  **Upgrade Raspberry Pi OS and the installed packages**

    ```sh
    sudo apt update -y
    sudo apt full-upgrade -y
    sudo apt install raspberrypi-kernel-headers -y
    sudo reboot
    ```
2. **Install git**

```bash
sudo apt install git -y
```

#### 3. If you are using the reTerminal from Seeed Studios, make sure all your driver's are installed

```bash
git clone --depth 1 https://github.com/Seeed-Studio/seeed-linux-dtoverlays
cd seeed-linux-dtoverlays
sudo ./scripts/reTerminal.sh
sudo reboot
```

