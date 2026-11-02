def reflex_vacuum_agent(location, status):
    """
    Returns an action based strictly on the current percept (location, status).
    """
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

environment = {'A': 'Dirty', 'B': 'Dirty'}
agent_location = 'A'

print(f"Starting environment: {environment}, Agent at: {agent_location}\n")

for step in range(1, 5):
    
    status = environment[agent_location]
    
    
    action = reflex_vacuum_agent(agent_location, status)
    print(f"Step {step}: Location = {agent_location}, Status = {status} -> Action: {action}")
    
    
    if action == 'Suck':
        environment[agent_location] = 'Clean'
    elif action == 'Right':
        agent_location = 'B'
    elif action == 'Left':
        agent_location = 'A'

print(f"\nFinal environment state: {environment}")