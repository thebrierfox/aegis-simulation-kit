#!/usr/bin/env python3
"""
A simple simulation runner that reads a scenario and a run file
and produces a report with SUMMARY, WHAT I DID, ARTEFACTS, BLOCKERS, NEXT
sections.
"""
import argparse
import json
import datetime
import os


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Run a scenario simulation and generate a report.")
    parser.add_argument('--scenario', required=True, help='Path to scenario JSON file')
    parser.add_argument('--run', required=True, help='Path to run JSON file')
    parser.add_argument('--out', required=True, help='Path to output report markdown')
    args = parser.parse_args()

    scenario = load_json(args.scenario)
    run_data = load_json(args.run)

    # Build sections
    summary = f"Ran scenario '{scenario.get('id')}' with {len(scenario.get('steps', []))} steps."
    what_i_did_lines = []
    for action in run_data.get('actions', []):
        step_id = action.get('step_id')
        status = action.get('status')
        note = action.get('note', '')
        what_i_did_lines.append(f"- Step {step_id}: {status}. {note}")

    artefacts = []
    blockers = []
    next_actions = []

    report_lines = []
    report_lines.append(f"SUMMARY\n\n{summary}\n")
    report_lines.append("WHAT I DID\n\n" + "\n".join(what_i_did_lines) + "\n")
    if artefacts:
        report_lines.append("ARTEFACTS\n\n" + "\n".join(artefacts) + "\n")
    else:
        report_lines.append("ARTEFACTS\n\nNone\n")
    if blockers:
        report_lines.append("BLOCKERS\n\n" + "\n".join(blockers) + "\n")
    else:
        report_lines.append("BLOCKERS\n\nNone\n")
    if next_actions:
        report_lines.append("NEXT\n\n" + "\n".join(next_actions) + "\n")
    else:
        report_lines.append("NEXT\n\nNone\n")

    # Write report
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w') as f:
        f.write("\n".join(report_lines))

    print(f"Report generated at {args.out}")

if __name__ == '__main__':
    main()
