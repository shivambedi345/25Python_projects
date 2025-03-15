import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello welcome to the speed typing test")
    stdscr.addstr("\nPress any key to start the test")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(0, 0, target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        
    stdscr.addstr(0, i, char, color)


def load_text():
    try:
        with open("test.txt", "r") as f:
            lines = f.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        # Provide fallback text if file isn't found
        return "The quick brown fox jumps over the lazy dog."


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        # Check if the test is completed
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
            
        try:
            key = stdscr.getkey()
        except curses.error:
            # No input available
            continue
        
        # Handle key input
        if ord(key) == 27:  # Escape key
            return False  # Signal to exit the program
        elif key == "KEY_BACKSPACE" or key == '\b' or key == '\x7f':
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text) and len(key) == 1:
            # Only add printable single characters
            current_text.append(key)
    
    return True  # Signal to continue


def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Hide the cursor
    curses.curs_set(0)
    
    start_screen(stdscr)
    
    while True:
        continue_game = wpm_test(stdscr)
        
        if not continue_game:
            break
            
        # Display completion message
        stdscr.nodelay(False)
        stdscr.clear()
        stdscr.addstr(0, 0, "You completed the text! Press any key to "
                            "continue...")
        stdscr.addstr(1, 0, "Press ESC to exit")
        stdscr.refresh()
        
        # Wait for user input
        key = stdscr.getkey()
        if ord(key) == 27:  # Escape key
        break


if __name__ == "__main__":
    wrapper(main)