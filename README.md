<h1 align="center">
  <img src="https://github.com/Hudson-Liu/Melanoma-Classification/blob/main/docs/readme_logo.png" width="30%">
  <br>
  SIIM-ISIC - Classification Project
  <br>
  <img src="https://img.shields.io/github/commit-activity/y/Hudson-Liu/Melanoma-Classification?style=for-the-badge&labelColor=%23343434&color=%23156b74" alt="Commit Frequency">
  <img src="https://img.shields.io/github/license/Hudson-Liu/Melanoma-Classification?style=for-the-badge&labelColor=%23343434&color=%23ce530a" alt="License">
</h1>

SIIM-ISIC 2020 Melanoma Challenge Dataset with Teachable Machine. A small project for my Bryn Mawr Machine Learning Classification Project. All code and any/all related files were created by myself (no generative AI).

Required directory structure:
```shell
Root Directory
├── LICENSE
├── README.md
├── requirements.txt
├── docs/
├── converted_keras/
│   ├── labels.txt
│   └── keras_model.h5
├── ISIC_2020_Training_JPEG/
│   ├── ISIC_2020_Training_GroundTruth.csv
│   └── train
│       ├── ISIC_1234.jpg
│       ├── ISIC_1234.jpg
│       │   ...
│       └── ISIC_9999.jpg
└── src/
    ├── eval.py
    └── data.py
```

When running the program, use the following commands from the project directory:
```bash
> pip install -r requirements.txt
> python src/data.py
> python src/eval.py
```
Make sure to use a Python version between 3.8 and 3.11, since Teachable Machine uses an older version of TensorFlow (2.12.1). On linux, the following can be used to create a proper virtual environment with pyenv:
```bash
> pyenv install 3.11.11
> pyenv local 3.11.11
> pyenv exec python3 -m venv [NAME_OF_ENV]
```
