# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import extract_numbers, fraction_to_float, normalize_string


class ChefkochExtended(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefkoch.de"

    def title(self):
        return self.schema.title()

    def description(self):
        return normalize_string(self.soup.select_one("p.recipe-text").get_text())

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_rows = self.soup.select("table.ingredients tbody tr")
        ingredients = []
        for row in ingredient_rows:
            amount = normalize_string(row.select_one("td.td-left").get_text())
            amount = fraction_to_float(amount)
            numbers = extract_numbers(amount)
            unit = amount
            for number in numbers:
                unit = unit.replace(str(number), "")
            unit = normalize_string(unit)
            amount = "" if sum(numbers) == 0 else sum(numbers)
            ingredient = normalize_string(row.select_one("td.td-right").get_text())
            ingredients.append(
                {"amount": amount, "unit": unit, "ingredient": ingredient}
            )

        return ingredients

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def tags(self):
        tag_links = self.soup.select("a.ds-tag.bi-tags")
        return [normalize_string(tag_link.get_text()) for tag_link in tag_links]

    def difficulty(self):
        return normalize_string(
            self.soup.select_one("span.recipe-difficulty").get_text()
        ).split(" ")[-1]

    def date(self):
        return normalize_string(
            self.soup.select_one("span.recipe-date").get_text()
        ).split(" ")[-1]
