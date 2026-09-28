"""MCP stdio server for Gale-Shapley Matching."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import GaleShapleyMatching

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compute_stable_matching",
                        "description": "Compute stable matching via Gale-Shapley deferred acceptance",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "proposers_preferences": {"type": "object"},
                                "receivers_preferences": {"type": "object"}
                            },
                            "required": ["proposers_preferences", "receivers_preferences"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "compute_stable_matching":
            p_pref = args.get("proposers_preferences", {})
            r_pref = args.get("receivers_preferences", {})
            res = GaleShapleyMatching.match(p_pref, r_pref)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"matches": res}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
