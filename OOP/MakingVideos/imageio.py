import imageio
import os

image_folder = 'D://Temp//Pictures//'
output_video = 'output_video.mp4'
fps = 24

images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(('.png', '.jpg'))]
image_paths = [os.path.join(image_folder, img) for img in images]

# Write to video
imageio.mimsave(output_video, [imageio.imread(img) for img in image_paths], fps=fps)
