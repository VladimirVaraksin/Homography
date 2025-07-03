from get_coordinates_pixels import get_points
from view_transformer import ViewTransformer
import numpy as np
import cv2
from ultralytics import YOLO

PERSON_CLASS_ID = 0
target_vertices = np.array(((0, 0), (0, 0), (0, 0), (0, 0)), dtype=np.float32)
path = 'images/image1.png'

def main ():
    pixel_vertices = get_points(path)
    view_transformer = ViewTransformer(pixel_vertices=pixel_vertices, target_vertices=target_vertices)

    camera = cv2.VideoCapture(0)
    model = YOLO('models/yolo12n.pt')

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Detect players
        results = model.predict(frame, classes=[PERSON_CLASS_ID], conf=0.4, verbose=False)

        # plot the results
        frame = results[0].plot() if results else frame

        # Display the frame with detections
        cv2.imshow("Showcase", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
