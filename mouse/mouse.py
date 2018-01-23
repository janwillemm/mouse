from pymouse import PyMouseEvent
import subprocess

class MouseHandler(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self, capture=True)
        self.curSong = 0
        self.numSongs = 4
        self.songs = ["CHAIR", "TEDDYBEAR", "BICYCLE", "DOOR"]


    def click(self, x, y, button, press):
        if not press:
        	return

        if button == 1:
        	nextSong = (curSong + 1) % self.numSongs
        	playSong(nextSong)
        	self.curSong = nextSong

        if button == 2:
        	nextSong = (curSong - 1)
        	if nextSong == -1:
        		nextSong = 4
        	self.playSong(nextSong, True)
        	self.curSong = nextSong

    def playSong(self, nextSong, reverse=False):
    	subprocess.call(['killall', 'mpg123'])
    	if nextSong == 0:
    		return

    	mp3name = "mp3/"
		mp3name += self.songs[nextSong-1]
		if reverse:
			mp3name += "_REVERSE"

		mp3name += ".mp3"
		subprocess.Popen(['mpg123', mp3name])


M = MouseHandler()
M.run()
