# Image Classification with EDGE IMPULSE (Duckie, cherry or tomato? )
In day one we will assemble our material and run a small test on the microcontroller. Afterwards, you will start gathering a dataset of Duckies, cherries and tomatoes and then we will go to edge impulse to create am image classifier and deploy it in your microcontroller.

## Your Microcontroller
We are working with [XIAO-ESP32-S3 Sense from Seed Studio](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)

in order to test it we will do the following:

first we need to install the libraries of the microcontroller. Make sure that you install the version 2.0.14 from Espressif Systems.

### Installing the library

- Open Arduino IDE
- Navigate to "File" > "Preferences", and add to "Additional Boards Manager URLs" this url: https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
- Open the "Boards manager": "Board" Symbol on the left side of the screen OR "Tools" > "Board" > "Boards Manager..."
- Search for "esp32" by Espressif Systems. Install the ESP board - **!Important!** version 2.0.14
- Plugin your MCU, and select in the Arduino IDE the right COM port and the right board-type ("XIAO ESP32S3")

### Testing the Microcontroller with the blink example
- Go to File -> Examples -> Basic -> Blink
- Connect your microcontroller
- Upload the code. The built-in LED should start blinking.

## Gathering data
We will use the camera server to gather the samples for our model. 
For this
- "File" > "Examples" > "esp32" > "camera" > "camera webserver"
    - modify the code for the right board (comment and uncomment defines)
    - ssid: given in workshop
    - pass: given in workshop
    - upload
    - open serial monitor
    - copy IP address
- With your code/text editor open get_images.py and update the IP address
- Open a terminal and navigate to the folder with the .toml file
- Check if you can run rye (type rye)
    - if not source "$HOME/.rye/env"
- make sure your PC/Laptop is connected to the same network as mentioned above
- run the camera server:
    -type rye run get_images
- By typing a digit you will save the corresponding image on the root folder under ./data/raw/ in a separate folder
- We recommend taking at least 70 images per object. 

## Training and Deploying the Classifier in Edge Impulse
First you need to log-in in [Edge Impulse Studio](https://studio.edgeimpulse.com/login) and create a new project. (You are limited to 2 private projects in the free version)

- Create your Model as explained in the Hands-On
- Deploy your Model

## Running inferences

### After deploying the model

- Add the zip library to Arduino
- Modify the features[] from static_buffer example

### Remember to activate the psram option

### Update the pins of the Microcontroller for the inference example
```
#define PWDN_GPIO_NUM     -1
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM     10
#define SIOD_GPIO_NUM     40
#define SIOC_GPIO_NUM     39


#define Y9_GPIO_NUM       48
#define Y8_GPIO_NUM       11
#define Y7_GPIO_NUM       12
#define Y6_GPIO_NUM       14
#define Y5_GPIO_NUM       16
#define Y4_GPIO_NUM       18
#define Y3_GPIO_NUM       17
#define Y2_GPIO_NUM       15
#define VSYNC_GPIO_NUM    38
#define HREF_GPIO_NUM     47
#define PCLK_GPIO_NUM     13



```

Project buzilt with Rye
