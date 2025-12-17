import numpy as np

def generate_layers(model_params):
    x_min = model_params["domain"]["x_min"]
    x_max = model_params["domain"]["x_max"]
    y_min = model_params["domain"]["y_min"]
    y_max = model_params["domain"]["y_max"]
    nx = model_params["domain"]["nx"]
    ny = model_params["domain"]["ny"]

    x = np.linspace(x_min, x_max, nx)
    y = np.linspace(y_min, y_max, ny)
    X, Y = np.meshgrid(x, y)

    layers_data = []

    for layer in model_params["layers"]:
        top = (
            layer["top_depth"]
            + layer["amplitude"]
            * np.sin(X / layer["frequency_x"])
            * np.cos(Y / layer["frequency_y"])
        )

        bottom = top - layer["thickness"]

        layers_data.append({
            "X": X,
            "Y": Y,
            "top": top,
            "bottom": bottom,
            "color": layer["color"],
            "opacity": layer["opacity"],
            "layer_type": layer["layer_type"]
        })

    return layers_data

model_params = {
    "domain": {
        "x_min": 0,
        "x_max": 1000,
        "y_min": 0,
        "y_max": 1000,
        "nx": 200,
        "ny": 200
    },
    "layers": [
        {
            "top_depth": -50,
            "thickness": 30,
            "amplitude": 10,
            "frequency_x": 150,
            "frequency_y": 200,
            "layer_type": "gas",
            "color": "orange",
            "opacity": 0.7
        },
        {
            "top_depth": -100,
            "thickness": 40,
            "amplitude": 8,
            "frequency_x": 180,
            "frequency_y": 170,
            "layer_type": "water",
            "color": "blue",
            "opacity": 0.6
        }
    ]
}