import math

def yarnRequired(skeinWeight, swatchLength, swatchWidth, swatchWeight, projectLength, projectWidth):
    swatcharea = swatchLength * swatchWidth
    projectarea = projectLength * projectWidth
    percm = swatchWeight / swatcharea
    totalyarn = projectarea * percm
    adjustedyarn = totalyarn * 1.1
    skien = adjustedyarn / skeinWeight
    return math.ceil(skien)
     

if __name__ == "__main__":
    print(yarnRequired(170, 10, 10, 4, 150, 125))