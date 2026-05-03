# My Money Manager

## Project Structure

- `schema/` directory defines all the schemas that are part of this app.
- `data/` directory stores YAML-formatted data in line with `schema/` definitions.
- `template/` holds Jinja2 templates that define HTML views, charts, and tables.
- `template/components/` holds reusable Jinja2 macros (currency formatting, badges, etc.).
- `scripts/generate_views.py` renders templates using data to produce `view/` pages.
- `.venv/` is the Python virtual environment for running scripts.

## Development

- Host the app with `npx live-server --host=0.0.0.0` after starting.
- Find the local IP with `ipconfig getifaddr en0` and share that URL (port 8080) to open the app on iPhone.
