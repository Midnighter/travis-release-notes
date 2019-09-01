# Copyright (c) 2019, Moritz E. Beber. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Test that the demo works as expected."""


import pytest
from hypothesis import given
from hypothesis.strategies import characters

import demo


@pytest.mark.parametrize("text, outcome", [
    ("", ""),
    ("snafu", "SNAFU"),
])
def test_shout_it(text: str, outcome: str, capsys):
    """Ensure that output is in uppercase."""
    demo.shout_it(text)
    captured = capsys.readouterr()
    assert captured.out.strip() == outcome


@given(text=characters(whitelist_categories=("Nd", "Lu")))
def test_upper_unicode(text: str, capsys):
    """Ensure that uppercase unicode is printed as is."""
    demo.shout_it(text)
    captured = capsys.readouterr()
    assert captured.out.strip() == text
