# Workshop: Practical Introduction to Artificial Intelligence on Embedded Devices

For this project you will need some dependencies. The project uses python version > 3.8, and dependencies are defined within the pyproject.toml file. 
We will build the dependencies using Rye. Details on the installation below. Also you will need Arduino IDE.
We will work with the Seeed Studio XIAO ESP32S3 with camera module. You will also be provided with a servomotor, an antenna and a 3d printed case.

Let start by downloading the software needed.

## Installing Rye
We will use Rye fo installing our dependencies. If you want to know more about it, you can watch the [introduction video about rye](https://rye.astral.sh/guide/)

### Installation for Linux

1. Open your Terminal
1. install [rye](https://rye.astral.sh/) with `curl -sSf https://rye.astral.sh/get | bash`

run through the installer like this:
- platform linux: yes
- preferred package installer: uv
- Run a Python installed and managed by Rye
- which version of python should be used as default: 3.10
- should the installer add Rye to PATH via .profile? : y
- run in the cli: `source "$HOME/.rye/env"`

### Installation for Mac

1. Open your Terminal
1. install [rye](https://rye.astral.sh/) with `curl -sSf https://rye.astral.sh/get | bash`

run through the installer like this:
- platform macos: yes
- Run the old default Python (provided by your OS, pyenv, etc.)
- should the installer add Rye to PATH via .profile? : y
- run in the terminal: `source "$HOME/.rye/env"`
- install python 3.10 as follow: `rye fetch 3.10`

### Installation for Windows


1. Activate "Developer Mode" on Windows. Follow the instruction of **Windows Developer Mode** [See this page](https://rye.astral.sh/guide/faq/#windows-developer-mode)
1. Download and install the latest release of [rye](https://rye.astral.sh/) 

## Installing dependencies with Rye

1. Clone or download the files of this repository
1. Open the terminal and cd to the root directory of the downloaded repository (where the .toml file is): `cd path-to-root-folder`
1. In the terminal run: `rye sync`




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
