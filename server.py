from flask import Flask, request, abort
import json
from data import me, catalog
import random
from random import randrange

# creating a new object in Python for the Flask class
# string, float, int are global varibles
# using double underscores __ are called "magic" varibles

app = Flask(__name__)


# to get to the root of the domanin
@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is just another endpoint"


@app.get("/about")
def about():
    return "About The developer Jimmy Smith"

##############################################################################################################
###########################################  API PRODUCTS ####################################################
##############################################################################################################


@app.get("/api/test")
def test_api():
    return json.dumps("Hello!")

@app.get("/api/about")
def about_me():
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)
    # return the list of products

@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    #must validate
    if not "title" in product:
        return abort(400, "Error: Title is empty")   

    if len(product["title"]) < 5:
        return abort(400, "Error: Title is less than 5 characters")
    
    #when sending a product this assigns a unique_id
    if not "price" in product:
        return abort(400, "Error: Price is empty"),
            
    if product["price"] < 1:
           return abort(400, "Error: Price is less than 1.00")

    product["_id"] = random.randint(100,100000)


    catalog.append(product)

    return product

@app.get("/api/count4")
def catalog_count():
    count = len(catalog)
    return json.dumps(count)


@app.get("/api/catalog/total")
def catalog_total():
    total = 0
    for prod in catalog:
        total += prod["price"]

    return json.dumps(total)


@app.get("/api/catalog/lowest")
def catalog_lowest():
    lowest = catalog[0]
    for prod in catalog:
        if prod["price"] < lowest["price"]:
            lowest = prod

    return json.dumps(lowest)


@app.get('/api/product/<id>')
def get_product_by_id(id):
    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return json.dumps("Erro ID is not valid")


@app.get('/api/products/<category>')
def get_product_by_cat(category):
    results = []
    for prod in catalog:
        if prod["category"].lower() == category.lower():
            results.append(prod)

    return json.dumps(results)

@app.post("/api/game/<pick>")
def rps_game(pick):

    num = random.randint(0,2)
    pc = ""
    if num == 0:
        pc = "paper"
    elif num == 1:
        pc = "rock"
    else:
        pc = "scissors"

    winner = ""
    if pick == "paper":
        if pc == "rock":
            winner = "you"
        elif pc == "scissors":
            winner = "pc" 
        else:
            winner = "draw"

    elif pick == "rock":
        if pc == "rock":
            winner = "draw"
        elif pc == "scissors":
            winner = "you" 
        else:
            winner = "pc"

    elif pick == "scissors":
        if pc == "rock":
            winner = "pc"
        elif pc == "scissors":
            winner = "draw" 
        else:
            winner = "you"
    
     
    results = {
        "you":pick,
        "PC":pc,
        "Winner": winner
    
    }
    
    return json.dumps(results)

