# 🧠 TNT 2025 - AI Applications

This repository contains machine learning and deep learning project examples using Python, scikit-learn, and PyTorch.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/andrediluca/tnt2025_ai_application.git
cd tnt2025_ai_application
```

### 2. Create a Virtual Environment (Recommended)

Using venv:

```bash
python -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows
```

Or with conda:

```bash
conda create -n tnt2025 python=3.12
conda activate tnt2025
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
To check if your setup is ready to go, run the ``:
```bash
python check_imports.py
```

- ✔ indicates successful import.

- ✘ indicates the package is missing.

- ⚠ shows other errors (e.g., version mismatches that raise exceptions on import)

### 4. Run the Jupyter Notebooks
```bash
jupyter notebook
```
Then open the .ipynb files inside the folder.

### 5. Download data
To be able to run `01-CNN_eregressor.ipynb`, create a folder `data` inside the project foder:
```bash
mkdir data
```

After that, download the data available [here](https://zenodo.org/records/846388#.WumAlC-B1-V) and move the files inside the `data` folder.


## Dataset Source
We use the following datasets:
-  [Breast Cancer Wisconsin Diagnostic Dataset](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) 
-  [Electromagnetic Calorimeter Shower Images with Variable Incidence Angle and Position](https://zenodo.org/records/846388#.WumAlC-B1-V) 


### License
This project is for academic and demonstration purposes.