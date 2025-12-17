import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.services.generate_layers import generate_layers, model_params

def visualize_volume(model_params):
    layers_data = generate_layers(model_params)
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    for layer in layers_data:
        X = layer["X"]
        Y = layer["Y"]
        top = layer["top"]
        bottom = layer["bottom"]

        # Кровля
        ax.plot_surface(
            X, Y, top,
            color=layer["color"],
            alpha=layer["opacity"],
            linewidth=0
        )

        # Подошва
        ax.plot_surface(
            X, Y, bottom,
            color=layer["color"],
            alpha=layer["opacity"] * 0.7,
            linewidth=0
        )

    ax.set_xlabel("X (м)")
    ax.set_ylabel("Y (м)")
    ax.set_zlabel("Глубина (м)")
    ax.set_title("Объёмная 3D-модель газоносных пластов")

    ax.invert_zaxis()

    plt.tight_layout()
    plt.show()

visualize_volume(model_params)