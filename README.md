# LingNLQ project

The current repository contains the data, code and results of the LingNLQ project.
It was realised by Karolin Boczoń, Dimitra Niaouri, Roham Roshanfekr and Muhammad Shahzaib for the 2022-2023 Software Project (UE905 EC1) at IDMC (Nancy), under the supervision of Miguel Couceiro and Esteban Marquer.

## Abstract
The LingNLQ is TBD.

## Content
- [Install instructions](#install-instructions)
- [Usage instructions](#usage-instruction)
- [Repository structure](#repository-structure)

## Install instructions

This project was designed and tested using Python 3.10.
To setup the project, you have to:
1. clone the repository;
2. [install the Python dependencies](#python-dependencies);
3. [download the datasets](#).

### Python dependencies
First install Pytorch:
 <code> pip install torch </code>
 Then install fairseq :
 <code> pip install fairseq </code>
 

### Dataset
To download the dataset, do as follows....
dowload the dataset from the following link:

https://drive.google.com/file/d/1ZNTZnE-rmH7OTuRTCqPR18wKTPGD3PQO/view?usp=sharing

then save it in a directory e.g. data/LC-QUAD

The original link to LC-QUAD v1 is accessable in the link below:

http://lc-quad.sda.tech/lcquad1.0.html



## Usage instructions
### Basic usage
### Reproduce the experiments mentionned in the report
download the checkpoint of the trained model ConvS2S from the following link: 

https://drive.google.com/file/d/1wirMkFL_rKcjMcAJoa75EkZkq8P49TW9/view?usp=sharing

and save it in a directory e.g. models/
then run the fairseq-generate command :

DDIR=data/LC-QUAD
MDIR=models
RDIR=results/ConvS2S

fairseq-generate $DDIR/fairseq-data-bin \
--gen-subset test \
--path $MDIR/checkpoint_best.pt \
--beam 5 > $RDIR/test_output.txt

## Repository structure
- [`README-example.md`](/README-example.md): this file.
- [`main.py`](/main.py): Python script for training the models.
- [`experiment1.py`](/experiment1.py): Python script to run the experiment on the synthetic data, mentionned in section 4.2. of the report.
- [`experiment2.py`](/experiment2.py): Python script to run the experiment on the real-world data from ..., mentionned in section 4.4. of the report.
- [`report/`](/report/): folder for project report PDF `Final_report-My_Awesome_Readme.pdf`.
- [`presentations/`](/presentations/): folder containing all the intermediate presentations as PDF (must be updated before each presentation session). Each file is labled using the template `[date]-Presentation_[presentation number]-My_Awesome_Readme.pdf`. *This template is my personal preference. You can use your own, as long as it is clear from the name which presentation corresponds to which file.*
- [`results/`](/results/): folder containing all the results generated during the project.
    - [`results/models/`](/results/models/): folder containing the models trained during the project.
    - [`results/plots/`](/results/plots/): folder containing the plots describing the performance and the experiments.
    - [`results/solutions/`](/results/solutions/): folder containing the solutions to the Ultimate Question of Life, The Universe, and Everything.
- [`articles/`](/articles/): folder containing all the articles read or mentioned in the report, as PDFs. Each file is labled using the template `[article topic]-[publication year]-[authors' last names].pdf`; if more than 3 authors are present, `[authors' last names]` is replaced by `[first author's last name]-et-al` instead.
