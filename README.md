# AlgoMonster - Algorithms & Data Structures Portfolio

A production-grade Python collection of classic Data Structures & Algorithms, featuring type-annotated implementations, LeetCode/AlgoMonster problem solutions, and comprehensive `pytest` suites.

---

## 📚 Table of Contents

- [Features](#-features)
- [Repository Structure](#-repository-structure)
- [Implemented Algorithms](#-implemented-algorithms)
  - [Binary Search](#-binary-search)
  - [Two Pointers](#-two-pointers)
  - [Sliding Windows](#-sliding-windows)
  - [Depth First Search](#-depth-first-search)
- [Getting Started](#-getting-started)
  - [Installation](#installation)
  - [Running Unit Tests](#running-unit-tests)
  - [Code Quality & Linting](#code-quality--linting)
- [Disclaimer & Production Notes](#-disclaimer--production-notes)

---

## ✨ Features

- **Strict Type Annotations**: Type hints (`mypy` compliant) across all algorithms and test files.
- **Comprehensive Testing**: 180+ unit tests powered by `pytest` with parameterized test cases.
- **Modern Tooling**: Code formatted and linted using `ruff` and type-checked with `mypy`.
- **Clean API Design**: Compatible with LeetCode `Solution` class definitions, standalone functions, and `snake_case` / `camelCase` aliases.

---

## 📁 Repository Structure

```text
algo_portfolio/
├── src/
│   ├── binary_search/             # Binary search patterns and variations
│   ├── depth_first_search/        # Depth-First Search tree algorithms
│   ├── two_pointers/              # Two-pointer technique implementations
│   ├── sliding_windows/           # Fixed and dynamic sliding window patterns
│   └── tests/                     # Comprehensive pytest test suites
│       ├── test_binary_search/
│       ├── test_depth_first_search/
│       ├── test_two_pointers/
│       └── test_sliding_windows/
├── pyproject.toml                 # Tool configuration for pytest, mypy, and ruff
├── README.md                      # Project documentation
└── LICENSE
```

---

## 🛠 Implemented Algorithms

### 🔍 Binary Search (`src/binary_search/`)
- **Basic Binary Search**: Standard search in a sorted array (`basic.py`)
- **Target Boundary Search**: Finding element or insertion index (`bigger_target.py`)
- **First & Last Occurrence**: Finding boundary indices for duplicate elements (`first_occurrence.py`, `last_occurrence.py`)
- **First True Element**: Finding the boundary condition in boolean arrays (`first_true.py`)
- **Rotated Sorted Array**: Finding the minimum element in a rotated array (`find_min_rotated.py`, `find_minimum_in_rotated_array.py`)
- **Peak Index in Mountain Array**: Binary search on monotonic properties (`peak_mountain.py`)
- **Square Root Estimation**: Integer square root calculation via binary search (`square_root_estimation.py`)

### 👈👉 Two Pointers (`src/two_pointers/`)
- **3Sum**: Finding all unique triplets summing to zero (`3sum.py`, `three_sum.py`)
- **Move Zeros**: In-place array modification preserving relative order (`move_zeros.py`)
- **Remove Duplicates**: In-place duplicate removal from sorted arrays (`remove_duplicates.py`)
- **Consecutive Characters**: Longest substring of identical characters (`consequtive_characters.py`)
- **Subarray Sum**: Fixed and target sum subarray problems (`subarray_sum.py`, `subarray_sum_target.py`)
- **Find All Anagrams**: String permutation search (`find_all_anagrams.py`)
- **Middle of Linked List**: Fast and slow pointer technique (`middle_of_linked_list.py`)
- **Index of First Occurrence**: Substring search (`index_of_first_occurrence_in_string.py`)

### 🪟 Sliding Windows (`src/sliding_windows/`)
- **Minimum Size Subarray Sum**: Minimal length subarray whose sum $\ge$ target (`min_sub_array_len.py`)
- **Minimum Positive Sum Subarray**: Smallest positive sum of subarray with size between $l$ and $r$ (`minimum_sum_subarray.py`)

### 🌲 Depth First Search (`src/depth_first_search/`)
- **Tree Max Depth**: Calculating maximum depth (number of edges on longest root-to-leaf path) of a binary tree (`tree_max_depth.py`)

---

## 🚀 Getting Started

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/komilolimov/algomonster.git
cd algo_portfolio
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt # or install pytest, ruff, mypy
```

### Running Unit Tests

Run the full test suite using `pytest`:

```bash
python -m pytest
```

Run tests with verbose output:

```bash
python -m pytest -v
```

### Code Quality & Linting

Check code formatting and linting rules with `ruff`:

```bash
# Run linter
python -m ruff check

# Format code
python -m ruff format
```

Run static type checking with `mypy`:

```bash
python -m mypy src
```

---

## ⚠️ Disclaimer & Production Notes

> **Note for Production**: Для реальных задач в Python следует использовать встроенный модуль [`bisect`](https://docs.python.org/3/library/bisect.html) (функции `bisect_left` и `bisect_right`), так как он оптимизирован на уровне C-API. Данная реализация написана исключительно в образовательных целях и для демонстрации понимания алгоритмов и структур данных.
