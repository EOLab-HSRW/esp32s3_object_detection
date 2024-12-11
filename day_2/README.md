# Under the Hood. Running the training locally [Under construction]
Until now we used edge impulse studio to go over our complete machine learning pipeline. However, Edge Impulse Studio has a limitation of training time of 20 minutes CPU for free accounts. More over, you can have a maximum of 3 Impulses for model comparisons.

Today we will see how to overcome this limitation by training in our local computer. 

First we will start making a simple convolutional model from scrath.

## Shallow CNN in Edge Impulse
- Create a new impulse and as training block, use a classification block
- Leave the standard configuration and run it
- Because of the ammount of images, you should not expect a good classifier.

## Under the hood of your CNN
We will have a deeper look on what Edge Impulse is doing for you in the background. 
First we will explore the notebook [Model_example.ipynb](../day_2/Model_Example.ipynb) using jupyter lab. It is already installed via rye, to run it do the following:

- Open a command prompt and navigate to your root folder (where the .toml is) `cd path_to_root`
- Check if you can run rye (type `rye`)
    - if not cannot, then type `source "$HOME/.rye/env"`. Now you should be able to call rye.
- type `rye run python -m jupyterlab` and open the Model_example notebook from day_2 folder.
- Run cell by cell the notebook, following the instructions it gives.

## Exploring and hyperparameter tuning using keras_tuner
Now that you know what edge impulse studio is doing, you can look for optimal hyperparameter values locally. For this, we will use the notebook [Hypertuning.ipynb](./Hypertuning.ipynb).
You can simply open it using your jupyter notebook directory. 

## Time to explore by yourself
Your task is to improve the your model. You know that your transfer learning model from Impulse performs better. So instead of using a shallow model, let's make use of a pretrained model and adapt it to our needs. 
We suggest you to do the following:

- In jupyterlab, duplicate the Hypertuning notebook and rename it, for example Hypertuning_Transfer.
- In Edge Impulse Studio, have a look to the Impulse of the Mobilenet network you used in day1. Open the "Expert mode" to have access to the code.
-  





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
