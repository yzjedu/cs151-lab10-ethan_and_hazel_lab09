Highest Level Tasks:
1. Read Data from the file to a table. 
   - (function)
2. Update the table by adding one element at each row to hold the profit. 
   - (function)
3. Writing the new table onto output file. (each row using CSV values onto another file.)
4. main function


* Name: read_file_to_table
* purpose: Read Data from the file to a table. 
* parameters:file
* algorithm:
1. Open file for reading
2. Set table as an empty table
3. Read each line from the file 
4. Split the line to create a list
5. For item in range length of the list:
   1. if the item index of row is a digit:
      1. item index of row is equal to the integer item index of row.
6. Add the list from the second step into the main list
7. Close the file
8. return table



* Name: update_table_profit
* purpose: Update the table by adding one element at each row to hold the profit and find the highest profiting movie
* parameters: table
* algorithm:
1. For each row in table:
   1. Set profit to equal the 5th element of row minus the 3rd element of row.
   2. Append profit to row.
2. return table

* Name: write_to_output_file
* purpose: Writing the new table onto output file. (each row using CSV values onto another file.)
* parameters: table, output file name.
* algorithm:
1. Open the file for writing
2. For row in table:
   1. Set line to an empty string
      1. For item in row:
         1. Check if item is a digit:
            1. Line equals string of item and ","
         2. else:
            1. line is equal to item and ","
      2. write line to the output file. 
3. Close the file


* Name: find_highest_profit_film
* purpose: finding the highest profiting film of a list of movies and output information based on that row.
* parameters: table
* algorithm:
1. initialize highest_profit
2. set highest_profit to equal table index 0
3. for row in table
   1. check if the sixth element is greater than highest_profit:
      1. Set highest_profit_row to equal row
4. Output Release Date, Movie Title, Movie Budget, Domestic Gross, Worldwide Gross, and profit of highest_profit row
5. Return


* Name: main
* purpose: analyze data on movies, their budgets, and their profits
* parameters: table, output file name.
* algorithm:
1. Output welcome message to user
2. Prompt user to enter the name of the file they would like analyzed. Store as input_file
3. While input_file does not exist:
   1. Re-prompt user to enter a valid file name
4. Prompt user to enter the name they would like the new data to be stored in. Store as output_file
5. Call read_file_to_data function and store as movie_table.
6. Call update_table_profit and store as movie_table
7. Call find_highest_profit_film
8. Call write_to_output_file function
9. Output ending / thank you message to user

