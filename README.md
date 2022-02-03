Talent vs luck; agent based simulation
=======================
Based on the ideas in the 2018 article "Talent versus luck: the role of 
randomness in success and failure"
by A. Pluchino et al. (see references), this project simulates how luck and 
skill contribute to people's success
achieved after a number of years. Skill could be interpreted as e.g. their
IQ level, which can be a determining factor in how well one is able to 
recognize and exploit opportunities throughout life. The skill of the people
is randomly distributed according to a normal distribution. 

The people 
(agents) in the simulated will sometimes be presented an opportunity. The 
higher their skill, the more likely they are to take advantage of the 
opportunity and thus increase their success/wealth. Misfortune will also 
sometimes strike, which will decrease the individual's wealth. They are not 
able to dodge these unlucky events as these could for instance be the death 
of a loved one or a car crash, making a major impact on the individual. 

## Setup
It is easy to setup. Using the terminal, do the following steps:
1. If you don't have a Python environment that you would like to use, 
create one using conda (skip if you already have an appropriate 
   Python environment):
   
       conda create --name talent_vs_luck_simulation python=3.7
       conda activate talent_vs_luck_simulation

2. Clone the repo from Github using Git and change into the directory:

       git clone https://github.com/hviidhenrik/talent_vs_luck_simulation.git
       cd talent_vs_luck_simulation

3. Install the requirements using pip

        pip install -e .
        pip install -r requirements.txt

## Usage
The simulation is straight forward to get started with. From the terminal:

    python talent_vs_luck/main.py

Additional arguments (with their default values) are 
- `--board-size=30` 
- `--num-agents=100`, 
- `--num-lucky-events=50`
- `--num-unlucky-events=50` 
- `--num-years=40`

To run the script with custom parameters, e.g., a bigger simulation 
landscape (board-size) but fewer people (agents) from the terminal:

    python talent_vs_luck/main.py --board-size=50 --num-agents=50

## References
*Talent versus luck: the role of randomness in success and failure*
by A. Pluchino et al.: https://arxiv.org/abs/1802.07068

## To do

- implement fixed salaries for agents to compare in the end what mattered most wrt wealth; steady salary or luck?
- unit tests