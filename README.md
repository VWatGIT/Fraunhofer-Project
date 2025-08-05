# Fraunhofer Jupyter Notebooks Project

This repository contains Jupyter notebooks for data analysis and research projects.

## Project Structure

```
├── notebooks/          # Jupyter notebooks
├── data/               # Data files (raw and processed)
├── src/                # Python modules and utilities
├── outputs/            # Generated outputs (plots, reports, etc.)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Fraunhofer
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start Jupyter Lab:
   ```bash
   jupyter lab
   ```

## Usage

- Place your notebooks in the `notebooks/` directory
- Store data files in the `data/` directory
- Add reusable Python code in the `src/` directory
- Generated outputs will be saved in the `outputs/` directory

## Contributing

1. Create a new branch for your work
2. Make your changes
3. Commit and push your changes
4. Create a pull request

## Dependencies

See `requirements.txt` for a list of Python packages required by this project.
