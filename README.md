# Game-of-LIFE-
Using Python tkinter , conway's game of life - 0 player

###**Pre Requirements :**
  1.Python3 (or Python2),and 
  2.installed tkinter (or Tkinter for python2) module, using pip3 installer / any other way
  
#### WHAT IS CONWAY'S GAME OF LIFE :
  Each unit(rectangle) acts as a cell (alive/dead)
  0 player game not your typical computer game- evolution depends on initial state of some cells alive 
    no further input req , for that particular state generations
  Each cell alive/ dead can be alive/dead in next generation, this depends on rules:
  
  #####The Rules
    * For a space that is 'populated':*
        a. Each cell with one or no neighbors dies, as if by solitude.
        b. Each cell with four or more neighbors dies, as if by overpopulation.
        c. Each cell with two or three neighbors survives.
    * For a space that is 'empty' or 'unpopulated'*
        a. Each cell with three neighbors becomes populated.
 
 ### FEATURES OF THIS SCRIPT:
 1. Fixed no of cells in a population, currently 50x75, though can be changed in script
 2. each cell (gray -dead, yellow - alive), is stored in numpy integer array (50x75), called grid:
    * if value of grid[i][j] =1 ,alive ;and if 0, dead
    * one time iteration on whole array to draw rectangles in canvas
 3. Primary Buttons -
    * Start -starts showing next generations , with some speed (inverse of time delay), which can be controlled by 'Speed' scaler
      a. 'rules' function checks the rules on each cell in array
      b. if that cell has to toggle its state(dead/alive) in next generation , make changes in the grid and draw new rectangle there
      c. above method can be changed using rectangles dict or by cleaning canvas on a particular interval
      d. this is better than drawing whole grid everytime, but yes, not yet the best
    * Stop (pause)
    * next - show next gen 
    * reset
    * quit
 4. INITIAL PATTERN:
    * choose a init state and 'go'; then press start/next
    * go - clears the canvas and calls the 1 time called func again to draw all rectangles.
 5. CUSTOM:
  * opens new window, copies current grid, draw rectangles(this time these are stored in a dict),based on that grid in this new window
  * each cell 'binded' with a function to toggle col as well as value in grid on mouse click
  * after custom updation on grid, 'clone' button sets cur grid equal to the parent /main/original grid and closes this window updating the changes in original grid
  * work required on : option menu and go button and 'remember me' button in new window that opens
  
  
  #### OPTIONAL
  to make it into an dekstop(ubuntu/debian/somewhat similar in mac)application
  1. make the py script executable 
    '''
    chmod +x <filename.py>
    '''
    in terminal.
  2.add this line on top of the .py script (python3/ python or as it is there in ur pc)
    '''python3
    #!/usr/bin/env python3
    '''
  3.make a text file with extension **.desktop** on desktop, and write following into it:
    '''
    [Desktop Entry]
    Version=1.0
    Name=GAME oF LiFE
    Exec=/home/ponyket/.. ../GOL.ani.py
    Icon=/home/ponyket/.. ../gol_yel_edited.png
    Type=Application
    '''
    
   image file is uploaded in the repository, wherever u save the image, write it's address in Icon
   exec is the address of the executable script u did in 1st point.
   *also, save the .desktop file in '~/.local/share/applications/' to make application available in 'Applications'* 
   
   
#####ENJOY !!
 
    
