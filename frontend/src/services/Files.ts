import api from "@/services/api";

export const FilesApi = {
  list() {
    return api.get("/files");
  },

  upload(file) {
    const formData = new FormData();
    formData.append("file", file);

    return api.post("/files/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
  },

  download(id) {
    return api.get(`/files/${id}/download`, {
      responseType: "blob",
    });
  },

  delete(id) {
    return api.delete(`/files/${id}`);
  },
};