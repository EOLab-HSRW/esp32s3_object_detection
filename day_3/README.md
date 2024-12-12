# Day 3: Object Detection with EDGE IMPULSE and taking actions

## Assemble the stand

## Servo Sweeping
As the ESP32S3 is using some new and different timers then other MCUs (Microcontroller Unit), we use a special library. Download this GitHub repository by SimGallery: [https://github.com/SimGallery/ESP32S3servo](ESP32S3servo). Then add the ZIP file as a library to the Arduino IDE (Sketch > Include Library > Add .ZIP)

After installing the library find the examples for the library and open the "Sweep" example. Upload it too your XIAO ESP32S3 and see if it is working. To get it working you have to change the 'servoPIN' to 44.
Try now to understand the code yourself. It is very simple and you can hopefully understand it quickly.

## Analyze code from Edge Impulse

## Combine servo and AI code for tracking
