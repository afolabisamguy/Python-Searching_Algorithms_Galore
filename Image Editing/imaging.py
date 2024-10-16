from PIL import Image, ImageEnhance, ImageFilter

# Open an image file
image = Image.open('C:/Users/Samguy/Downloads/samuel.jpg')

# Enhance the brightness
enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(1.5)  # Increase brightness by 50%
brightened_image.show()

# Save the brightened image
brightened_image.save('brightened_example.jpg')

# # Apply additional filters
# # 1. Sharpen
# sharpened_image = image.filter(ImageFilter.SHARPEN)
# sharpened_image.show()
# sharpened_image.save('sharpened_example.jpg')
#
# # 2. Blur
# blurred_image = image.filter(ImageFilter.BLUR)
# blurred_image.show()
# blurred_image.save('blurred_example.jpg')
#
# # 3. Edge Enhance
# edge_enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)
# edge_enhanced_image.show()
# edge_enhanced_image.save('edge_enhanced_example.jpg')
#
# # 4. Contour
# contoured_image = image.filter(ImageFilter.CONTOUR)
# contoured_image.show()
# contoured_image.save('contoured_example.jpg')
#
# # 5. Detail
# detailed_image = image.filter(ImageFilter.DETAIL)
# detailed_image.show()
# detailed_image.save('detailed_example.jpg')
#
# # 6. Emboss
# embossed_image = image.filter(ImageFilter.EMBOSS)
# embossed_image.show()
# embossed_image.save('embossed_example.jpg')
