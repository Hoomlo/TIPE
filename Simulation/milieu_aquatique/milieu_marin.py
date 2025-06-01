from vecteurs import Vect

WATER_RESISTANCE = 0.05

def apply_water_resistance(point):
    """applique la resistance de l'eau proportionelle a la vitesse de chaque point"""
    point.acceleration = point.velocity * (-WATER_RESISTANCE)
    
    