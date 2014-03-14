import autopy, sys, time

offset_x = 197+310
offset_y = 150+160
tile_size = 45

Column1 = [0,0,0,0,0,0,0,0] 
Column2 = [0,0,0,0,0,0,0,0] 
Column3 = [0,0,0,0,0,0,0,0] 
Column4 = [0,0,0,0,0,0,0,0] 
Column5 = [0,0,0,0,0,0,0,0] 
Column6 = [0,0,0,0,0,0,0,0] 
Column7 = [0,0,0,0,0,0,0,0] 
Column8 = [0,0,0,0,0,0,0,0] 
Rows = [Column1,Column2,Column3,Column4,Column5,Column6,Column7,Column8]
C1 = [0,0,0,0,0,0,0,0] 
C2 = [0,0,0,0,0,0,0,0] 
C3 = [0,0,0,0,0,0,0,0] 
C4 = [0,0,0,0,0,0,0,0] 
C5 = [0,0,0,0,0,0,0,0] 
C6 = [0,0,0,0,0,0,0,0] 
C7 = [0,0,0,0,0,0,0,0] 
C8 = [0,0,0,0,0,0,0,0] 
R = [C1,C2,C3,C4,C5,C6,C7,C8]

gameOverCounter = 0
moveCounter = 0

# make a small delay using big loops
def delay(length):
  for x in range(length):
    for y in range(length):
      pass

# scan for main game frame offset by seaching top left corner colors
def get_offset():
  screen_cap = autopy.bitmap.capture_screen()
  for corner_col in screen_cap.find_every_color(3939856):
    xpos,ypos = corner_col
    if (autopy.color.hex_to_rgb(screen_cap.get_color(xpos-1, ypos-1)) == (255, 255, 255) and 
          autopy.color.hex_to_rgb(screen_cap.get_color(xpos, ypos-1)) == (153, 153, 153) and 
          autopy.color.hex_to_rgb(screen_cap.get_color(xpos-1, ypos)) == (255, 255, 255) and 
          autopy.color.hex_to_rgb(screen_cap.get_color(xpos, ypos)) == (60, 30, 16)):
            print "Found game corner at",xpos,ypos
            return xpos+310, ypos+160
  autopy.alert.alert("Cannot find top left corner of game frame!")
  try:
    sys.exit(1)
  except SystemExit as e:
    sys.exit(e)

offset_x, offset_y = get_offset()

# capture main screen and check for colors
def getScreen():
  screen_cap = autopy.bitmap.capture_screen()
  for y in reversed(range(8)):
    screen_cap = autopy.bitmap.capture_screen()
    for x in reversed(range(8)):

      col_x = offset_x+21+(x*tile_size)
      col_y = offset_y+20+(y*tile_size)
      R[x][y] = screen_cap.get_color(col_x, col_y)
      #print "color:",R[x][y],"mouseX,mouseY:",col_x,col_y,"x,y:",x,y

      #yellows - 16776964
      if((R[x][y] > 16776500) and (R[x][y] < 16777000)):
        Rows[x][y] = 1
        #break
      #blues - 5602531
      if((R[x][y] > 5600000) and (R[x][y] < 5650000)):
        Rows[x][y] = 2
        #break
      #whites - 14737638
      if((R[x][y] > 14600000) and (R[x][y] < 14800000)):
        Rows[x][y] = 3
        #break
      #purple - 13041919
      if((R[x][y] > 13000000) and (R[x][y] < 13200000)):
        Rows[x][y] = 4
        #break    
      #oranges - 16750848
      if((R[x][y] > 16740000) and (R[x][y] < 16755000)):
        Rows[x][y] = 5
        #break  
      #greens - 3407616
      if((R[x][y] > 3400000) and (R[x][y] < 3410000)):
        Rows[x][y] = 6
        #break       
      #reds - 15466496
      if((R[x][y] > 15400000) and (R[x][y] < 15600000)):
        Rows[x][y] = 7
        #break

      # bonus stuff
      if Rows[x][y] != 99:
        #white bolt - 16777215
        if((R[x][y] > 16777200) and (R[x][y] < 16777300)):
          Rows[x][y] = 3
        #yellow bolt - 16770884
        if((R[x][y] > 16770800) and (R[x][y] < 16770900)):
          Rows[x][y] = 1
        #purple bolt - 14052851
        if((R[x][y] > 14052000) and (R[x][y] < 14053000)):
          Rows[x][y] = 4
        #yellow coins - 16774052
        if((R[x][y] > 16773000) and (R[x][y] < 16775000)):
          Rows[x][y] = 1
        #green poison - 9502605
        if((R[x][y] > 9502000) and (R[x][y] < 9503000)):
          Rows[x][y] = 6
        #green 4 arrows - 6941287
        if((R[x][y] > 6940000) and (R[x][y] < 6942000)):
          Rows[x][y] = 6
        #red ball - 16475236
        if((R[x][y] > 16475000) and (R[x][y] < 16476000)):
          Rows[x][y] = 7
        #orange ball - 16759952
        if((R[x][y] > 16759000) and (R[x][y] < 16760000)):
          Rows[x][y] = 5
        #green ball - 13696207
        if((R[x][y] > 13695000) and (R[x][y] < 13697000)):
          Rows[x][y] = 6
        #red multiplier - 16462129
        if((R[x][y] > 16460000) and (R[x][y] < 16466000)):
          Rows[x][y] = 7
        #white multiplier - 9868950
        if((R[x][y] > 9868000) and (R[x][y] < 9870000)):
          Rows[x][y] = 3
        #red something? - 16729670
        if((R[x][y] > 16729000) and (R[x][y] < 16730000)):
          Rows[x][y] = 7
        #red something? - 16409186
        if((R[x][y] > 16408000) and (R[x][y] < 16410000)):
          Rows[x][y] = 7
        #purple something? - 12070798
        if((R[x][y] > 12070000) and (R[x][y] < 12072000)):
          Rows[x][y] = 4
        #purple something? - 12203407
        if((R[x][y] > 12202000) and (R[x][y] < 12204000)):
          Rows[x][y] = 4
        #white gray something? - 12632256
        #if((R[x][y] > 12631000) and (R[x][y] < 12633000)):
        #  Rows[x][y] = 3
        #green something? - 7907448
        if((R[x][y] > 7907000) and (R[x][y] < 7908000)):
          Rows[x][y] = 6
        #yellow something? - 16772736
        if((R[x][y] > 16771000) and (R[x][y] < 16773000)):
          Rows[x][y] = 1
        #purple something? - 13718772
        if((R[x][y] > 13718000) and (R[x][y] < 13719000)):
          Rows[x][y] = 4
        #purple something? - 11679189
        if((R[x][y] > 11679000) and (R[x][y] < 11680000)):
          Rows[x][y] = 4
        #green something? - 1368064
        if((R[x][y] > 1367000) and (R[x][y] < 1369000)):
          Rows[x][y] = 6
        #purple something? - 9961644
        if((R[x][y] > 9961000) and (R[x][y] < 9963000)):
          Rows[x][y] = 4
        #purple something? - 12867724
        if((R[x][y] > 12867000) and (R[x][y] < 12868000)):
          Rows[x][y] = 4
        #red something? - 13434880
        if((R[x][y] > 13433000) and (R[x][y] < 13436000)):
          Rows[x][y] = 7
        #white something? - 15790320
        if((R[x][y] > 15790000) and (R[x][y] < 15791000)):
          Rows[x][y] = 3
        #green something? - 893232
        if((R[x][y] > 893000) and (R[x][y] < 894000)):
          Rows[x][y] = 6
        #green something? - 2023424
        if((R[x][y] > 2023000) and (R[x][y] < 2024000)):
          Rows[x][y] = 6
        #red something? - 13500416
        if((R[x][y] > 13500000) and (R[x][y] < 13502000)):
          Rows[x][y] = 7
        #green something? - 34560
        if((R[x][y] > 34500) and (R[x][y] < 34600)):
          Rows[x][y] = 6
        #green something? - 3046153
        if((R[x][y] > 3045000) and (R[x][y] < 3047000)):
          Rows[x][y] = 6

      if Rows[x][y] == 0:
        if R[x][y] != 0:
          print "unid. color:",R[x][y],"mouseX,mouseY:",col_x,col_y,"x,y:",x,y

      #Check end game
      if screen_cap.get_color(offset_x+200, offset_y+420) > 13670000 and screen_cap.get_color(offset_x+200, offset_y+420) < 13671000:
        autopy.alert.alert("Game finished!")
        try:
          sys.exit(1)
        except SystemExit as e:
          sys.exit(e)
      
def findMove():
  foundMove = False
  for x in range(8):
    for y in range(8):
      #move up
      #check up
      x1 = x
      y1 = y-2
      x2 = x
      y2 = y-3
      if(y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up up')
          makeMove((x,y),(x,y-1))
          break
      #check left
      x1 = x-1
      x2 = x-2
      y1 = y-1
      y2 = y-1
      if(x2 >= 0 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up left')
          makeMove((x,y),(x,y-1))
          break
      #check right
      x1 = x+1
      x2 = x+2
      y1 = y-1
      y2 = y-1
      if(x2 <= 7 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up right')
          makeMove((x,y),(x,y-1))
          break
      #check around
      x1 = x+1
      x2 = x-1
      y1 = y-1
      y2 = y-1
      if(x1 <= 7 and x2 >= 0 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up around')
          makeMove((x,y),(x,y-1))
          break
      #move left
      #check up
      x1 = x-1
      y1 = y-1
      x2 = x-1
      y2 = y-2
      if(y2 >= 0 and x1 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving left up')
          makeMove((x,y),(x-1,y))
          break
      #check left
      x1 = x-2
      x2 = x-3
      y1 = y
      y2 = y
      if(x2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving left left')
          makeMove((x,y),(x-1,y))
          break
      #check down
      x1 = x-1
      x2 = x-1
      y1 = y+1
      y2 = y+2
      if(x2 >= 0 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving left down')
          makeMove((x,y),(x-1,y))
          break 
      #check around
      x1 = x-1
      x2 = x-1
      y1 = y+1
      y2 = y-1
      if(x2 >= 0 and y1 <= 7 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving left around')
          makeMove((x,y),(x-1,y))
          break 
      #move right
      #check up
      x1 = x+1
      y1 = y-1
      x2 = x+1
      y2 = y-2
      if(y2 >= 0 and x1 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving right up')
          makeMove((x,y),(x+1,y))
          break
      #check right
      x1 = x+2
      x2 = x+3
      y1 = y
      y2 = y
      if(x2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving right right')
          makeMove((x,y),(x+1,y))
          break
      #check down
      x1 = x+1
      x2 = x+1
      y1 = y+1
      y2 = y+2
      if(x2 <= 7 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving right down')
          makeMove((x,y),(x+1,y))
          break
      #check around
      x1 = x+1
      x2 = x+1
      y1 = y+1
      y2 = y-1
      if(x2 <= 7 and y1 <= 7 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving right around')
          makeMove((x,y),(x+1,y))
          break
      #move down
      #check down
      x1 = x
      y1 = y+2
      x2 = x
      y2 = y+3
      if(y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up up')
          makeMove((x,y),(x,y+1))
          break
      #check left
      x1 = x-1
      x2 = x-2
      y1 = y+1
      y2 = y+1
      if(x2 >= 0 and y2 <=7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up left')
          makeMove((x,y),(x,y+1))
          break
      #check right
      x1 = x+1
      x2 = x+2
      y1 = y+1
      y2 = y+1
      if(x2 <= 7 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up right')
          makeMove((x,y),(x,y+1))
          break
      #check around
      x1 = x+1
      x2 = x-1
      y1 = y+1
      y2 = y+1
      if(x1 <= 7 and x2 >= 0 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          #print('found move at',x,y,' with color',R[x][y],'moving up around')
          makeMove((x,y),(x,y+1))
          break
  #for ix in range(0,8):
  	#print(Column1[ix],Column2[ix],Column3[ix],Column4[ix],Column5[ix],Column6[ix],Column7[ix],Column8[ix])
  
def makeMove(fromLoc, toLoc):
  #print(moveCounter,'from',fromLoc,'to',toLoc)
  from_x = (fromLoc[0]*tile_size)+offset_x+21
  from_y = (fromLoc[1]*tile_size)+offset_y+20
  #print "Moving from",from_x,from_y
  autopy.mouse.move(from_x,from_y)
  delay(1000)
  autopy.mouse.toggle(True)
  delay(1000)
  try:
    to_x = (toLoc[0]*tile_size)+offset_x+21
    to_y = (toLoc[1]*tile_size)+offset_y+20
    #print "Moving to",to_x,to_y
    #autopy.mouse.smooth_move(to_x,to_y)
    autopy.mouse.move(to_x,to_y)
  except ValueError:
    autopy.mouse.toggle(False)
    return
  delay(1000)
  autopy.mouse.toggle(False)
  #getScreen()
  
def main():
  autopy.mouse.move(offset_x,offset_y)
  delay(1000)
  autopy.mouse.click()
  delay(1000)
  
  while(True):
    getScreen()
    findMove()

if __name__ == '__main__':
  main()


