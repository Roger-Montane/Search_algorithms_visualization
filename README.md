# Search_algorithms_visualization

This project was carried out during the summer of 2019, and I used it as a way to consololidate my knowledge on search algorithms while at the same time building a real time visualizer to display how they work and make decisions. I created a simple GUI using the Pygame library (which I learned while doing this project) where you can select the start and finish nodes in a grid, put some walls between them and choose the algorithm you want to use (BFS, DFS, UCS, IDS, GREEDY, A*). The project is unfinished and still needs some work. Real time visualization is not working at the moment (it only displays the path when the algorithm is finished) and some algorithms are still not implemented. There is also a bug which causes the start and finish nodes to change when an algorithm is executed which needs to be fixed.

---

### How to use the GUI
In order to select the starting node, click on the `START` button, select the square on the grid that you want (with left click) and then click the `OK` button to apply the changes (you can also delete the start node you selected by right clicking it).

To select the finish node, follow the same method as for the start node. 

As for the walls, select the `WALLS` button and then you can start selecting squares by left clicking them (which will turn them gray, meaning they are now a wall). You can also hold left click and drag the mouse to put walls faster. As for deleition, follow the same method from insertion but with right click. After you have put the desired walls, click the `OK` button to apply the changes.

To select an algorithm, simply left click on it, which will turn it green meaning it is selected and will be used when running.

Once you have a start and finish node, you have put all the desired walls and you have selected an algorithm, click the `BEGIN` button to run. Once it is finished, you sill see the path in green and the visited nodes in red.

If you want to clear the grid , simply click on the `CLEAR` button.

The `STOP` button is meant to stop the algorithm when running in real time and since that feature is still not functional, the button has no use for the moment.
