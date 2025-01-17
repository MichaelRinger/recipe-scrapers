from recipe_scrapers.chefkoch_extended import ChefkochExtended
from tests import ScraperTest


class TestChefkochExtendedScraper(ScraperTest):
    scraper_class = ChefkochExtended

    def test_host(self):
        self.assertEqual("chefkoch.de", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.chefkoch.de/rezepte/1170311223132029/Hackbraten-supersaftig.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Saftiger Hackbraten im Ofen")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Delphinella")

    def test_description(self):
        self.assertEqual(
            self.harvester_class.description(),
            "klassischer saftiger Hackbraten mit viel Soße",
        )

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://img.chefkoch-cdn.de/rezepte/1170311223132029/bilder/1508325/crop-960x540/hackbraten-supersaftig.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "{'amount': 1.5, 'unit': '', 'ingredient': 'Semmel(n), altbacken'}",
                "{'amount': 2, 'unit': '', 'ingredient': 'Gewürzgurke(n)'}",
                "{'amount': 2, 'unit': 'kleine', 'ingredient': 'Zwiebel(n)'}",
                "{'amount': 1, 'unit': 'kl. Bund', 'ingredient': 'Petersilie'}",
                "{'amount': 2, 'unit': 'EL', 'ingredient': 'Zitronensaft'}",
                "{'amount': 50, 'unit': 'g', 'ingredient': 'Butter'}",
                "{'amount': 600, 'unit': 'g', 'ingredient': 'Hackfleisch, gemischtes'}",
                "{'amount': 2, 'unit': 'kleine', 'ingredient': 'Ei(er)'}",
                "{'amount': 125, 'unit': 'ml', 'ingredient': 'Fleischbrühe'}",
                "{'amount': 125, 'unit': 'ml', 'ingredient': 'Sahne'}",
                "{'amount': 1, 'unit': 'EL', 'ingredient': 'Crème fraîche'}",
                "{'amount': 1, 'unit': 'TL', 'ingredient': 'Paprikapulver, edelsüßes'}",
                "{'amount': '', 'unit': '', 'ingredient': 'Salz und Pfeffer, schwarzer'}",
                "{'amount': '', 'unit': '', 'ingredient': 'Cayennepfeffer'}",
                "{'amount': '', 'unit': '', 'ingredient': 'Fett für die Form'}",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Die Semmeln in Scheiben schneiden und mit Wasser übergießen, quellen lassen. Gut ausdrücken. Die Gewürzgurken in sehr feine Würfel schneiden. Zwiebeln ebenfalls in feine Würfel schneiden.\n\n1 EL Butter erhitzen und die Zwiebeln glasig anschwitzen. Petersilie dazugeben. \n\nZwiebel-Petersilienmischung in eine Schüssel geben. Semmeln, Gewürzgurken, Hackfleisch, Eier und Zitronensaft zufügen. Alles mit Salz, Cayennepfeffer und schwarzem Pfeffer würzen und kräftig durchkneten. \n\nDie restliche Butter schmelzen, eine Form fetten. Den Fleischteig zu einem Laib formen und in die Form legen. Auf der unteren Schiene 30 Minuten (Umluft 180 °C) backen, dabei immer mit der flüssigen Butter bestreichen. \n\nDie Fleischbrühe erhitzen und mit der Sahne, der Crème fraîche und dem Paprikapulver verrühren. (wer sehr viel Soße mag, kann die Soßenmenge einfach verdoppeln). Die Soße über den Hackbraten gießen und weitere 10 - 15 Minuten garen. \n\nDazu passen hervorragend Salzkartoffeln.",
            self.harvester_class.instructions(),
        )

    def test_total_time(self):
        return self.assertEqual(85.0, self.harvester_class.total_time())

    def test_cook_time(self):
        return self.assertEqual(45.0, self.harvester_class.cook_time())

    def test_prep_time(self):
        return self.assertEqual(40.0, self.harvester_class.prep_time())

    def test_tags(self):
        return self.assertEqual(
            [
                "Fleisch",
                "Hauptspeise",
                "Rind",
                "Saucen",
                "Schwein",
                "Braten",
                "Resteverwertung",
                "ketogen",
                "Low Carb",
            ],
            self.harvester_class.tags(),
        )

    def test_difficulty(self):
        return self.assertEqual(
            "normal",
            self.harvester_class.difficulty(),
        )
