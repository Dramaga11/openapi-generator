# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import sys
import unittest

import petstore_api
try:
    from petstore_api.model import child_cat
except ImportError:
    child_cat = sys.modules[
        'petstore_api.model.child_cat']
try:
    from petstore_api.model import grandparent_animal
except ImportError:
    grandparent_animal = sys.modules[
        'petstore_api.model.grandparent_animal']
from petstore_api.model.parent_pet import ParentPet


class TestParentPet(unittest.TestCase):
    """ParentPet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParentPet(self):
        """Test ParentPet"""

        # test that we can make a ParentPet from a ParentPet
        # which requires that we travel back through ParentPet's allOf descendant
        # GrandparentAnimal, and we use the descendant's discriminator to make ParentPet
        model = ParentPet(pet_type="ParentPet")
        assert isinstance(model, ParentPet)


if __name__ == '__main__':
    unittest.main()