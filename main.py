import colorgram
from Turtle import Hirst


def final_result(colors):
    rgb = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        x = (r, g, b)
        rgb.append(x)
    return rgb


# Extract 6 colors from an image.
num_color = 30
_colors = colorgram.extract('image.jpg', num_color)
image_colors = final_result(_colors)

Graph = Hirst(image_colors)