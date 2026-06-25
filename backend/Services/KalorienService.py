class KalorienService:

    @staticmethod
    def berechne_kalorien(
        gewicht: float,
        groesse: float,
        alter: int,
        geschlecht: str,
    ):

        if geschlecht.lower() == "m":
            grundumsatz = (
                (10 * gewicht
                + 6.25 * groesse
                - 5 * alter
                + 5) *1,4
            )
        else:
            grundumsatz = (
                (10 * gewicht
                + 6.25 * groesse
                - 5 * alter
                - 161) * 1,4
            )


        return {
            "grundumsatz": round(grundumsatz, 2)
        }