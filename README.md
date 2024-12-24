# Gess The Flag API

This is a first take on an API for the _Guess The Flag_ game.

## Features

When a session is launched ( a session is basically a game launched, _i.e_ a flag that has been chosen randomly and all the attempts to guess it correctly ), the user should be able to:

- First and foremost, a user should be able to start a session,
- Given a valid session ID, the user should be able to accompany it with a guess of the flag, and get an output as to how close he is so far in matching the flag
- when the flag is guessed correctly, the session ends.

## Quick overview

### Session

What should a session be ? A session should be identified with a unique ID. This ID is returned to the user when they start a new session, and it is their only means of sending guesses to the session.

On top of that, the session consists, of course, in choosing a random flag that the user will try to guess. We should also use the session to log the cumulative resemblance to the flag at any given point, and (optional, but why not) keep a record of all the guesses the user have come up with.
