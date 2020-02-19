from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()

# model type to RetinaNet
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "models/resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

# video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "videos/traffic.mp4"),
#                                              output_file_path=os.path.join(execution_path, "traffic_detected")
#                                              , frames_per_second=20, log_progress=True)
# print(video_path)


custom_objects = detector.CustomObjects(person=True, bicycle=True, motorcycle=True)

video_path = detector.detectCustomObjectsFromVideo(
                custom_objects=custom_objects,
                input_file_path=os.path.join(execution_path, "traffic.mp4"),
                output_file_path=os.path.join(execution_path, "traffic_custom_detected"),
                frames_per_second=20, log_progress=True)
print(video_path)