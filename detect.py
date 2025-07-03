import numpy as np
import cv2

def detect(frame, results, view_transformer, class_names):
    for detections in results:
        for box in detections.boxes:
            # Extract bounding box coordinates (x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Compute the bottom-center point of the bounding box
            point = np.array([(x1 + x2) / 2, y2], dtype=np.float32)
            # Compute the pitch coordinates using the view transformer
            pitch_point = view_transformer.transform_point(point)
            # get class index and label
            cls = int(box.cls[0])
            label = class_names[cls]
            confidence = round(float(box.conf[0]), 2)

            # add annotation to the frame if pitch_point is not None
            if pitch_point is not None:
                pitch_x, pitch_y = pitch_point[0]
                label_text = f'{label}, conf:{confidence}, ({pitch_x:.2f}, {pitch_y:.2f})'
                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
                cv2.putText(frame, label_text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    return frame