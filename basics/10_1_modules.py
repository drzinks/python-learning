import figures_module
from enum import IntEnum
Figures = IntEnum("Figures","square rectangle triangle")
def surface(figures,a,b):
    if(figures.square):
        return figures_module.square_surface(a)
    elif(figures.rectangle):
        return figures_module.rectangle_surface(a,b)
    elif(figures.triangle):
        return figures_module.triangle_surface(a,b)    
    
print(surface(Figures.square,3,0))
print(surface(Figures.rectangle,4,3))
print(surface(Figures.triangle,4,5))


