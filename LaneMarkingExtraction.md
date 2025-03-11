# About the lane Marking extraction Problem
To solve this problem I used opencv library of python.
All images are just 3 2d array combined together each element of array representing a pixle and the entries in the array are the
3 parameters that you used to color the pixle they can change with the color system you choose to use 
for the problem of extraction that was presented the selection critera is based on color so we chosed the hsv color wheel system
as the distinction is pased on color and type of color can be easily represented by hsv system with the 'h' parameter


![Alt Text](https://upload.wikimedia.org/wikipedia/commons/a/a0/Hsl-hsv_models.svg)
![Alt Text](https://upload.wikimedia.org/wikipedia/commons/3/33/HSV_color_solid_cylinder_saturation_gray.png)


we provided the upper and lower limits with np.array thing we the inRange function we created the mask by only kepping those pixles which are within our defined range with the bitwise_and function only those pixles which were common in both the original image and mask were kept