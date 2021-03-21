import sys
import wave

CHANNELS = 1
swidth = 2
Change_RATE = float(sys.argv[3])


print ("Usage Python change_speed.py input.wav output.wav changerate")
spf = wave.open(sys.argv[1], 'rb')
RATE=spf.getframerate()
signal = spf.readframes(-1)

print ("saving in...",sys.argv[2])
wf = wave.open(sys.argv[2], 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(RATE*Change_RATE)
wf.writeframes(signal)
wf.close()
