import cv2
import numpy as np

clicked_points = []
done = False  # Globales Flag

def click_event(event, x, y, flags, params):
    global done
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Clicked: ({x}, {y})")
        if len(clicked_points) == 4:
            print("Alle 4 Punkte erfolgreich geklickt!")
            print("video_points = np.array([")
            for pt in clicked_points:
                print(f"    [{pt[0]}, {pt[1]}],")
            print("], dtype=np.float32)")
            done = True
            cv2.destroyAllWindows()

def get_points(path=None):
    global done
    done = False
    frame = cv2.imread(path)
    window_name = 'Click 4 Points: Top-Left, Top-Right, Bottom-Right, Bottom-Left'
    cv2.imshow(window_name, frame)
    cv2.setMouseCallback(window_name, click_event)

    while not done:
        if cv2.waitKey(20) & 0xFF == 'q':  # q zum Abbrechen
            break

    cv2.destroyAllWindows()
    return np.array(clicked_points, dtype=np.float32)

if __name__ == "__main__":
    get_points('images/image.png')