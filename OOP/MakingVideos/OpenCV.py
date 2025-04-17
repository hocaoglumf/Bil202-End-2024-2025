import cv2
import os

# Folder with your images
image_folder = "D:\\Temp\\Pictures\\"
output_video = 'D:\\Temp\\Pictures\\Video\\output.avi'
fps = 1

# List images and sort them
images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.JPG'))]
images.sort()

# Read the first image to get frame size
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, _ = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Write each frame
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    cv2.putText(frame, "My Video Banner", (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2, cv2.LINE_AA)
    if frame is not None:
        resized = cv2.resize(frame, (width, height))
        video.write(resized)


video.release()
cv2.destroyAllWindows()

print("Video successfully created.")
