# -*- coding: utf-8 -*-
from unittest import TestCase

from process import preprocess_input


class TestProcess(TestCase):
    def test_preprocess_input_1(self):
        input = u"ngày 13/3"
        expected = u"ngày 13 / 3"
        actual = preprocess_input(input)
        self.assertEqual(expected, actual)

    def test_preprocess_input_2(self):
        input = u"vỉa hè,"
        expected = u"vỉa hè , "
        actual = preprocess_input(input)
        self.assertEqual(expected, actual)

    def test_preprocess_input_3(self):
        input = u"Ngày 13/3, các quận nội thành Hà Nội tiếp tục ra quân xử lý lấn chiếm vỉa hè, lòng đường."
        expected = u"Ngày 13 / 3 ,  các quận nội thành Hà Nội tiếp tục ra quân xử lý lấn chiếm vỉa hè ,  lòng đường . "
        actual = preprocess_input(input)
        print actual
        self.assertEqual(expected, actual)
