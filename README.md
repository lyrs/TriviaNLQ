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
2. [install the Python dependencies](#python-dependencies);
3. [download the datasets](#dataset).

### Python dependencies
- Install requirements:
<br /> <code> pip3 install -r code/requirements.txt </code>

 

### Dataset
- Download a dataset from the following link(s):

    [Monument dataset](https://drive.google.com/file/d/1ZNTZnE-rmH7OTuRTCqPR18wKTPGD3PQO/view?usp=sharing)
  <br />   [LC-QUAD dataset](https://drive.google.com/file/d/1ZNTZnE-rmH7OTuRTCqPR18wKTPGD3PQO/view?usp=sharing)

- Save it in a directory:
    <br /> <code>data/monument_600 </code>
    <br /> <code>data/LC-QUAD </code>


## Usage instructions
### Basic usage
### Reproduce the experiments mentionned in the report
- Download a checkpoint of the trained model ConvS2S from the following link: 

   [ConvS2S model Checkpoint trained on Monument dataset ](https://drive.google.com/file/d/1wirMkFL_rKcjMcAJoa75EkZkq8P49TW9/view?usp=sharing)
<br />   [ConvS2S model Checkpoint trained on LC-QUAD dataset ](https://drive.google.com/file/d/1wirMkFL_rKcjMcAJoa75EkZkq8P49TW9/view?usp=sharing)

- Save it in the directory <code>output/models/</code> with the name <code>checkpoint_best.pt</code>
- For having an experience on asking a question(in NL) and seeing the query(in SPARQL):
<br /> <code> python3 code/main.py </code>
- For evaluating the model over test portion (and dev poertion) of dataset, run:
<br /> <code> python3 training/test.py $DDIR $MDIR $RDIR</code>
The arguments are data nad model and results folder respectivly. default values can be:
<code>DDIR = data/monuments_600</code>
<code>MDIR = output/models</code>
<code>RDIR = results/result</code>
<br />
then select test_fairsec option. the result will be in the corresponding folder.


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
