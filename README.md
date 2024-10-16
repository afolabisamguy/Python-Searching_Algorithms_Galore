# Python-Searching_Algorithms_Galore

## Overview

This project is a collection of various search algorithms implemented to test their efficiency and speed. While working on a larger project that involved building a server capable of receiving requests and searching for files in under 0.005 milliseconds, I explored multiple search algorithms to determine which was the fastest and most efficient for the task. Though the server implementation is not included in this project, the search algorithms used for testing are presented here for educational purposes.

## Search Algorithms Implemented

The project contains implementations of several popular search algorithms, including but not limited to:

- **Boyer-Moore**: A pattern matching algorithm that skips sections of the text to achieve efficient searching.
- **Knuth-Morris-Pratt (KMP)**: A search algorithm that pre-processes the pattern to allow for efficient searching with no backtracking.
- **Aho-Corasick**: An efficient multi-pattern search algorithm that constructs a state machine to find multiple occurrences of patterns.
- **Fibonacci Search**: A comparison-based algorithm similar to binary search but uses Fibonacci numbers for division.
- **Other Algorithms**: Several other searching algorithms are also included to test their performance in different scenarios.

## Project Structure

- **boyermoore.py**: Contains the implementation of the Boyer-Moore search algorithm.
- **kmp.py**: Implements the Knuth-Morris-Pratt (KMP) search algorithm.
- **ahocorasick.py**: Implements the Aho-Corasick multi-pattern matching algorithm.
- **fibonacci.py**: Implements the Fibonacci search algorithm.
- **constants.py**: Contains any constants used across the project.
- **other_algorithms.py**: Includes other search algorithms explored during this project.

## Purpose

The primary goal of this project is to benchmark various search algorithms to determine which performs the fastest under different conditions. The server this work was intended for required extremely fast file searching, and this repository captures the experimentation with multiple algorithms to find the optimal one.

Although this project does not include the actual server code, it serves as a useful reference for testing and comparing different search algorithms for tasks that require efficient searching.

## Installation and Usage

To run the search algorithms, follow these steps:

1. **Clone the repository**:
  
2. **Navigate to the project directory**:

3. **Run the individual scripts**:
   You can run the Python files independently to see how each algorithm works:

## Key Features

- **Efficiency Testing**: Each algorithm can be used to measure its speed and efficiency in different search scenarios.
- **Multiple Algorithm Implementations**: Provides a range of algorithms for pattern matching and searching tasks.
- **Performance Benchmarking**: This project enables you to compare various search algorithms under the same conditions.

## Future Improvements

In the future, this project could be expanded to:
- Include detailed performance benchmarks for each algorithm.
- Test the algorithms with larger datasets and various file types.
- Integrate the algorithms into an actual server project to demonstrate real-world usage.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to explore the different search algorithms and use them in your own projects to find the most efficient search solution for your specific needs!
