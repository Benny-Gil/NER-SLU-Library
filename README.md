# NER-SLU-Library
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)


A Named Entity Recognition (NER) project for the SLU Library (hypothetical), extracting entities such as places, persons, and events.

## Getting Started

1. Clone the repository:
```sh
git clone https://github.com/username/NER-SLU-Library.git
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Run the web app:
```sh
streamlit run app.py
```
4. Use the displayed local URL to view the interactive NER demo.

## Project Overview

```bash
.
├── README.md              # Documentation
├── api                    # Depracated Rest API
│   └── ner_api.py
├── app.py                 # Streamlit entry point
├── requirements.txt       # Project dependencies
└── training               # Training/processing scripts and outputs
    ├── config.cfg         # spaCy config
    ├── corpus             # .spacy data files
    ├── data               # Raw labels and sentences
    ├── output             # Model artifacts
    ├── preprocess.ipynb   # Data preprocessing
    └── training.ipynb     # Model training
```

## Dataset
Walia, A. (2018). Annotated Corpus for Named Entity Recognition. Kaggle. https://www.kaggle.com/datasets/abhinavwalia95/entity-annotated-corpus
