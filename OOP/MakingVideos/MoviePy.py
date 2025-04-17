from moviepy.editor import ImageSequenceClip
import os

# Path to your image folder
image_folder = 'D://Temp//Pictures//'
fps = 24

# Collect image paths, sorted
images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg'))]
images.sort()  # Ensure correct order

# Create full paths
image_paths = [os.path.join(image_folder, img) for img in images]

# Create clip
clip = ImageSequenceClip(image_paths, fps=fps)

# Export to video
clip.write_videofile("output_video.mp4", codec='libx264')
