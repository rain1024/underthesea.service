# -*- coding: utf-8 -*-
from unittest import TestCase

from process import preprocess_input, postprocess_output


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

    def test_postprocess_output_1(self):
        input = u"[nội thành]"
        expected = u"nội_thành"
        actual = postprocess_output(input)
        self.assertEqual(expected, actual)

    def test_postprocess_output_2(self):
        input = u"[nội thành] [Hà Nội tiếp tục]"
        expected = u"nội_thành Hà_Nội_tiếp_tục"
        actual = postprocess_output(input)
        self.assertEqual(expected, actual)
