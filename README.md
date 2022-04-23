# pygame_sandbox

Purpose of this project is to make python programming exercises in the game form
like in codecombat, codingame, letpy etc.

User receives some virtual world environment, and he has to write code to solve given problem.
Each step should be animated and easy to navigate.
Text only tasks like "here is the input, give me the output" are not fun.
Ideally, code written to solve the task should be written in the game window, not in the text editor outside.
Initially there is no need for several quests, single one is enough.
Let's say it would be the same diamond collecting quest from codecombat. 

Some ideas for the future:
* move to the target using compas (Thor quest from codingame)
* fire missile at the closest enemy (first trivial quest from codingame)
  * 2 enemies by name
  * N enemies by name
  * N coordinates
* delivery man and the building
* mazes solving
* tasks from human resource machine

## Roadmap

* v0.1.0 no programming part. Only main architecture and game world manipulated via keyboard
  * make a proper Game class and proper game loop
  * add map data with several graphics layers (use 2d arrays from NumPy)
  * add world (or player) manipulation from the keyboard
  * add trivial graphics, so it doesn't look ugly
  * add simple ui
  * add some kind of playback functions. Begin from the scratch, animate next step, animate prev step
* v0.2.0 programmatically solvable game, but without code editor
  * replace player control from the hardcoded script
  * run script selected by file selection dialog
  * isolate code execution so crashes of script does not affect the game
    * https://stackoverflow.com/a/3068475
    * https://discuss.python.org/t/interpreter-independent-isolated-virtual-environments/5378
  * show selected code in the game window
  * show code output in the game window
* v0.3.0 add code editing inside 
  * make more or less complete support for code editing
    * all standard text editor features like ctrl+A, ctrl+Z, double click to select the word etc
    * coloring
    * autocompletion
    * selection
