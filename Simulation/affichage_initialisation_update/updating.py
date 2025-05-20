
import math
    

def update(creature, stepCount, delta_time_produit: float, delta_time_prev):
        
    # if the two points are not at the correct distance then a force of attraction or repulsion is applied
    for lien in creature.list_of_link:
            
        longueur = (lien.A.pos - lien.B.pos).dist()
        
        distance_a_rapprocher = longueur - lien.longueur
            
        Vect = (lien.B.pos - lien.A.pos) / longueur            
            
        lien.A.pos += Vect * (distance_a_rapprocher/2)
        lien.B.pos -= Vect * (distance_a_rapprocher/2)
    
        
        
    # if there is a collision on the replacement points correctly
    for point1 in creature.list_of_points:
        for point2 in  creature.list_of_points:
            
            if point1 != point2:
                if point1.detect_collision(point2):
                        
                    point1.solve_collision(point2)
        
    
    """print("before")
    v = [s.velocity for s in creature.list_of_points]
    print(v)"""
   
        
    for point in creature.list_of_points:
        
        point.UpdatePreviousPosFromDeltaTimeQuotient(delta_time_produit / delta_time_prev)
        
        if (stepCount > 1) :
            point.updatePosition(delta_time_produit)
            
        else :
            point.updateEuler(delta_time_produit)
    
    """print("after")
    v = [s.velocity for s in creature.list_of_points]
    print(v)"""


