The Dockerfile and Scraper.py are included in the PyCharm project. You can either build the image from these files, or use the pre-built compressed image myscraper.tar.gz included in the project. To install the image on your local Docker, run the following command: <br>
     docker load -i myscraper.tar.gz<br>
Once the image is installed locally, you can run the scraper with: <br>
     docker run --rm -v C:/LyricsTextMining/Songs:/songs myscraper python Scraper.py --start_page 1 --end_page 100 --genre grunge --output 50_100_grunge.csv<br>
Where:<br>
    • C:/LyricsTextMining/Songs → The location where the CSV file will be saved.<br>
    • -- start_page / -- end_page → The range of website pages you want to crawl.<br>
    • -- genre → Optional filter by music genre.<br>
    • -- output → The name of the output CSV file.<br>
<br>
<br>
Part1_Crawling.ipynb connects to the website, crawls the songs, and saves them into a CSV file.<br>
That CSV can be generated either from the Docker container or directly from Jupyter.<br>
The CSV should then be imported into an SQL database called TextMiningHa, which contains a single table named songs. A backup of this database is also included in the PyCharm project.<br><br>
**Note:**All functions in the Jupyter notebooks pull their data from this database. If you want the project to run on your local machine, you will need to update the connection string stored into db_config.txt<br>
Just change the credential SERVER=IVAN_PC\SQLEXPRESS to match the SQL server on your local machine.<br> 
<br><br>
Part2_PreProcessing.ipynb handles preprocessing tasks, including text cleaning and feature analysis. <br>
<br>
Part3.1_Clustering&Evaluation.ipynb – applies three clustering methods, then visualizes and evaluates the results for each clustering method.<br>
Part3.3.1_SoftGridSearch.ipynb – performs grid search optimization for the soft clustering method.<br>
Part3.3.2_HardGridSearch.ipynb – performs grid search optimization for the hard clustering method.<br>
Part3.3.3_LDAGridSearch.ipynb – performs grid search optimization for the LDA  method.<br>
Part4.1_SimilaritySearch.ipynb – implements similarity search methods to compare and retrieve relevant songs.<br>
Part4.2_TitlevsLyrics.ipynb – analyzes the relationship between song titles and their corresponding lyrics.<br>
<br><br>
Note: Each cell in all Jupyter notebooks is documented with a Markdown cell describing its functionality, and all code is commented accordingly.
In addition, in the end of  each notebook includes a Markdown cell with conclusions and final thoughts. 

