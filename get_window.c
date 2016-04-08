#include <stdio.h>
#include <Windows.h>

char *get_active_window () {
	char *window_title = malloc(500);
	if(!window_title)
        return NULL;
	
	HWND foreground = GetForegroundWindow();
	if (foreground) {
		GetWindowText(foreground, window_title, 500);
	}
	
	return window_title;
}

int main () {
	char *current_window = get_active_window();
	printf("%s", current_window);
	free(current_window);

	return(0);
}