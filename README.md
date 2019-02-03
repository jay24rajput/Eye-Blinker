# Eye-Blinker

Software for reducing eye strain which occurs due to constantly staring at digital screen for long periods of time. 
Normallly a human blinks about to 10-20 times per minute but due to constant staring at screens this number reduces to about 3-8 times a minute. Eye-Blinker is designed to prevent this very scenario.<br>
## Features of Eye-Blinker are:<br>
### 1.Three different levels of warnings.<br>
* Level 1: Issuing warning stating your blink rate is low.
* Level 2: Adjusting brightness as blink rate is lower than usual.
* Level 3: Prompting the user to look away from the screen for 15 seconds as blink rate is critically low.
### 2.Script runs in the backgroud while working offline.
### 3.Generation of graphical model on the basis of blink rate of 15 seconds for further analysis.<br>
## How to install: <br>
1. Clone the repository and ```cd``` into ```Eye-blinker```.<br>
2. Check opencv version using <br>
```$ python3```<br>
```>>> import cv2```<br>
```>>> cv2.__version__```
3. If not present then install opencv using:<br>
```pip install opencv-python``` for python 2 <br>
```pip3 install opencv-python``` for python 3
4. Install dlib using: <br>
``` pip install dlib``` for python 2 <br>
``` pip3 install dlib``` for python 3
5. Install PyQt using: <br>
``` sudo apt-get install python-qt5 ``` for python 2<br>
``` sudo apt-get install python3-qt5``` for python 3<br>
6. Run driver.py as:<br>
``` python3 driver.py``` <br>
## File Description: <br>
1.```driver.py```:Runs the python GUI using multithreading.<br>
2. ```detect_blinks```: Detects the eyes of the reader and calculates the blinks for each minute.<br>
3. ```generate_reports```: Generate graph for each session on the basis of blinks.<br>
4. ```bright.py```: Tweaks the brightness of the screen in level 2.<br>
5. ```level3.py```: Prompts the user to look away and calculates the time where he looks away in level 3.
