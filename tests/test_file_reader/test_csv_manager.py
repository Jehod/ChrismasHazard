from unittest import TestCase

from entity.participant import Participant
from exception.custom_exception import CustomException
from file_reader.csv_manager import read, check_mail_format
from metier.utils import to_string
from tests import test_constants

resource_test_path = test_constants.RESOURCE_TEST_PATH

dumb_list = {"toto": Participant("toto", "tutu", "dumbo@gmail.com"),
             "tutu": Participant("tutu", "titi", "dumbo@gmail.com"),
             "titi": Participant("titi", "toto", "dumbo@gmail.com")}

dumb_list_with_empty = {"toto": Participant("toto", "", ""),
                        "tutu": Participant("tutu", "", "dumbo@gmail.com"),
                        "titi": Participant("titi", "toto", "")}


class Test(TestCase):
    def test_read_no_file(self):
        excepted = {}
        result = read(resource_test_path + "toto.csv")
        self.assertEqual(excepted, result)

    def test_read_ok(self):
        excepted = to_string(dumb_list)
        result = read(resource_test_path + "csv_test_ok.csv")
        self.assertEqual(excepted, to_string(result))

    def test_read_malformed_header(self):
        excepted = {}
        result = read(resource_test_path + "csv_test_malformed.csv")
        self.assertEqual(excepted, result)

    def test_read_ok_with_empty(self):
        excepted = to_string(dumb_list_with_empty)
        result = read(resource_test_path + "csv_test_ok_with_empty.csv")
        self.assertEqual(excepted, to_string(result))

    def test_read_without_header(self):
        excepted = {}
        result = read(resource_test_path + "csv_test_no_head.csv")
        self.assertEqual(excepted, result)

    def test_read_malformed_2(self):
        excepted = {}
        result = read(resource_test_path + "csv_test_malformed2.csv")
        self.assertEqual(excepted, result)

    def test_read_already_added(self):
        excepted = {}
        result = read(resource_test_path + "csv_test_doublon.csv")
        self.assertEqual(excepted, result)


    def test_check_mail_format_ok(self):
        mail = "toto@toto.com"
        ok = 'ko'
        try:
            check_mail_format(mail)
            ok = 'ok'
        except CustomException as ex:
            ok = 'ko'

        self.assertEqual('ok', ok)


    def test_check_mail_format_ko(self):
        mails = ["toto", "toto.toto", "toto@toto", "toto.com","@toto.com","to@to.", "toto@.com"]

        for mail in mails:
            ok = 'ko'
            try:
                check_mail_format(mail)
                ok = 'ok'
            except CustomException as ex:
                print(ex)
                ok = 'ko'

            self.assertRaises(CustomException)
            self.assertEqual('ko', ok)
