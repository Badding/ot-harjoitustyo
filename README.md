# PokerSquares

PokerSquares is a desktop game where the player places cards in a 5x5 grid and tries to make the best possible poker hand on each row and column.

The project is a part of a course at the University of Helsinki.

## Documents
* [Link to Requirements specification](dokumentaatio/vaatimusmaarittelu.md)
* [Link to Changelog](ddokumentaatio/changelog.md)
* [Link to Time used](ddokumentaatio/tuntikirjanpito.md)


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
Run 
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