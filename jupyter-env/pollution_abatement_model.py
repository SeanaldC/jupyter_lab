import agentpy as py

# data vis
import seaborn as sns

# computation
import numpy as np

# Data manipulation and analysis
import pandas as pd

# Create agent
class FirmAgent(ap.Agent):
    def setup(self):
        self.production_capacity = self.random.randint(50, 100)
        self.inventory = 0
        self.profit = 0
    
    def production(self):
        self.inventory += self.production_capacity