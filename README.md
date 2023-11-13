# **Farmbot - Livestream**

## **Launch the stream**
`sudo python3 /path/to/main.py`

## **Automate stream on boot**
`sudo nano /etc/profile`  
At the end of the file add your `sudo python3 /path/to/main.py`

## **Dependencies** 
Recommended Initial steps

```
sudo apt-get update
sudo apt-get upgrade
```

```
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqt5gui5 libqt5webkit5 libqt5test5
sudo apt-get libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install imutils
```

**NOTE:** You can use
```
sudo pip3 install opencv-contrib-python
sudo pip3 install opencv-python
```
But be warned they may take a very long time to install on a pi3

**RECOMMENDED**
```
sudo apt-get install libopencv-dev python3-opencv
```

## **Documentation to Add**
1. **Nginx**
2. **Duckdns**


## **Packages used**

1. **Flask**  
Flask is used for the web app to serve the video streaming  
and picture capturing from the raspberry pi.

2. **OpenCv**  
We are using Open CV for capturing the frames from the camera  
encoding them, and for saving pictures taken.

3. **imutils**  
Convenience library for OpenCV, to simplify common tasks.  
For Farmbot it's working with the video stream.

4.  **numpy**  
Numpy is a library for numerical operations in Python.  
We are using it for array manipulation, more so for the  
frame flipping.

5. **jQuery**  
Fast and small JS library. Used in Farmbot for handling button  
click events and making async requests to the server

6. **Nginx**  
Currently setup ready to go.  
But as the network does not have exposed ports, I am unable to get it functioning.

