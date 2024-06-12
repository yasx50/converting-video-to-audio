import moviepy.editor

from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.editor.VideoFileClip(vid)
aud = video.audio
aud.write_audiofile("demo.mp3")
print("ending...")

# step 1 --> 
'''
first install package named moviepy using command 
pip install moviepy
'''
# step 2 -->
'''
start writing the code and begin with importing the module moviepy.editor as well as tikinter
'''
# step 3 -->
'''
use function of tkinter module which is  askopenfilename() this function helps us to select the file by UI unlike giving path of video file ,store this function in vdo variable '''

# step 4 -->
'''
now we are using the main library function which is -> moviepy.editor.VideoFileClip(var name where you have stored the video) and also store this function in video variable coZ here we are giving our video to main function which will create audio from it'''

# step 5 -->
'''now we have t use  var_name_of_step4.audio method ,it will convert our file into audio and yes we have to store this in aud variable'''

# step 6 --> (final step)
'''if we are successfully executed the above code then we have to give format to our audio means m3 or m4 and name of that file like --> name-of-file.format-of-file in this program we have given "demo.mp3"'''
