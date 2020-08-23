# Image_caption_generation

## An introduction of Image caption

With the rapid development of machine learning and artificial intelligence, researchers tried to integrate knowledge of computer vision and natural language processing into the task of image caption generation, which programs automatically generate natural language describing the content observed in the images.

Researchers develop the image description models and systems to solve some problems. 
### The models could help the visually impaired people to understand the content of images.
### The system could improve the images searching
### It could help photographers to sort photos by contents observed from the images
### For self-driving cars, if systems could caption what devices detect, this could boost the performance of the self-driving systems.
### CCTV cameras now are prevalent. With the increasing video surveillance data, it could impose the cost to process the data and then turn them into useful information without tedious efforts. If the captioning system could build effectively, it would help monitor accidents, like raising alarm for crime. 

There is a system created by Microsoft called Caption Bot (https://www.captionbot.ai/), which you can upload the url of an image and captions would be generated. This task is similar to this task. I will build my own machine learning model and create a web application for this task.

## Dataset: COCO 2020 (Common Objects in Context)
### COCO is a large-scale object detection, segmentation, and captioning dataset.
### COCO has several features:
#### Object segmentation
#### Recognition in context
#### Superpixel stuff segmentation
#### 330K images (>200K labeled)
#### 1.5 million object instances
#### 80 object categories
#### 91 stuff categories
#### 5 captions per image
#### 250,000 people with keypoints
##### reference : https://cocodataset.org/#home
### We are now using the validation set in this dataset to train our model.
### We splitted into 20011 of training set and  5003 of validation set.

