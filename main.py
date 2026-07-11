from PIL import Image

# Open image
image = Image.open("sample.jpg")

# Resize image
resized = image.resize((300, 300))
resized.save("resized.jpg")

# Convert to grayscale
gray = image.convert("L")
gray.save("grayscale.jpg")

print("Image processed successfully!")