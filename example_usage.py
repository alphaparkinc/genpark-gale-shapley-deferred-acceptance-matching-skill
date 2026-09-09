"""
Demonstration of Gale-Shapley Deferred Acceptance Matching Skill
"""

from client import GaleShapleyMatcher

def main():
    print("=== Gale-Shapley Deferred Acceptance Stable Matching ===")

    # 3 Autonomous Worker Agents proposing to 3 Specialized Compute Tasks
    worker_prefs = {
        "Worker_A1": ["Task_T1", "Task_T2", "Task_T3"],
        "Worker_A2": ["Task_T2", "Task_T1", "Task_T3"],
        "Worker_A3": ["Task_T1", "Task_T2", "Task_T3"]
    }

    task_prefs = {
        "Task_T1": ["Worker_A2", "Worker_A1", "Worker_A3"],
        "Task_T2": ["Worker_A1", "Worker_A2", "Worker_A3"],
        "Task_T3": ["Worker_A1", "Worker_A2", "Worker_A3"]
    }

    matcher = GaleShapleyMatcher(worker_prefs, task_prefs)
    results = matcher.solve_stable_matching()

    print("Stable Matching Results:")
    for w, t in sorted(results["matches_by_proposer"].items()):
        print(f"  {w} -> {t}")

    assert results["matches_by_proposer"]["Worker_A1"] == "Task_T1"
    assert results["matches_by_proposer"]["Worker_A2"] == "Task_T2"
    assert results["matches_by_proposer"]["Worker_A3"] == "Task_T3"

    print("\nGale-Shapley Stable Matching Verification PASS!")

if __name__ == "__main__":
    main()
