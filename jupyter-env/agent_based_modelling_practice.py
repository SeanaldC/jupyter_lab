# Model design
import agentpy as ap
import numpy as np # a library for scientific computing

# Visualization
import seaborn as sns

# Start by defining a new type of "Agent"
class WealthAgent(ap.Agent):

    """ An agent with wealth """
    # setup() is automatically called when a new agent is created and initializes the variable "wealth"
    def setup(self):
        self.wealth = 1

    # randomly selects one agent from the agent pop managed by the model instance
    # where instance refers to a unique copy of a class
    # whereas the "model instance" is the individual occurence of the class, which carries its defined attributes
    def wealth_transfer(self):
        if self.wealth >0:
            partner = self.model.agents.random()
            partner.wealth += 1
            self.wealth -= 1

# Define a method to calculate the Gini Coefficient
def gini(x):
    """ Calculate Gini Coefficient """
    x = np.array(x)
    mad = np.abs(np.subtract.outer(x,x)).mean() # mean absolute difference
    rmad = mad / np.mean(x) # relative mean absolute difference
    return 0.5 * rmad

class WealthModel(ap.Model):
    """ A simple model of random wealth transfers """

    # Defines how many agents should be created at the beginning of the game
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, WealthAgent)

    # Calls all agents to perform their wealth_transfer method
    def step(self):
        self.agents.wealth_transfer()

    # Calculates and records the current Gini coefficient after each time-step or wealth transfer
    def update(self):
        self.record('Gini Coefficient', gini(self.agents.wealth))

    # Called at the end of the simulation to record the wealth of each agent
    def end(self):
        self.agents.record('wealth')


# Run simulation
parameters = {
    'agents': 100,
    'steps': 100,
    'seed': 42,
}

model = WealthModel(parameters)
results = model.run()