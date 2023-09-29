import pandas as pd
from datetime import datetime
from models.horse import Horse
import services


class HorseService:
    """Horse service."""

    def get(self, horseId: str, categoryFilter: str, yearFilter: int) -> Horse:
        """Get and return one Horse.

        Args:
          horseId: the horseId to get
          categoryFilter: the category to filter on
          yearFilter: the year to filter on

        Returns: the horse entity, None if we failed to fetch horse
        """
        horse: Horse = services.ffe.load(horseId)

        if horse is None:
            return None

        filtered = filter(
            lambda horseback: (
                categoryFilter == None or horseback.category == categoryFilter
            )
            and (
                datetime.strptime(horseback.date, "%d/%m/%Y").date().year == yearFilter
            ),
            horse.horsebacks,
        )
        horse.horsebacks = list(filtered)
        return horse

    def to_dataframe(self, horse: Horse) -> pd.DataFrame:
        """Converts horse to DataFrame with 3 columns.

        Columns:
          Horse : name of the horse
          Category: composite key with category / discipline
          Points: points win for this horsebacks
        """
        result = []
        for horseback in horse.horsebacks:
            key = f"{horseback.category} - {horseback.discipline}"
            row = {"Horse": horse.name, "Category": key}
            row["Points"] = horseback.points
            result.append(row)

        pd.DataFrame(data=result)
        return pd.DataFrame(data=result)

    def to_array(self, horse: Horse) -> list:
        """Converts horse to list.

        Dict:
          Horse : name of the horse
          Category: composite key with category / discipline
          Points: points win for this horsebacks
        """
        result = []
        for horseback in horse.horsebacks:
            key = f"{horseback.category} - {horseback.discipline}"
            row = {"Horse": horse.name, "Category": key}
            row["Points"] = horseback.points
            result.append(
                {"Horse": horse.name, "Category": key, "Points": horseback.points}
            )

        return result
