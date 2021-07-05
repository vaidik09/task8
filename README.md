# NumberPlate-Detection-FlaskAPP

## Contributors:

💠 [Devansh Bhatt](https://www.linkedin.com/in/devansh-bhatt-9b4102208/)  💠 [Dhiren Soneji](https://www.linkedin.com/in/dhiren-soneji-63a8001b7/)  💠 [Rahul Kashyap](https://www.linkedin.com/in/rahul-kashyap18/)  💠 [Rohit Vishwakarma](https://www.linkedin.com/in/rohit0110/)  💠 [Vaidik Patel](https://www.linkedin.com/in/vaidik099/)

# <p align="center"> ResNet </p>

ResNet, short for Residual Networks is a classic neural network used as a backbone for many computer vision tasks. This model was the winner of ImageNet challenge in 2015. The fundamental breakthrough with ResNet was it allowed us to train extremely deep neural networks with 150+layers successfully. Prior to ResNet training very deep neural networks was difficult due to the problem of vanishing gradients.

![ResNet Architecture](https://miro.medium.com/max/2400/1*hEU7S-EiVqcmtAlj6kgfRA.png)

### <p align="center"> ResNet50 Architecture </p>

The ResNet-50 model consists of 5 stages each with a convolution and Identity block. Each convolution block has 3 convolution layers and each identity block also has 3 convolution layers. The ResNet-50 has over 23 million trainable parameters.

### Conclusion

•	ResNet is a powerful backbone model that is used very frequently in many computer vision tasks

•	ResNet uses skip connection to add the output from an earlier layer to a later layer. This helps it mitigate the vanishing gradient problem

•	You can use Keras to load their pretrained ResNet 50 or use the code ResNet.

### Step by Step Procedure:

Step 1 :- First load the dataset. [Click Here](https://www.kaggle.com/andrewmvd/car-plate-detection) to Download the Dataset
         
Step 2 : -  Give the path of xml file of dataset and then do labeling on it like file_path , xmin , xmax , ymin , ymax  and save the file in label.csv

Step 3 :- First of all load the label.csv and get images path from dataset.

Step 4 :- Data preprocessing on dataset in this resize the image size and then normalize the labels.

Step 5 :- Split the dataset in training and testing part. 

Step 6 :- Using keras library load the Resnet model through  InceptionResNetV2  function  then use Flatten layer and then Dense layer.

Step 7  :- Compile model and train the model and then save it. [Click Here](https://drive.google.com/file/d/1F1XuZLuHwKrsQIwJxLDdCnFEizx8XkS9/view?usp=sharing) To Download Trained Model.

Step 8 :- Load the train model using Keras library.

Step 9 :- Draw the boundary of rectangle on number plate using the coordinate.

Step 10 :- Crop the image of that rectangle part.

Step 11 :- Using OCR(Optical Character Recognition) convert image character into String.

Step 12 :- Put this String in API of Licence-Plate Information and get details of that particular Car.
