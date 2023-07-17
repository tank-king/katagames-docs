# Structure of the Game

Before proceeding to programming the game, we need to decide its structure.
There will be many `scenes` or `states` of the game.


color = #36354A


Flowchart for the structure

<div align="center">

```mermaid
flowchart TB
    start((start)) --> Home
    Home --> |play| Game
    Home --> |quit| Stop((Stop))
    Game --> |win| Win[Win Screen]
    Game --> |lose| Lose[Lose Screen]
    Win --> |home| Home
    Win --> |quit| Stop
    Lose --> |replay| Game
    Lose --> |quit| Stop
```

</div>
