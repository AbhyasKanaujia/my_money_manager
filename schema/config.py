CONFIG_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "currency": {
            "type": "string",
            "default": "INR",
        },
        "currency_symbol": {
            "type": "string",
            "default": "₹",
        },
        "monthly_salary": {
            "type": "number",
            "description": "Monthly salary in INR",
        },
        "monthly_sip": {
            "type": "number",
            "description": "Monthly SIP investment in INR",
        },
        "monthly_rainy_day_fund_transfer": {
            "type": "number",
            "description": "Monthly transfer to rainy day fund in INR",
        },
        "monthly_life_fund_transfer": {
            "type": "number",
            "description": "Monthly transfer to life fund in INR",
        },
        "emergency_fund_target": {
            "type": "number",
            "description": "Emergency fund target amount in INR",
        },
        "monthly_expense": {
            "type": "number",
            "description": "Monthly expense in INR",
        },
        "assumptions": {
            "type": "object",
            "properties": {
                "salary_growth_percentage_per_year": {
                    "type": "number",
                    "description": "Assumed salary growth percentage per year (e.g., 10 for 10%)",
                },
                "expense_growth_percentage_per_year": {
                    "type": "number",
                    "description": "Assumed expense growth percentage per year (e.g., 6 for 6%)",
                },
                "sip_increase_per_year": {
                    "type": "number",
                    "description": "SIP increase amount per year in INR",
                },
                "expected_annual_return_percentage": {
                    "type": "number",
                    "description": "Expected annual return percentage (e.g., 12 for 12%)",
                },
            },
            "required": [
                "salary_growth_percentage_per_year",
                "expense_growth_percentage_per_year",
                "sip_increase_per_year",
                "expected_annual_return_percentage",
            ],
        },
        "emergency_sources": {
            "type": "array",
            "description": "Account and investment IDs that make up the emergency fund",
            "items": {
                "type": "string",
            },
        },
    },
    "required": [
        "monthly_salary",
        "monthly_sip",
        "monthly_rainy_day_fund_transfer",
        "monthly_life_fund_transfer",
        "emergency_fund_target",
        "monthly_expense",
        "assumptions",
    ],
}
