from flask import Flask, redirect, render_template, url_for, request;
import json


app  = Flask(__name__, static_folder= "static", template_folder="template");
host = "0.0.0.0";
port = 5050;

data_file = open("data.json");
game_data = json.load(data_file);

@app.route("/")
def index():
    return redirect(url_for("home"));

@app.route("/home", methods=["POST", "GET"])
def home():
    return render_template("home.html", navigations=get_navigation("home"), gold=game_data["gold"]);

@app.route("/exploration", methods=["POST", "GET"])
def exploration():
    Enemys = [];

    for enemy in game_data["enemys"]:
        Enemys.append({
            "name": enemy["name"],
            "img": "static/Assets/IconsEnemy/" + enemy["img"],
        });

    return render_template("exploration.html", navigations=get_navigation("exploration"), enemys=Enemys, gold=game_data["gold"])

@app.route("/fight", methods=["POST", "GET"])
def fight():
    if request.method == "POST":
        for enemy in game_data["enemys"]:
            if request.form.getlist(enemy["name"]):
                enemy_img = "static/Assets/IconsEnemy/" + enemy["img"];
                enemy_hp = enemy["hp"];

                return render_template("fight.html", navigations=get_navigation("fight"), gold=game_data["gold"], enemy_hp=enemy_hp, enemy_img=enemy_img);
    
    if request.method == "GET":
        return redirect(url_for("exploration"));

@app.route("/get_attack", methods=["GET"])
def get_attack():
    if request.method == "GET":
        test_attack = "1";
        return test_attack;

@app.route("/currency", methods=["POST", "GET"])
def currency():
    if request.method == "POST":
        damage = request.form.getlist("damage");
        gold = game_data["gold"];
        print(gold, damage);

        return "data received";

def get_navigation(route): 
    for data in game_data["navigation"]:
        if data["name"] == route:
            
            navigation = [];

            for path in data["path"]:
                navigation.append({
                    "name": path,
                    "img": game_data["navigations_icons"]  + path + ".png",
                });

            return navigation;


if __name__ == "__main__":
    app.run(host, port, debug=True);