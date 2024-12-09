# esp32s3_object_detection

## Arduino

- Boards manager
- esp32 by Espressif Systems. Important! version 2.0.14
- examples-> esp32 -> camera -> cameraserver
    - modify the code for the right board
    - ssid: iotlab-mobile
    - pass: iotlab18
    - upload
    - open serial monitor
    - copy IP address
- Go to src/get_images.py and update the IP address
- Open a terminal and navigate to the folder with the .toml file
- Check if you can run rye (type rye)
    - if not source "$HOME/.rye/env"
- run the camera server:
    -type rye run get_images

## After deploying the model

- Add the zip library to Arduino
- Modify the features[] from static_buffer example

## Remember to activaze the psram option

## Update the pins of the Microcontroller
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
