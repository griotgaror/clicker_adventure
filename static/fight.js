
const lifebar = $(".lifebar");
const lifebar_value = $(".lifebar_value");
const life = lifebar_value.text();
const enemy = $(".enemy");

enemy.click(function() {
    $.get("get_attack", {}, function(data, status) {
        if (status == "success") {
            const damage = parseInt(data);
            const new_life = parseInt(lifebar_value.text()) - damage;

            if (new_life > 0) {
                lifebar_value.text(new_life);
                currency(damage);
            }
            else {
                lifebar_value.text(0);
                enemy.hide();
            };
        
        };
    });
});


var currency = function(damage) {
    $.post("currency", {"damage": damage}, function() {});
};