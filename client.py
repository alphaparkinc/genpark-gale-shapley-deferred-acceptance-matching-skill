"""Gale-Shapley Deferred Acceptance Stable Matching.
100% Python Standard Library.
"""

class GaleShapleyMatching:
    """Computes proposer-optimal stable matching between two disjoint sets of agents."""
    @staticmethod
    def match(proposers_pref, receivers_pref):
        free_proposers = list(proposers_pref.keys())
        proposals_made = {p: 0 for p in free_proposers}
        engagements = {}
        
        while free_proposers:
            p = free_proposers.pop(0)
            p_prefs = proposers_pref[p]
            if proposals_made[p] < len(p_prefs):
                r = p_prefs[proposals_made[p]]
                proposals_made[p] += 1
                
                if r not in engagements:
                    engagements[r] = p
                else:
                    curr_p = engagements[r]
                    r_pref = receivers_pref[r]
                    if r_pref.index(p) < r_pref.index(curr_p):
                        engagements[r] = p
                        free_proposers.append(curr_p)
                    else:
                        free_proposers.append(p)
                        
        return {r: engagements[r] for r in sorted(engagements.keys())}
