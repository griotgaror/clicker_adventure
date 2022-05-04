
const lifebar = $(".lifebar");
const lifebar_value = $(".lifebar_value");
const life = lifebar_value.text();
const enemy = $(".enemy");

enemy.click(function() {
    //get damage from server
    $.get("get_attack", {}, function(data, status) {
        if (status == "success") {
            const damage = parseInt(data);
            const new_life = parseInt(lifebar_value.text()) - damage;
            
            //make damage on enemy
            if (new_life > 0) {
                lifebar_value.text(new_life);
                currency(damage);
            }
            //respawn enemy
            else {
                lifebar_value.text(0);
                enemy.hide();
                setTimeout(function() {
                    enemy.show();
                    lifebar_value.text(life);
                }, 200);
            };
        };
    });
});


//currency to server
var currency = function(damage) {
    const gold = $("#gold");
    gold.text(parseInt(gold.text()) + parseInt(damage));

    $.post("currency", {"new_gold": parseInt(gold.text())}, function(data, status) {

    });
};