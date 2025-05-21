from Structure_creature.points import Points
from Structure_creature.lien import Lien
from vecteurs import Vect
import random as rd


class Creature:
    
    def __init__(self) -> None:
        
        self.list_of_points = []
        self.list_of_link = []
        
        self.horloge = rd.random() * 10
        self.nb_position = rd.randint(2, 10)
        self.time_between_pos = self.horloge / self.nb_position
        
    def update_list_of_points (self, list_of_points):
        
        self.list_of_points = [point for point in list_of_points]
    
    def update_list_of_link (self):
        n = len(self.list_of_points)
        
        for i in range(n - 1):
            self.list_of_link.append(Lien(self.list_of_points[i], self.list_of_points[i+1]))
            

    """ implementation de la première loi de newton """
    
    def cherche_indice_in_list_point(self, point):
        n = len(self.list_of_points)
        
        for i in range(n):
            if self.list_of_points[i] == point:
                return i
    
    
    def newton_sum_of_velocity_nul_on_link (self):
        
        sauv_velocity = [point.velocity for point in self.list_of_points] # sauvegarde des vitesse de chaque point
        
        n_list_point = len(self.list_of_points)
        
        # on parcours la liste des points pour crée la liste des liens tel que point appartient au lien
        for i in range(n_list_point - 1): 
            
            point = self.list_of_points[i]
            tab_lien_tq_point_C_lien = []
            
            for lien in self.list_of_link:
                
                if point == lien.A or point == lien.B:
                    tab_lien_tq_point_C_lien.append(lien)
            
            # disjonction de cas selon le nombre de lien aux quels appartient le point
            n_list_lien_de_point = len(tab_lien_tq_point_C_lien)
            
            if n_list_lien_de_point == 0: # si le lien n'appartient a aucun lien il n'y a rien a faire
                pass
            
            elif n_list_lien_de_point == 1: # si le lien appartient a un seul lien on soustrait la vitesse de l'autre point a sa vitesse
                
                if tab_lien_tq_point_C_lien[0].A == point:
                    other_point = tab_lien_tq_point_C_lien[0].B
                else:
                    other_point = tab_lien_tq_point_C_lien[0].A
                
                new_v = sauv_velocity[i] - sauv_velocity[self.cherche_indice_in_list_point(other_point)]
                point.velocity = Vect.convert_into_int(new_v)
            
            else: 
                """ si le lien appartient a plus d'un lien on soustrais
                n-1 (le nombre de lien aux quel appartient le point) fois la somme des vitesses des autres points
                à n fois la vitesse de point"""
                
                list_other_points = []
                
                
                for lien in tab_lien_tq_point_C_lien:
                    
                    if point != lien.A:
                        list_other_points.append(lien.A)
                    else:
                        list_other_points.append(lien.B)   
                
                sum_of_velocity = Vect(0,0)
                
                
                for other_point in list_other_points:

                    sum_of_velocity += sauv_velocity[self.cherche_indice_in_list_point(other_point)]
                
                
                new_v = ((n_list_lien_de_point - 1)*n_list_lien_de_point)/2 * sauv_velocity[i] - (n_list_lien_de_point - 1) * sum_of_velocity
                point.velocity = Vect.convert_into_int(new_v)
               
        """v = [s.velocity for s in self.list_of_points]
        print("\n init vel ")
        print(v)"""
                
    def fonctionnement_liens (self):
        # if the two points are not at the correct distance then a force of attraction or repulsion is applied
        for lien in self.list_of_link:
            
            longueur = (lien.A.pos - lien.B.pos).dist()
        
            distance_a_rapprocher = longueur - lien.longueur
            
            Vect = (lien.B.pos - lien.A.pos) / longueur            
            
            lien.A.pos += Vect * (distance_a_rapprocher/2)
            lien.B.pos -= Vect * (distance_a_rapprocher/2)
    
    def traitement_collision (self):
        # if there is a collision on the replacement points correctly
        for point1 in self.list_of_points:
            for point2 in self.list_of_points:
                
                if point1 != point2:
                    if point1.detect_collision(point2):
                            
                        point1.solve_collision(point2)
          
    def mouvement_creature (self, stepCount, delta_time_produit: float, delta_time_prev):
        for point in self.list_of_points:
        
            point.UpdatePreviousPosFromDeltaTimeQuotient(delta_time_produit / delta_time_prev)
            
            if (stepCount > 1) :
                point.updatePosition(delta_time_produit)
                
            else :
                point.updateEuler(delta_time_produit)    
            
                    
