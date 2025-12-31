# diag2025

A small repository containing several Python mini-projects and ML notebooks used for coursework and exercises.

---

## Project structure

- `basic_python/` 🔧
  - `miniproject01/` ✅
    - `main.py` — Number guessing game (CLI). Contains functions to generate a random number, compute distance to the guess, and a game loop with input validation.
    - `miniproyecto1.py` — Duplicate of `main.py` (same number guessing game) — alternate entry.
    - `test_main.py` — PyTest unit tests for the number-guessing game (tests generation, distance calculation and game behavior via mocks).
    - `pyproject.toml` — Project metadata / package configuration (present but minimal).
    - `README.md` — (empty) intended for this miniproject.
  - `miniproject02/` ✅
    - `miniproyecto2.py` — Store comparator simulator. Functions to generate 3-letter store codes, process instructions (discount, shipping, quantity x price), and run an interactive CLI to simulate rounds and determine a winner.
  - `miniproject03/` ✅
    - `miniproyecto3.py` — Lab management CLI. Loads available tests from `disponibilidad.txt` and patient requests from `pacientes.csv`, supports commands to attend patients, add test availability, and print availability status.
    - `disponibilidad.txt` — Initial availability of tests (test name + available slots).
    - `pacientes.csv` — Example patients and their requested tests.

- `ml_and_genai/` 🧠
  - `final_project.ipynb` — Final project notebook for "Fundamentos de Machine Learning e Inteligencia Artificial Generativa". Implements data loading, EDA and model experiments for a Hate Speech Detection task (data analysis, preprocessing, classic ML and transformer-based approaches). Includes analysis, visualization and training/evaluation code.

- `python_for_machine_learning/` 📚
  - `Miniproyecto_1.ipynb` — Exploratory data analysis exercises (pandas): data cleaning, descriptive statistics and basic transforms.
  - `Miniproyecto_2.ipynb` — Regression tasks: data generation, closed-form linear regression, plotting and error analysis.
  - `Miniproyecto_3.ipynb` — Clustering tasks: k-means implementation and visualization.
