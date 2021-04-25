# ODS Supply and Demand Analysis (In Progress)
Codes for Hondura's power grid demand analysis. This codes aims to study the changes in marginal prices due to energy provider changes on supply. Updates the weekly and daily energy flows.

Data Source : https://www.ods.org.hn


----------- Current state -------------

1. Downloading data module: ✓ (scrapdocs.py)

        a. Inputs: File type, list of URLs, directories (browser, download, database)

        b. Outputs: A set of files in the database directory.

        c. Past problems: Error when reading downloaded file and when a file is already on database. Solution -> Exeptions, and delete duplicated files.

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
