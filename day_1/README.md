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
- **!!Important** 




- "File" > "Examples" > "esp32" > "camera" > "camera webserver"
    - modify the code for the right board
    - ssid: given in workshop
    - pass: given in workshop
    - upload
    - open serial monitor
    - copy IP address
- Go to src/get_images.py and update the IP address
- Open a terminal and navigate to the folder with the .toml file
- Check if you can run rye (type rye)
    - if not source "$HOME/.rye/env"
- make sure your PC/Laptop is connected to the same network as mentioned above
- run the camera server:
    -type rye run get_images
## Setup
- Create an account in Edge Impulse: https://edgeimpulse.com
- Create a new personal project
- Clone the CIFAR Dataset repository: https://github.com/YoongiKim/CIFAR-10-images/
- Add Existing Data (Select two classes to start with)
    - Creating Windows...
    - Creating Embeddings


```

Project buzilt with Rye
