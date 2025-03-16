# NER-SLU-Library
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)

A Named Entity Recognition (NER) project for the SLU Library(hypothetical), designed to automatically extract and tag entities such as places, major persons, events, and organizations from user input.

## Getting Started

1. Clone the repository:
```sh
git clone https://github.com/username/NER-SLU-Library.git
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Run and use the web app:
```sh
cd agent
streamlit run app.py
   ```
4. Open the local URL displayed in the terminal to view the interactive NER demo.

### Project Overview
Below is a overview of the project structure:
```bash
.
├── README.md              # Project documentation
├── agent                  # Streamlit web app
│   └── app.py
├── model                  # Depracated Rest API
│   └── ner_api.py
├── requirements.txt       # Python dependencies
└── training               # Training/processing scripts and output artifacts
    ├── config.cfg         # spaCy config file
    ├── corpus             # Preprocessed .spacy data
    ├── data               # Raw label and sentence files
    ├── output             # Model training outputs
    ├── preprocess.ipynb   # Preprocessing notebook
    └── training.ipynb     # Training notebook
```

## Dataset
Walia, A. (2018). Annotated Corpus for Named Entity Recognition. Kaggle. https://www.kaggle.com/datasets/abhinavwalia95/entity-annotated-corpus

