# ODS Supply and Demand Analysis (In Progress)
Codes for Hondura's power grid demand analysis. This codes aims to study the changes in marginal prices due to energy provider changes on supply. Updates the weekly and daily energy flows.

About the Pre-dispatch (24Hrs cycle - Daily reports): 

I. The pre-dispatch reports accounts for the forcasted energy production for each of hondrura's power providers. The generation report is devided into energy types: Hydroelectric, renewable (Solar, Wind, Geothermic, Tidal), thermoelectric plants and others (6 unidentified sources. 3 unites @ CJN, 1 unite @ CRL, 2 unites @ RLN). This last concept has a defined minimun generation (180 Mw @ CJNs and 10 Mw for the others). Hydroelectric stations have a defined energy reserve "Asignacion de reserva de regulacion secundaria de frecuencias". 

II. Demand, Deficit and "intentional" Leaks: Total national grid demand by hour. Real time power plants market share.

III. Power flux on the electrical substations: Unmaped substations list. Power flux on critical lines.

IV. Node's marginal costs & thermoelectric variable costs: The variable costs take in account the plant efficiency, fuel costs, and operation and mantinance costs. Some thermoelectric plants have different operating modes (e.g. ENR (<180Mw & >180Mw)). 

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

        c. Comments: Map the regional producers to a node. Energy producers might affect the prices in adjacent nodes, the power cost increases by distance (Olancho has the higher pricing distribution)
        
        d. Marginal cost variations:  Weighted average with price and energy market share.
        
                   Assumptions: New energy provider will sell at the local node price. New suppies will change the energy market share and                              therefore the local margial price. A MC assigned to a node could be influenced by near neighbors.
                
        
