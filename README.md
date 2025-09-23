# Algorithm Animations with Manim

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Manim](https://img.shields.io/badge/Manim-222c3a?style=for-the-badge&logo=manim&logoColor=white) ![Algorithms](https://img.shields.io/badge/Algorithms-FF6B6B?style=for-the-badge&logo=algorithms&logoColor=white)
![Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)

## Description

This repository contains animated visualizations of popular sorting algorithms created using [Manim](https://www.manim.community/), a mathematical animation engine. These animations are designed to help visualize and understand how different sorting algorithms work step-by-step.

## Current Status of Implemented Algorithms

- ✅ **Bubble Sort**: Completed
- ✅ **Insertion Sort** - Completed
- ✅ **Selection Sort** - Completed
- Merge Sort
- Quick Sort

## Getting Started

### Requirements

- Python 3.7+
- [Install Manim Community Edition](https://docs.manim.community/en/stable/installation.html)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rishabpremish/Algorithms-Animations-Manim.git
   cd Algorithms-Animations-Manim
   ```

2. Install Manim:
   ```bash
   pip install manim
   ```

### Running Animations

To generate an animation, use the following command:

```powershell
python -m manim filename.py ClassName -pql
```

Example:

```powershell
# Bubble Sort animation
python -m manim bubble_sort.py BubbleSort -pql
```

> **Tip:** For a better development experience, consider using the [Manim Sideview](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview) extension for Visual Studio Code. It provides live previews of your animations as you work.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Manim Community](https://www.manim.community/) for the amazing animation framework
