import time
import subprocess
from collections import Counter
import json
import ctypes

user32 = ctypes.windll.user32

RESOLUTION = 3
WRITE_INTERVAL = 10 # write to file every WRITE_INTERVAL * RESOLUTION seconds
STATS_FILE = 'stats.json'

def main ():
	windows = {}
	iteration = 0
	
	while True:
		window_title = get_window_title()
		if window_title in windows:
			windows[window_title] = windows[window_title] + RESOLUTION
		else:
			windows[window_title] = RESOLUTION
				
		if iteration == WRITE_INTERVAL:
			with open(STATS_FILE, 'r') as f:
				old_stats = Counter(json.load(f))
				new_stats = Counter(windows)
				merged_stats = old_stats + new_stats
			
			with open(STATS_FILE, 'w') as f:
				merged_stats_json = json.dumps(merged_stats, indent=4)
				f.write(merged_stats_json)
			
			iteration = 0
		else:
			time.sleep(RESOLUTION)
		
		iteration = iteration + 1

def get_window_title():
    hwnd = user32.GetForegroundWindow()
    title_length = user32.GetWindowTextLengthW(hwnd)
    title = ctypes.create_unicode_buffer(title_length + 1)
    user32.GetWindowTextW(hwnd, title, title_length + 1)

    return title.value

if __name__ == '__main__':
	main()