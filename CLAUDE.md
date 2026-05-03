# My Money Manager

## Project Structure

- `schema/` directory defines all the schemas that are part of this app.
- `data/` directory stores YAML-formatted data in line with `schema/` definitions.
- `template/` holds Jinja2 templates that define HTML views, charts, and tables.
- `template/components/` holds reusable Jinja2 macros (currency formatting, badges, etc.).
- `scripts/generate_views.py` renders templates using data to produce `view/` pages.
- `.venv/` is the Python virtual environment for running scripts.

## Onboarding

The agent walks the user through interactive setup:

1. **Environment**: Ensure `.venv/` exists with `pyyaml` and `jinja2` installed.
2. **Copy examples**: In `data/`, copy `*.yaml.example` to `*.yaml`.
3. **Fill `data/config.yaml`**: Ask the user for each field — monthly salary, SIP target, expenses, assumptions, emergency fund target, and emergency source IDs. Explain what each field means and how it affects projections.
4. **Fill `data/accounts.yaml`**: Ask how many accounts they have, then for each ask name, balance, type, and note. Compute totals automatically.
5. **Fill `data/investments.yaml`**: Ask for each fund — name, invested amount, monthly SIP target, whether active, and stop-adding rule.
6. **Generate views**: Run `.venv/bin/python scripts/generate_views.py`.
7. **Preview**: Open `view/portfolio.html` and verify charts and tables match expectations.

## Development

- Host the app with `npx live-server --host=0.0.0.0` after starting.
- Find the local IP with `ipconfig getifaddr en0` and share that URL (port 8080) to open the app on iPhone.
