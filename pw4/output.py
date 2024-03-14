import curses

def display_summary(stdscr, header_line, data):
    stdscr.clear()
    stdscr.addstr(0, 0, header_line)

    line_number = 4
    for row in data:
        stdscr.addstr(line_number, 0, row)
        line_number += 1

    stdscr.refresh()
    stdscr.getch()
