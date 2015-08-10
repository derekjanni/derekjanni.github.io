---
layout: post
title: Optical Character Recognition in Python
---

[Optical Character Recognition]() is an old and well studied problem. The MNIST dataset, which comes included in popular machine learning packages, is a great introduction to the field. In [scikit-learn](http://scikit-learn.org/stable/), for instance, you can find data and models that allow you to acheive great accuracy in classifying the images seen below: ![The MNIST Dataset](http://i.ytimg.com/vi/0QI3xgXuB-Q/hqdefault.jpg)

My recent work in the field approaches a different, but no less critical problem in the field: how to deal with noisey, real-world image data. In emerging fields like autonomous vehicles and computer-assisted sight, there is a great need for not only being able to "read" and convert optical input into strings, but also to also account for the immense variety in typefaces encountered on an average street:

![The Chars74k Dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/Samples/english.png)

As you can see, the Chars74k dataset contains images of characters with varying backgroungs, orientations, image qualities and typefaces - which turns OCR into a much more interesting problem!

The secret here is that pre-processing has an amazing effect on results. When I ran a slew of classifier algorithms on a test set of roughly 6000 images, none was more than 30% accurate. However, after applying [Otsu's method](https://en.wikipedia.org/wiki/Otsu%27s_method) and nudging the dataset by way of some easy linear algebra, my test set performance climbed closer to 60% - so high that I'm currently in the top ten for the related [Kaggle Competition](https://www.kaggle.com/c/street-view-getting-started-with-julia/leaderboard)!

It turns out that nudging, or duplicating existing images in different orientations, has a big part to play in improving results. Just a small shift of 1 pixel to the left, right, top and bottom of the frame (on each image) effectively increases the size of your training data by 5 times - allowing the computer to recognize images that are aligned differently. While I have yet to implement [affine transformations](https://en.wikipedia.org/wiki/Affine_transformation) into my dataset, i suspect that they would also greatly improve performance in cases where the input data is skewed.

For a more in-depth look at my work in the field, visit my project site, [PyOCR](derekjanni.github.io/pyocr/) to see the code and some visualitations (the confusion matrix is the most interesting, if you ast me) that came out of my work thus far. Evenutally, I will have an app embedded that can handle user-uploaded images or show examples characters that the computer is trying to classify.


