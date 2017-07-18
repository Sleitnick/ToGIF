# Author:   Stephen Leitnick
# Date:     July 17, 2017
# License:  MIT (see LICENSE file)

from subprocess import call
from tempfile import gettempdir
import argparse
import os

PALETTE_NAME = os.path.join(gettempdir(), "pallete.png")

#os.system("cls" if os.name=="nt" else "clear")
print("\nToGif - Convert Video to GIF\n")

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

# Command-line arguments:
parser = argparse.ArgumentParser(prog="togif")
parser.add_argument("-v", "--video", required=True)
parser.add_argument("-g", "--gif", required=True)
parser.add_argument("-f", "--fps", required=True)
parser.add_argument("-s", "--start", required=True)
parser.add_argument("-l", "--length", required=True)
parser.add_argument("-c", "--scale", required=True)
args = parser.parse_args()

# Arguments:
video_file = args.video
gif_file   = args.gif
fps        = args.fps
start      = args.start
length     = args.length
scale      = args.scale

# Argument assertions:
assert os.path.isfile(video_file), "Video file (-v, --video) argument must point to an existing file"
assert is_int(fps) and int(fps) > 0, "FPS (-f, --fps) argument must be an integer > 0"
assert is_int(start) and int(start) >= 0, "Start (-s, --start) argument must be an integer >= 0"
assert is_int(length) and int(length) > 0, "Length (-l, --length) argument must be an integer > 0"
assert is_int(scale) and int(scale) > 0, "Scale (-c, --scale) argument must be an integer > 0"

# Append '.gif' prefix to GIF file if missing:
if not gif_file.endswith(".gif"):
	print("Appending '.gif' to GIF file:")
	gif_file += ".gif"
	print(gif_file)

# FFmpeg generate pallete image:
call([
	"ffmpeg", "-y",
	"-ss", start,
	"-t", length,
	"-i", video_file,
	"-vf", "fps=" + fps + ",scale=" + scale + ":-1:flags=lanczos,palettegen", PALETTE_NAME
])

# FFmpeg generate GIF:
call([
	"ffmpeg",
	"-ss", start,
	"-t", length,
	"-i", video_file,
	"-i", PALETTE_NAME,
	"-filter_complex", "fps=" + fps + ",scale=" + scale + ":-1:flags=lanczos[x];[x][1:v]paletteuse", gif_file
])

# Remove temporary palette image created from ffmpeg:
os.remove(PALETTE_NAME)

print("\nGIF created: " + gif_file + "\n")
