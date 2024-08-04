## Focus
- Getting all main menu functions working except play
    - Add searching for another word after search and cancel
    - Need to add a cancel to add noun

## Title screen logic
- A title screen asking what you want to do:
    - Play
        - Choose how many words you want to practice, which creates a queue with those words
    - Add word
        - Need to save the word to the csv
    - Print list of words
    - Search for word
    - Edit word
        - Also delete
    - Close program

## Play function
- Standard mode
    - Pull out the 15 top nouns
    - Show front side
    - Give options for article
    - Give options for plural
    - Show rear side
    - Keep score
    - Finish criteria: Until all cards have been finished twice

## Database csv 
- Write tests for read and write

## NounList class
- Have populate_from_list function use a loop to make it work when changing csv format
- Expand the sorting function to add the ability to sort on a different column
- Create tests
- Function to remove duplicates

## Noun class
- Implement time/date

## Bugs
- Need to clean the screen before main menu. But then maybe add a sleep
- Crash when you choose done before editing a word

## Finished
- Implement algorithm for choosing which card to show. Spaced repetition
- Custom amount of Nouns mode

## For Later
- Sorting improvement NounList: If we have the same noun with different articles, sort Der->Die->Das
- Implement ability to have multiple decks
- Apply filter to the list
- Find out what to implement for spaced repetition
- Play endless mode
- Graphic for terminal view, nice card, menu

## Done since last commit
