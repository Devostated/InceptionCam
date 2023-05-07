import xml.etree.ElementTree as ET
import PySimpleGUI as sg
import sys

sg.theme('SystemDefault1')
from data import images
layout = [
    [sg.Text('Enter getpos:'), sg.InputText()],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Convert')]
]
window = sg.Window('Inception Cam', layout, icon=images)


if len(sys.argv) < 2:
    sys.exit(1)
filename = sys.argv[1]

tree = ET.parse(filename)
root = tree.getroot()

def writeValues(newX, newY, newZ):
    prev_x, prev_y, prev_z = None, None, None
    xyz_list = []

    for point in root.iter('p'):
        x, y, z = float(point.get('x')), float(point.get('y')), float(point.get('z'))
        qy, qz = float(point.get('qy')), float(point.get('qz'))

        test_x, test_y, test_z = x, y, z

        if prev_x is not None:
            x_diff = test_x - prev_x
            point.set('x', str(x_diff))
        else:
            x_diff = 0

        if prev_y is not None:
            y_diff = test_y - prev_y
            point.set('y', str(y_diff))
        else:
            y_diff = 0

        if prev_z is not None:
            z_diff = test_z - prev_z
            point.set('z', str(z_diff))
        else:
            z_diff = 0
        point.set('qy', str("{:.6f}".format(-qy)))
        point.set('qz', str("{:.6f}".format(-qz)))
        xyz_list.append((x_diff, y_diff, z_diff))

        prev_x, prev_y, prev_z = x, y, z

    for loop, point in enumerate(root.iter('p')):
        x_diff, y_diff, z_diff = xyz_list[loop]

        if prev_x == 0:
            point.set('x', str("{:.6f}".format(newX)))
            newX_diff = float(newX)
        else:
            newX_diff = float(newX) - float(x_diff)
            point.set('x', str("{:.6f}".format(newX_diff)))

        if prev_y == 0:
            point.set('y', str("{:.6f}".format(newY)))
            newY_diff = float(newY)
        else:
            newY_diff = float(newY) - float(y_diff)
            point.set('y', str("{:.6f}".format(newY_diff)))

        if prev_z == 0:
            point.set('z', str("{:.6f}".format(newZ)))
            newZ_diff = float(newZ)
        else:
            newZ_diff = float(newZ) - float(z_diff)
            point.set('z', str("{:.6f}".format(newZ_diff)))

        newX, newY, newZ = newX_diff, newY_diff, newZ_diff

    prev_x, prev_y, prev_z = xyz_list[-1][0], xyz_list[-1][1], xyz_list[-1][2]

    tree.write('updated_file.xml', encoding='utf-8')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Convert':
        input_str = values[0]
        parts = input_str.split(';')[0].split()
        if len(parts) >= 3:
            if parts[0] == 'setpos':
                output_str = f'{parts[0]} {parts[1]} {parts[2]} {parts[3]}'
                window['-OUTPUT-'].update("Campath converted")
                writeValues(parts[1], parts[2], parts[3])
            else:
                output_str = f'{parts[0]} {parts[1]} {parts[2]}'
                window['-OUTPUT-'].update("Campath converted")
                writeValues(parts[0], parts[1], parts[2])
        window.close()

window.close()
