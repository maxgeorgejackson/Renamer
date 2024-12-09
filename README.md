# Renamer
This is the github page showing how to install and use the renamer from Pathology or Hospital number to Biobank number.

## Installing environment (Windows)
This should all be done within the command prompt (CMD).

### 1. Create a conda environment:

```
conda create -n biobank python=13.1 -y
conda activate biobank
```
### 2. Installing dependancies

```
git clone https://github.com/maxgeorgejackson/Renamer/
dir Renamer
pip install pandas openpyxl
```

### 3. Using Renamer
Below is a sample script:
```
python app.py --path_excel "Sheet" --path_folder "Images" --search_column "Pathology number" --rename_column "Bio number"
```
