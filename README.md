# Roulette_POC
A POC roulette game, that will start deleting files if you don't answer its questions correctly <br>

Eventually I would like this to be in Rust so it can be an executable, but that will come later

> NOTE: for developing purposes, typing 'specialescape' will exit the program with no damage.

Changing Questions: To change the questions, check out the 'Question Blocks' section of the code, here you can add, remove, or change what <br>
questions get asked to the victim. If adding questions, add the function name (ex question_one.q) to 'question_list' under main() <br>

Changing files to delete: To change files/directories to delete, check out the file variable under file_nuke(), here you can put in whatever directories <br>
you want to potentially delete. <br>

Initial screen:<br>
  ![image](https://user-images.githubusercontent.com/91687869/187047228-9819ab4a-f933-4e1a-9886-40fcb1886fff.png)

Bad Answer:<br>
  ![image](https://user-images.githubusercontent.com/91687869/187047248-8b507e0a-5a94-4ba5-bdde-062ab1ec57e5.png)

Good Answer:<br>
  ![image](https://user-images.githubusercontent.com/91687869/187047263-bffd3071-85a2-4ba9-ab5c-51cd9469dc14.png)

CTRL+C Escape attempt:<br>
  ![image](https://user-images.githubusercontent.com/91687869/187047283-c1cf7ecd-3a0e-4657-b1e6-848ce92f3224.png)
