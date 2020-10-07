from unittest import TestCase

from entity.participant import Participant
from metier.mixer import see_possibilities

toto_n = "toto"
titi_n = "titi"
tutu_n = "tutu"
tete_n = "tete"
tyty_n = "tyty"
tata_n = "tata"
riri_n = "riri"
rere_n = "rere"

toto = Participant(toto_n, tutu_n, "")
tutu = Participant(tutu_n, titi_n, "")
titi = Participant(titi_n, toto_n, "")
tata = Participant(tata_n, "", "")
tyty = Participant(tyty_n, rere_n, "")
tete = Participant(tete_n, rere_n, "")
riri = Participant(riri_n, rere_n, "")
rere = Participant(rere_n, "", "")

crois1 = Participant("crois1", "crois2", "")
crois2 = Participant("crois2", "crois1", "")

couples_possibles = {toto_n: toto, titi_n: titi, tutu_n: tutu}
couples_cross = {"crois1": crois1, "crois2": crois2, tata_n: tata}
couples_possibles_with_empty = {toto_n: toto, titi_n: titi, tata_n: tata, tutu_n: tutu}
couples_No_possibles = { tyty_n: tyty, tete_n: tete, riri_n: riri,rere_n:rere}
couples_possibles_but_error = {toto_n: toto, tata_n: tata, tutu_n: tutu, tete_n: tete}


class Test(TestCase):

    def test_see_possibilities_ok(self):
        bob = see_possibilities(couples_possibles)
        self.assertTrue(bob)

    def test_see_possibilities_cross_ko(self):
        bob = see_possibilities(couples_cross)
        self.assertFalse(bob)

    def test_see_possibilities_ok_with_empty(self):
        bob = see_possibilities(couples_possibles_with_empty)
        self.assertTrue(bob)

    def test_see_possibilities_ko(self):
        bob = see_possibilities(couples_No_possibles)
        self.assertFalse(bob)

    def test_see_possibilities_exclued_nobody(self):
        bob = see_possibilities(couples_possibles_but_error)
        self.assertFalse(bob)
