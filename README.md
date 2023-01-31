# TriviaNLQ project

The current repository contains the data, code and results of the LingNLQ project.
It was realised by Karolin Boczoń, Dimitra Niaouri, Roham Roshanfekr and Muhammad Shahzaib for the 2022-2023 Software Project (UE905 EC1) at IDMC (Nancy), under the supervision of Miguel Couceiro and Esteban Marquer.

## Abstract
This project introduces TriviaNLQ, a web-application that utilizes text-to-SPARQL modeling to query the DBpedia knowledge graph and answer trivia questions. It also acts as a survey on available text-to-SPRARQL models. For building our application we trained a Convolutional Sequence-to-Sequence model (CNN architecture) based on a Neural Machine Translation(NMT) approach using Facebook's Fairseq toolkit. The datasets that we used are LC-QUAD and Monument datasets. Our results suggest a better performance of the model when using the Monument dataset, having a BLEU score of 97.6 on the validation set and 97.3 on the test set.

## Content
- [Install instructions](#install-instructions)
- [Usage instructions](#usage-instructions)
- [Repository structure](#repository-structure)

## Install instructions

This project was designed and tested using Python 3.10.
To setup the project, you have to:
1. clone the repository;
2. run `source build.sh`

The script will create a virtual environment for this project and download datasets and models used.
After the setup, the virtual environment will be activated so you can immediately use the system.

### Dataset


[Monument dataset](https://drive.google.com/file/d/15wo0HuLbAOkGgdY7zbwqppzfgiWeity9/view?usp=share_link)
<br />[LC-QUAD dataset](https://drive.google.com/file/d/1ZNTZnE-rmH7OTuRTCqPR18wKTPGD3PQO/view?usp=sharing)


## Usage instructions
### Basic usage
### Reproduce the experiments mentionned in the report

- For having an experience on asking a question(in NL) and seeing the query(in SPARQL):
<br /> <code> python3 code/main.py </code>
- For evaluating the model over test portion (and dev poertion) of dataset, run:
<br /> <code> python3 training/test.py $DDIR $MDIR $RDIR</code>
The arguments are data nad model and results folder respectively. Default values can be:
<code>DDIR = data/monuments_600</code>
<code>MDIR = output/models</code>
<code>RDIR = results/result</code>
<br />
then select test_fairsec option. the result will be in the corresponding folder.


## Repository structure
- [`README-example.md`](/README-example.md): this file.
- [`main.py`](/main.py): Python script for training the models.
- [`report/`](/report/): folder for project report PDF.
- [`presentations/`](/presentations/): folder containing all the intermediate presentations as PDF. 
- [`results/`](/results/): folder containing all the results generated during the project.
    - [`results/Monument/`](/results/Monument/): folder containing the results of the model trained on the Monument dataset during this project.
    - [`results/LC-QUAD/`](/results/Monument/): folder containing the results of the model trained on the LC-QUAD dataset during this project.
- [`training/`](/training/):folder containg the scripts to train the models and get the results.
- [`articles/`](/articles/): folder containing all the articles read or mentioned in the report, as PDFs. Each file is labled using the template `[article topic]-[publication year]-[authors' last names].pdf`; if more than 3 authors are present, `[authors' last names]` is replaced by `[first author's last name]-et-al` instead.
