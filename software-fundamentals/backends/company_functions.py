"""Functions that interact with company data."""

import json

def is_valid_company(company: dict) -> bool:
    """Returns True if a dict has all required keys."""
    return all(key.lower() in company for key in ["name", "country"])


def get_next_id(companies: list[dict]) -> int:
    """Returns the next valid company ID."""
    return max(company.get("id") for company in companies) + 1


def add_new_company(companies: list[dict], new_company: dict) -> dict:
    """Adds a new company to the storage."""
    company_id = get_next_id(companies)

    new_company["id"] = company_id

    companies.append(new_company)

    return new_company


def load_companies() -> list[dict]:
    """Reads company data from a file."""

    with open("companies.json", "r", encoding="utf-8") as f:
        companies = json.load(f)

    return companies

def save_companies(data: list[dict]):

    with open("companies.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)