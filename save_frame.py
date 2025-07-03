import cv2

def save_frame(cam):
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to capture frame from camera.")
            break
        cv2.imshow("Press q to save frame and exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("images/image.png", frame)
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    save_frame(camera)
    camera.release()
    cv2.destroyAllWindows()