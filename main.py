# Programmers: Ethan D'Souza & Hazel Osborne
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/20/2024
# Lab Assignment: 10
# Problem Statement: Analyzing data on movies, their budgets, and their profits.
# Data In: A CSV file containing movie data with columns: Release Date, Title, Budget, Domestic Gross, and Worldwide Gross.
# Data Out: output showing the movie with the highest profit and a new CSV file with the original data plus a Profit column.


# Function to read data from the file into a table
def read_file_to_table(file):
    try:
        f = open(file, 'r')  # Open file for reading
        table = []
        for line in f:
            row = line.strip().split(',')  # Split line into list
            for i in range(len(row)):
                if row[i].isdigit():  # Convert numeric values to integers
                    row[i] = int(row[i])
            table.append(row)  # Add row to the table
        f.close()  # Close the file
        return table
    except FileNotFoundError:
        return None


# Function to update the table by adding a profit column
def update_table_profit(table):
    for row in table[1:]:  # Skip the header row
        profit = row[4] - row[2]  # Worldwide Gross - Budget
        row.append(profit)
    return table


# Function to write the updated table to an output file
def write_to_output_file(table, output_file_name):
    f = open(output_file_name, 'w')  # Open file for writing
    for row in table:
        line = ""
        for i in range(len(row)):
            if i < len(row) - 1:
                line += str(row[i]) + ","
            else:
                line += str(row[i])
        f.write(line + '\n')
    f.close()  # Close the file


# Function to find the highest profit film and display its details
def find_highest_profit_film(table):
    highest_profit_row = table[1]  # Start with the first movie row (skip header)
    highest_profit = highest_profit_row[4] - highest_profit_row[2]  # Calculate the first movie's profit

    for row in table[2:]:  # Start checking from the second movie row
        profit = row[4] - row[2]  # Calculate the current movie's profit
        if profit > highest_profit:  # Compare with the highest profit
            highest_profit = profit
            highest_profit_row = row

    # Output movie details with the highest profit
    print("\nMovie with the Highest Profit:")
    print("Release Date:", highest_profit_row[0])
    print("Title:", highest_profit_row[1])
    print("Budget:", highest_profit_row[2])
    print("Domestic Gross:", highest_profit_row[3])
    print("Worldwide Gross:", highest_profit_row[4])
    print("Profit:", highest_profit)


# Main function to orchestrate the program
def main():
    print("Welcome to the Movie Profit Analyzer!")

    # Prompt user for input file name
    movie_table = None
    while movie_table is None:
        input_file = input("Enter the name of the file to analyze: ")
        movie_table = read_file_to_table(input_file)
        if movie_table is None:
            print("File not found. Please enter a valid file name.")

    # Prompt user for output file name
    output_file = input("Enter the name of the output file: ")

    # Update table with profit
    movie_table = update_table_profit(movie_table)

    # Find the highest profit film
    find_highest_profit_film(movie_table)

    # Write updated data to output file
    write_to_output_file(movie_table, output_file)

    print("\nAnalysis complete! Data has been saved to", output_file)
    print("Thank you for using the Movie Profit Analyzer!")


# Run the program
main()

