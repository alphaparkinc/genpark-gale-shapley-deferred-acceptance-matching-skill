"""Example demonstrating Gale-Shapley stable marriage."""
from client import GaleShapleyMatching

def main():
    men = {"M1": ["W1", "W2"], "M2": ["W1", "W2"]}
    women = {"W1": ["M1", "M2"], "W2": ["M1", "M2"]}
    matches = GaleShapleyMatching.match(men, women)
    print("Stable Matching Result (Receiver -> Proposer):", matches)

if __name__ == "__main__":
    main()
