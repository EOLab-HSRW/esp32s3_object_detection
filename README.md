# Workshop: Practical Introduction to Artificial Intelligence on Embedded Devices

This workshop was developed as part of the [Latin American Summer School on Robotics (LACORO) 2024] as a three day workshop.
- [Day 1 - Image Classification via Edge Impulse](./day_1/README.md)
- [Day 2 - AI for embedded devices from Scratch via Python](./day_2/README.md)
- [Day 3 - Object Detection on ESP32 and controlling a servo](./day_3/README.md)

## Preparation
For this project you will need some dependencies. The project uses python version > 3.8, and dependencies are defined within the pyproject.toml file. 
We will build the dependencies using Rye. Details on the installation below. Also you will need Arduino IDE.
We will work with the [Seeed Studio XIAO ESP32S3 Sense](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/). You will also be provided with a servo motor, an antenna and a 3d printed test stand.

### BOM
TBD

### Installing Rye
We will use Rye fo installing our dependencies. If you want to know more about it, you can watch the [introduction video about rye](https://rye.astral.sh/guide/)

#### Installation for Linux

1. Open your Terminal
1. install [rye](https://rye.astral.sh/) with `curl -sSf https://rye.astral.sh/get | bash`

run through the installer like this:
- platform linux: yes
- preferred package installer: uv
- Run a Python installed and managed by Rye
- which version of python should be used as default: 3.10
- should the installer add Rye to PATH via .profile? : y
- run in the cli: `source "$HOME/.rye/env"`

#### Installation for Mac

1. Open your Terminal
1. install [rye](https://rye.astral.sh/) with `curl -sSf https://rye.astral.sh/get | bash`

run through the installer like this:
- platform macos: yes
- Run the old default Python (provided by your OS, pyenv, etc.)
- should the installer add Rye to PATH via .profile? : y
- run in the terminal: `source "$HOME/.rye/env"`
- install python 3.10 as follow: `rye fetch 3.10`

#### Installation for Windows


1. Activate "Developer Mode" on Windows. Follow the instruction of **Windows Developer Mode** [See this page](https://rye.astral.sh/guide/faq/#windows-developer-mode)
1. Download and install the latest release of [rye](https://rye.astral.sh/) 
1. The windows installer normally will automatically register the rye path in the PATH environment variable. If this does not work you will need to manually perform the following steps:

    - Press Win+R, enter sysdm.cpl and hit Enter.
    - In the "System Properties" dialog, click the "Advanced" tab.
    - Click on "Environment Variables".
    - In the top list, double click on the Path variable.
    - In the "Edit environment variable" dialog click on "New".
    - Enter %USERPROFILE%\.rye\shims and hit Enter.
    - Click repeatedly on "Move Up" until the newly added item is at the top.
    - Click on "OK" and close the dialog.
    - Note that you might need to restart your login session for this to take effect.

### Installing dependencies with Rye

1. Clone or download the files of this repository: https://github.com/EOLab-HSRW/esp32s3_object_detection.git
1. Open the terminal and cd to the root directory of the downloaded repository (where the .toml file is): `cd path-to-root-folder`
1. In the terminal run: `rye sync`

### Downloading Arduino IDE
If you don't have it already, please download  and install the IDE from the [official site](https://www.arduino.cc/en/software)

### Access Edge Impulse
1. If you don't have an account already, please register in EdgeImpulse [official site](https://studio.edgeimpulse.com/signup)
