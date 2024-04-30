# UserManual

Download the newest [release](https://github.com/Badding/ot-harjoitustyo/releases), click  __Source code__ from __Assets__

### Installation

To Install dependencies 

poetry install

Run before starting the app the database needs to initialized

poetry run invoke build

Run app

poetry run invoke start

## To play quick game without user account

In the login screen click "Quick play"

![](./pics/start.png)

## Create new user

In the login screen click "Create User"

Enter User name and repeat password to both password fields. Click "Create User"
If User was created successfully a "User created!" message appears.
Click "Back" to go back to login screen. 

![](./pics/create.png)

## Login to game

Enter user name and password and click login

![](./pics/login.png)


## Gameplay

The object of this game is to get the best possible poker hand for each row and column. You can place a card by pressing the blue button. The game ends when the whole table is full

![](./pics/game.png)


## Help screen and logout

To access help screen press the "I" button on top right of the game screen. This screen shows info and info how scoring works in the game.
To logout, click "Logout". User returns to login screen.

![](./pics/help.png)
