from fastapi import APIRouter
from Services.KalorienService import KalorienService

router = APIRouter()

@router.get("/kalorien")
def berechne_kalorien(
    gewicht: float,
    groesse: float,
    alter: int,
    geschlecht: str
):
    return KalorienService.berechne_kalorien(
        gewicht,
        groesse,
        alter,
        geschlecht
    )