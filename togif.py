# Author:   Stephen Leitnick
# Date:     July 17, 2017
# License:  MIT (see LICENSE file)

from subprocess import call
from tempfile import gettempdir
import os

PALETTE_NAME = os.path.join(gettempdir(), "pallete.png")

os.system("cls" if os.name=="nt" else "clear")
print("\n  ToGif - Convert Video to GIF\n")

# Inputs from user:
video_file = raw_input("  Video File: ")
gif_file   = raw_input("    GIF File: ")
fps        = raw_input("         FPS: ")
start      = raw_input("       Start: ")
length     = raw_input("      Length: ")
scale      = raw_input("       Scale: ")

# Call ffmpeg to convert video to GIF:
call(["ffmpeg", "-y", "-ss", start, "-t", length, "-i", video_file, "-vf", "fps=" + fps + ",scale=" + scale + ":-1:flags=lanczos,palettegen", PALETTE_NAME])
call(["ffmpeg", "-ss", start, "-t", length, "-i", video_file, "-i", PALETTE_NAME, "-filter_complex", "fps=" + fps + ",scale=" + scale + ":-1:flags=lanczos[x];[x][1:v]paletteuse", gif_file])

# Remove temporary palette image created from ffmpeg:
os.remove(PALETTE_NAME)

print("\nGIF created: " + gif_file + "\n")
