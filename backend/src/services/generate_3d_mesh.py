# src/services/generate_3d_mesh.py
import os
import uuid
import numpy as np
import trimesh
from trimesh.visual import color as tcolor
from src.services.generate_layers import generate_layers

SAVE_DIR = "files/models/"

# Простая конвертация CSS-имён в hex
CSS_COLORS = {
    "orange": "#ffa500",
    "blue": "#0000ff",
    "red": "#ff0000",
    "green": "#00ff00",
    "yellow": "#ffff00",
    "gray": "#808080",
    "white": "#ffffff",
    "black": "#000000",
}

# src/services/generate_3d_mesh.py
import os
import uuid
import numpy as np
import trimesh
from trimesh.visual import color as tcolor
from src.services.generate_layers import generate_layers

SAVE_DIR = "files/models/"

# Простая конвертация CSS-имён в hex
CSS_COLORS = {
    "orange": "#ffa500",
    "blue": "#0000ff",
    "red": "#ff0000",
    "green": "#00ff00",
    "yellow": "#ffff00",
    "gray": "#808080",
    "white": "#ffffff",
    "black": "#000000",
}


def _surface_to_mesh(x, y, z, rgba=None):
    """
    Превращает параметрическую поверхность (X,Y,Z) в triangulated mesh с цветом.
    """
    m, n = x.shape
    vertices = np.vstack([x.ravel(), y.ravel(), z.ravel()]).T

    faces = []
    for i in range(m - 1):
        for j in range(n - 1):
            v0 = i * n + j
            v1 = i * n + (j + 1)
            v2 = (i + 1) * n + j
            v3 = (i + 1) * n + (j + 1)
            faces.append([v0, v1, v2])
            faces.append([v1, v3, v2])
    faces = np.array(faces, dtype=np.int64)

    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
    if rgba is not None:
        mesh.visual.vertex_colors = np.tile(rgba, (vertices.shape[0], 1))
    return mesh


def save_3d_model_gltf(model_params: dict) -> str:
    os.makedirs(SAVE_DIR, exist_ok=True)

    layers_data = generate_layers(model_params)
    meshes = []

    for layer in layers_data:
        X, Y, top, bottom = layer["X"], layer["Y"], layer["top"], layer["bottom"]

        # Получаем RGBA
        color_hex = CSS_COLORS.get(layer["color"].lower(), "#ffffff")
        rgba = tcolor.hex_to_rgba(color_hex)
        rgba[3] = int(layer["opacity"] * 255)

        # Верхняя и нижняя поверхности
        top_mesh = _surface_to_mesh(X, Y, top, rgba)
        bottom_mesh = _surface_to_mesh(X, Y, bottom, rgba)

        meshes.extend([top_mesh, bottom_mesh])

    # Объединяем все слои
    combined = trimesh.util.concatenate(meshes)

    # Генерируем уникальный путь
    filename = f"{uuid.uuid4()}.glb"
    file_path = os.path.join(SAVE_DIR, filename)

    # Экспортируем в GLB
    combined.export(file_path, file_type="glb")

    return file_path