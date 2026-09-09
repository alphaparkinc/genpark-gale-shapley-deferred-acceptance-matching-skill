"""
Gale-Shapley Deferred Acceptance Matching Skill Client
Pure Python Standard Library implementation of the Gale-Shapley Deferred Acceptance algorithm.
Produces a provably stable bipartite matching (no blocking pairs) between proposing agents
and receiving resource/task units according to strict ordinal preference lists.
"""

from typing import Dict, List, Any, Optional


class GaleShapleyMatcher:
    def __init__(self, proposer_prefs: Dict[str, List[str]], acceptor_prefs: Dict[str, List[str]]):
        self.proposer_prefs = {k: list(v) for k, v in proposer_prefs.items()}
        self.acceptor_prefs = {k: list(v) for k, v in acceptor_prefs.items()}
        self.acceptor_ranks = {
            acc: {prop: idx for idx, prop in enumerate(prefs)}
            for acc, prefs in self.acceptor_prefs.items()
        }

    def solve_stable_matching(self) -> Dict[str, Any]:
        """Run Deferred Acceptance algorithm until all proposers are matched or exhausted."""
        free_proposers = list(self.proposer_prefs.keys())
        proposals_made: Dict[str, int] = {p: 0 for p in free_proposers}
        matches: Dict[str, str] = {}  # acceptor -> proposer

        while free_proposers:
            p = free_proposers.pop(0)
            p_prefs = self.proposer_prefs[p]
            idx = proposals_made[p]
            if idx >= len(p_prefs):
                continue  # Exhausted all options
            acceptor = p_prefs[idx]
            proposals_made[p] += 1

            if acceptor not in matches:
                matches[acceptor] = p
            else:
                curr_partner = matches[acceptor]
                rank_curr = self.acceptor_ranks[acceptor].get(curr_partner, 999)
                rank_new = self.acceptor_ranks[acceptor].get(p, 999)
                if rank_new < rank_curr:  # New proposer is preferred
                    matches[acceptor] = p
                    free_proposers.append(curr_partner)
                else:
                    free_proposers.append(p)

        prop_matches = {prop: acc for acc, prop in matches.items()}
        return {
            "matches_by_proposer": prop_matches,
            "matches_by_acceptor": matches,
            "is_stable": True
        }
