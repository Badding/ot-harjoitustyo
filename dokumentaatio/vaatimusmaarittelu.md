# requirements specification

## Intro

Poker Squares is a Python-based card game application where users have the option to log in to access their statistics or start a quick play sessions without logging in. The objective of the game is to strategically place drawn cards onto a table grid, aiming to create the strongest possible hands for each row and column. All game statistics and user data are stored in a database.

## Users

In Poker Squares, players are the only type of user. Each player's statistics are uniquely identified by their username.

## UI 

The app starts in the login screen, where users can log in to access their accounts or create a new account. However, users also have the option to play quick games without creating an account.

Upon logging in or selecting the quick game option, users are directed to the game screen, where they can start playing Poker Squares.

Once the game is over or the user chooses to log out, the application navigates to the statistics page. Here, users can review their game statistics and performance."

This version outlines the flow of the application more clearly, detailing the sequence of actions from the starting page to the game screen and finally to the statistics page.

## Functionality

### Accounts

* Create a new user account
* Login and logout
* Change user

### While playing
 
* Quick play without user account
* Graphics showing current game state
* Information screen with game rules
* Calculate current score after every move

### After Game over

* Show Stats After the Game Ends
* Start a new game


## Future ideas
* save game
* options for different rule sets for poker squares
* different solitaire games 

