import sys
sys.path.insert(0, 'src')

from synapse.core.goals import parse_goal, infer_plan

def test_goal_parse():
    goal = parse_goal("maximize(reward)")
    assert goal['type'] == 'maximize'

def test_infer_plan():
    plan = infer_plan({'type': 'maximize', 'objective': 'reward'})
    assert len(plan) > 0
