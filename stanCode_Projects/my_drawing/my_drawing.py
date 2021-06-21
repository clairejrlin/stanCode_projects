"""
File: My drawing - The neuron cell cycle of brain neural development
Name:Claire Lin
----------------------
TODO: The cell cycle of brain neural development. It's also like a programming.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


window = GWindow(width=1200, height=500, title='Brain neural development')


def main():
    """
    TODO: The cell cycle of brain neural development. It's also like a programming.
    """
    lines()
    g1_s_cell()
    s_cell()
    g2_cell()
    m_cell()
    g1_cell()
    g1_s2_cell()
    neurons()
    word()
    arrow()


def g1_s_cell():
    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'lightblue'
    neuron.fill_color = 'lightblue'
    window.add(neuron, x=100, y=280)
    line = GLine(140, 200, 140, 200)
    line.color = 'gray'
    window.add(line)
    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 110, 270)
    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 100, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 96, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 110, 340)
    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 125, 70)
    arc = GArc(7, 110, 270, 260)  # on first fiber
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 121, 60)
    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 123, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 116, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 127, 20)
    fiber = GArc(7, 80, 95, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 120, 340)
    arc = GArc(35, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 109, 386)
    arc = GArc(35, 110, 215, 95)  # cell head
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 112, 225)
    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'wheat'
    nucleus.fill_color = 'wheat'
    window.add(nucleus, x=105, y=290)



    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'lightblue'
    neuron.fill_color = 'lightblue'
    window.add(neuron, x=150, y=280)
    line = GLine(190, 200, 190, 200)
    line.color = 'gray'
    window.add(line)
    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 160, 270)
    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 150, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 146, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 160, 340)
    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 175, 70)
    arc = GArc(7, 110, 270, 260)  # on first fiber
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 171, 60)
    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 173, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 166, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 177, 20)
    fiber = GArc(7, 80, 95, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 170, 340)
    arc = GArc(35, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 159, 386)
    arc = GArc(35, 110, 215, 95)  # cell head
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 162, 225)
    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'wheat'
    nucleus.fill_color = 'wheat'
    window.add(nucleus, x=155, y=290)


    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'skyblue'
    neuron.fill_color = 'skyblue'
    window.add(neuron, x=120, y=280)
    line = GLine(160, 200, 160, 200)
    line.color = 'gray'
    window.add(line)
    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 130, 270)
    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 120, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 116, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 130, 340)
    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 145, 70)
    arc = GArc(7, 110, 270, 260)   # on first fiber
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 141, 60)
    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 143, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 136, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 147, 20)
    fiber = GArc(7, 80, 95, 180)   # second fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 140, 340)
    arc = GArc(35, 80, 230, 90)   # cell bottom
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 129, 386)
    arc = GArc(35, 110, 215, 95)   # cell head
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 132, 225)
    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, x=125, y=290)


def s_cell():
    neuron = GOval(width=40, height=70)
    neuron.filled = True
    neuron.color = 'skyblue'
    neuron.fill_color = 'skyblue'
    window.add(neuron, x=238, y=227)
    neuron = GOval(width=40, height=50)
    neuron.filled = True
    neuron.color = 'skyblue'
    neuron.fill_color = 'skyblue'
    window.add(neuron, x=231, y=240)
    arc = GArc(55, 65, 60, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 221, 230)

    arc = GArc(80, 100, 210, 85)   # neuron head
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 235, 192)

    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 260, 70)
    fiber = GArc(5, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 263, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 255, 25)
    head = GArc(25, 70, 30, 70)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 262, 22)

    fiber = GArc(9, 140, 80, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 242, 290)

    arc = GArc(30, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 231, 386)

    arc = GArc(35, 80, 22, 113)  # cell bottom
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 231, 283)

    arc = GArc(57, 45, 60, 170)  # cell bottom
    arc.filled = True
    arc.color = 'orange'
    arc.fill_color = 'orange'
    window.add(arc, 233, 233)
    arc = GArc(50, 50, 250, 150)  # cell bottom
    arc.filled = True
    arc.color = 'orange'
    arc.fill_color = 'orange'
    window.add(arc, 232, 228)


def g2_cell():
    cell = GArc(80, 80, 80, 180)  # left cell body
    cell.filled = True
    cell.color = 'skyblue'
    cell.fill_color = 'skyblue'
    window.add(cell, 340, 300)
    cell = GArc(80, 80, 265, 180)  # right cell body
    cell.filled = True
    cell.color = 'skyblue'
    cell.fill_color = 'skyblue'
    window.add(cell, 338, 298)

    bottom = GArc(50, 50, 50, 80)
    bottom.filled = True
    bottom.color = 'skyblue'
    bottom.fill_color = 'skyblue'
    window.add(bottom, 344, 370)
    head = GArc(50, 60, 230, 70)
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 350, 277)

    fiber = GArc(10, 240, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 360, 70)
    fiber = GArc(5, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 363, 28)
    head = GArc(6, 50, 330, 190)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 355, 20)
    head = GArc(25, 70, 30, 60)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 362, 22)

    nucleus = GArc(40, 50, 70, 180)  # left cell nucleus
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 350, 315)
    nucleus = GArc(35, 50, 255, 180)  # right cell body nucleus
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 350, 313)

    fiber = GArc(9, 40, 80, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 358, 380)

    arc = GArc(50, 50, 240, 70)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 345, 398)


def m_cell():
    cell = GArc(170, 65, 90, 180)  # left cell body
    cell.filled = True
    cell.color = 'skyblue'
    cell.fill_color = 'skyblue'
    window.add(cell, 430, 356)
    cell = GArc(175, 65, 270, 180)  # right cell body
    cell.filled = True
    cell.color = 'skyblue'
    cell.fill_color = 'skyblue'
    window.add(cell, 432, 356)

    head = GArc(70, 80, 236, 100)
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 433, 328)

    fiber = GArc(10, 290, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 458, 70)
    fiber = GArc(5, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 461, 28)
    head = GArc(6, 53, 340, 180)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 453, 20)
    head = GArc(25, 90, 30, 60)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 460, 22)

    chromosome = GArc(10, 30, 140, 180)   # chromosome 1
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 473, 360)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 473, 360)
    chromosome = GArc(10, 20, 140, 180)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 465, 355)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 465, 370)

    chromosome = GArc(10, 30, 140, 180)  # chromosome 2
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 473, 368)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 473, 368)
    chromosome = GArc(10, 20, 140, 180)
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 465, 363)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 465, 378)

    chromosome = GArc(10, 30, 140, 180)  # chromosome 3
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 473, 376)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 473, 376)
    chromosome = GArc(10, 20, 140, 180)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 465, 371)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 465, 386)

    chromosome = GArc(10, 30, 140, 180)  # chromosome 4
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 473, 388)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 473, 388)
    chromosome = GArc(10, 20, 140, 180)
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 465, 383)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'darkorange'
    chromosome.fill_color = 'darkorange'
    window.add(chromosome, 465, 390)

    chromosome = GArc(10, 30, 140, 180)  # chromosome 5
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 473, 396)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 473, 398)
    chromosome = GArc(10, 20, 140, 180)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 465, 390)
    chromosome = GArc(10, 20, 60, 190)
    chromosome.filled = True
    chromosome.color = 'orange'
    chromosome.fill_color = 'orange'
    window.add(chromosome, 465, 402)

    microtubule = GArc(30, 60, 40, 140)
    microtubule.color = 'white'
    window.add(microtubule, 446, 370)
    microtubule = GArc(30, 65, 60, 100)
    microtubule.color = 'white'
    window.add(microtubule, 446, 380)
    microtubule = GArc(30, 50, 190, 140)
    microtubule.color = 'white'
    window.add(microtubule, 446, 375)
    microtubule = GArc(30, 50, 180, 120)
    microtubule.color = 'white'
    window.add(microtubule, 446, 380)
    microtubule = GArc(25, 50, 160, 150)
    microtubule.color = 'white'
    window.add(microtubule, 446, 380)
    microtubule = GArc(25, 50, 240, 100)
    microtubule.color = 'white'
    window.add(microtubule, 446, 375)
    microtubule = GArc(25, 50, 240, 100)
    microtubule.color = 'white'
    window.add(microtubule, 426, 377)
    microtubule = GArc(35, 50, 265, 90)
    microtubule.color = 'white'
    window.add(microtubule, 426, 377)
    microtubule = GArc(35, 50, 195, 90)
    microtubule.color = 'white'
    window.add(microtubule, 430, 368)
    microtubule = GArc(35, 50, 175, 90)
    microtubule.color = 'white'
    window.add(microtubule, 438, 360)

    microtubule = GArc(35, 50, 195, 90)   # microtubule right
    microtubule.color = 'white'
    window.add(microtubule, 505, 380)
    microtubule = GArc(35, 45, 170, 90)
    microtubule.color = 'white'
    window.add(microtubule, 503, 380)
    microtubule = GArc(35, 45, 110, 100)
    microtubule.color = 'white'
    window.add(microtubule, 497, 390)
    microtubule = GArc(45, 60, 80, 110)
    microtubule.color = 'white'
    window.add(microtubule, 490, 390)

    microtubule = GArc(40, 50, 60, 110)
    microtubule.color = 'white'
    window.add(microtubule, 495, 385)
    microtubule = GArc(40, 50, 90, 90)
    microtubule.color = 'white'
    window.add(microtubule, 502, 375)
    microtubule = GArc(40, 50, 90, 90)
    microtubule.color = 'white'
    window.add(microtubule, 502, 375)
    microtubule = GArc(20, 40, 60, 145)
    microtubule.color = 'white'
    window.add(microtubule, 500, 365)
    microtubule = GArc(20, 20, 20, 165)
    microtubule.color = 'white'
    window.add(microtubule, 485, 386)
    microtubule = GArc(30, 60, 10, 110)
    microtubule.color = 'white'
    window.add(microtubule, 480, 380)
    microtubule = GArc(40, 70, 5, 120)
    microtubule.color = 'white'
    window.add(microtubule, 470, 370)

    centrosome = GOval(width=5, height=5)   # centrosome
    centrosome.filled = True
    centrosome.color = 'darksalmon'
    centrosome.fill_color = 'darksalmon'
    window.add(centrosome, 443, 385)
    centrosome = GOval(width=5, height=5)
    centrosome.filled = True
    centrosome.color = 'darksalmon'
    centrosome.fill_color = 'darksalmon'
    window.add(centrosome, 500, 385)

    cell = GArc(95, 65, 90, 180)  # left cell body
    cell.filled = True
    cell.color = 'skyblue'
    cell.fill_color = 'skyblue'
    window.add(cell, 545, 356)
    cell = GArc(100, 60, 270, 180)  # right cell body
    cell.filled = True
    cell.color = 'skyblue'
    cell.fill_color = 'skyblue'
    window.add(cell, 545, 360)
    head = GArc(70, 80, 236, 70)
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 549, 328)

    nucleus = GOval(width=25, height=40)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 555, 370)

    fiber = GArc(10, 290, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 567, 70)
    fiber = GArc(5, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 568, 28)
    head = GArc(6, 53, 340, 180)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 560, 20)
    head = GArc(25, 90, 30, 62)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 567, 28)

    fiber = GArc(7, 10, 75, 180)  # on second fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 568, 415)

    cell = GArc(95, 70, 90, 180)  # left cell body
    cell.filled = True
    cell.color = 'steelblue'
    cell.fill_color = 'steelblue'
    window.add(cell, 573, 305)
    cell = GArc(100, 70, 270, 180)  # right cell body
    cell.filled = True
    cell.color = 'steelblue'
    cell.fill_color = 'steelblue'
    window.add(cell, 573, 305)
    head = GArc(70, 90, 60, 86)
    head.filled = True
    head.color = 'steelblue'
    head.fill_color = 'steelblue'
    window.add(head, 579, 358)
    fiber = GArc(12, 80, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 598, 345)
    arc = GArc(70, 60, 250, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 582, 393)
    nucleus = GOval(width=25, height=40)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 585, 320)


def g1_cell():
    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'skyblue'
    neuron.fill_color = 'skyblue'
    window.add(neuron, 650, 280)

    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 660, 270)

    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 650, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 646, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 660, 340)

    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 675, 70)
    arc = GArc(7, 110, 270, 260)  # on first fiber
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 671, 60)
    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 673, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 666, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 677, 20)

    fiber = GArc(7, 80, 95, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 670, 340)

    arc = GArc(35, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 659, 386)

    arc = GArc(35, 110, 215, 95)  # cell head
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 662, 225)

    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 655, 290)

    body = GOval(width=40, height=40)
    body.filled = True
    body.color = 'steelblue'
    body.fill_color = 'steelblue'
    window.add(body, 700, 190)

    arc = GArc(10, 60, 60, 250)   # foot 1
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 718, 150)
    head = GArc(50, 60, 230, 70)
    head.filled = True
    head.color = 'steelblue'
    head.fill_color = 'steelblue'
    window.add(head, 707, 167)

    arc = GArc(250, 100, 150, 25)  # foot 2
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 658, 190)
    head = GArc(50, 60, 300, 70)
    head.filled = True
    head.color = 'steelblue'
    head.fill_color = 'steelblue'
    window.add(head, 682, 184)

    arc = GArc(260, 110, 150, 25)  # foot 3
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 725, 195)
    head = GArc(50, 70, 150, 80)
    head.filled = True
    head.color = 'steelblue'
    head.fill_color = 'steelblue'
    window.add(head, 732, 184)

    arc = GArc(15, 45, 150, 160)  # foot 4
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 730, 208)

    arc = GArc(12, 80, 50, 160)  # foot 5
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 700, 224)

    nucleus = GOval(width=20, height=22)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 712, 195)


def g1_s2_cell():

    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'skyblue'
    neuron.fill_color = 'skyblue'
    window.add(neuron, 800, 280)

    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 810, 270)

    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 800, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 796, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 810, 340)

    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 825, 70)

    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 823, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 816, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'skyblue'
    head.fill_color = 'skyblue'
    window.add(head, 827, 20)

    fiber = GArc(7, 80, 95, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'skyblue'
    fiber.fill_color = 'skyblue'
    window.add(fiber, 820, 340)

    arc = GArc(35, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 809, 386)

    arc = GArc(35, 110, 215, 95)  # cell head
    arc.filled = True
    arc.color = 'skyblue'
    arc.fill_color = 'skyblue'
    window.add(arc, 812, 225)

    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 805, 290)

    neuron = GArc(120, 60, 270, 180)
    neuron.filled = True
    neuron.color = 'steelblue'
    neuron.fill_color = 'steelblue'
    window.add(neuron, 810, 150)
    neuron = GArc(35, 60, 90, 180)
    neuron.filled = True
    neuron.color = 'steelblue'
    neuron.fill_color = 'steelblue'
    window.add(neuron, 830, 150)

    fiber = GArc(20, 90, 270, 190)
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 826, 70)

    fiber = GArc(50, 70, 140, 90)
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 832, 115)

    fiber = GArc(15, 105, 270, 190)
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 828, 170)

    arc = GArc(160, 11, 120, 210)  # foot
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 830, 271)
    head = GArc(50, 70, 240, 50)
    head.filled = True
    head.color = 'steelblue'
    head.fill_color = 'steelblue'
    window.add(head, 823, 245)
    arc = GArc(15, 100, 190, 100)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 920, 251)
    arc = GArc(10, 45, 190, 100)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 950, 255)

    nucleus = GOval(width=20, height=30)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 840, 165)


def lines():
    line = GLine(50, 425, 1150, 425)
    line.color = 'gray'
    window.add(line)

    line = GLine(50, 18, 1150, 18)
    line.color = 'gray'
    window.add(line)

    line = GLine(50, 300, 1150, 300)
    line.color = 'gray'
    window.add(line)

    line = GLine(50, 190, 1150, 190)
    line.color = 'gray'
    window.add(line)


def neurons():
    cell = GArc(80, 80, 80, 180)  # left cell body
    cell.filled = True
    cell.color = 'lightblue'
    cell.fill_color = 'lightblue'
    window.add(cell, 1050, 300)
    cell = GArc(80, 80, 265, 180)  # right cell body
    cell.filled = True
    cell.color = 'lightblue'
    cell.fill_color = 'lightblue'
    window.add(cell, 1048, 298)
    bottom = GArc(50, 50, 50, 80)
    bottom.filled = True
    bottom.color = 'lightblue'
    bottom.fill_color = 'lightblue'
    window.add(bottom, 1054, 370)
    head = GArc(50, 60, 230, 70)
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1060, 277)
    # fiber = GArc(10, 240, 95, 180)  # first fiber
    # fiber.filled = True
    # fiber.color = 'lightblue'
    # fiber.fill_color = 'lightblue'
    # window.add(fiber, 1070, 70)
    # fiber = GArc(5, 110, 75, 180)  # on first fiber
    # fiber.filled = True
    # fiber.color = 'lightblue'
    # fiber.fill_color = 'lightblue'
    # window.add(fiber, 1073, 28)
    head = GArc(6, 50, 330, 190)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1065, 20)
    head = GArc(25, 70, 30, 60)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1072, 22)
    nucleus = GArc(40, 50, 70, 180)  # left cell nucleus
    nucleus.filled = True
    nucleus.color = 'wheat'
    nucleus.fill_color = 'wheat'
    window.add(nucleus, 1060, 315)
    nucleus = GArc(35, 50, 255, 180)  # right cell body nucleus
    nucleus.filled = True
    nucleus.color = 'wheat'
    nucleus.fill_color = 'wheat'
    window.add(nucleus, 1060, 313)
    fiber = GArc(9, 40, 80, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1068, 380)
    arc = GArc(50, 50, 240, 70)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1055, 398)






    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'lightblue'
    neuron.fill_color = 'lightblue'
    window.add(neuron, x=990, y=280)
    line = GLine(140, 1090, 140, 1090)
    line.color = 'gray'
    window.add(line)
    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1000, 270)
    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 990, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 986, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1000, 340)
    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1015, 70)
    arc = GArc(7, 110, 270, 260)  # on first fiber
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1011, 60)
    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1013, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1006, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1017, 20)
    fiber = GArc(7, 80, 95, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1010, 340)
    arc = GArc(35, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 999, 386)
    arc = GArc(35, 110, 215, 95)  # cell head
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1002, 225)
    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'wheat'
    nucleus.fill_color = 'wheat'
    window.add(nucleus, x=995, y=290)


    neuron = GOval(width=40, height=60)
    neuron.filled = True
    neuron.color = 'lightblue'
    neuron.fill_color = 'lightblue'
    window.add(neuron, x=1090, y=280)
    line = GLine(140, 1190, 140, 1190)
    line.color = 'gray'
    window.add(line)
    arc = GArc(50, 80, 250, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1100, 270)
    arc = GArc(55, 95, 70, 210)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1090, 265)
    arc = GArc(40, 70, 80, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1086, 280)
    arc = GArc(35, 110, 45, 85)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1100, 340)
    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1115, 70)
    arc = GArc(7, 110, 270, 260)  # on first fiber
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1111, 60)
    fiber = GArc(9, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1113, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1106, 25)
    head = GArc(5, 55, 200, 170)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1117, 20)
    fiber = GArc(7, 80, 95, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1110, 340)
    arc = GArc(35, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1099, 386)
    arc = GArc(35, 110, 215, 95)  # cell head
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1102, 225)
    nucleus = GOval(width=25, height=45)
    nucleus.filled = True
    nucleus.color = 'wheat'
    nucleus.fill_color = 'wheat'
    window.add(nucleus, x=1095, y=290)

    neuron = GOval(width=40, height=70)
    neuron.filled = True
    neuron.color = 'lightblue'
    neuron.fill_color = 'lightblue'
    window.add(neuron, x=1038, y=227)
    neuron = GOval(width=40, height=50)
    neuron.filled = True
    neuron.color = 'lightblue'
    neuron.fill_color = 'lightblue'
    window.add(neuron, x=1031, y=240)
    arc = GArc(55, 65, 60, 200)
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1021, 230)
    arc = GArc(80, 100, 210, 85)  # neuron head
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1035, 192)
    fiber = GArc(10, 210, 95, 180)  # first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1060, 70)
    fiber = GArc(5, 110, 75, 180)  # on first fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1063, 28)
    head = GArc(6, 40, 330, 200)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1055, 25)
    head = GArc(25, 70, 30, 70)  # on first fiber head
    head.filled = True
    head.color = 'lightblue'
    head.fill_color = 'lightblue'
    window.add(head, 1062, 22)
    fiber = GArc(9, 140, 80, 180)  # second fiber
    fiber.filled = True
    fiber.color = 'lightblue'
    fiber.fill_color = 'lightblue'
    window.add(fiber, 1042, 290)
    arc = GArc(30, 80, 230, 90)  # cell bottom
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1031, 386)
    arc = GArc(35, 80, 22, 113)  # cell bottom
    arc.filled = True
    arc.color = 'lightblue'
    arc.fill_color = 'lightblue'
    window.add(arc, 1031, 283)
    arc = GArc(57, 45, 60, 170)  # cell bottom
    arc.filled = True
    arc.color = 'wheat'
    arc.fill_color = 'wheat'
    window.add(arc, 1033, 233)
    arc = GArc(50, 50, 250, 150)  # cell bottom
    arc.filled = True
    arc.color = 'wheat'
    arc.fill_color = 'wheat'
    window.add(arc, 1032, 228)




    neuron = GOval(width=40, height=45)
    neuron.filled = True
    neuron.color = 'steelblue'
    neuron.fill_color = 'steelblue'
    window.add(neuron, x=1029, y=64)
    arc = GArc(100, 100, 240, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1026, 23)
    arc = GArc(135, 135, 350, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 975, 70)
    arc = GArc(145, 130, 130, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1052, 70)
    fiber = GArc(20, 50, 270, 190)
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 1040, 24)
    arc = GArc(175, 17, 80, 130)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 980, 98)
    arc = GArc(180, 15, 300, 150)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1030, 95)
    nucleus = GOval(20, 25)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 1040, 70)



    neuron = GOval(width=40, height=45)
    neuron.filled = True
    neuron.color = 'steelblue'
    neuron.fill_color = 'steelblue'
    window.add(neuron, x=1089, y=74)
    arc = GArc(100, 100, 240, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1086, 33)
    arc = GArc(135, 135, 350, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1035, 80)
    arc = GArc(145, 130, 130, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1112, 80)
    fiber = GArc(20, 50, 270, 190)
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 1100, 34)
    arc = GArc(175, 17, 80, 130)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1040, 108)
    arc = GArc(180, 15, 300, 150)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 1090, 105)
    nucleus = GOval(20, 25)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 1100, 80)

    neuron = GOval(width=40, height=45)
    neuron.filled = True
    neuron.color = 'steelblue'
    neuron.fill_color = 'steelblue'
    window.add(neuron, x=969, y=84)
    arc = GArc(100, 100, 240, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 966, 43)
    arc = GArc(135, 135, 350, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 915, 90)
    arc = GArc(145, 130, 130, 60)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 992, 90)
    fiber = GArc(20, 70, 270, 190)
    fiber.filled = True
    fiber.color = 'steelblue'
    fiber.fill_color = 'steelblue'
    window.add(fiber, 980, 24)
    arc = GArc(175, 17, 80, 130)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 920, 118)
    arc = GArc(180, 15, 300, 150)
    arc.filled = True
    arc.color = 'steelblue'
    arc.fill_color = 'steelblue'
    window.add(arc, 970, 115)
    nucleus = GOval(20, 25)
    nucleus.filled = True
    nucleus.color = 'orange'
    nucleus.fill_color = 'orange'
    window.add(nucleus, 980, 90)


def word():
    label = GLabel('G1/S')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 120, 460)

    label = GLabel('S')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 240, 460)

    label = GLabel('G2')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 350, 460)

    label = GLabel('M')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 520, 460)

    label = GLabel('G1')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 690, 460)

    label = GLabel('G1/S')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 810, 460)

    label = GLabel('VZ')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 50, 370)

    label = GLabel('SVZ')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 45, 250)

    label = GLabel('IZ')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 52, 175)

    label = GLabel('CP')
    label.font = '-15'
    label.filled = True
    label.color = 'black'
    window.add(label, 52, 55)

    citation = GLabel('J Cell Biol. 2005 Sep 12;170(6):935-45.')
    citation.font = '-8'
    citation.filled = True
    citation.color = 'black'
    window.add(citation, 1000, 490)


def arrow():
    point = GRect(3, 60)
    point.filled = True
    point.color = 'darkgray'
    point.fill_color = 'darkgray'
    window.add(point, 160, 350)
    arc = GArc(60, 60, 240, 60)
    arc.filled = True
    arc.color = 'darkgray'
    arc.fill_color = 'darkgray'
    window.add(arc, 147, 323)

    point = GRect(3, 60)
    point.filled = True
    point.color = 'darkgray'
    point.fill_color = 'darkgray'
    window.add(point, 280, 270)
    arc = GArc(60, 60, 60, 60)
    arc.filled = True
    arc.color = 'darkgray'
    arc.fill_color = 'darkgray'
    window.add(arc, 266, 323)

    # point = GRect(3, 60)
    # point.filled = True
    # point.color = 'darkgray'
    # point.fill_color = 'darkgray'
    # window.add(point, 383, 340)
    # arc = GArc(60, 60, 60, 60)
    # arc.filled = True
    # arc.color = 'darkgray'
    # arc.fill_color = 'darkgray'
    # window.add(arc, 369, 393)

    point = GRect(15, 3)
    point.filled = True
    point.color = 'darkgray'
    point.fill_color = 'darkgray'
    window.add(point, 523, 390)
    arc = GArc(50, 50, 150, 60)
    arc.filled = True
    arc.color = 'darkgray'
    arc.fill_color = 'darkgray'
    window.add(arc, 529, 379)

    arc = GArc(180, 7, 80, 130)
    arc.filled = True
    arc.color = 'darkgray'
    arc.fill_color = 'darkgray'
    window.add(arc, 749, 182)
    arc = GArc(60, 60, 160, 60)
    arc.filled = True
    arc.color = 'darkgray'
    arc.fill_color = 'darkgray'
    window.add(arc, 795, 167)

    point = GRect(3, 60)
    point.filled = True
    point.color = 'darkgray'
    point.fill_color = 'darkgray'
    window.add(point, 875, 120)
    arc = GArc(60, 60, 240, 60)
    arc.filled = True
    arc.color = 'darkgray'
    arc.fill_color = 'darkgray'
    window.add(arc, 862, 93)










if __name__ == '__main__':
    main()
