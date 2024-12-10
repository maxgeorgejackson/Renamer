# Renamer
This is the github page showing how to install and use the renamer from Pathology or Hospital number to Biobank number.

## Installing environment (Windows NON-MWS)
This should all be done within the command prompt (CMD).

If you do not already have conda installed, run the code below in the CMD.

```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" .\miniconda.exe /S
del miniconda.exe
```
** This can take some time to install but will not need to be done again after the first time **

## Installing environment (Windows MWS)
On univeristy computers the above installation will not work due to admin privilages.

Go to:
-> Install Univeristy Applications -> Miniconda3 (any version) 

This will propt a reboot but after this has been done once, you won't have to do it again.

### 1. Create a conda environment:

```
conda create -n biobank python -y
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
python app.py --path_excel "folder/Sheet" --path_folder "folder/Images" --search_column "Pathology number" --rename_column "Bio number"
```
Description:

--path_excel 

This is the path to your excel sheet.

--path_folder

This is the path to your folder containing the images.

--search_column

This is the column header that would contain the names of the exisitng images.

--rename_column

This is the column header that contains the new names of the files.

### Notes
- When using the paths any \ must be changed to a / due to formating. On windows when copying and pasting it sometimes uses \ .
- All of the above are case sensitive so make sure to check this.
- This only currently works for .tif files, more functionality is being added.
