import cv2
import numpy as np

clicked_points = []  # List to store clicked points
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Clicked: ({x}, {y})")
        if len(clicked_points) == 4:
            print(" All 4 points clicked successfully!")

            print("video_points = np.array([")
            for pt in clicked_points:
                print(f"    [{pt[0]}, {pt[1]}],")
            print("], dtype=np.float32)")
            cv2.destroyAllWindows()

def get_points(path):
    """
    Returns the clicked points as a NumPy array of shape (4, 2).
    """
    frame = cv2.imread(path)
    # Show image and capture clicks
    window_name = 'Click 4 Points: Top-Left, Top-Right, Bottom-Right, Bottom-Left'
    cv2.imshow(window_name, frame) # show the image
    cv2.setMouseCallback(window_name, click_event) # set mouse callback to capture clicks

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return np.array(clicked_points, dtype=np.float32)