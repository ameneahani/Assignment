import pysynth
music = (('a',2),('b',1),('c',2),('d',4),('e',4),('f',2),('g',8))

pysynth.make_wav(music, fn = "my_music.wave")