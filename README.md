# Time Tracker
Track the amount of time spent using each application

### Requirements
- Python 3
- GCC
- Windows 2000 or greater (unfortunately it's Windows-only for now, looking to expand it to Linux and OS X)

### Get it up and running

1. Compile the C program

```bash
gcc get_window.c -o get_window 
```

2. Run `track.py`

```bash
python track.py
```

### Optional Config

You can update some basic configs in `track.py` such as:

- `RESOLUTION` - how often you want to check for the active window (default is 3 seconds)
- `WRITE_INTERVAL` - append the updated stats to the file every `WRITE_INTERVAL * RESOLUTION` seconds
- `STATS_FILE` - path to the stats file. This must be a valid JSON file
- `GET_WINDOW_EXEC` - path to the get_window.exe you compiled in step 1
