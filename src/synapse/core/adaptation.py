from synapse.core.goals import infer_plan

def adapt_plan(current_plan, feedback):
    """Adapt plan based on feedback, e.g., {'reward': low}"""
    if feedback.get('reward') == 'low':
        # Switch to exploration
        return ['explore'] * len(current_plan)
    elif feedback.get('reward') == 'high':
        return ['exploit'] * len(current_plan)
    return current_plan

def test_adaptation():
    plan = ['explore', 'exploit']
    adapted = adapt_plan(plan, {'reward': 'low'})
    return adapted == ['explore', 'explore']  # Adapted

if __name__ == "__main__":
    print("Adaptation test:", test_adaptation())
