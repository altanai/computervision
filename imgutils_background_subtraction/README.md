# Background subtraction

Bayesian (probability) based foreground and background segmentation,
using cv2.createBackgroundSubtractorGMG  function 

**How background subtraction helps in identfying motion in video frame? **

The background of our video stream is largely static and unchanging over consecutive frames of a video. Therefore, by modelling the background, we can monitor it for substantial changes. 
If there is a substantial change, we can detect it — this change normally corresponds to motion.

**Using first frame to model background**
The first frame of our video file will contain no motion and just background therefore, we can model the background of our video stream using only the first frame of the video.

**convert the image to grayscale**
color has no bearing on our motion detection algorithm
we need to apply Gaussian blurring to smooth our images.

[![Gif](https://github.com/altanai/computervision/blob/master/imgutils_background_subtraction/screenshots/Screenshot%202019-12-15%20at%2010.24.49%20PM.png?raw=true)](https://github.com/altanai/computervision/blob/master/imgutils_background_subtraction/output.gif?raw=true)

## Converting mov to gif 
```
ffmpeg -i Screen\ Recording\ 2019-12-15\ at\ 10.31.00\ PM.mov -pix_fmt rgb24 output.gif
```

References :
- https://github.com/jrosebr1/imutils
