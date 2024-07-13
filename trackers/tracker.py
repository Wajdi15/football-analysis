from ultralytics import YOLO
import supervision as sv

class Tracker : 
    def __init__(self,model_path) :
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()
    
    def detect_frames(self,frames) :
        batch_size = 20 
        detections = []
        #detet 20 frame by 2à frames
        for i in range (0,len(frames),batch_size) :
            #i use predict bc i need to count the gk as player
            detections_batch = self.model.predict(frames[i:i+batch_size],conf=0.1)
            detections += detections_batch
            break
        return detections
    
    def get_object_tracks(self,frames) :

        detections = self.detect_frames(frames)
        for frame_num , detection in enumerate(detections) :
            cls_names = detection.names
            cls_names_inv = { v:k for k,v in cls_names.items()}

            #convert to supervision detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)
            #convert gk to player object
            for object_index,class_id in enumerate(detection_supervision.class_id) :
                if cls_names[class_id] == "goalkeeper" :
                    detection_supervision.class_id[object_index] = cls_names_inv["player"]

            print(detection_supervision)
            break
