#!/usr/bin/env .venv/bin/python3
"""Generate HTML views from Jinja2 templates + YAML data."""

import json
import os
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
TEMPLATE_DIR = PROJECT_ROOT / "template"
VIEW_DIR = PROJECT_ROOT / "view"


def format_inr(value):
    if value is None:
        return "—"
    s = "{:.2f}".format(float(value))
    parts = s.split(".")
    integer_part = parts[0]
    decimal_part = parts[1]

    negative = integer_part.startswith("-")
    if negative:
        integer_part = integer_part[1:]

    length = len(integer_part)
    if length > 3:
        result = integer_part[-3:]
        remaining = integer_part[:-3]
        while remaining:
            chunk = remaining[-2:] if len(remaining) >= 2 else remaining
            result = chunk + "," + result
            remaining = remaining[:-2]
    else:
        result = integer_part

    if negative:
        result = "-" + result

    return result + "." + decimal_part


def load_yaml_data():
    context = {}
    for file in DATA_DIR.glob("*.yaml"):
        with open(file, "r") as f:
            data = yaml.safe_load(f)
            key = file.stem
            if isinstance(data, dict):
                if key in data:
                    context[key] = data[key]
                else:
                    context[key] = data
            elif isinstance(data, list):
                context[key] = data
            else:
                context[key] = data
    return context


def render_views():
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    env.filters["tojson"] = lambda v: json.dumps(v, default=str)
    env.filters["inr"] = format_inr

    data = load_yaml_data()
    VIEW_DIR.mkdir(exist_ok=True)

    for template_path in TEMPLATE_DIR.glob("*.html.j2"):
        template = env.get_template(template_path.name)
        html = template.render(**data)
        output_name = template_path.stem
        output_path = VIEW_DIR / output_name
        with open(output_path, "w") as f:
            f.write(html)
        print(f"Generated {output_path}")


if __name__ == "__main__":
    render_views()
