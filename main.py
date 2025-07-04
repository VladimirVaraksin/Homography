import numpy as np
import cv2
from ultralytics import YOLO
import os
from get_coordinates_pixels import get_points
from view_transformer import ViewTransformer
from save_frame import save_frame
from detect import detect

person_class_id = 0
pixel_vertices = None # Pixel coordinates of the corners in the input image
target_vertices = np.array([[0, 0],[1.8, 0],[1.8, 3.8],[0, 3.8]], dtype=np.float32) # Real-world coordinates in meters
model = YOLO('models/yolo12n.pt')
class_names = list(model.names.values())

def main ():
    global person_class_id, target_vertices, model, class_names, pixel_vertices

    camera = cv2.VideoCapture(0)

    if not os.path.exists('images/image.png'):
        save_frame(camera)  # Save a frame to click points on
    if pixel_vertices is None:
        pixel_vertices = get_points('images/image.png')  # Get pixel coordinates from the saved frame
    view_transformer = ViewTransformer(pixel_vertices=pixel_vertices, target_vertices=target_vertices)

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame from camera.")
            break

        # Detect people
        results = model.predict(frame, classes=[person_class_id], conf=0.4, verbose=False, stream=True)

        # Process the detection results and annotate the frame
        frame = detect(frame, results, view_transformer, class_names)

        # Display the frame with detections
        cv2.imshow("Live Camera Feed", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()


if __name__ == "__main__":
    main()
