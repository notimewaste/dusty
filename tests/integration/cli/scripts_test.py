from datetime import datetime
from os import path
from shutil import rmtree
from subprocess import check_call, check_output
from tempfile import mkdtemp
import time

import git
from mock import patch

from dusty import commands
from ...fixtures import single_specs_fixture
from ...testcases import DustyIntegrationTestCase

class TestScriptsCLI(DustyIntegrationTestCase):
    def setUp(self):
        super(TestScriptsCLI, self).setUp()
        self.fake_repo_location = path.join(mkdtemp(), 'appa')
        self._set_up_fake_local_repo(path=self.fake_repo_location)
        single_specs_fixture()
        self.run_command('repos override github.com/app/a {}'.format(self.fake_repo_location))
        self.run_command('bundles activate bundle-a')
        self.run_command('up')

    def tearDown(self):
        try:
            self.run_command('stop --rm')
        except Exception:
            pass
        rmtree(self.fake_repo_location)
        super(TestScriptsCLI, self).tearDown()

    def test_basic(self):
        self.assertFileNotInContainer('appa', '/app/a/foo')
        self.run_command('scripts appa example')
        self.assertFileInContainer('appa', '/app/a/foo')
        self.exec_in_container('appa', 'rm /app/a/foo')
