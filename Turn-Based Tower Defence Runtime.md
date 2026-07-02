# Turn-Based Tower Defence Runtime

## Program Description

Build a small terminal program for a turn-based tower defence simulation. This is not a graphics game. It should run in the command line, accept text commands from the user, and keep the game state in memory while it is running.

In the game, enemies move toward the base, towers attack enemies, the base loses health when enemies reach it, and the game ends when base health becomes `0`. The user should be able to run commands, see the current state, and see what happened so far.

The game starts with base health of `10`.

For the base version, use a single lane named `lane1`. The lane has 5 positions, from `0` to `4`, and then the base.

The base enemy type is `goblin`. A goblin has health `3` and speed `1`.

The base tower does `1` damage and can attack enemies within 1 step.

The program should allow the user to spawn goblins, add towers, run turns, view status, view history, and exit.

Enemies start at position `0` and move toward the base. Towers attack enemies that are close enough. When an enemy reaches the base, it reduces base health by `1` and is removed from the lane.

Each enemy and tower should have a unique ID, such as `E1`, `E2`, `T1`, `T2`.

`STATUS` should print the current game status, turn number, base health, and lane view with enemies, towers, positions, and base.

`HISTORY` should print useful events that happened so far, such as spawned enemies, added towers, attacks, movement, deaths, base damage, and game lost.

The program should not crash on invalid input. It should print a useful error and continue running.

### Required Commands

Your program must support these commands:

```txt
SPAWN <lane> <enemyType>
ADD_TOWER <lane> <position>
RUN_TURN
STATUS
HISTORY
EXIT
```

### Rules

- Only valid enemy types can be spawned.
- Towers can only be added at valid lane positions.
- Each tower can attack at most one enemy in one turn.
- A tower can attack only an enemy that is within 1 step of the tower.
- Tower damage reduces enemy health.
- Enemies with `0` or less health are removed.
- Living enemies move toward the base.
- Enemies that reach the base reduce base health by `1` and are removed.
- Base health should not go below `0`.
- When base health becomes `0`, game status becomes `LOST`.
- After the game is `LOST`, running more turns should not continue the game.
- If multiple enemies can be attacked, choose a consistent behavior.

### Do

- Build a working terminal program.
- Keep game state in memory.
- Make commands work one by one.
- Keep the rules consistent.
- Print useful output after commands.
- Handle invalid commands safely.
- Make the code readable enough to explain.

### Do Not

Do not build:

- graphics,
- animation,
- browser UI,
- React UI,
- canvas,
- real-time keyboard control,
- external game engine,
- database storage.

Do not add extra features before the required commands work.

---

## Sample Run

Your output does not need to match this word-for-word, but `STATUS` should print the lane clearly with positions, enemies, towers, and base.

```txt
Tower Defence Runtime Started.

> SPAWN lane1 goblin
Spawned E1 goblin on lane1 at position 0.

> SPAWN lane1 goblin
Spawned E2 goblin on lane1 at position 0.

> SPAWN lane1 goblin
Spawned E3 goblin on lane1 at position 0.

> ADD_TOWER lane1 2
Added T1 tower on lane1 at position 2.

> STATUS
Status: RUNNING
Turn: 0
Base Health: 10

lane1:
0        1     2     3     4     BASE
E1,E2,E3 .     T1    .     .     🏰

> RUN_TURN
Turn 1 started.
T1 found no enemy in range.
E1 moved from 0 to 1.
E2 moved from 0 to 1.
E3 moved from 0 to 1.

> STATUS
Status: RUNNING
Turn: 1
Base Health: 10

lane1:
0     1        2     3     4     BASE
.     E1,E2,E3 T1    .     .     🏰

> RUN_TURN
Turn 2 started.
T1 attacked E1 for 1 damage. E1 hp=2.
E1 moved from 1 to 2.
E2 moved from 1 to 2.
E3 moved from 1 to 2.

> STATUS
Status: RUNNING
Turn: 2
Base Health: 10

lane1:
0     1     2           3     4     BASE
.     .     T1,E1,E2,E3 .     .     🏰
```


---

## Submission

Submit:

- source code,
- any assumptions you made,
- explanation of your approach and how you built the game.
