# Video Detecion 

## Traffic Detection 
--tbd

## hololens detection in video 

Download hololens-ex-60--loss-2.76.h5
```bash
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/hololens-ex-60--loss-2.76.h5
```
setup detetion config with object and anchors 
Then run the detector python code
```python
python VideoObjectDetection_hololens.py
```

Ref :
https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/Custom/CUSTOMDETECTION.md

todo :
find for vehicle and animals 

**I found that frame by frame detection is too slow and processor intensive to even 
work at my laptop , let alone a Rpi , 
hence M droppping the video object detection approach for self navigation**