## Focus

## Title screen logic
- A title screen asking what you want to do:
    - Play
        - Choose how many words you want to practice, which creates a queue with those words
    - Add word
    - Print list of words
    - Search for word
    - Edit word
        - Also delete
    - Close program

## Database csv
- Create the edit-function
    - Edit word, definite article, plural, translation
- Write tests for read and write

## Bugs


## For later
- Refactor db_csv_handler.py to only be reading and writing to csv, and move all list handling to another module or class
- Sorting improvement: If we have the same noun with different articles, sort Der->Die->Das
- 