import time
import subprocess
from collections import Counter
import json

RESOLUTION = 3
GET_WINDOW_EXEC = 'get_window.exe'
WRITE_INTERVAL = 3 # write to file every WRITE_INTERVAL * RESOLUTION seconds
STATS_FILE = 'stats.json'

def main ():
	windows = {}
	iteration = 0
	
	while True:
		output = subprocess.check_output(GET_WINDOW_EXEC).decode("utf-8")
		if output in windows:
			windows[output] = windows[output] + RESOLUTION
		else:
			windows[output] = RESOLUTION
				
		if iteration == WRITE_INTERVAL:
			with open(STATS_FILE, 'r') as f:
				old_stats = Counter(json.load(f))
				new_stats = Counter(windows)
				merged_stats = old_stats + new_stats
			
			with open(STATS_FILE, 'w') as f:
				merged_stats_json = json.dumps(merged_stats)
				f.write(merged_stats_json)
			
			iteration = 0
		else:
			time.sleep(RESOLUTION)
		
		iteration = iteration + 1

if __name__ == '__main__':
	main()