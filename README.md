# PokerSquares

PokerSquares is a desktop game where the player places cards in a 5x5 grid and tries to make the best possible poker hand on each row and column.

The project is a part of a course at the University of Helsinki.



## Documents
* [Link to Manual](dokumentaatio/manual.md)
* [Link to Releases](https://github.com/Badding/ot-harjoitustyo/releases)
* [Link to Requirements specification](dokumentaatio/vaatimusmaarittely.md)
* [Link to Architecture](dokumentaatio/arkkitehtuuri.md)
* [Link to Changelog](dokumentaatio/changelog.md)
* [Link to Time used](dokumentaatio/tuntikirjanpito.md)


### Requirements 
- Python 3.8 or higher.
- Poetry installed

## Installation

Clone repository
```bash
git clone https://github.com/Badding/ot-harjoitustyo.git
```
Install
```bash
poetry install
```
Run before starting the app
```bash
poetry run invoke build
```
Run app
```bash
poetry run invoke start
```
Run tests 
```bash
poetry run invoke test
```
Run tests with coverage report
```bash
poetry run invoke coverage-report
```
Run pylint
```bash
poetry run invoke lint
```