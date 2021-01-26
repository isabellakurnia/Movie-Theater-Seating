# Movie Theater Seating

## Approach
Go through the list of inputs chronologically and assign seats from left to right until a row is full, and repeat this until the whole cinema is full. </br>
</br>
Tradeoff: May have leftover seats for each row where no other groups can fit into. </br>
Solution: Split up remaining groups to hopefully allow some more people who have reserved into the theatre.

## Assumptions
- Customers have no preference on their seats
- Late customers are fine with being divided from their groups
- Safety is the number one priority, hence will include both three seats over and one row buffer

## Instructions for Usage
1. Run the script
2. User will be prompted with the input file. </br> Note: Input file must be a txt file
3. Program will return the output file path

## Executing Tests
In order to change inputs, simply create a txt file with any name and ensure that it is in the same folder as the project. Plug in this name to the prompt that users will see when running the program.
