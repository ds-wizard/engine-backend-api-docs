import unittest

from versions import compute_diff_versions


class VersionsTest(unittest.TestCase):

    def test_compute_diff_versions_1(self):
        # GIVEN:
        versions = [
            (3, 20, 0)
        ]
        expectation = []
        # WHEN:
        result = compute_diff_versions(versions)
        # THEN:
        self.assertEqual(expectation, result)

    def test_compute_diff_versions_2(self):
        # GIVEN:
        versions = [
            (3, 20, 0),
            (3, 21, 0),
            (4, 0, 0),
        ]
        expectation = [
            ('3.20.0', '3.21.0'),
            ('3.21.0', '4.0.0')
        ]
        # WHEN:
        result = compute_diff_versions(versions)
        # THEN:
        self.assertEqual(expectation, result)

    def test_compute_diff_versions_3(self):
        # GIVEN:
        versions = [
            (3, 20, 0),
            (3, 20, 1),
        ]
        expectation = [('3.20.0', '3.20.1')]
        # WHEN:
        result = compute_diff_versions(versions)
        # THEN:
        self.assertEqual(result, expectation)

    def test_compute_diff_versions_4(self):
        # GIVEN:
        versions = [
            (3, 20, 0),
            (3, 21, 0),
            (3, 21, 1),
            (3, 21, 2),
            (3, 22, 0),
        ]
        expectation = [
            ('3.20.0', '3.21.0'),
            ('3.21.0', '3.21.1'),
            ('3.21.1', '3.21.2'),
            ('3.21.2', '3.22.0'),
        ]
        # WHEN:
        result = compute_diff_versions(versions)
        # THEN:
        self.assertEqual(expectation, result)

    def test_compute_diff_versions_5(self):
        # GIVEN:
        versions = [
            (3, 20, 0),
            (3, 21, 0),
            (3, 21, 1),
            (3, 21, 2),
            (3, 22, 0),
            (3, 22, 1),
            (4, 0, 0),
            (4, 1, 0),
        ]
        expectation = [
            ('3.20.0', '3.21.0'),
            ('3.21.0', '3.21.1'),
            ('3.21.1', '3.21.2'),
            ('3.21.2', '3.22.0'),
            ('3.22.0', '3.22.1'),
            ('3.22.1', '4.0.0'),
            ('4.0.0', '4.1.0'),
        ]
        # WHEN:
        result = compute_diff_versions(versions)
        # THEN:
        self.assertEqual(expectation, result)


if __name__ == '__main__':
    unittest.main()
