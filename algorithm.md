# Algorithm Document

High Level Tasks:
- Error Check the User Input (for filename)
- Read the file (into tables)
- Calculate the profit for each movie 
- Find the highest profit
- Write the info out of the file
- Output information for highest grossing (main)/display

Highest Level Tasks:
1. Read Data from the file to a table. 
   - (function)
2. Update the table by adding one element at each row to hold the profit. 
   - (function)
3. Writing the new table onto output file. (each row using CSV values onto another file.)
4. main function




Name: read_file_to_table
purpose: Read Data from the file to a table. 
parameters: None
algorithm:
1. Set movie_table to be an empty list.
1. Read each line from a file 
1. Split the line to create a list
2. For item in range length of the list:
    - if the item index of row is a digit:
      - item index of row is equal to the integer item index of row.
1. Add the list from the second step into the main list


Name: update_table_profit
purpose: Update the table by adding one element at each row to hold the profit. 
parameters: table
algorithm: 
1. Set profit to equal 0.
1. For each row in table:
   - Set budget equal to the 3rd element of the row. 
   - Set worldwide_gross to equal the 5th element of the row.
   - Set profit to equal worldwide_gross - budget.
   - Append profit to row. 

Name: write_to_output_file
purpose: Writing the new table onto output file. (each row using CSV values onto another file.)
parameters: table, output file name.
algorithm:
1. For row in table:
    - Set line to an empty string
    - For item in row:
      - If item is a digit:
        - Line equals string of item and ","
      - else:
        - line is equal to item + ","
      - write line to the output file. 





