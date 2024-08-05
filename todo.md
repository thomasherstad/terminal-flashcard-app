## Focus
- 
    

## Title/Menus screen logic
- Add searching for another word after search and cancel
- Need to add a cancel to add noun

## Play function
- Standard mode
    - Pull out the 15 top nouns
    - Show front side
    - Give options for article
    - Give options for plural
    - Show rear side
    - Need to re-sort on the datetime object

## Database csv 
- Write tests for read and write

## NounList class
- Have populate_from_list function use a loop to make it work when changing csv format
- Create tests
- Function to remove duplicates

## Noun class
- Implement spaced repetition
    - Status
    - Steps
    - Ease
- Move it up and down in the steps/status

## Bugs
- Need to clean the screen before main menu. But then maybe add a sleep
- Crash when you choose done before editing a word

## For a Finished App
- Custom amount of Nouns mode

## For Later
- Sorting improvement NounList: If we have the same noun with different articles, sort Der->Die->Das
- Implement ability to have multiple decks
- Apply filter to the list
- Find out what to implement for spaced repetition
- Play endless mode
- Graphic for terminal view, nice card, menu

## Done since last commit
- Sort list on time in main before playing
- Sort list on noun before printing to csv