# implementation of Spaceship - program template for RiceRocks
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
bonus1 = 0
bonus2 = 0
lives = 0
time = 0
started = False
age_michetti = 0
age_nivel_3 = 0
final = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False, resize = 1.0):
        self.center = center
        self.size = size
        self.radius = radius
        self.resize = float(resize)
        
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
    def get_resize(self):
        return self.resize

    def get_resized(self):
        return (self.size[0] * self.resize, self.size[1] * self.resize)

    def get_centered_resized(self):
        return (self.get_resized()[0]/2, self.get_resized()[1]/2)

def draw_animated(canvas,image,info,pos = (WIDTH/2, HEIGHT/2),resize = 1):
        global age_macri
        
        current_index = (age_macri % info.get_lifespan()) // 1
        current_center = [info.get_center()[0] +  current_index * info.get_size()[0], info.get_center()[1]]
        
        canvas.draw_image(image, current_center, info.get_size(),
                         pos, [info.get_size()[0]*resize, info.get_size()[1]*resize])
        age_macri += .08

def draw_animated_costado(canvas,image,info,sound,resize):
    global age_michetti, WIDTH, HEIGHT
    
    if age_michetti == 0:
        sound.rewind()
        sound.play()
    
    cuanto_sale = .3
    if age_michetti <= 1:
        pos = [WIDTH-(info.get_size()[0]*cuanto_sale*age_michetti), HEIGHT/2]
        
    if age_michetti > 1:
        pos = [WIDTH-info.get_size()[0]*cuanto_sale+(info.get_size()[0]*cuanto_sale*(age_michetti-1)), HEIGHT/2]
           
            #current_index = (age % info.get_lifespan()) // 1
            #current_center = [info.get_center()[0] +  current_index * info.get_size()[0], info.get_center()[1]]
        
    canvas.draw_image(image, info.get_center(), info.get_size(),pos, [info.get_size()[0]*resize,info.get_size()[1]*resize])
        
    age_michetti += .01

        
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")
debris_image2 = simplegui.load_image("https://dl.dropboxusercontent.com/s/avykhp7w27ayzje/oie_2aHEWvZM8Pi0.png?dl=0")
# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://www.unidiversidad.com.ar/cache_2/arsat-movilion_473_945_c.jpg")
nebula_2 = simplegui.load_image("https://dl.dropboxusercontent.com/s/fy74elzova1ia9i/51767658_299872170729270_2577318185367764992_n.png?dl=0")
nebula_3 = simplegui.load_image("https://dl.dropboxusercontent.com/s/zczcwt3xxime9wz/maxresdefault_800x600.jpg?dl=0")
# splash image

splash_info = ImageInfo([794, 1123], [1588, 2246], resize=0.2)
splash_image = simplegui.load_image("https://raw.githubusercontent.com/fnahuelc/tarifazo/master/media/canvas.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://i.imgur.com/I4TWrLd.gif")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([35, 35], [70, 70], 30)
asteroid_image = simplegui.load_image("https://raw.githubusercontent.com/fnahuelc/tarifazo/master/media/macri.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

macri_info = ImageInfo([280, 360], [560, 720], 360, 36, True)
macri_image = simplegui.load_image("https://raw.githubusercontent.com/fnahuelc/tarifazo/master/media/macri.png")

monstruo_final_info = ImageInfo([167,173], [334, 346], 40, None, False, .4)
monstruo_final_image = simplegui.load_image("http://wiserer.com/static/images/trumpet.png")

michetti_info = ImageInfo([254,330.5], [508, 661], 250)
michetti_image = simplegui.load_image("https://raw.githubusercontent.com/fnahuelc/tarifazo/master/media/51767658_299872170729270_2577318185367764992_n.png")

bonus1_info = ImageInfo([36,36], [72, 72], 10, 300, False, 1)
bonus1_image = simplegui.load_image("https://dl.dropboxusercontent.com/s/cywhecpcqq93kvl/oie_transparent%20%284%29.png?dl=0")    

bonus2_info = ImageInfo([100,85], [200, 170], 10, 300, False, .4)
bonus2_image = simplegui.load_image("http://images.wikia.com/left4dead/images/2/2e/Propane-tank2.png")    

#bonus3_info = ImageInfo([200, 150],[400,300], 10, 300, False, .2)
#bonus3_image = simplegui.load_image("http://www.aumentativa.net/imagenes/aceite.png")    

#bonus4_info = ImageInfo([512,322.5], [1024, 645], 10, 300, False, .06)
#bonus4_image = simplegui.load_image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/SUBE_frente.svg/1024px-SUBE_frente.svg.png")    

bonus_image = [bonus1_image, bonus2_image]
bonus_info = [bonus1_info, bonus2_info]

alien_info = ImageInfo([107,107], [214, 214], 35, None, False, .4)
alien_image = simplegui.load_image("http://media.perfil.com/divas/files/2012/11/mirtha.png")    

final_info = ImageInfo([499,701.5], [998, 1403], 35, None, False, .1)
final_image = simplegui.load_image("http://argentinatoday.org/wp-content/uploads/2016/01/i-want-to-believe-peron.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/s/u6p18rqz5cjigi3/AGUANTAAA.mp3?dl=0")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
michetti_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/s/3twiwu6ecm1g60g/hay_que_saltar.mp3?dl=0")
# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
soundtrack = simplegui.load_sound("https://dl.dropboxusercontent.com/s/wz9oebx5do5itv6/MACRI_CANTA.mp3?dl=0")
final_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/s/nwaxt1vouyyuoq2/AGUANTAAAaaaaaaa.mp3?dl=0")
final_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/s/nwaxt1vouyyuoq2/AGUANTAAAaaaaaaa.mp3?dl=0")
bonus_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/s/stin5cywk7am9r8/bonus_sound%20%281%29.mp3?dl=0")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
            
        self.vel[0] *= .99
        self.vel[1] *= .99

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
       
    def increment_angle_vel(self):
        self.angle_vel += .05
        
    def decrement_angle_vel(self):
        self.angle_vel -= .05
        
    def shoot(self):
        global missile_group
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        missile_group.add(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.pos 
    
    def collide(self, other_object):
        dist(self.get_position(),other_object.get_position()) <= self.get_radius()+other_object.get_radius()

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None, parpadea = False):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.parpadea = parpadea
        self.resize = info.get_resize()
        self.age_move_circle = 0
        self.vida = 2

        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        
        if self.parpadea and self.age % 10 < 5:
            return
                
        if self.animated: 
            current_rock_index = (self.age % self.lifespan) // 1
            current_rock_center = [self.image_center[0]+  current_rock_index * self.image_size[0], self.image_center[1]]
            canvas.draw_image(self.image, current_rock_center, self.image_size,
                              self.pos, self.image_size, self.angle)
          
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, (self.image_size[0] * self.resize, self.image_size[1] * self.resize), self.angle)
                    
    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        # update age
        self.age += 1
        
        return self.age >= self.lifespan
        
    def get_position(self):
        return self.pos
    
    def get_velocity(self):
        return self.vel 
    
    def get_radius(self):
        return self.radius
  
    def collide(self,other_object):
        return dist(self.get_position(),other_object.get_position())<=self.get_radius()+other_object.get_radius()
    
    def change_image(self, image, info):
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()    
        self.radius = info.get_radius()
        self.resize = info.get_resize()
        
    def move_circle(self,frec):
        vel = .005
        self.pos[0] = (WIDTH/2) + (WIDTH/3) *math.sin(2*math.pi*math.pi*self.age_move_circle*vel)
        self.pos[1] = (HEIGHT/2) + (HEIGHT/3) *math.cos(2*math.pi*math.pi*self.age_move_circle*vel)
        self.age_move_circle += .1
    
    def cambiar_vida(self):
        self.vida -= 1
        
    def get_vida(self):
        return self.vida
    
    def get_lifespan(self):
        return self.lifespan
    
    def get_image(self):
        return self.image
        
# key handlers to control ship   
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.increment_angle_vel()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.decrement_angle_vel()
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, score, lives, bonus1, bonus2
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        score = 0
        lives = 0
        bonus1 = 0
        bonus2 = 0
        

        missile_group = set([])
        soundtrack.rewind()
        soundtrack.play()
        
age_macri = 0       
def draw(canvas):
    global final, monstruo_final,nivel, age_michetti,age_nivel_3,macri_image,macri_info, time, started,lives, score, bonus1, bonus2, bonus_group, rock_group, missile_group

#  	NIVELES    
    if score < 10:
        nivel = 1
    elif score < 20:
        nivel = 2
    else:
        nivel = 3
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    
    
#    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])

    if nivel ==1:
        canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
#        canvas.draw_image(debris_image2, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    elif nivel==2:
        canvas.draw_image(nebula_2, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
        change_image_group(rock_group,alien_image,alien_info)
        asteroid_image = alien_image
        asteroid_info = alien_info
        
    elif  nivel==3:
        canvas.draw_image(nebula_3, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw UI
    canvas.draw_text("Tarifazos", [50, 50], 22, "White")
    canvas.draw_text("Gas", [305, 50], 22, "White")
    canvas.draw_text("Aceite", [380, 50], 22, "White")
    canvas.draw_text("Puntos", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score * 10), [680, 80], 22, "White")
           
    canvas.draw_text(str(bonus2 * 10), [305, 80], 22, "White")
    canvas.draw_text(str(bonus1 * 10), [380, 80], 22, "White")

    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    
    process_sprite_group(canvas,rock_group)
    process_sprite_group(canvas,missile_group)
    process_sprite_group(canvas,bonus_group)
    process_sprite_group(canvas,explosion_group)
    
    if final:
        for object_in_group in set(rock_group):
            explosion_group.add(Sprite(object_in_group.get_position(), (0,0), 0, 0, explosion_image, explosion_info))
            explosion_sound.rewind()
            explosion_sound.play()
            rock_group.remove(object_in_group)
            
        canvas.draw_image(final_image, final_info.get_center(), 
                          final_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          [WIDTH / 2, HEIGHT / 2])    
    
    if nivel == 3 and not final:
        monstruo_final.move_circle(score)
        monstruo_final.draw(canvas)
        if group_collide(missile_group,monstruo_final):
            monstruo_final.cambiar_vida()
           
            if monstruo_final.get_vida() == 0:
                final = True
                
    if group_collide(rock_group,my_ship):
        lives += 1
        if lives == 3:
            started = False
            final_sound.play()
           
    [sum_bonus1,sum_bonus2] = group_collide_bonus(bonus_group,my_ship)
    bonus1 += sum_bonus1 
    bonus2 += sum_bonus2
         
    score += group_group_collide(rock_group,missile_group)
        
    if score > 1:
        draw_animated_costado(canvas,michetti_image,michetti_info,michetti_sound,.5)
         
        
    # draw splash screen if not started
    if not started:
#        draw_animated(canvas,macri_image,macri_info,(WIDTH/2-250,HEIGHT/2-40))          

        canvas.draw_image(splash_image,
                          splash_info.get_center(),
                          splash_info.get_size(),
                          [WIDTH/2, HEIGHT/2],
                          splash_info.get_resized()

                          )
        rock_group = set([])
        missile_group = set([]) 
        bonus_group = set([]) 

#        canvas.draw_text("En el 2019 Macri envio a los pobres hacia el espacio exterior", [130, 500], 22, "White")
#        canvas.draw_text("obligandolos a seguir combatiendo el aumento del gas esta", [130, 525], 22, "White")
#        canvas.draw_text("vez necesario para sus naves...Combate los aumentos en el espacio,", [130, 550], 22, "White")
#        canvas.draw_text("recuerda que solo puedes soportar 3 Tarifazos.", [130, 575], 22, "White")
        
        # timer handler that spawns a rock    
        
def rock_spawner():
    global rock_group,monstruo_final,score,nivel,age_nivel_3
    if started and len(rock_group)<=12:
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        rock_vel = [(1 + (score/5))*random.random() * .6 - .3, (1 + (score/5))*random.random() * .6 - .3 ]
        rock_avel = random.random() * .2 - .1        
        if nivel == 3:
            if final:
                return
            if age_nivel_3 == 0:
                rock_group = set([])
            rock_vel = [my_ship.get_position()[0] - monstruo_final.get_position()[0],my_ship.get_position()[1] - monstruo_final.get_position()[1]]
            rock_vel = [rock_vel[0]* 0.01, rock_vel[1]* 0.01]
            rock_group.add(Sprite(monstruo_final.get_position(), rock_vel, 0, rock_avel, asteroid_image, asteroid_info))
            age_nivel_3 += 1
        else:
            
            if dist(rock_pos,my_ship.get_position())<asteroid_info.get_radius()+ship_info.get_radius()+20:
                return

            rock_group.add(Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info))
        
def process_sprite_group(canvas,sprite_group):
    for sprite in set(sprite_group):    
        if sprite.update():
            sprite_group.remove(sprite)
        sprite.draw(canvas)
        
def change_image_group(sprite_group,image,info):
    global asteroid_image,asteroid_info,alien_image,alien_info
    for sprite in set(sprite_group):    
        sprite.change_image(image,info)
    
def group_collide(group, other_object):
    col = 0
    for object_in_group in set(group):
        if object_in_group.collide(other_object):
            explosion_group.add(Sprite(object_in_group.get_position(), (0,0), 0, 0, explosion_image, explosion_info))
            bonus_group.add(Sprite(object_in_group.get_position(), object_in_group.get_velocity(), 0, 0, bonus_image[score%len(bonus_image)], bonus_info[score%len(bonus_info)], False, True))
            explosion_sound.rewind()
            explosion_sound.play()
            group.remove(object_in_group)
            col +=1            

    return col > 0

def group_collide_bonus(group, other_object):
    col_bonus1 = 0
    col_bonus2 = 0
    
    for object_in_group in set(group):
        if object_in_group.collide(other_object):
            if object_in_group.get_image() == bonus_image[0]:
                col_bonus1 += 1
            else:  
                col_bonus2 += 1
                    
            group.remove(object_in_group)
            bonus_sound.rewind()
            bonus_sound.play()

    return col_bonus1,col_bonus2

def group_group_collide(group1, group2):
    num_col = 0
    for element_in_group2 in set(group2):
        if group_collide(group1, element_in_group2):
            num_col += 1       
            group2.remove(element_in_group2)
    return num_col

# initialize stuff
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
missile_group = set([]) 
explosion_group = set([])
bonus_group = set([])
monstruo_final = Sprite((WIDTH/2, HEIGHT/4), (0,0), 0, 0, monstruo_final_image, monstruo_final_info)

# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
