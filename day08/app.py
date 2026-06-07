from fastapi import FastAPI
from pydantic import BaseModel
from materials_logic import analyze_materials, classify_band_gap

app = FastAPI(title="Materials Project Analyzer")


class Material(BaseModel):
    material_id: str
    formula: str
    band_gap_eV: float | None
    density_g_cm3: float
    energy_above_hull_eV_atom: float
    is_stable: bool


@app.get("/")
def home():
    return {"message": "Materials Project Analyzer API"}


@app.get("/classify/{band_gap}")
def classify(band_gap: float):
    return {
        "band_gap_eV": band_gap,
        "classification": classify_band_gap(band_gap)
    }


@app.post("/analyze")
def analyze(materials: list[Material]):
    materials_as_dicts = [material.model_dump() for material in materials]
    return {
        "number_of_materials": len(materials),
        "results": analyze_materials(materials_as_dicts)
    }
