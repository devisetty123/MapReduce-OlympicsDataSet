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
