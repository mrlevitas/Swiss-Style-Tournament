#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(player_id) FROM Players;")
    total = c.fetchone()[0]
    return total


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute(
        "INSERT INTO Players (player_name, num_wins) VALUES (%s, 0);", (name,))
    conn.commit()

    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(player_id) FROM Players;")
    total = c.fetchone()[0]

    num_of_players = countPlayers()
    standings = [None]*num_of_players

    c.execute("SELECT * FROM wins_sorted_view;")
    winners = c.fetchall()

    i = 0
    for player in winners:
        standings[i] = (player[0], player[1], player[2], player[3])
        i += 1

    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()

    query = "INSERT INTO Matches (winner, loser) VALUES (%s, %s);"
    c.execute(query, ((winner, ), (loser, ), ))

    # UPDATE Orders SET Quantity = Quantity + 1 WHERE ...
    # http://stackoverflow.com/questions/973380/sql-how-to-increase-or-decrease-one-for-a-int-column-in-one-command
    query = "UPDATE Players SET num_wins = num_wins +1 WHERE player_id = (%s);"
    c.execute(query, (winner,))

    query = """
        UPDATE Players SET num_matches = num_matches +1 WHERE player_id = (%s);
        """
    c.execute(query, (winner,))

    query = """
        UPDATE Players SET num_matches = num_matches +1 WHERE player_id = (%s);
        """
    c.execute(query, (loser,))

    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    # http://discussions.udacity.com/t/swisspairing-hints/19179
    pairs = [
        (standings[i-1], standings[i]) for i in range(1, len(standings), 2)]

    # assume even number of matches/players
    swissPairs = [None] * (len(standings) / 2)

    i = 0
    for match in pairs:
        swissPairs[i] = (match[0][0], match[0][1], match[1][0], match[1][1])
        i += 1

    return swissPairs
