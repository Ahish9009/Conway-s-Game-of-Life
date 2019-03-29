import pygame as pg

pg.init()

screen_size=(1000,700)
grid_size=()

grid_size+=(input('Enter width of grid: '),)
grid_size+=(input('Enter height of grid: '),)

screen=pg.display.set_mode(screen_size)
pg.display.set_caption('Game of Life')

#colors
green=(255,255,255)
black=(0,0,0)

#clock
clock=pg.time.Clock()

def default_grid_setter():

    #for vertical grid lines
    a=0
    d=float(screen_size[0]/grid_size[0])
    S=0 #sum
    while S<screen_size[0]:
        pg.draw.lines(screen, green, True, [(S,0), (S,screen_size[1])],1)
        S+=d

    #for horizontal grid lines
    a=0
    d=float(screen_size[1]/grid_size[1])
    S=0 #sum
    while S<screen_size[1]:
        pg.draw.line(screen, green, (0,S), (screen_size[0],S))
        S+=d

def get_tile_number(pos):

    dx=float(screen_size[0]/grid_size[0])
    dy=float(screen_size[1]/grid_size[1])
    
    x,y=pos[0],pos[1]
    tile=(int(x/dx)+1)+(int(y/dy)*grid_size[0])
    
    return tile

def get_coordinates(tile):

    dx=float(screen_size[0]/grid_size[0])
    dy=float(screen_size[1]/grid_size[1])

    #gets top left corner coordinates
    x=(tile%grid_size[0]-1)*dx
    if x==-dx:
        x=screen_size[1]-dx

    y=tile/grid_size[0]*dy
    if tile%grid_size[0]==0:
        y-=dy

    return x,y

class grid_keeper:
    def __init__(self):

        self.grid={}
        self.dx=float(screen_size[0]/grid_size[0])
        self.dy=float(screen_size[1]/grid_size[1])
        self.x=grid_size[0]
        self.y=grid_size[1]
        
        for i in range(1,grid_size[0]*grid_size[1]+1):
            self.grid[i]=0 #0 signifies cell is dead

    def switch(self,tile):
        
        if self.grid[tile]==0:
            self.grid[tile]=1
        else:
            self.grid[tile]=0

    def change(self):

        new_grid={}
        
        for i in self.grid:

            #to check number of neighbors alive
            total=0
            #for left
            try:
                if self.grid[i-1]:
                    total+=1

##                    print i-1
            except:
                pass
            #for right
            try:
                if self.grid[i+1]:
                    total+=1
##                    print i+1
            except:
                pass
            #for up
            try:
                if self.grid[i-self.x]:
                    total+=1
##                    print i-self.x
            except:
                pass
            #for down
            try:
                if self.grid[i+self.x]:
                    total+=1
##                    print i+self.x
            except:
                pass
            #for top left
            try:
                if self.grid[i-self.x-1]:
                    total+=1
##                    print i-self.x-1
            except:
                pass
            #for top right
            try:
                if self.grid[i-self.x+1]:
                    total+=1
##                    print i-self.x+1
            except:
                pass
            #for bottom left
            try:
                if self.grid[i+self.x-1]:
                    total+=1
##                    print i+self.x-1
            except:
                pass
            #for bottom right
            try:
                if self.grid[i+self.x+1]:
                    total+=1
##                    print i+self.x+1
            except:
                pass

            if self.grid[i]:
                if total==2 or total==3:
                    new_grid[i]=1
                else:
                    new_grid[i]=0
            else:
                if total==3:
                    new_grid[i]=1
                else:
                    new_grid[i]=0

        self.grid=new_grid

    def update(self):
        
        for i in self.grid:
            x,y=get_coordinates(i)
            
            if self.grid[i]:
                pg.draw.rect(screen, green, (x, y, self.dx, self.dy))
            else:
                pg.draw.rect(screen, black, (x, y, self.dx, self.dy))

flag=0
looper=True
show_grid=True
while looper:

    if flag==0: #initial setup

        screen.fill(black)
        grid=grid_keeper()
        default_grid_setter()

        flag=1

    if flag==1: #inital cell selection

        default_grid_setter()

        for event in pg.event.get():
            if event.type==pg.QUIT:
                looper=False
                
            if event.type==pg.MOUSEBUTTONDOWN:

                pos=pg.mouse.get_pos()
                tile=get_tile_number(pos)
                grid.switch(tile)
                grid.update()

            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    flag=2
                    screen.fill(black)

    if flag==2: #game starts

        #changes and displays
        grid.change()
        grid.update()

        #checks whether to show grid
        if show_grid:
            default_grid_setter()

        for event in pg.event.get():
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_g:
                    show_grid= not show_grid #to change grid status
                    
                if event.key==pg.K_RETURN:
                    flag=0 #to reset
            if event.type==pg.QUIT:
                looper=False

    for event in pg.event.get():
        if event.type==pg.QUIT:
            looper=False

    pg.display.update()
    clock.tick(10) #to control speed

pg.quit()
        
