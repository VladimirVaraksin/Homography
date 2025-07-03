import cv2

def save_frame(camera):
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        cv2.imshow("Press q to save frame and exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("images/image.png", frame)
            break

    cv2.destroyAllWindows()