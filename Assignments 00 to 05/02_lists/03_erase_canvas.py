from graphics import Canvas
import time

# --- Constants ---
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20
ERASER_COLOR = 'pink'
CELL_COLOR = 'blue'
ERASED_COLOR = 'white'
SLEEP_DURATION = 0.05


# --- Helper Functions ---
def create_cell_grid(canvas: Canvas) -> None:
    """Draws a grid of blue cells on the canvas."""
    rows = CANVAS_HEIGHT // CELL_SIZE
    cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(rows):
        for col in range(cols):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, CELL_COLOR)


def create_eraser(canvas: Canvas, x: int, y: int) -> int:
    """Creates and returns the eraser object at the given (x, y) location."""
    return canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, ERASER_COLOR)


def move_eraser_to_mouse(canvas: Canvas, eraser: int) -> None:
    """Moves the eraser to the current mouse position."""
    x = canvas.get_mouse_x()
    y = canvas.get_mouse_y()
    canvas.moveto(eraser, x, y)


def erase_overlapping_cells(canvas: Canvas, eraser: int) -> None:
    """Sets color to white for all cells overlapping with the eraser (excluding the eraser itself)."""
    x = canvas.get_mouse_x()
    y = canvas.get_mouse_y()
    x2 = x + ERASER_SIZE
    y2 = y + ERASER_SIZE

    overlapping = canvas.find_overlapping(x, y, x2, y2)

    for obj in overlapping:
        if obj != eraser:
            canvas.set_color(obj, ERASED_COLOR)


# --- Main Function ---
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    create_cell_grid(canvas)

    canvas.wait_for_click()
    start_x, start_y = canvas.get_last_click()
    eraser = create_eraser(canvas, start_x, start_y)

    while True:
        move_eraser_to_mouse(canvas, eraser)
        erase_overlapping_cells(canvas, eraser)
        time.sleep(SLEEP_DURATION)


if __name__ == '__main__':
    main()
