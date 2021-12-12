# virtualpaint

The code focusses on allowing the users to paint according to their handmotion and the color of the tip of the marker or highlighter that they are holding.
Currently, just three colors are added into the color dictionary: Green, Purple and Orange.

The my_colors dictionary represents the hue_min,saturation_min,value_min, hue_max, saturation_max and value_max values for the colors mentioned
The color_values dictionary represents the rgb value for the colors in the keys

The find_contours function finds the contour of the image and returns the outer bounding rectangle
The find_color function helps to detect the color of the pen tip and helps to draw on the canvas using the drawOnCanvas function


![virtual paint](https://user-images.githubusercontent.com/34358548/145703235-9b87eb41-7750-42b2-b75d-0c40a399a632.png)
