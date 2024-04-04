# RiotData
Repository of code to collect and analyze data from Riot Games API

## Context

League of Legends is a MOBA (Multiplayer Online Battle Arena) where two teams (Blue and Red) of five players compete over each other's resources and neutral objectives to destroy the enemy base (Nexus). There are three lanes; Top, Middle (Mid), and Bottom (Bot), each with defensive structures (Towers or Turrets); a jungle, filled with neutral monsters that give gold, experience and some give buffs (power-ups); a River with epic neutral objectives that provide permanent buffs (Void Grubs and Dragons) and some that provide temporary boosts to your team (Elder Dragon, Baron and Rift Herald). After the 15 minute mark, teams have the option to surrender (colloquially known as "ff" for "forfeit"). This dataset was inspired by [this dataset](https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min).

## Content

This dataset contains game metrics of the first 15 minutes of a match--games usually last between 25-35 minutes, but can surpass an hour. The data collected represents approximately 20,000 games of ranked solo queue (players can only queue up for a game with maximum one other person) from *current* Diamond Players (n.b. Patch 14.6, all games are from between March 20th and March 31st). The target value is blue_Wins (1 represents a Blue Team Victory, 0 represents a Red Team Victory)

Each game is unique and there should be no missing values, *match_id* can be used to GET more data from the Riot Games API.

## Glossary

**Wards**: The in game map includes Fog of War, which means players can only see what is in their immediate vicinity. Wards are totems that players can drop to temporarily or permanently gain vision in areas.
1. Yellow Wards: Usable after level 1, a player may have up to 3 activate at any time, can be placed up to 600 units away, last 90-120 seconds (based on average champion level) or until they are destroyed (3 HP).
2. Sight Wards: Functionally the same as a Yellow Ward, usually placed by Supports (Please correct if wrong)
3. Blue Wards: Only usable after level 9, a player may only have 1 active at any time, can be placed up to 4000 units away, last until they are destroyed (1 HP).
4. Control Wards: Purchasable single-use wards available from level 1, a player may only have 1 activate at any time. Reveals invisible units, last until they are destroyed (4 HP)

**Ace**: When a team kills all members of the enemy team such that all enemy players are dead at a given moment.

**Assist**: When a player helps secure a kill (but did not give the killing blow themself), either by damaging, using crowd control (slowing, stunning, etc), or buffing (healing, powering up) an ally that also participated in the kill.

**Void Grub**: A Neutral Epic Monster that gives players an increase in damage to enemy structures (Towers/Turrets, Inhibitors) increasing for every extra Void Grub defeated. Only 3 or 6 will spawn in a game, but not all need to be or will be killed. *n.b.* if a team kills 5 or 6 Void Grubs, they will periodically summon 1 or 2 Voidmites (little alien things) that assist in destroying objects).

**Dragons**: Neutral Epic Monster that grant permanent bonuses to a team. Only 3 types of non-Elder Dragons (Not included in this dataset as Elder cannot appear prior to 15 minutes) will spawn in a given game.
1. Cloud Drake: makes players faster
2. Infernal Drake: increases player attack damage and ability power
3. Mountain Drake: increases player armor and magic resistance
4. Ocean Drake: gives players extra health regeneration
5. Chemtech Drake: grants players resistance to crowd control and extra healing and shielding
6. Hextech Drake: increases the rate at which players can attack and use spells

**Herald**: A Neutral Objective that assists players in destroying enemy structures

**Towers/Turrets**: "Tower" and "Turret" are used interchangeably, these are defensive structures that must be destroyed to reach the enemy Nexus. There are 3 in each lane, and 2 at the enemy Nexus. They give gold and have plates

**Turret Plates**: The first/outer turrets in each lane have 5 plates that grant extra resistances to the tower for the first 14 minutes. Each plate destroyed prior to 14 minutes grants additional gold.

**Inhibitor**: A structure at the enemy base, destroying this gives your minions additional power and at least one must be destroyed to destroy the enemy Nexus. They regenerate after a few minutes.

**Gold**: A resource earned by killing minions, jungle monsters, enemy players and destroying neutral objectives, enemy structures, wards. Gold is used to buy items to increase player strength.

**XP**: XP and Experience used interchangeably--A resource earned by killing minions, jungle monsters, enemy players and destroying neutral objectives, enemy structures. XP allows a player to level-up, granting additonal strength and allowing players to learn new and upgrade abilities.

**Level**: Champion Level, starts at 1, maximum of 18.

**CS**: Creep Score / Minions. Each team spawns minions in their lanes. Creep score is a count of how many minions a team has killed, (they must land the final blow on a creep to gain gold, but can gain XP by just being in the vicinity when one dies).

**Jungle Monsters**: Outside of the Lanes is the Jungle, filled with neutral monsters that grant gold, XP and some grant buffs

## License
Dataset belongs to Riot Games

## Acknowledgements
Thanks, Riot.
