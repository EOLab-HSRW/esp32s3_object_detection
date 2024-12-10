# Image Classification with EDGE IMPULSE (Duckie, cherry or tomato? )
In day one we will assemble our material and run a small test on the microcontroller. Afterwards, you will start gathering a dataset of Duckies, cherries and tomatoes and then we will go to edge impulse to create am image classifier and deploy it in your microcontroller.

## Your Microcontroller
We are working with [XIAO-ESP32-S3 Sense from Seed Studio](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)

in order to test it we will do the following:

first we need to install the libraries of the microcontroller. Make sure that you install the version 2.0.14 from Espressif Systems.

### Installing the library
In arduino follow this steps:

- Go to Boards Manager
- Search for esp32 and install the version 2.0.14
- Once the installation is finished close the IDE and Open it again


### Testing the Microcontroller with the blink example
- Go to File -> Examples -> Basic -> Blink
- 
- Connect you microcontroller
- Select the right board and port

## Setup
- Create an account in Edge Impulse: https://edgeimpulse.com
- Create a new personal project
- Clone the CIFAR Dataset repository: https://github.com/YoongiKim/CIFAR-10-images/
- Add Existing Data (Select two classes to start with)
    - Creating Windows...
    - Creating Embeddings


```

Project buzilt with Rye
