# ODS Supply and Demand Analysis
Codes for Hondura's power grid demand analysis. This codes aims to study the changes in marginal prices due to energy provider changes on supply. Updates the weekly and daily energy flows.

Data Source : https://www.ods.org.hn


----------- Current state -------------

1. Downloading data module:  (scraper.py)

        a. Inputs: website with the excel (weekly) & pdf (daily) files.

        b. Outputs: Excel file in a desired directory.

        c. Past problems: N/A

        d. Possible Upgrades: N/A.
          Comments: Webscraping.


2. Reading files module: ✓ (getnames.py + pandas.read_excel(***) )

        a. Inputs: file's directory, file's type (e.j. .xlsx)

        b. outputs: Dataframes for each file.

        c. Past problem: Wont use the directory's path -> Solution: Read files in the scrip's directory.

        d. Possible Upgrades: Convert into a API.


3. Data Analysis: (Master.py)

        a. Inputs: Dataframes

        b. Outputs: Graphs.

        c. Comments: Identify regional producers.    
