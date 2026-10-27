import sys
import traceback
import Interface
# Commented sections serve as reminders for future development.

# import check_seat_pricing.py
# import sales.py
# import interface.py 

# Check for:
# Does the file exist?
# Are there blank spaces?
# Do lowercase letters work?
# What happens to invalid inputs? (Different types, not real seats, etc)


def _test(expected, actual, call):
    try:
        assert actual == expected, f'{call} should return {expected}. Your code: {actual}'
        print(f'\u2713 passed: {call} \u2192 {expected}')
    except AssertionError as ae:
        print(f'\u2717 failed: {ae}')



class TestGallery:

    TEST_FILE = "testing_booked_seats.txt"

    def __init__(self, module_name):
        self.module = module_name

    # Helper function to write data into a file and clear it afterwards.
    def _load_with_contents(self, contents):
        try:
            with open(self.TEST_FILE, "w") as file:
                file.write(contents)
            return Interface.load_unavailable_seats(self.TEST_FILE)
        finally:
            open(self.TEST_FILE, "w").close()
        


    # interface.py testing

    def test_01_interface_file_not_existing(self):
        print('-' * 5, sys._getframe().f_code.co_name, '-' * 5)
        _test(expected={},
            actual=Interface.load_unavailable_seats('missing.txt'),
            call="load_unavailable_seats('missing.txt')")

    def test_02_interface_blank_spaces(self):
        print('-' * 5, sys._getframe().f_code.co_name, '-' * 5)
    
        try:
            _test(expected={'A5': True, 'C7': True},
                actual=self._load_with_contents("A5\n\nC7"),
                call="load_unavailable_seats() with 'A5\\n\\nC7'")
            
            _test(expected={'A5': True, 'C7': True},
                            actual=self._load_with_contents("\nA5\n\nC7"),
                            call="load_unavailable_seats() with '\\nA5\\n\\nC7'")

            _test(expected={'A5': True, 'C7': True},
                            actual=self._load_with_contents("A5\n\nC7\n"),
                            call="load_unavailable_seats() with 'A5\\n\\nC7\\n'")
                    
        except Exception as e:
            print(f"\u2717 FAILED. calling load_unavailable_seats() raised an exception. {type(e).__name__}: {e}")
            print(traceback.format_exc())


    def test_03_interface_lowercase(self):
        print('-' * 5, sys._getframe().f_code.co_name, '-' * 5)
  
        try:
            _test(expected={'A5': True, 'C6': True},
                actual=self._load_with_contents("a5\nc6"),
                call="load_unavailable_seats('testing_booked_seats.txt')")

            _test(expected={'B8': True, 'D4': True},
                        actual=self._load_with_contents("B8\nd4"),
                        call="load_unavailable_seats('testing_booked_seats.txt')")

            _test(expected={'G7': True, 'A1': True},
                        actual=self._load_with_contents("g7\nA1"),
                        call="load_unavailable_seats('testing_booked_seats.txt')")
            
        except Exception as e:
            print(f"\u2717 FAILED. calling load_unavailable_seats() raised an exception. {type(e).__name__}: {e}")
            print(traceback.format_exc())






test = TestGallery(sys.modules[__name__])
test.test_01_interface_file_not_existing()
test.test_02_interface_blank_spaces()
test.test_03_interface_lowercase()