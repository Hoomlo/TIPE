
import math
    

def update(creature, stepCount, delta_time_produit: float, delta_time_prev):
    
    creature.fonctionnement_liens()
    creature.traitement_collision()
    creature.mouvement_creature(stepCount, delta_time_produit, delta_time_prev)
    