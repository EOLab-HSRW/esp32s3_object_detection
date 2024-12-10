# Under the Hood. Running the training locally
Until now we used edge impulse studio to go over our complete machine learning pipeline. However, Edge Impulse Studio has a limitation of training time of 20 minutes CPU for free accounts. More over, you can have a maximum of 3 Impulses for model comparisons.

Today we will see how to overcome this limitation by training in our local computer. This time we will use 



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
