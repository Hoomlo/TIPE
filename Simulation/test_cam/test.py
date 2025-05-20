import arcade
import arcade.key

WIN_WIDTH = 1250
WIN_HEIGHT = 720

class Mygame(arcade.Window):
    
    def __init__(self) -> None:
        super().__init__(WIN_WIDTH, WIN_HEIGHT, resizable= True)
        
        self.set_location(75, 75)
        arcade.set_background_color(arcade.color.WHITE)
        
        self.camera = arcade.Camera(WIN_WIDTH, WIN_HEIGHT)
        self.camera_left_bottom_angle = 0, 0
        
        self.Q_pressed = False
        self.D_pressed = False
        self.Z_pressed = False
        self.S_pressed = False
        self.right_pressed = False
        self.left_pressed = False
     

        
    def on_draw(self):
        
        arcade.start_render()
        self.camera.use()
        
        arcade.draw_circle_filled(600, 400, 100, arcade.color.RED)
        
        return super().on_draw()
    
    def update_cam_pos(self):
        
        cam_x, cam_y = self.camera_left_bottom_angle
        
        if self.Q_pressed:
            self.camera_left_bottom_angle = (cam_x + 10, cam_y)
        if self.D_pressed:
            self.camera_left_bottom_angle = (cam_x - 10, cam_y)
        if self.Z_pressed:
            self.camera_left_bottom_angle = (cam_x, cam_y - 10)
        if self.S_pressed:
            self.camera_left_bottom_angle = (cam_x, cam_y + 10)
        
        self.camera.move_to(self.camera_left_bottom_angle)
        
    def update_delta_time(self, delta_time):
        
        if self.right_pressed:
            delta_time += 0.01
        if self.right_pressed:
            delta_time -= 0.01
        
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.Q:
            self.Q_pressed = True
        elif key == arcade.key.D:
            self.D_pressed = True
        elif key == arcade.key.Z:
            self.Z_pressed = True
        elif key == arcade.key.S:
            self.S_pressed = True
        
        # gestion de delta time
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.Q:
            self.Q_pressed = False
        elif key == arcade.key.D:
            self.D_pressed = False
        elif key == arcade.key.Z:
            self.Z_pressed = False
        elif key == arcade.key.S:
            self.S_pressed = False
        
        # gestion delat time
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    
    def on_update(self, delta_time: float):
        
        self.update_cam_pos()
        self.update_delta_time(delta_time)
        
        return super().on_update(delta_time)
    

def main():
    window = Mygame()
    arcade.run()

if __name__ == "__main__":
    main()