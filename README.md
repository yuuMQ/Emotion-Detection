# Emotion-Detection
## Dataset:
you can get the ExpW dataset from https://universe.roboflow.com/
### Running code:
You can use any model as yolov5, yolov8 to detect the emotion.

Example:
+ git clone https://github.com/ultralytics/yolov5
+ cd yolov5
+ pip install -r requirements.txt
## Training and Detect
### After installed yolov5 model, check emotion.yaml and train
+ python train.py --img 640 --batch 16 --epoch 100 --data emotion.yaml --weights yolov5n.pt
### Detect:
+ python detect.py --weights PATH_TO_YOUR_best.py --source YOUR_IMAGE
+ python detect.py --weights PATH_TO_YOUR_best.py --source -0
