# ToGIF
Convert video files to GIF files.

# Dependencies
- [Python 2.7](https://www.python.org/)
- [ffmpeg](https://ffmpeg.org/)

# Usage
```
togif.py -v VIDEO_FILE -g GIF_FILE -f FPS -s START -l LENGTH -c SCALE
```
| Argument    | Alias | Description
| ----------- | ----- | -----------
| `--video`   | `-v`  | Full video filepath source
| `--gif`     | `-g`  | Full GIF filepath destination
| `--fps`     | `-f`  | GIF frames-per-second
| `--start`   | `-s`  | Starting point in video (seconds)
| `--length`  | `-l`  | Length of GIF (seconds)
| `--scale`   | `-c`  | Width of video (pixels)