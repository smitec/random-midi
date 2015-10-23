from mido import MidiFile, MidiTrack, Message
import random

mid = MidiFile(type=0)

track = MidiTrack()

mid.tracks.append(track)

notes = range(40, 90)

for i in range(20):
    note = random.choice(notes)
    track.append(Message('note_on', note=note, velocity=100, time=i*100))
    track.append(Message('note_off', note=note, velocity=100, time=(i+1)*100))

mid.save('random.mid')

