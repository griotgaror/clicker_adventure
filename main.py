from distutils.spawn import spawn
from flask import Flask, redirect, render_template, request_tearing_down, url_for, request


app = Flask(__name__, template_folder= "template");
host = "0.0.0.0";
port = 5050;

#########################Index###########################
@app.route("/")
def index():
    return redirect(url_for("home"));

#########################Home###########################
@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html", navigations=get_navigations("home"));

#########################Exploration####################
@app.route("/exploration", methods=["POST", "GET"])
def exploration():
    return render_template("exploration.html", navigations=get_navigations("exploration"), enemys=enemys)

#########################Fight###########################
@app.route("/fight", methods=["POST", "GET"])
def fight():
    enemy_img = False;
    enemy_hp = False;
    
    if request.method == "POST":
        data = request.form;
        print(request.form);

        for enemy in enemys:
            if request.form.getlist(enemy["name"]):
                enemy_img = enemy["img"];
                enemy_hp = enemy["hp"];

    return render_template("fight.html", navigations=get_navigations("fight"), enemy_img=enemy_img, enemy_hp=enemy_hp);

@app.route("/get_attack", methods=["GET"])
def get_attack():
    if request.method == "GET":
        test_attack = "1";
        return test_attack;


#########################Variablen#######################
navigation_icons = "/static/assets/icons_navigation/";
enemy_icons = "static/assets/icons_enemy/";

enemys = [
        {"name": "Enemy_1", "img": enemy_icons + "enemy_1.png", "hp": 500},
        {"name": "Goblin", "img": enemy_icons + "goblin.png", "hp": 1000},
        {"name": "Enemy_3", "img": enemy_icons + "enemy_3.png", "hp": 1800},
        {"name": "Black_Crow", "img": enemy_icons + "black_crow.png", "hp": 3000},
        {"name": "Big_Bear", "img": enemy_icons + "big_bear.png", "hp": 4500},
        {"name": "Enemy_6", "img": enemy_icons + "enemy_6.png", "hp": 6000},
    ];    

##################Functions##############################
def get_navigations(path):
    home = {"name": "home", "img": navigation_icons + "home.png"};
    exploration = {"name": "exploration", "img": navigation_icons + "exploration.png"};     
    merchant = {"name": "merchant", "img": navigation_icons + "merchant.png"};
    collection = {"name": "collection", "img": navigation_icons + "collection.png"};
    archivments = {"name": "archivments", "img": navigation_icons + "archivments.png"}

    navigation = {
        "home": [exploration, merchant, collection, archivments],
        "exploration": [home, merchant, collection],
        "fight": [home, exploration, merchant],
    };

    return navigation[path];


if __name__ == "__main__":
    app.run(host, port, debug = True);