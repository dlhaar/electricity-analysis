# Electricy Generation and Consumption in Germany - Analysis

## Table of Contents
1. [Introduction](#introduction)
2. [To run the jupyter notebooks](#To_run_jupyter_notebooks)
	1. [Prerequisites](#prerequisites)
	2. [Steps](#steps)
3. [Analysis in Tableau](#Analysis_in_Tableau)

## Introduction
This project aims to review electricity generation and consumption in Germany from 2017 through 2022.

Questions considered were:
- How has production by source changed?
- Are there any trends in the production?
- What are the consumption rates and have these rates changed?
- How do production and consumption compare?
- What is the trend for residental electricity prices?

The data for this project was retrieved from [SMARD](https://www.smard.de/en) and [Destatis](https://www-genesis.destatis.de/genesis/online). 


## To run the jupyter notebooks

### Prerequisites
To run the jupyter notebooks, you should have the following installed:
- an environment (e.g. venv)
- jupyter lab

### Steps
1. Fork and clone the git repository
2. Navigate to the project folder and activate the environment 
3. In the terminal type:

  ```shell
  pip install -r requirements.txt
  ```
4. Launch `jupyter lab`


## Analysis in Tableau
An analysis of the data can be found in Tableau Public [here](https://public.tableau.com/app/profile/deborah.haar/viz/smard_electricity_germany/ElectricitygenerationandconsumptioninGermany2017-2022)

Sample of findings:
- Between 2017 and 2022, wind and solar are gaining share of the total electricity market. In 2022, they made up 36.6% of the market, up from 25.4% in 2017.
- Germany has been phasing out its nuclear plants (the last ones were shut in April 2023) and we see a sharp decrease in output from them beginning 2021.
- Production of electricity has been in a slow decline. 2020 and 2022 saw the lowest production out of the six years.
- Average residential prices for electricity have been steadily increasing.
