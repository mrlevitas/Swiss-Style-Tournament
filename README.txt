5/29/2015
code written by: Roman Levitas & Udacity team
contact: mrlevitas@yahoo.com

Directions given:
https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true

***************************Summary**********************************
This zip contains 4 files which combine to simulate a swiss style tournament in
Python using a postgreSQL database as a back-end to store data about the players
in the tournament and their matches.

The files are:
1) tournament.py
2) tournament.sql
3) tournament_test.py
4) gistfile1.py

More on the tournament can be read here:
http://en.wikipedia.org/wiki/Swiss-system_tournament



***************************General Usage****************************
Download and install Python 2.7 as well as PSQL.

PSQL is a terminal-based front-end to PostgreSQL. 
It enables you to type in queries interactively, issue them to PostgreSQL, 
and see the query results. Alternatively, input can be from a file, which in
this case is 'tournament.sql'.

To run/execute tournament example:
1) Create tournament db by typing into PSQL: 
	\i tournament.sql;
2) Run test script by executing:
	python tournament_test.py


*******************************files*******************************

tournament.sql
################################################################################
This file is used to set up the database used to store the players in the 
tournament as well as the matches each of which occupy their own table.

Players associate themselves with a unique id, their name, the number of wins &
losses they have, and the total number of games they have played all recorded in
the Players table.

The matches table contains a unique id and the winner & loser of the match.


A view is also created which "highlights" specific columns from the Players
table, namely the wins in descending order.

 
tournament.py
################################################################################
This file contains all the methods necessary to get a tournament up and running,
gather information about the state of the tournament & players, as well as clear
the tournament data. It also finds the specific matches necessary to create a 
swiss-style tournament.

Methods defined in this file are listed below:
connect()
deleteMatches()
deletePlayers()
countPlayers()
registerPlayer(name)
playerStandings()
reportMatch(winner, loser)
swissPairings()

Further detail about the arguments and return values of above methods can be 
found in tournament.py.


tournament_test.py
################################################################################
This file is a test script used to check the functionality of the swiss-style 
tournament. It clears the tables in the database, populates it with players and 
games, and is used to simulate a simple tournament.

Specifically, it runs the following self-explanatory methods:

    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()

gistfile1.py
################################################################################
This is another test script but it is more primitive as it doesn't exhaustively
check the programs functionality.

Downloaded from:
https://gist.github.com/jeffudacity/d4ccde9860a7ae40070a

It simulates another tournament which is random. 
Mainly used for checking insertions into db tables.