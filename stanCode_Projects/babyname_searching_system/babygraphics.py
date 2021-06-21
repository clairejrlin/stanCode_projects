"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This is for showing the trend of baby names every year.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'orange']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    distance = (width-2*GRAPH_MARGIN_SIZE) / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + (distance*year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH-GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), (CANVAS_WIDTH-GRAPH_MARGIN_SIZE),
                       (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE))

    for year_index in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text((x_coordinate+TEXT_DX), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[year_index], anchor=tkinter.NW, font='times 10')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    for name in lookup_names:
        if name in name_data:
            for i in range(len(lookup_names)):

                x1, y1, year_index = 0, 0, 0
                for year in YEARS:
                    if str(year) in name_data[lookup_names[i]]:
                        # print(name_data[name][str(year)]) <-- for check
                        # Every files only records 1000 baby names.
                        # so if it's in rank 1000, then it shows up the year.

                        start_x = get_x_coordinate(CANVAS_WIDTH, year_index)   # set the point
                        size = CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE
                        start_y = (int(name_data[lookup_names[i]][str(year)])/1000)*size+GRAPH_MARGIN_SIZE

                        canvas.create_text(start_x+TEXT_DX, start_y,
                                           text=lookup_names[i] + str(' ') + name_data[lookup_names[i]][str(year)],
                                           anchor=tkinter.SW, font='calibri 11', fill=COLORS[i % 5])

                        if str(year) == str(YEARS[0]):
                            x1 = start_x
                            y1 = start_y
                        else:
                            x2 = start_x
                            y2 = start_y
                            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[i % 5])
                            x1 = x2
                            y1 = y2
                        year_index += 1

                    elif str(year) not in name_data[lookup_names[i]]:
                        # If it's not in rank 1000, it would not have the year.

                        start_x = get_x_coordinate(CANVAS_WIDTH, year_index)   # set the point
                        start_y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

                        canvas.create_text(start_x+TEXT_DX, start_y2,
                                           text=lookup_names[i] + str(' ') + str('*'),
                                           anchor=tkinter.SW, font='calibri 11', fill=COLORS[i % 5])

                        if str(year) == str(YEARS[0]):
                            x1 = start_x
                            y1 = start_y2
                        else:
                            x2 = start_x
                            y2 = start_y2
                            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[i % 5])
                            x1 = x2
                            y1 = y2
                        year_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
