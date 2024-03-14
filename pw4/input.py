import curses

def get_input(stdscr, prompt):
    curses.echo()
    stdscr.addstr(2, 0, prompt)
    stdscr.refresh()
    try:
        user_input = stdscr.getstr(3, len(prompt), 20).decode('utf-8')
    except curses.error:
        user_input = ""
    curses.noecho()
    return user_input

def get_float_input(stdscr, prompt):
    curses.echo()
    stdscr.addstr(2, 0, prompt)
    stdscr.refresh()
    try:
        user_input = float(stdscr.getstr(3, len(prompt), 20).decode('utf-8'))
    except (curses.error, ValueError):
        user_input = 0.0
    curses.noecho()
    return user_input
