# DIS-P09
DIS final project team P09
1.	Pair Number: P17.
2.	Team Members: Anil, Dasari
                              Sri Harsha, Devisetty
3.	Summary: We will be using 2016 Olympics held in Rio de Janeiro data as our data set. We are working on How many male and female were participated and How many silver medals did india won
4.	About Data Source: Our data source is csv file which is structured data. It contains 11 fields Id, name, nationality, sex, dob, height, weight, sport, gold, silver, bronze .It is of 747 kb
5.	Link to data source: https://www.kaggle.com/rio2016/olympic-games (Links to an external site.)
6.	Volume and veracity of our data source makes it a big data problem as its size is 747kb with 11539 records and also the data is cleaned and trustworthy.
7.	MapReduce problems: 
a.	What is the total number of male and female athletes participated.
b.	What is the total Number of silver medals won by different countries.
8.	Mapper input: 	  id            name          nationality   sex         dob        height   weight  sport     gold  silver  bronze
					736041664     A Jesus Garcia     ESP        male      10/17/1969    1.72     64    athletics   0      0      0
					266237702     Aaron Russell      USA        male       6/4/1993     2.05     98    volleyball  0      0      1
9.	Mapper output/ Reducer input: 
a.  male	1
	female	1
	male	1
	female	1
b.  GBR	2
	CHN	0
	GER	1
	CPV	0
       
10.	Example of Reducer output:  
a.	 Male 100
	 Female 50
b.	USA	54
	UZB	2
	VEN	1
	VIE	1
11.	Language: Python.
12.	Process: We are processing numeric data. No data cleaning is required for the data set.

13. GitHub link: https://github.com/devisetty123/MapReduce-OlympicsDataSet . It is a public repository. 

# Steps to run MapReduce problem and check output:
* Step1:- Clone or Download the project from the URL mentioned above to your local machine.
* Step2:- Right click on the project and use Git Bash here to run the project. 
* Step3:- To execute our mapper which takes olympic_dataset.csv as input, use `python mapper.py` , This produces intermediate output in intermediate_output1.txt and intermediate_output2.txt files.
* Step4:- To sort the output from mapper we will send these intermediate outputs to sort.py Using `python sort.py` command , which produces sort01.txt and sort02.txt as outputs.
* Step5:- To execute our reducer which takes the sorted outputs from the previous step as input, use `python reducer.py` , This produces outputs in output01.txt and output02.txt files.
* Step6:- You can edit our files by right clicking on the file you want to edit and choose open with Notepad++ or Notepad.
* Step7:- Save the files you edited and perfom step 2 - step 5 to check the output for the files you edited.

![Output1 Graph](/Images/Output01_Graph.JPG)
![Output2 Graph](/Images/Output02_Graph.JPG)
