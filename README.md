# ENGG1330
A game that me and my group made in 2023 for the course ENGG1330 

--------------
About Our Game
--------------
The game we've made is called 'Poker Crush'. 
Similar to the popular mobile game Candy Crush Saga, it's a match-3 puzzle game where the player needs to "connect" 3 of the SAME symbols to cancel them.
Instead of candy, we have used the poker symbols (♡,♢,♤,♧) from the poker card game to represent the so-called "candy"
In the code, this is represented by "h","d","s","c" respectively. However, when the board is printed, the actual symbols are shown
Our game has different difficulties that the player can choose at the start
Depending on the difficulty that the player has chosen, he/she will get more/less moves and the board will also be bigger/smaller. 
Every move, a player can choose to swap a piece with another piece. However, this swap will ONLY work if the swap results in a match of 3 or more symbols. 
Otherwise, the move is considered invalid and the user is prompted to enter the move again
Each time a player connects 3 symbols together, those symbols disappear from the board and 3 points are awarded and added to the total score.
The player can also connect more than 3 symbols in a row/column resulting in a cancellation of those symbols and the symbol being "upgraded".
These upgraded symbols are represented by coloured-in versions of the original poker symbols (♥,♦,♠,♣). 
In the code, the upgraded pieces are represented by uppercase versions of the letters "h","d","s","c" i.e. "H","D","S","C"
Apart from the regular symbols, we also have a super piece represented by a ✮ symbol and this is represented by the letter "A" in our code
When the same upgraded symbols are matched with the same type of symbol, the score increases by a much larger amount.
(The different types of upgraded symbols, their features, how they work are listed in the user manual below)
Our score system works exponentially, meaning that a larger number of matches/connecitons result in a much greater score increase. 
If the player runs out of moves or if the game has no valid moves left, then the game is over and the player's score is displayed at the end

You may be inclined to think that this is a candy crush rip-off 
Although it is a match-3 puzzle game in essence, what sets us apart are our upgraded pieces and our exponential scoring system.
Our upgradeded pieces are designed to be unique from candy crush and have different abilities depending on different matches with them 
(upgraded pieces listed in the user manual below)
Our exponential scoring system is unique in that the more matches a player can get at once, the score scales exponentially which 
is not something that a normal match-3 puzzle game has. By doing this, we essentially reward players that are able to spend more time looking for matches


-------------------------------------
The User Manual & How to run the game
-------------------------------------
***********READ THOROUGHLY***********

1. run the game by typing "python maingame.py" in the terminal

2. The player is first prompted to enter the difficulty and can type 'easy', 'medium' or 'hard' to select the relevant difficulty

3. The higher the difficulty, the smaller the board and the fewer the number of moves the player gets

4. The player can then choose which piece they want to swap by inputting the x and y coordinate and the direction(w,a,s,d), 
this move should be in the form of (x y direction). For the direction, enter "w" to swap up, "a" to swap left,
"s" to swap down, and "d" to swap right. As an example, if you wanted to move the piece at 
position (2,4) upwards, you would enter "2,4,w". (Note: WITH commas) 

5. If you would like to exit the game, simply type "exit" when you are prompted to enter a move

6. The move is tested for validity. A move is valid if it is within the range of the board AND 
if swapping the piece results in a cancellation. 

7. If there are 3 of the same symbols in a row/column, the 3 symbols will be cleared and 3 will be added to the score of the player

8. If there are MORE than 3 of the same symbols in a row/column, then the following apply:
    if there are 4 pieces in a row/column: clear the 4 pieces AND generate a upgraded coloured piece with each poker symbol having a different power:
                ♥: clear 1 horizontal row (if contain upgrade, clear more rows)
                ♦: clear 1 vertical column (if contain upgrade, clear more columns)
                ♠: clear 3 * 3 area with itself as the center (if contain upgrade, clear area = (3 + upgrade count * 2) * (3 + upgrade count * 2))
                ♣: if x is odd, row clear odd x position, else clear even x position, same with column
                
    if there are 5 pieces in a row/column: generate a "super piece" with a ✮ symbol. 
    For a super piece, swapping with ANY piece is valid (even if it doesnt create a match of 3 or more).
    This will clear all the pieces of the same type that the super piece is swapped with. 
    For example, if ✮ is swapped with ♧, then all the ♧ pieces will get cleared from the board 
    and the number of cleared pieces will be added to the player's total score

    if there are 5 pieces in a T-shape or an L-shape, then those pieces will get cleared and also generate a super piece 


9. win condition: there isn't one! Just try to get as much score as possible and compare it to others to see how well you do!
