import re
from typing import Optional
from pyquery import PyQuery
from models.horseback import Horseback
from models.horse import Horse


class FfeService:
    """Service used to load horse's datas on Ffe.

    Hint: this service should works without changes,
          but feel free to do some modifications if you want.
    """

    def load(self, id: str) -> Optional[Horse]:
        """Loads and parse Horse on FFE website."""
        pq = PyQuery(
            url=f"https://ffecompet.ffe.com/cheval/detail/performances/{id}?direction=0&countResultPerPage=60&page=1"
        )

        # Check for 404
        div_error = pq("div").filter(".error-desc")
        if div_error.length > 0:
            return None

        horse = Horse()

        # Get Horse name
        p = pq("p").filter(".inline")
        horse.name = re.search("[A-Z\s]{2,}", p.html()).group().strip()  # type: ignore

        # Parse HTML table for Horseback results
        rows = pq("tr").filter(".d-none")

        for row in rows:
            horseback = Horseback()
            columns = PyQuery(row).children("td")

            # Skip headers
            date = PyQuery(columns[0]).text()
            if date == "Date":
                continue

            # Fill results
            horseback.date = date  # type: ignore
            horseback.place = PyQuery(columns[1]).text()  # type: ignore
            horseback.category = PyQuery(columns[2]).text()  # type: ignore
            horseback.discipline = PyQuery(columns[4]).text()  # type: ignore
            horseback.ranking = PyQuery(columns[7]).text()  # type: ignore

            horse.horsebacks
            horse.horsebacks.append(horseback)

        return horse
