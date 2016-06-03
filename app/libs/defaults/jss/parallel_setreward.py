# Get the action that was used
action = self.action["action"]

policies = [1,2,3]                # Array of policy id's

# Run through each of the policies:
for policy in policies:
    
    # Get the action suggested by the policy
    # Note that all objects (action, context, reward)
    # are passed to the policy by default
    Exp = Experiment(policy)
    suggested = Exp.run_action_code(policy)
    
    # If the same, then update
    if suggested == action:
        # Again note that the reward object is passed
        Exp.run_reward_code(policy)