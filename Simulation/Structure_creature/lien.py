from Structure_creature.points import Points

class Lien:
    
    def __init__(self, pointA : Points, pointB : Points) -> None:
        
        self.A = pointA
        self.B = pointB
        
        self.thickness = 3
        self.longueur = 100 
        