from ultralytics import YOLO
import cv2

# -------------------------------------------
# STEP 1: Load your trained model
# -------------------------------------------
# YOLO() loads the model weights from the file you trained or downloaded.
model = YOLO("models/helmet_model.pt")

# -------------------------------------------
# STEP 2: Open the video file
# -------------------------------------------
# VideoCapture opens the video so we can read it frame by frame.
cap = cv2.VideoCapture("testvid.mp4")

# Read basic properties of the video
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = int(cap.get(cv2.CAP_PROP_FPS))

print(f"Video loaded | {width}x{height} @ {fps}fps")

# -------------------------------------------
# STEP 3: Setup output video writer
# -------------------------------------------
# VideoWriter saves the annotated video to a new file.
# *"mp4v" unpacks the string into 4 characters — that's just how OpenCV needs it.
out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

# -------------------------------------------
# STEP 4: Track how many violations happened
# -------------------------------------------
violation_count = 0

print("Processing... Press Q to quit early.")

# -------------------------------------------
# STEP 5: Loop through every frame
# -------------------------------------------
while cap.isOpened():
    ret, frame = cap.read()

    # ret is False when the video ends or has an error — so we stop the loop
    if not ret:
        break

    # -------------------------------------------
    # STEP 6: Run helmet detection on this frame
    # -------------------------------------------
    # conf=0.4 means only show detections the model is 40%+ confident about.
    # verbose=False stops YOLO from printing results every frame (too noisy).
    results = model(frame, conf=0.4, verbose=False)

    # -------------------------------------------
    # STEP 7: Check if anyone is without a helmet
    # -------------------------------------------
    # results[0].names is a dict like {0: "helmet", 1: "no-helmet"}
    # results[0].boxes has all the detected boxes in this frame
    no_helmet_found = False

    for box in results[0].boxes:
        class_id   = int(box.cls[0])               # which class was detected
        class_name = results[0].names[class_id]    # get its name

        if class_name in ("no-helmet", "no_helmet", "without_helmet"):
            no_helmet_found = True
            violation_count += 1

    # -------------------------------------------
    # STEP 8: Draw boxes + a simple status label
    # -------------------------------------------
    # .plot() draws all bounding boxes with labels on the frame
    annotated_frame = results[0].plot()

    # Show a red or green status text in the top-left corner
    if no_helmet_found:
        label = "VIOLATION DETECTED"
        color = (0, 0, 255)   # red  (OpenCV uses BGR not RGB)
    else:
        label = "ALL SAFE"
        color = (0, 255, 0)   # green

    cv2.putText(annotated_frame, label, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # -------------------------------------------
    # STEP 9: Save and show the frame
    # -------------------------------------------
    out.write(annotated_frame)
    cv2.imshow("Helmet Detection", annotated_frame)

    # waitKey(1) waits 1ms between frames. & 0xFF is a standard bitmask for key reading.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -------------------------------------------
# STEP 10: Clean up
# -------------------------------------------
# Always release the video and close windows at the end.
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Done! Total violations detected: {violation_count}")
print("Output saved as output.mp4")