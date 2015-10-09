import requests
import unittest
__author__ = 'pisar_iv'

class TasksTestCase(unittest.TestCase):
    def test_cteate_task(self):
        r = requests.put("http://127.0.0.1:8000/pu/tasks/4/", json={'task_des': '550884','task_ok':'true'})
        self.assertEqual(r.status_code, 200)

