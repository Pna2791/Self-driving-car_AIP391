# Self-driving-car_AIP391
## AI subject project

**Authors**: Anh Phan Ngoc, Thinh Ngo Duy, Truong Nguyen Nhat

**Advisor**: Trung Nguyen Quoc


**Proposal**: [Here](https://docs.google.com/document/d/1pJ-1mpVCfOzMSC11danirGs2GOsCmb-buNbJHjdytLo/edit?usp=sharing) |
**Timelines**: [Here](https://docs.google.com/spreadsheets/d/1tI2cD12YLB2aPiFoT3_adGZfaXKjOTtR2en1cJyj28g/edit?usp=sharing) | 
**Google Drive folder**: [Here](https://drive.google.com/drive/folders/14z2X1SkVipk8dSuBQIf7gDxpjtQ_vyRX?usp=sharing) | 
**Youtube playlist**: [Here](https://www.youtube.com/watch?v=2_eudxkdsTU&list=PLzFeP9tMTVBOUq5C_iDwmGKAX8VWUAkw1)

# Using our model
You can down load this repositories following:

```
git clone https://github.com/Pna2791/Self-driving-car_AIP391
cd Self-driving-car AIP391
pip install -r requirements.txt
```
You can run demo on ```Demo/Demo.py```

# Abstract
In this report, we present methods to solve the problem of self-driving cars running on 1-lane roads and enforcing signs of signals in the real environment. Based on the image from the real-time camera, the system will process and give a suitable set of parameters containing the car's direction control parameters and the car speed adjustment parameters. We divide the problem into two main parts, lane detection and traffic sign recognition, respectively. For the lane detection part, we used the data set consisting of 3 classes of approximately 7000 images each to train the convolution neural network (CNN). For the traffic sign recognition part, we use YOLOv5 to detect the position of the signs, then continue to use CNN to classify the signs. The dataset we built for this part is 22 classes with about 500 images each. According to the results of system testing, the recognition accuracy was 95%.
