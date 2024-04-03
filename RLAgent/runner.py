from agent import AgentWorker
from brain import Brain
from environment import Environment

args = {
    'agent_count': 9,
    'learning_rate': 0.001,
    'memory_model': 'PER',
    'memory_capacity': 10000,
    'target_type': 'DDQN',
    'target_frequency': 1000,
    'maximum_exploration': 1000,
    'batch_size': 32,
    'gamma': 0.95,
    'number_nodes': 256,
    'optimizer': 'Adam',
    'memory_capacity': 1000000,
    'pr_scale': 0.5,
    'test': False
}

def get_agent_type(agent_index):
    if agent_index < 3:
        return 1
    elif agent_index < 5:
        return 2
    else:
        return 3

if __name__ == "__main__":
    agents = []
    
    """
    w1x, w1y, w2x, w2y, w3x, w3y, w4x, w4y, …….. , w9x, w9y
    ,s1x, s1y, s2x, s2y, ….., s9x, s9y
    , CurrentBudget, CostsIncurredSoFar, RewardsExtractedSoFar
    """
    state_size = 39
    action_size = 11
    
    for idx, agent in enumerate(range(args['agent_count'])):
        
        agent_type = get_agent_type(idx)
        agent_name = f'agent_{idx}_type_{agent_type}'
        agent_learning_rate = 0.00005
        timestamp = 0
        
        new_agent = AgentWorker(args, type=agent_type, start=None, rate=agent_learning_rate, timestamp=timestamp, agent_index=idx, state_size=state_size, action_size=action_size, agent_name=agent_name)
        
    environment = Environment(agents, isTrain=True)
    environment.train()