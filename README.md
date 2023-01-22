# TriviaNLQ project

The current repository contains the data, code and results of the TriviaNLQ project.
It was realised by Karolin Boczoń, Dimitra Niaouri, Roham Roshanfekr and Muhammad Shahzaib for the 2022-2023 Software Project (UE905 EC1) at IDMC (Nancy), under the supervision of Miguel Couceiro and Esteban Marquer.

## Abstract
The TriviaNLQ is TBD.

## Content
- [Install instructions](#install-instructions)
- [Usage instructions](#usage-instruction)
- [Repository structure](#repository-structure)

## Install instructions

This project was designed and tested using Python 3.10.
To setup the project, you have to:
1. clone the repository;
2. [install the Python dependencies](#python-dependencies);
3. [download the datasets](#dataset).

### Python dependencies
These are listed in `requirements.txt`. Run `pip install -r requirements.txt`.

Additionally, `spacy`-related models are needed:
```
python -m spacy download en_core_web_sm
python -m spacy_entity_linker "download_knowledge_base"
```

### Dataset
We're using a modified version of [LC-QuAD 2.0 dataset](http://lc-quad.sda.tech/) created for ["Entity Linking and Filling for Question Answering over Knowledge Graphs"](https://arxiv.org/abs/2107.02865v1) paper.

```
wget -P data/ 'https://raw.githubusercontent.com/thesemanticwebhero/ElNeuKGQA/main/data/dataset_lcquad2.json'
```

## Usage instructions
### Basic usage

You can run the `demo.ipynb` notebook.

### Reproduce the experiments mentionned in the report


## Repository structure
- [`README`](/README.md): this file.
- [`main.py`](/main.py): Python script for training the models.
- [`report/`](/report/): folder for project report PDF `Final_report-My_Awesome_Readme.pdf`.
- [`presentations/`](/presentations/): folder containing all the intermediate presentations as PDF (must be updated before each presentation session). Each file is labled with the date of presentations.
- [`results/`](/results/): folder containing all the results generated during the project.
    - [`results/models/`](/results/models/): folder containing the models trained during the project.
    - [`results/plots/`](/results/plots/): folder containing the plots describing the performance and the experiments.
    - [`results/solutions/`](/results/solutions/): folder containing the solutions to the Ultimate Question of Life, The Universe, and Everything.
- [`articles/`](/articles/): folder containing all the articles read or mentioned in the report, as PDFs. Each file is labled using the template `[article topic]-[publication year]-[authors' last names].pdf`; if more than 3 authors are present, `[authors' last names]` is replaced by `[first author's last name]-et-al` instead.
