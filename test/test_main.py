import unittest

import sys
sys.path.insert(0, '')

from main import ParkingLot


def build_output(values: list, size: int = 10):
    # Builds the output given a list size and list of car names.
    output = ['' for i in range(10)]

    for i, v in enumerate(values):
        output[i] = v

    output = ', '.join(output)

    return output


class TestParkingLot(unittest.TestCase):
    # Testing parkingg lot allocation and management.

    def test_return_cars(self):
        # Wrong ticket number format (string)
        with self.assertRaises(ValueError):
            ParkingLot('pABC;uABC;')
            ParkingLot('pABC;u[][;')

        # Wrong compact command.
        with self.assertRaises(ValueError):
            ParkingLot('pABC;u5000;c33;')

        # Wrong compact command.
        with self.assertRaises(ValueError):
            ParkingLot('u5000;')

        # Output quality check.
        output_expected = build_output(['ABC'])
        self.assertEqual(ParkingLot('pABC;'), output_expected,
                         msg=f'ERROR: Expected: {output_expected}')
        self.assertEqual(ParkingLot('pABC;pRRR;pQQQ;u5001;u5002;'), output_expected,
                         msg=f'ERROR: Expected: {output_expected}')
        self.assertEqual(ParkingLot('pABC;c;p232;u5001;pAAA;u5002;'), output_expected,
                         msg=f'ERROR: Expected: {output_expected}')
        self.assertEqual(ParkingLot('pAAA;c;pABC;u5000;c;pABB;u5002;'), output_expected,
                         msg=f'ERROR: Expected: {output_expected}')


if __name__ == '__main__':
    unittest.main()