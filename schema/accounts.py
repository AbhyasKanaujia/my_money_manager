ACCOUNT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "description": "Unique account identifier",
        },
        "name": {
            "type": "string",
            "description": "Account name",
        },
        "balance": {
            "type": "number",
            "description": "Current account balance",
        },
        "type": {
            "type": "string",
            "description": "Account type (e.g., savings, investment, emergency)",
        },
        "note": {
            "type": "string",
            "description": "Optional note about the account",
        },
    },
    "required": ["id", "name", "balance", "type"],
}
