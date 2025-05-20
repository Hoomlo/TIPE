from vecteurs import Vect
from Structure_creature.points import Points
from Structure_creature.creature import Creature
from math import sqrt


def initialiser(creature):

    point1_pos = Vect(450, 600)
    point2_pos = Vect(500, 600)
    point3_pos = Vect(550, 600)
        
    point1_v = Vect(0, -100)
    point2_v = Vect(0, 0)
    point3_v = Vect(0, -100)
            
    point1 = Points(point1_pos, point1_v)
    point2 = Points(point2_pos, point2_v)
    point3 = Points(point3_pos, point3_v)
        
    list_of_points = [point1, point2, point3]
        
    creature.update_list_of_points(list_of_points)

    creature.update_list_of_link()
        
    creature.newton_sum_of_velocity_nul_on_link()
        
    
    """print("initialisation")
    
    print(point1.velocity)
    print(list_of_points[0].velocity)
    
    print(point2.velocity)
    print(list_of_points[1].velocity)
    
    print(point3.velocity)
    print(list_of_points[2].velocity)"""