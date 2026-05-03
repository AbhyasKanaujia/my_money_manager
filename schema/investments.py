INVESTMENT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Short unique identifier, 3-5 characters",
        },
        "name": {
            "type": "string",
            "description": "Investment name",
        },
        "type": {
            "type": "string",
            "description": "Investment type (e.g., mutual_fund, stock, fd, ppf, epf, nps)",
        },
        "invested_amount": {
            "type": "number",
            "description": "Total amount invested",
        },
        "investment_target": {
            "type": "number",
            "description": "Target allocation amount for this investment",
        },
        "active_sip": {
            "type": "boolean",
            "description": "Whether monthly contributions are actively being made",
        },
        "stop_adding_rule": {
            "type": "string",
            "description": "Rule or condition that stops further contributions to this investment",
        },
        "note": {
            "type": "string",
            "description": "Optional note about the investment",
        },
    },
    "required": ["id", "name", "type", "invested_amount", "active_sip"],
}
