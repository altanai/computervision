# Object Detection

object detection is a two-step process

1. Find bounding boxes containing objects such that each bounding box has only one object.

Sliding Window Approach - used by HAAR cascades and HOG + SVM 

2. Classify the image inside each bounding box and assign it a label.

R-CNN Object Detector 
Fast R-CNN Object Detector
Faster R-CNN Object Detector


object detection model file

## RetinaNet 
Size = 145 mb
high performance and accuracy, with longer detection time

## YOLOv3 
Size = 237 mb, 
moderate performance and accuracy, with a moderate detection time

## TinyYOLOv3 
Size = 34 mb
optimized for speed and moderate performance, with fast detection time

## RetinaNet 
Size = 145 mb
high performance and accuracy, with longer detection time



object detection model (RetinaNet) supported by ImageAI can detect 80 different types of objects.

person,  bicycle,  car, motorcycle, airplane, bus, train,  truck,  boat,  traffic light,  fire hydrant, stop_sign,
parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,   oven,
toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,   toothbrush.


**ref** :
https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection