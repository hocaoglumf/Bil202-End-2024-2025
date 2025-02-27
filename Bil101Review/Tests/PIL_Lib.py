from PIL import Image

# Open the image
image = Image.open("D:/Academic/PetriNetsWrappedbyModels/Figures/robot2.png")

# Convert to grayscale
bw_image = image.convert("L")

# Save the black and white image
bw_image.save("D:/Academic/PetriNetsWrappedbyModels/Figures/output_bw.png")
