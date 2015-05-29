-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.

--drop database if tournament db already exists
\c vagrant;
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
-- connect to database
\c tournament;

create table Players (
player_id serial primary key,
player_name text,
num_wins int default 0,
num_matches int default 0
);

create table Matches(
match_id serial primary key,
winner int,
loser int
);

create view wins_sorted_view as select player_id , player_name, num_wins , 
	num_matches from Players order by num_wins DESC; 