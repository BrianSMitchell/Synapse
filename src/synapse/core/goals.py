def parse_goal(goal_str):
    """Parse goal declaration, e.g., 'maximize(reward)'"""
    if 'maximize' in goal_str:
        objective = goal_str.split('(')[1].strip(')')
        return {'type': 'maximize', 'objective': objective}
    # Add more
    return {'type': 'unknown'}

def infer_plan(goal):
    """Infer simple plan from goal"""
    if goal['type'] == 'maximize':
        if goal['objective'] == 'reward':
            return ['explore', 'exploit', 'learn']
    return []

def execute_plan(plan):
    """Execute plan (placeholder)"""
    results = []
    for action in plan:
        results.append(f"Executed {action}")
    return results

def test_goals():
    goal = parse_goal("maximize(reward)")
    plan = infer_plan(goal)
    results = execute_plan(plan)
    return len(plan) > 0 and len(results) > 0

if __name__ == "__main__":
    print("Goal inference:", test_goals())
