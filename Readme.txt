Waste collection and disposal is a complex process that requires the use of money and elaborate management of logistics. This paper will elaborate the structural design working and overall hierarchical description of the system. In this system, without making much of the alterations to the traditional garbage vehicle the proposed system could be mounted on the top of the vehicle canopy for automatically filled level detection. The design is based on two stereoscopic cameras dealing with depth ranging information for filled level detection. Based on deep simulation with image processing and trialling at day to day basis. The core of the proposed design lies depth estimation through a 3D model construction of captured image in using open source system. A tabulation of simulation data with field test experiments verify that design system works energy efficiently and in an orderly manner.

This experiment requires 2 webcameras to be at same level and the lens distance should be 6 centi-meters.
Step1: Check both the webcams are working:
In Test folder you will find below 3 codes:
1. live_webcam_feed.py will help you to get the Live feed of webcam.
2. video_capture.py will capture the video and
video_play.py will run the captured video.
3.camtest.py will provide you the live color video feed

Step2: Create Twilio Account for Text-Message Notifiacation.
configure "credentials.py" file.

Step3: Run the level "leveldetect.py"

This will run both the camera and will trigger the text-notification once it is reaches threshold.