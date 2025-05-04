# CrossDomain

## Overview

**CrossDomain** is a simple image colorization application that uses a pre-trained Caffe model to colorize grayscale images. It is designed to demonstrate how to apply deep learning-based colorization using OpenCV’s DNN module. This project is suitable for processing static images and can be extended to handle real-time video or webcam streams.

---

## Features

- Convert grayscale images to color using a deep learning model

- Uses the `colorization_release_v2.caffemodel` and associated `.prototxt` for inference

- Overlay original and colorized images side-by-side

- Easy-to-use script-based workflow

---

## Installation 

1. Install dependencies:

```bash
pip install requirement.txt
```

2. Donwload the pre-trained model:

- Place the following files into the models/ directory:

`colorization_release_v2.caffemodel`

`colorization_deploy_v2.prototxt`

`pts_in_hull.npy`

---

## How It Works

1. Loads a pre-trained deep learning model for colorization using OpenCV’s DNN module.

2. Converts the input RGB image to Lab color space.

3. Feeds the L channel (lightness) into the neural network.

4. Predicts the a and b channels (color) and reconstructs the color image.

5. Displays the result side-by-side with the original.

---
