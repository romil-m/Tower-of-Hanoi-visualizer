# Tower-of-Hanoi-visualizer
This is a visualization of the puzzle of Tower of Hanoi which is getting solved for 4 discs ( & 3 pegs) in Python.
To solve Tower of Hanoi recursion is used. 

Used graphics.py which is a wrapper around Tkinter(https://docs.python.org/3/library/tkinter.html) & should run on any platform where Tkinter is available.

To use the visualizer simply download all the files & do pip install if the modules in python are absent.
Then run "Hanoi.py" file. Then you will be able to see the visualization in the window opened.
A screenshot of the puzzle getting solved:

![image](https://user-images.githubusercontent.com/73889488/181034856-de94de7a-ebbc-4760-b78f-8e5b7fc8ed37.png)

Along with the final stage of the puzzle the number of steps in which the puzzle is getting solved is also printed in output along with the movements of the discs in the pegs in the terminal window.
A screenshot of output in terminal: 

![image](https://user-images.githubusercontent.com/73889488/181035850-bcb6afa6-e878-4df5-a929-28c0caa7e1ef.png)

In order to change the number of discs open Hanoi.py and make model as [[1,2,3],[],[]] (for 3 discs)
 Then accordingly do changes in the discAttributes & the poles if needed.
