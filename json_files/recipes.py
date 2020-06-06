import json

data = {}

recipe_list = [
    {
        "name": "omelette",
        "ingredients": [
            "2 large eggs",
            "2 Tablespoon water",
            "1/8 Tablespoon salt",
            "Pepper",
            "1 Teaspoon butter",
            "1/3 cup shredded cheese"
        ],
        "directions": [
            "BEAT eggs, water, salt and pepper in small bowl until blended.",
            "HEAT butter in 6 to 8-inch nonstick omelet pan or skillet over medium-high heat until hot. TILT pan to "
            "coat bottom. POUR egg mixture into pan. Mixture should set immediately at edges. ",
            "Gently PUSH cooked portions from edges toward the center with inverted turner so that uncooked eggs can "
            "reach the hot pan surface. CONTINUE cooking, tilting pan and gently moving cooked portions as needed. ",
            "When top surface of eggs is thickened and no visible liquid egg remains, PLACE filling on one side of "
            "the omelet. FOLD omelet in half with turner. With a quick flip of the wrist, TURN pan and INVERT or "
            "SLIDE omelet onto plate. SERVE immediately. "
        ],
        "picture": "https://cdn.yemek.com/mncrop/940/625/uploads/2015/05/omlet-yemekcom.jpg"
    },

    {
        "name": "scrambled egg with sausage",
        "ingredients": [
            "6 sausage",
            "6 eggs",
            "3/4 cup milk",
            "3/4 cup shredded sharp Cheddar cheese"
        ],
        "directions": [
            "Place sausage in a large, deep skillet. Cook over medium high heat until evenly brown. Drain and chop "
            "into bite-size pieces; set aside.",
            "While sausage is cooking, beat eggs and milk together. Pour eggs into griddle. Add cheese and cook until "
            "eggs are set. Stir in sausage and serve warm. "

        ],
        "picture": "https://i.nefisyemektarifleri.com/2019/11/20/sosisli-yumurta-3.jpg"
    },

    {
        "name": "tuna fish sandwich",
        "ingredients": [
            "1 (12 ounce) can tuna, drained",
            "1/4 cup Cheddar cheese crumbles (optional)",
            "8 slices pepper or diced",
            "2 tablespoons mayonnaise"
        ],
        "directions": [
            "Stir tuna, Cheddar cheese, diced jalapeno, mayonnaise, relish, lemon juice, "
            "and pepper together in a bowl. Spread tuna mixture on a slice of toast "
            "and top with remaining slice to make a sandwich."
        ],
        "picture": "https://iasbh.tmgrup.com.tr/0a1513/800/600/0/0/0/0?u=https://isbh.tmgrup.com.tr/sbh/2016/03/25/GenelBuyuk/1458893244841.jpg"
    },

    {
        "name": "chicken pilaf",
        "ingredients": [
            "2 cups boneless cooked chicken (cut into cubes)",
            "8 tablespoons butter",
            "1 teaspoon salt",
            "1 1/2 cups raw long-grain rice",
            "1/2 teaspoon ground black pepper"
        ],
        "directions": [
            "Melt butter in a medium saucepan over medium-low heat. ",
            "Add chicken and cook for 3 minutes Add salt, pepper, and coriander, and mix until well combined",
            "Add rice and cook, stirring, for 5 minutes until all the grains of rice are coated with the fat",
            "Cover, reduce heat to low, and simmer for 20 minutes, or until the rice is tender and the liquid has "
            "been absorbed.. ",
            "Remove from heat and let stand for 5 minutes, covered"
        ],
        "picture": "https://i.nefisyemektarifleri.com/2019/06/28/nohutlu-tavuklu-pilav.jpg"
    }

]
