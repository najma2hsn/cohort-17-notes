"""An API for company data."""

import json
from random import choice

from flask import Flask, abort, request

from company_functions import is_valid_company, add_new_company, get_next_id, load_companies, save_companies

api = Flask(__name__)  # Create an instance of a server/API

@api.get("/")  # Use this function when someone hits the / route with a GET
def index():
    return "Welcome to the Companies API."


@api.route("/company", methods=["GET", "POST"])
def company_index():
    """Returns data on all companies."""
    parameters = request.args
    companies = load_companies()
    if request.method == "GET":

        if "country" in parameters:
            return [c for c in companies if c["country"] == parameters["country"]]
        else:
            return companies

    if request.method == "POST":
        new_company = request.json
        if not is_valid_company(new_company):
            return {"error": True, "message": "Not a valid company"}, 400
        
        created_company = add_new_company(new_company)

        return created_company, 201
    

@api.route("/company/<int:id>", methods=["GET", "DELETE", "PATCH"])
def company_show(id: int):
    """Returns data on a single company or deletes a company."""
    companies = load_companies()
    if request.method == "GET":
        for c in companies:
            if c["id"] == id:
                return c
        return {"error": True, "message": f"Unable to find a company with ID {id}"}, 404
    elif request.method == "DELETE":
        companies = [c for c in companies if c["id"] != id]
        save_companies(companies)
        return { "success": True }
    else:
        company = [c for c in companies if c["id"] == id][0]
        if "edited" in company:
            company["edited"] += 1
        else:
            company["edited"] = 1
        save_companies(companies)
        return company


@api.get("/company/random")
def company_random():
    """Returns a random company's details."""
    companies = load_companies()
    return choice(companies)


if __name__ == "__main__":

    api.run(port=8080, debug=True)  # Actually set it listening
