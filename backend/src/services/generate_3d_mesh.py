# src/services/generate_3d_mesh.py
import os
import uuid
import numpy as np
import trimesh  # [web:180]

from src.services.generate_layers import generate_layers

SAVE_DIR = "files/models/"


def _surface_to_mesh(x, y, z):
    """
    Превращает параметрическую поверхность (X,Y,Z) в triangulated mesh.
    """
    # x,y,z – одинаковой формы (m, n)
    # строим квадраты по сетке и делим на два треугольника
    m, n = x.shape
    vertices = np.vstack([
        x.ravel(),
        y.ravel(),
        z.ravel()
    ]).T

    faces = []
    for i in range(m - 1):
        for j in range(n - 1):
            # индексы четырёх вершин квадрата
            v0 = i * n + j
            v1 = i * n + (j + 1)
            v2 = (i + 1) * n + j
            v3 = (i + 1) * n + (j + 1)
            # два треугольника
            faces.append([v0, v1, v2])
            faces.append([v1, v3, v2])

    faces = np.array(faces, dtype=np.int64)
    return trimesh.Trimesh(vertices=vertices, faces=faces, process=False)


def save_3d_model_stl(model_params: dict) -> str:
    os.makedirs(SAVE_DIR, exist_ok=True)

    layers_data = generate_layers(model_params)

    meshes = []

    for layer in layers_data:
        X = layer["X"]
        Y = layer["Y"]
        top = layer["top"]
        bottom = layer["bottom"]

        # верхняя поверхность
        top_mesh = _surface_to_mesh(X, Y, top)

        # нижняя поверхность
        bottom_mesh = _surface_to_mesh(X, Y, bottom)

        # можно дополнительно замкнуть объём боковыми стенками,
        # но даже просто две поверхности уже можно смотреть в 3D

        meshes.extend([top_mesh, bottom_mesh])

    # объединяем все слои в один mesh
    combined = trimesh.util.concatenate(meshes)  # [web:180]

    filename = f"{uuid.uuid4()}.stl"
    file_path = os.path.join(SAVE_DIR, filename)

    combined.export(file_path)  # STL по умолчанию

    return file_path