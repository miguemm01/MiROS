#define VIDEO_ADDRESS 0xb8000
#define MAX_ROWS 25
#define MAX_COLS 80
//DEFAULT COLOR SCHEME
#define WHITE_ON_BLACK 0x0f

//Screen IO ports
#define REG_SCREEN_CTRL 0x3D4
#define REG_SCREEN_DATA 0x3D5

int get_screen_offset(int col, int row);
int get_cursor();
void set_cursor(int offset);
void print_at(char* message, int col, int row);
void print(char* message);
void printf(char* message);
void clearscr();
int handle_scrolling(int cursor_offset);