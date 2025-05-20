from vecteurs import Vect
import milieu_aquatique.milieu_marin

class Points:
    
    def __init__(self, pos, velocity, prevX = 0, prevY = 0) -> None:
        
        self.pos = pos
        self.previousPosition = Vect(prevX,prevY)
        
        self.velocity = velocity

        
        self.acceleration = Vect(0,0)
        
        self.diam = 10
        
        self.liste_lien = []
    
    
    # Position processing during simulation
    
    def updateEuler(self, deltaTime):
        self.previousPosition = self.pos   # Save of the last position
        self.velocity += self.acceleration * deltaTime   # update the velocity with the acceleration
        self.pos += self.velocity * deltaTime   # finally we update the position
        
        

    def updatePosition(self, deltaTime):
        # Vertex integration
        """milieu_aquatique.milieu_marin.apply_water_resistance(self)"""
        
        newPos = self.pos * 2 - self.previousPosition + self.acceleration * (deltaTime * deltaTime)
        
        self.previousPosition = self.pos
        self.pos = newPos
        self.velocity += self.acceleration * deltaTime
        
    
    def UpdatePreviousPosFromDeltaTimeQuotient (self, deltaTime_quotient):
        self.previousPosition = (self.previousPosition - self.pos) * deltaTime_quotient + self.pos
        
        
    # collision management
    
    def detect_collision(self, point):
        """if two points are too close we return True""" 
        
        if (self.pos - point.pos).dist() < self.diam/2 + point.diam/2:
            return True
        return False
        
    def solve_collision(self, point):
        """if two points are too close 
        we spread them to recover a distance between the two centers of twice the radius"""
        
        longueur = (self.pos - point.pos).dist()
        Vector = (self.pos - point.pos) / longueur
        distance_a_eloigner = self.diam/2 + point.diam/2 - longueur
        
        self.pos += Vector * distance_a_eloigner/2
        point.pos -= Vector * distance_a_eloigner/2
        