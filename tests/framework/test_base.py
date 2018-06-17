import unittest
from framework.request_wrapper import RequestWrapper


class RESTTests(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self._test_case_id = self.id()
        self._test_case_name = self.id().split('.')[-1]
        self.client = RequestWrapper()

    def tearDown(self):
        self.RunTestCaseSpecificTearDown()
        super().tearDown()

    @property
    def test_case_id(self):
        return self._test_case_id

    @property
    def test_case_name(self):
        return self._test_case_name

    def RunTestCaseSpecificSetup(self):
        """Runs the test specific setUp method

        Note:
            The test specific setUp method must follow a specific naming convention to be picked
            up.
            setUp_<test_case_name> (test case name after the first '_')
            i.e.: For a test case named - 'test_basic_rule' the test case specific setup method
            should be named 'setUp_basic_rule' for it to be picked up.

        Usage:
            Call this method at the end of the Test Class setUp:
            self.RunTestCaseSpecificSetup()
        """
        # Determines the setUp method name
        try:
            test_case_setup = 'setUp_{0}'.format(self.test_case_name[5:])
        except IndexError:
            # Handles case where a test case name does not contain an underscore
            pass
        else:
            if hasattr(self, test_case_setup):
                getattr(self, test_case_setup)()

    def RunTestCaseSpecificTearDown(self):
        """Runs the test case specific tearDown method

        Note:
            The test specific tearDown method must follow a specific naming convention to be
            picked up.
            tearDown_<test_case_name> (test case name after the first '_')
            i.e.: For a test case named - 'test_basic_rule' the test case specific setup method
            should be named 'tearDown_basic_rule' for it to be picked up.

        Usage:
            Call this method at the end of the Test Class tearDown:
            self.RunTestCaseSpecificTearDown()
        """
        # Determines the tearDown method name
        try:
            test_case_teardown = 'tearDown_{0}'.format(self.test_case_name[5:])
        except IndexError:
            # Handles case where a test case name does not contain an underscore
            pass
        else:
            if hasattr(self, test_case_teardown):
                getattr(self, test_case_teardown)()