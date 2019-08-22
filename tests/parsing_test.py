#  Copyright (c) 2019 Markus Ressel
#  .
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  .
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  .
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from telegram_click.argument import Argument
from telegram_click.util import parse_telegram_command
from tests import TestBase


class ParsingTest(TestBase):

    @staticmethod
    def test_named_argument():
        arg1 = Argument(
            name="int_arg",
            description="str description",
            type=int,
            example="5"
        )
        arg2 = Argument(
            name="str_arg",
            description="str description",
            example="text"
        )
        arg3 = Argument(
            name="float_arg",
            description="str description",
            type=float,
            example="1.23",
            default=12.5
        )

        bot_username = "mybot"
        command_line = '/command 12345 --{} "two words"'.format(arg2.name)
        expected_args = [
            arg1,
            arg2,
            arg3
        ]

        target, command, parsed_args = parse_telegram_command(bot_username, command_line, expected_args)

        def test(str_arg, int_arg, float_arg):
            assert int_arg == 12345
            assert str_arg == "two words"
            assert float_arg == arg3.default
            return True

        assert target == bot_username
        assert command == "command"
        assert len(parsed_args) == len(expected_args)
        assert test(**parsed_args)
