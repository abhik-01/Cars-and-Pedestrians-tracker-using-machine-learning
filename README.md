<h1 align='center'>Cars & Pedestrians Tracker</h1>

## Summary

This is a `Machine Learning` model built using `Python` & `OpenCV`. It takes a video file & detects the
cars & pedestrians by drawing rectangles around them.

## Pretrained models

For this project I've used a pretrained `cascade classifier` which uses `haar features` to detect objects.
`haar features` are like a building block having two sections, one is dark and the other one is light. The
classifier counts the pixels in both the sections, adds those pixels of that particular section & compare
the results. By this approach it identifies objects.

## How the application works

Firstly, it captures every single frame from the video file using the `VideCapture()` function of `OpenCV`,
reads the captured frame using the `read()` function & converts each frame to `greyscale` using the
`cvtColor()` function as it takes less computing power as well as time because when an image is in `RGB` format,
it contains a lot of information. By converting to `greyscale`, it reduces the color information while not
compromising on the object.

After this, it uses the pretrained classifier & detects cars and pedestrians in each frame using the `detectMultiScale()`
function. When it detects a car or a pedestrian, it draws a rectangle around the object using the `rectangle()`
function. Then it returns the processed frame using the `imshow()` function.

You can check this repo for the source code of this project.
