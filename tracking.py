import cv2

video_file = cv2.VideoCapture('Pedestrians.mp4')  # Capture every single frame from the video file

# import the trained models
car_tracker_file = 'cars_detector.xml'
pedestrian_tracker_file = 'pedestrians_detector.xml'
car_tracker = cv2.CascadeClassifier(car_tracker_file)  # Create car classifier
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)  # Create pedestrian classifier
while True:
    read_frame, frame = video_file.read()  # Reading the frames

    if read_frame:
        # Convert the frames into greyscale as it makes the process faster

        greyscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    else:
        break

    # Detect cars and pedestrians
    cars = car_tracker.detectMultiScale(greyscale_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(greyscale_frame)

    # Draw rectangles
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255 * 65536, 255 * 256, 0), 2)
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the image of cars and pedestrians
    cv2.imshow('car and pedestrian tracking', frame)
    key = cv2.waitKey(1)  # Display one frame for 1ms

    if key == 81 or key == 113:  # To exit the program on keypress
        break
