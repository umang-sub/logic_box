# Logic Box

Logic Box is a beginner-friendly Python command-line application for practicing basic programming logic. It provides an interactive menu where users can generate a star pattern, analyze a range of numbers, and calculate the total sum of that range.

## Overview

This project demonstrates core Python concepts such as:

- User input handling
- Conditional statements
- Loops
- Range-based number processing
- Basic command-line interaction

The application runs entirely in the terminal and does not require any external libraries.

## Features

- Interactive menu-driven interface
- Star pattern generation based on user-defined row count
- Even and odd number identification within a selected range
- Sum calculation for all numbers in the selected range
- Simple exit option for ending the program

## Project Structure

```text
logic_box/
├── README.md
└── logicBox.py
```

## Requirements

- Python 3.x

No additional dependencies are required.

## Getting Started

### 1. Clone or Download the Project

Place the project files on your local machine.

### 2. Navigate to the Project Directory

```bash
cd logic_box
```

### 3. Run the Application

```bash
python3 logicBox.py
```

You can also run it from the parent directory:

```bash
python3 logic_box/logicBox.py
```

## Usage

After starting the program, the following menu is displayed:

```text
1. Generate a pattern
2. Analyze a number
3. Exit
```

Enter the number that matches the action you want to perform.

## Example Output

### Pattern Generation

Input:

```text
Enter the number of rows for the pattern: 4
```

Output:

```text
*
* *
* * *
* * * *
```

### Number Analysis

Input:

```text
Enter the start of the range: 1
Enter the end of the range: 5
```

Output:

```text
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
sum of all numbers from 1 to 5 is: 15
```

## How It Works

The application uses a continuous loop to keep showing the menu until the user chooses to exit. Based on the selected option:

- Option 1 asks for a row count and prints a star pattern.
- Option 2 asks for a start and end value, checks each number for even or odd status, and calculates the range sum.
- Option 3 exits the program.

## File Description

| File | Description |
| --- | --- |
| `logicBox.py` | Main Python script containing the menu, pattern generator, and number analyzer. |
| `README.md` | Project documentation. |

## Future Improvements

Possible improvements for this project include:

- Add input validation for non-numeric values.
- Handle invalid menu choices more clearly.
- Split the program into reusable functions.
- Add more number analysis options, such as prime number checking or factorial calculation.
- Improve formatting of terminal output.

## License

This project is currently not licensed. Add a license file if you plan to share or distribute it publicly.


[![Click Here](https://img.shields.io/badge/Click%20Here-Explanation%20Video-blue?style=for-the-badge&logo=youtube)](https://drive.google.com/file/d/14uTa8monF2tsOfqgJyUtyPeZRPjWAef5/view?usp=sharing)
