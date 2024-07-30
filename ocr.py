# import easyocr
# import matplotlib.pyplot as plt
# import cv2
#
# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])
#
# # Load the image
# image_path = 'image_2.jpg'
# image = cv2.imread(image_path)
#
# # Use EasyOCR to read the text from the image
# results = reader.readtext(image_path)
#
# # Prepare to save the text
# text_output = []
#
# # Display the image and the text
# for (bbox, text, prob) in results:
#     # Displaying the bounding box
#     (top_left, top_right, bottom_right, bottom_left) = bbox
#     top_left = tuple([int(val) for val in top_left])
#     bottom_right = tuple([int(val) for val in bottom_right])
#
#     cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
#     cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
#
#     # Append the text to the list
#     text_output.append(text)
#
# # Save the text to a file
# with open('extracted_text.txt', 'w') as file:
#     for line in text_output:
#         file.write(line + '\n')
#
# # Display the image with the text
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()

# import easyocr
#
# # Initialize the EasyOCR reader
# reader = easyocr.Reader(['en'])
#
# # Load the image
# image_path = 'image_2.jpg'
#
# # Use EasyOCR to read the text from the image
# results = reader.readtext(image_path)
#
# # Prepare to save the text
# text_output = []
#
# # Extract the text from the results
# for (bbox, text, prob) in results:
#     text_output.append(text)
#
# # Save the text to a file
# with open('extracted_text.txt', 'w') as file:
#     for line in text_output:
#         file.write(line + '\n')
#
# print("Text extraction completed and saved to 'extracted_text.txt'.")
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=True)

# Load the image
image_path = 'image_2.jpg'

# Use EasyOCR to read the text from the image
results = reader.readtext(image_path)

# Prepare to save the text
text_output = []

# Extract the text from the results
for (bbox, text, prob) in results:
    text_output.append(text)

# Save the text to a file
with open('text.txt', 'w') as file:
    for line in text_output:
        file.write(line + '\n')

print("Text extraction completed and saved to 'extracted_text.txt'.")
