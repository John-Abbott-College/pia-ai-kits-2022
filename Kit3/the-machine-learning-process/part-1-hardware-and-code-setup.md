# Part 1: Hardware & Code Setup

```
// Some code
```

## Setup the microphone on the Raspberry Pi (Pi).

<table data-header-hidden><thead><tr><th width="134"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 15 minutes to complete the steps.</td></tr><tr><td><p></p><p><strong>Do</strong></p></td><td><p></p><p>If the audio recording fails after step 2, then help students troubleshoot by completing the following steps:</p><p></p><ol><li><strong>Check the sound card playback number</strong> (as seen by the operating system) for <code>seeed2micvoicec</code> with the command <code>aplay -l</code>:</li></ol><p>              a. Run in your command line:</p><p>              b. (In this case, the playback audio device number is 0, taken from the line <code>card 0: seeed2micvoicec</code>)</p><pre class="language-bash" data-overflow="wrap"><code class="lang-bash">aplay –l

**** List of PLAYBACK Hardware Devices ****
card 0: seeed2micvoicec [seeed2micvoicec], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 [bcm2835-i2s-wm8960-hifi wm8960-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

</code></pre><ol start="2"><li><strong>Check the sound card capture number</strong> (as seen by the operating system) for <code>seeed2micvoicec</code> with the command <code>arecord -l</code>. </li></ol><p>              a. Run in your command line:</p><p>              b. (In this case, the capture audio device number is 0, according to the line <code>card 0: seeed2micvoicec</code>)</p><pre class="language-bash" data-overflow="wrap"><code class="lang-bash">bashCopy codearecord -l

**** List of CAPTURE Hardware Devices ****
card 0: seeed2micvoicec [seeed2micvoicec], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 [bcm2835-i2s-wm8960-hifi wm8960-hifi-0]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
</code></pre><ol start="3"><li><strong>Test that you can record audio</strong> with the CLI command below. </li></ol><p>            a. Replace the 0 in <code>plughw:0,0</code> with your capture device number from step 2.</p><p>            b. The audio file name you generated should be <code>test.wav</code>.</p><pre class="language-bash" data-overflow="wrap"><code class="lang-bash">arecord -D "plughw:0,0" -f S16_LE -r 16000 -d 5 -t wav test.wav
</code></pre><ol start="4"><li><strong>Test that you can play audio</strong> with the CLI command below.</li></ol><p>             a. Replace the 0 in <code>plughw:0,0</code> with your capture device number from step 3. </p><p>              b. To listen to the audio, connect headphones to the ReSpeaker.</p><pre class="language-bash"><code class="lang-bash">aplay -D "plughw:0,0" test.wav
</code></pre><p></p></td></tr></tbody></table>

#### &#x20;

## Create an Edge Impulse Account

<table data-header-hidden><thead><tr><th width="140"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 10 minutes to complete the steps.</td></tr></tbody></table>

&#x20;

## **Install the Edge Impulse CLI tools and SDK on the Pi.**

<table data-header-hidden><thead><tr><th width="148"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 10 minutes to complete the steps.</td></tr></tbody></table>

&#x20;

## **Downloading the project’s repository from GitHub.**

<table data-header-hidden><thead><tr><th width="152"></th><th></th></tr></thead><tbody><tr><td><strong>Ask</strong></td><td>Students to complete the steps listed in the student guide with their partner.</td></tr><tr><td><strong>Do</strong></td><td>Give students 5 minutes to complete the steps.</td></tr></tbody></table>
