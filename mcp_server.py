"""
MCP Server for Gale-Shapley Deferred Acceptance Matching Skill
"""

import json
import sys
from client import GaleShapleyMatcher

def handle_call(name: str, args: dict) -> dict:
    if name == "compute_stable_matching":
        p_prefs = args.get("proposer_prefs", {"A": ["T1", "T2"], "B": ["T1", "T2"]})
        a_prefs = args.get("acceptor_prefs", {"T1": ["A", "B"], "T2": ["B", "A"]})
        matcher = GaleShapleyMatcher(p_prefs, a_prefs)
        return matcher.solve_stable_matching()
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
