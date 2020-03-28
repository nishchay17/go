
## **welcome to go directory utility**

It is a simple cmd utility, which decreases the amount of time to *cd* into desired directory, it works by storing path of *dir* in the database with a name associated with it, and if you want to *cd* into a *dir*, you just type go "name".
**Example**:
- Here we added a new *dir* into the database, with the name **projectgo**, using command `go add projectgo` (it adds the current *dir*)
![Here we added a new dir into the database](https://raw.githubusercontent.com/nishchay17/nishchay17.github.io/master/go/go1.jpg)

 - Here we  use command `go all` to view all the *dir* stored inside our database, and used `go projectgo`
 ![Here we  use command go all to view all the dir stored inside our database](https://raw.githubusercontent.com/nishchay17/nishchay17.github.io/master/go/go2.jpg)
 
 - Here is our new window opened, with the *dir* that we stored
 ![enter image description here](https://raw.githubusercontent.com/nishchay17/nishchay17.github.io/master/go/go3.jpg)
## Available commands:

 1. add - To add current directory to database

		 go add <name>

2. all - To show all directory stored in database

		go all

3. go - To go to the directory associated to the name

		go <name>

4. remove - To remove directory from database

		go remove <name>

## Installation 
Run  `pip install -e .` in the root directory of the project, you might get some error
while doing so, but it will work just fine.
