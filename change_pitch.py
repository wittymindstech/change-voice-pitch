import sys
from pydub import AudioSegment
from pydub.playback import play

# take audio mp3 a first argument from command line
print ("Usage: python change_pitch.py input.wav output.wav frequency")
sound = AudioSegment.from_file(sys.argv[1], format="wav")

# shift the pitch up by half an octave (speed will increase proportionally)
#change below parameter to see change in voice pitch
octaves = float(sys.argv[3])

new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

# keep the same samples but tell the computer they ought to be played at the 
# new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# now we just convert it to a common sample rate (44.1k - standard audio CD) to 
# make sure it works in regular audio players. Other than potentially losing audio quality (if
# you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
hipitch_sound = hipitch_sound.set_frame_rate(44100)

#Play pitch changed sound
play(hipitch_sound)

#export / save pitch changed sound
hipitch_sound.export(sys.argv[2], format="wav")
