# Architecture

## Structure

The application has three layers, UI, service and repositories. The package UI contains the user interface, in the service is responsible of logic and through repository is the interface to database.

## UI

### Views

+ login 
+ createuser
+ game
+ info

The class UI handles the change between views. Loginview contains way to login, change to createuser view and quickplay option without logging in. In the game view is the main usage of the application. Game view contains transition to info view.

### Service

The service class is a bridge between the UI and repository

### Repository

UserReposotory class handles sql queries to the database. 

## Class diagram
```mermaid
 classDiagram
    AppService <|-- UI
    UserRepository <|-- AppService
    GameRepository <|-- AppService
    GameRepository <|-- "1" Deck
    Deck <|-- "52"Card
```

## Functionality

Diagrams from main functionality of the game. User creates username and then logs in to the game.

### user Login sequence diagram

```mermaid
    sequenceDiagram
        actor User
        User->>+UI: "login"
        UI ->>+ App_service: login("molli", "olli")
        App_service ->>+ UserRepository: check_password("molli", "olli")
        UserRepository -->>- App_service: True
        App_service -->>- UI: handle_quickplay()
        UI-->>-User: "game starts"
```

Sequence diagram for user creation.

### User creation sequence diagram

```mermaid
    sequenceDiagram
        actor User
        User->>+UI: "create user"
        UI ->>+ App_service: create_user("keijo", "keke1")
        App_service ->>+ UserRepository: get_user("keijo")
        UserRepository -->>- App_service: None
        App_service ->>+ UserRepository: add_user("keijo")
        App_service -->>- UI: True
        UI-->>-User: "User created!"
```

### Placing the last card sequence diagram

Sequence diagram for user placing the last card to the game.

```mermaid
    sequenceDiagram
        actor User
        User->>+UI: "click button"
        UI ->>+ App_service: place_card(row)
        App_service ->>+ Game: place_card(row)
        Game -->>- App_service: True
        App_service -->>- UI: True
        UI --> UI: place_label(row, index, card)
        UI --> UI: update_scores()
        UI --> UI: update_delt_card()
        UI --> UI: update_total_score()
        UI -->+ App_service: is_game_over()
        App_service ->>+ Game: is_game_over()
        Game -->>- App_service: True
        App_service -->>- UI: True
        UI --> UI: place_newgame_button()
        UI-->>-User: "click newgame"
```
