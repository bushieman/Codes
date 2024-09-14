from notion_client import Client
import datetime
import sys

# CredentialS setup
notion = Client(auth="secret_t95TQhIUkorpwTryOuILOznRkJuo8mlEjo89XQWzU5g")

#* Setup 1: Updating Dishi na Arif Programme
database_id = "6a4295004c2c48538db28241280b3851"
page_id = "dcc7872f85f14ffebc4f3f16ac4715f2"

# Fetch the current debt
debt = notion.pages.retrieve(page_id=page_id)['properties']['Debt']['number']

# Update the debt by $2 (The daily avg spending on food each day per capita in Kenya. Adjust this value based on the current economy.)
new_debt = debt + 2

# Update the database
notion.pages.update(
    page_id=page_id,
    properties={
        "Debt": {
            "number": new_debt
        }
    }
)
