# Flashcard App for Learning German Noun Articles
This is a spaced-repetition terminal app specifically made for learning articles for German nouns. Currently there are very few nouns included, but users can easily add their own. 
The app is text-based and inputs are usually given by the user as a number from the menu followed by Enter to confirm. It is using the anki algorithm, found [here](https://faqs.ankiweb.net/what-spaced-repetition-algorithm.html).

This is a beginner project to learn how to make terminal programs, so expect some bugs to be present. It is also still a work in progress with multiple known errors.

## Getting Started
Use `git clone https://github.com/thomasherstad/terminal-flashcard-app.git` to clone the repo. 

Start the app in the terminal by running the command `. main.sh`. This will print the main menu where you have multiple options.

### 1. Play
There is only one mode supported at the moment. It goes through every single noun in the csv-file sorted by the "next review time" property. I will add a limit to how many nouns with the status "learning" you can have at the same time at some point in the future.

### 2. View All Nouns
All nouns in the list can be viewed from the main menu by typing 1 then Enter.

### 3. Adding a Noun
Add a noun from the main meny by typing 2 then Enter, then follow the instructions given. Nouns can theoretically also be added by directly editing the csv-file, but make sure filling in at least Noun and Article, otherwise the app might break.

### 4. Search for a Noun
It's possible to search the list to see if a noun already exists. This is done from the main menu by typing 3 and Enter. It will prompt the user for a noun and nly the noun itself is needed, so leave the article out of the query. Where multiple nouns are the same but have different articles, for instance die See (Ocean) and der See (Lake), all of them will be returned.

### 5. Editing or Remove a Noun
The user can edit or remove the nouns directly in the program. Follow the steps from the main menu.

### 6. Saving Changes
Save any changes you have made by choosing this option.