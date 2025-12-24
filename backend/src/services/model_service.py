import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from src.services.generate_layers import generate_layers
import uuid
import os

SAVE_DIR = "files/models/"

def save_3d_model_png(model_params) -> str:
    os.makedirs(SAVE_DIR, exist_ok=True)

    layers_data = generate_layers(model_params)

    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    for layer in layers_data:
        ax.plot_surface(
            layer["X"], layer["Y"], layer["top"],
            color=layer["color"],
            alpha=layer["opacity"]
        )
        ax.plot_surface(
            layer["X"], layer["Y"], layer["bottom"],
            color=layer["color"],
            alpha=layer["opacity"] * 0.7
        )


    ax.set_xlabel("X (м)")
    ax.set_ylabel("Y (м)")
    ax.set_zlabel("Глубина (м)")
    ax.set_title("Объёмная 3D-модель газоносных пластов")
    ax.invert_zaxis()
    ax.invert_xaxis()

    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(SAVE_DIR, filename)

    plt.savefig(file_path, dpi=200)
    plt.close(fig)

    return file_path