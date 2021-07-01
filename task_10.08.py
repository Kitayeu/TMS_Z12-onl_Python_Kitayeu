from csv_utils import read, write, add_line, delete_line

filename = "F:/Python/lesson_08/product_information.csv"
fields = ['Product name', 'Price', 'Quantity', 'Comment']
rows = [
    ['Television set', '6000', '5', 'high quality'],
    ['Fridge', '25000', '8', 'high quality'],
    ['Iron', '2000', '3', 'high quality'],
    ['Vacuum cleaner', '3000', '12', 'high quality'],
    ['Teapot', '1200', '25', 'high quality'],
    ['Blender', '3000', '15', 'high quality'],
    ['Food processor', '7800', '11', 'high quality'],
    ['Microwave oven', '4500', '30', 'high quality'],
]
write(filename, fields, rows)
read(filename)
new_row = ['Fan', '1500', '18', 'high quality']
add_line(filename, new_row)
read(filename)
delete_line(filename, 3)
read(filename)
