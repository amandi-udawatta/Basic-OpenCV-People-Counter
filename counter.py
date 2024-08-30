import cv2
import imutils
import time

capture = cv2.VideoCapture('people_sample.mp4')

# position of the counting line (ROI) in px
roi_line_position = 300 # when you increase this, roi line moves down

people_in=0
people_out=0

# Initialize the background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

min_contour_area = 700
crossed = False
last_count_time = time.time()


# Loop over frames from the video
while True:
    ret, frame = capture.read()
    if not ret:
        break

    frame = imutils.resize(frame, width=900)
    
    # Apply the background subtractor to get the foreground mask
    fgmask  = fgbg.apply(frame)
    cv2.imshow('Foreground mask', fgmask)

    # Define a kernel for morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    #morphological operations to remove noise (using filters and masks)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('morphology close mask', fgmask)

    #find contours of moving objects
    #cv2.findContours(binary image, contour retrieval mode, contour approximation method): RETR_EXTERNAL=retrieve external boundry, CHAIN_APPROX_SIMPLE=
    contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    #line(video frame we are drawing on, start coordinate, end coordinate, colour of line, thickness of ine in px)
    #frame.shape[1] gives the width of the frame(rightmost edge of the frame)
    cv2.line(frame, (0, roi_line_position), (frame.shape[1], roi_line_position), (0,255,255), 2)

    for contour in contours:

        #if the contoured area is smaller than the minimum one neglect it
        if cv2.contourArea(contour) < min_contour_area:
            continue

        #get bounding box for contoured areas
        (x, y, w, h) = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        solidity = cv2.contourArea(contour) / float(w * h)

        if solidity < 0.3 or aspect_ratio > 1.5 or aspect_ratio < 0.2:
            continue
        center_y = y+h // 2

        #draw bounding box
        #rectangle(image, lower left, uppser right, colour, thickness)
        cv2.rectangle(frame, (x,y), (x+w , y+h), (0,255,0), 2)

        #check if going in or out using roi
        if not crossed and (center_y > roi_line_position - 8) and (center_y < roi_line_position + 8) : #to check if a person is crossing the line
            if time.time() - last_count_time > 0.5:  # Only count if 0.5 seconds have passed
                if center_y < roi_line_position:
                    people_out += 1
                else:
                    people_in += 1
                crossed = True
                last_count_time = time.time()

        # Reset the crossed flag if the person has moved away from the line
        if center_y < roi_line_position - 50 or center_y > roi_line_position + 50:
            crossed = False

    # Display the counts on the frame
    #puttext(image, text, position, font, font size, color, thickness)
    cv2.putText(frame, f"In: {people_in}", (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame, f"Out: {people_out}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('people counter', frame)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
capture.release()
cv2.destroyAllWindows()
