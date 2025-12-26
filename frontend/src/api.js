import axios from "axios";

const API_URL = "http://localhost:9000/well"; 

export const fetchWells = () => axios.get(API_URL);
export const createWell = (well) => axios.post(API_URL, well)
                                    
export const updateWell = (well) => axios.put(`${API_URL}/${well.id}`, well);
export const deleteWell = (id) => axios.delete(`${API_URL}/${id}`);