*Inside the chest, you find a leather and brass cup such as one might use for rolling dice.  Closer inspection reveals a humming sound and the click of tiny gears coming from it, suggesting a gnomish design.  You lift the cup out of the chest, and it makes a churning vibration in your hand, as though an unknown number of tiny objects are rattling and shaking inside.  
You have found the legendary Gnomish Dice Cup!*



# gnomish-dice-cup
A Python-based dice roller for Dungeons and Dragons or other tabletop RPGs that uses natural language input to generate a complete roll with modifiers, weapon/spell selection, and advantage/disadvantage.

The initial phase of development intends to produce a natural language dice roller, while the second phase will extend to use multiple data sources (JSON, Mongo, MySQL/MariaDB) to store weapon, spell, modifier, and other data for players.
This will allow users to issue commands such as *swing*, *cast magic missile*, *shoot*, *reflex save*, etc, and get appropriate rolls without having to specify the dice info.  The base roll commands will also still be available, for maximum flexibility in game sessions.

## Backstory
While working on various tutorials and drills to hone my Python and development skills, I found myself not really getting into the projects and wanting to do something different.
During this time, I also discovered D&D gameplay videos by Critical Role, Viva la Dirt League, and others, and spent a lot of my spare time watching and listening to D&D games using the 5th Edition rules, which were very different from 2E, the last rules that I played under.


As I was watching a game, it occurred to me to write a dice roller, but one that would accept "D&D style" natural language commands, like "roll 4d6".
The initial scratch code came together pretty quickly, and I moved to regex for processing the command input.

After a couple of hours of futzing, (and more than a little nostalgia for the halcyon days of D&D in high school and college) I plotted out what else I might try to make it do.  This resulted in a rough development roadmap:

### Base Functionality
* Natural language input
* Be object-oriented
* Roll dice with modifiers
* Streamlined rolling with back-end data storing weapon, spell, modifier, and character info
* Generate rolls for:
  * attack (hit and damage)
  * spellcasting (hit (if applicable) and damage)
  * hit points at level up (including con and class/feat modifiers)
  * saving throws
  * skill checks
  * generic, based on dice (such as 5d8, to "roll" 5 eight sided dice)
* Utilize multiple sources for back-end data
  * JSON
  * MONGO
  * MySQL/Maria
* Multiple implementations
  * Standalone (local)
  * Full stack web (Flask back-end, React front-end)
    * Allow "sessions" with multiple users.
    * "DM" can see all character data and roll for characters, as well as see all character rolls
    * "DM" rolls can be shown to players or not
    * All players see all "public" rolls
  * Docker for all implementations.  (Not strictly necessary, but I wanted to learn Docker, sooooo....)
  * AWS implementation, ideally able to host multiple discrete sessions (also, similar motives to Docker, just to get a feel for it)



## Examples
### (Phase 1)
* 1d20 -1 (str) +1 (weapon) +1 (feat) with advantage
  * Generates two random integers between 1 and 20 (inclusive).  The higher of the two rolls is selected, and the sum of modifiers is added, to produce a final, modified roll result 
* 5d4 +5
  * Produces the sum of 5 random integers and adds 5 to produce a final result


### (Phase 2)
* swing
  * Generates a melee attack roll (using the default melee weapon if none is specified) with modifiers (bonuses from stats, weapon, etc) from the character data.
  * Users can specify advantage/disadvantage
  * Generates a damage roll (dice, sides, modifiers), allowing for each attack to use a single command to generate hit and damage
* cast magic missile
  * generate a roll of 3d4 +3 (the default for magic missile)
  * user may specify that the spell is cast at higher level by appending 'level X' (cast magic missle level 3)
    * This would generate 5d4 +5, as the spell is being cast at third level, gaining an extra die for each level above 1 (up to a total of 10 dice +10 for all the rules lawyers out there...**you know who you are** :P)
  * Ideally, if a spell requires a hit roll or contested check (based on user data), GDC will generate that as well
* shoot
  * generates a ranged attack roll (using the default weapon)
  