# Covid-19-Detection-using-Chest-X-rays
Chest diseases are very serious health problems in the life of people. These diseases  include chronic obstructive pulmonary disease, pneumonia, asthma, tuberculosis, and lung  diseases such as right now “COVID-19”. The timely diagnosis of chest diseases is very  important. Application of deep learning techniques can be helpful for the accurate detection of  the “COVID - 19”, and can also be assistive to overcome the problem of a lack of specialized  physicians in remote villages.This project would involve taking X-ray images as input and  classifying the chest disease that person is linked with by performing certain Convolutional  Neural networks (CNN) techniques on that image.


Requirement Analysis
Features that have been implemented in our application and are the core of the application are the following modules: 
1.	Dataset of X Rays(Covid positive and covid negative)
2.	Model(for classifying the x ray in covid positive and covid negative)
3.	Login module
4.	Flask based web application
5.	Remotemysql database for user authentication and registering

Under our project we will be using Chest X-Rays to detect whether the person is infected with covid-19 or not.To implement this we will be using one of the best image detection algorithm named: Inception V3. This model will use the concept of Convolutional Neural Network (CNN) which is specifically designed for object detection. 
We will be using a dataset consisting of Covid-19 positive patient’s chest X-rays (lungs).We will be using different parameters to achieve the best accuracy and within a reasonable time. After the completion of our first phase, which is the back-end , we will focus on developing the front-end in which we will use the Flask framework for creating the web application for our project that will be helpful for the doctors to operate easily.
Our project will be specifically for the doctors to operate and our aim is not only to achieve the best accuracy and faster results but also the usage of this technology to remote locations which are affected by the global pandemic- covid-19.

![image](https://user-images.githubusercontent.com/51341748/117271325-aeaf5700-ae77-11eb-8286-ba3502b4bc5c.png)

![image](https://user-images.githubusercontent.com/51341748/117271412-c981cb80-ae77-11eb-8696-588cdeaa857c.png)

Project Implementation
●	 Importing all libraries:
The important dependencies required for our project needs to be imported first.So, here we start by importing libraries. Since our project involves the application of deep neural networks therefore, the neural network layers are imported from keras library. The model which we are going to use will be Inception V3 to train the dataset.
 
●	Setting epoch size along with batch size and path to the dataset:
The image dimensions are resized to 224 x 224 .Since, this is a pre-trained model therefore it requires an input of 224x224. The epochs for the model is set to 500 with a batch size of 32.This indicates that the model will train ,test and validate the dataset 500 times.
 
●	 Setting dimensions and converting color :
The dataset contains several images of Covid-19 and normal chest X-rays. The below    snapshot shows that the images are resized to dimension 224 x 224 and are classified as Covid and Non-covid under different folders from the existing dataset folder.
 

●	Visualizing first 40 images from dataset:
Here, we have shown the actual images from the dataset under Positive and Negative labels  for Covid-19 with the help of “matplotlib” library by using its “imshow” function.
 
 

●	Normalization:
 It really comes down to math and getting a value between 0-1. Since 255 is the maximum value in RGB pixels, dividing by 255 expresses a 0-1 representation. The image is an array of pixels which ranges from 0-255. By dividing each value of the array with 255, the values in  the array falls between 0-1 which is much more easier for the neural network to process and saves computation time.
 
●	Train Test Split : 
 The dataset is then splitted into training and testing datasets for the sake of training the model. First the split(train and test) is made of Covid dataset and later the same procedure is followed for splitting Non-covid dataset. The covid and Non-covid splits are then concatenated as a one.LabelBinarizer function is used to perform the transform operation of labels with fixed classes. It assigns a unique value or number to each label in a categorical feature.
 

●	Visual a few images from Training and Test sets :
 The training and testing dataset is being displayed here with the help of “matplotlib” library.
 
 

●	Building Model Inception V3
We extracted the inception v3 model from keras library. After that we defined the flatten layer and set the dropout at 0.5  


●	 Model Summary
Below is the model summary which shows the layers of the inception v3 along with the total parameters.
 

●	Training the model
We trained the model for 500 epochs which took approx 2 and a half hours. We showed the accuracy and the loss at each epoch. After this we saved the model.
 
 


●	Image preprocessing, feature extraction and classification of Disease explained: 
	Image preprocessing
One of the significant phases in the data preprocessing was to resize the X‐Ray images as the image input for algorithms were different. We implemented some image pre-processing techniques to increase the performance of our system by speeding up training time. First, we resized all our images to 224x224x3 to increase processing time and also to be suitable in Inception V3. In the image preprocessing step, we need to label the data since the learning technique of convolution neural networks fits into administered learning in machine learning.
 
❏	Image Data augmentation:
CNN needs a sufficient amount of data to achieve excellent performance. We apply data augmentation techniques to increase the insufficient data in training, and the techniques used include vertical flip, horizontal flip, and rotate the image . This will increase the number of images to be fed to the network.
 
 
❏	Transfer learning:
Transfer learning is a machine learning technique which is based on the concept of reusability Transfer learning is often used with CNN in the way that all layers are kept except the last one, which is trained for the specific problem. This technique can be particularly useful for medical applications since it does not require as much training data, which can be hard to get in medical situations. In the analysis of medical data, one of the biggest difficulties faced by researchers is the limited number of available datasets. Deep learning models often need a lot of data. Labeling this data by experts is both costly and time consuming. The biggest advantage of using a transfer learning method is that it allows the training of data with fewer datasets and requires less calculation costs. With the transfer learning method, which is widely used in the field of deep learning, the information gained by the pre-trained model on a large dataset is transferred to the model to be trained. The Inception V3 model which performs convolution, pooling, softmax and fully connected procedures. Here a pre-trained neural network established for one task can be utilized as the initial point of another task. The Inception-v3 architecture comprises two fragments:
 I. Use the feature extraction section of the convolutional neural network. 
II. Classification section utilizing fully-connected and softmax layers. 
 
To use transfer learning for classifying chest X-ray images, we used the TensorFlow library to load the Inception V3 model on our local machine, retrain it on the chest X‐ray dataset and then classify new images to be one of the two categories normal and COVID‐19. It is a deep learning framework established by Google that can control all neurons (nodes) in the system and has a library appropriate for image processing.  






❏	Feature extraction process with the help of transfer learning:
The steps for the projected classification architecture are as follows: 
I. Recursively perform convolution and pooling on images.
II. Apply drop out and fully connected. Now the image must be classified according to the labelled training class.Convolution is a gradual process. Extracts various features of input. Each kernel is responsible for producing output function. Low-level features of the image, such as edges, lines and corners are determined by the lower layer, and the higher-level features are extracted by the higher layer. Pooling is applied to make the features obtained from convolution robust against noise. Pooling layers are usually of two types namely, average pooling and max pooling. It is basically a dimensionality reduction or feature extraction
 
 

  
Hence, chest X-ray images are taken as input, Inception V3 is applied, convolution, pooling, softmax, and fully connected processes are performed. Upon completing these tasks, they are classified according to different training modules and eventually classified as normal and COVID-19 classes. Inception V3 is one of the states of art architectures in image classification challenge. The best network for medical image analysis seems to be the Inception V3 architecture and it preforms better than even the more recent architectures. So, we selected Inception V3 model that is implemented using TensorFlow and hence the retraining is done with TensorFlow.



●	Making Predictions : 

 
 
●	Plot ROC Curve:
An ROC curve (receiver operating characteristic curve) is a graph showing the performance of a classification model at all classification thresholds.This curve plots two parameters:
●	True Positive Rate
●	False Positive Rate
The greater the area under the curve , the better the model is.
The closer the curve is to the top left corner , the better the model is able to do classification.

 

●	 Plot Confusion Matrix
A confusion matrix is a performance measurement technique for Machine learning classification. It is a kind of table which helps you to know the performance of the classification model on a set of test data for which the true values are known. Here,we tried to show the confusion matrix in a more descriptive way. The second matrix shows the percentage rate instead of values. The model did a pretty good job in classifying the labels as Covid and Non_covid which can be understood by analyzing the confusion matrix.
 
 
●	Classification Report :
The classification report visualizer displays the precision, recall, F1, and support scores for the model.A Classification report is used to measure the quality of predictions from a classification algorithm. The accuracy achieved is  more than 95% for the dataset.(more than 1000 images)

 




●	 Accuracy and Loss Plots:
The accuracy of a model is usually determined after the model parameters are learned and fixed and no learning is taking place. Then the test samples are fed to the model and the number of mistakes (zero-one loss) the model makes are recorded, after comparison to the true targets. Then the percentage of misclassification is calculated.
For example, if the number of test samples is 1000 and the model classifies 952 of those correctly, then the model's accuracy is 95.2%.
 The accuracy graphs for the model (InceptionV3) which was used to train the dataset can be seen in the graph below which was plotted using the training and test-validation accuracy. Both the graphs when superimposed on each other showed similar accuracy rates. With the increasing no. of  epochs , the accuracy was also seen to be increased.
 
 
The lower the loss, the better a model (unless the model has over-fitted to the training data). The loss is calculated on training and validation and its interpretation is how well the model is doing for these two sets. Unlike accuracy, loss is not a percentage. It is a summation of the errors made for each example in training or validation sets. With each epoch , the loss was seen to fluctuate and as the epochs reached the end , there was significant decrease in the model loss.
 
 

