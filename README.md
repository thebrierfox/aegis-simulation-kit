# Aegis Simulation Kit

A lightweight Python toolkit for defining, running, and reporting on agent scenarios. Scenarios are JSON documents that describe a sequence of steps; runs record what the agent actually did against those steps.

## Structure

```
schemas/          JSON schemas for scenario and run documents
examples/
  scenarios/      Example scenario definitions
  runs/           Example run records
scripts/
  simulation_run.py   Run a scenario and generate a Markdown report
  validate.py         Validate scenario/run files against schemas
meta/             Directive and smoke-test definitions
```

## Quickstart

Python 3.9+ required. No third-party dependencies.

```bash
# Validate a scenario file
python scripts/validate.py --schema schemas/scenario.schema.json --file examples/scenarios/hello_world_scenario.json

# Run a scenario and produce a report
python scripts/simulation_run.py \
  --scenario examples/scenarios/hello_world_scenario.json \
  --run examples/runs/hello_world_run.json \
  --out report.md

cat report.md
```

## Scenario format

```json
{
  "id": "my-scenario",
  "description": "What this scenario tests",
  "steps": [
    {"id": "step-1", "desc": "Do something", "type": "internal"},
    {"id": "step-2", "desc": "Call external API", "type": "external"}
  ]
}
```

See `schemas/scenario.schema.json` and `schemas/run.schema.json` for full field definitions.

---

*IntuiTek¹ / ~K¹ (William Kyle Million)*
