# Copyright (c) 2016 Cisco Systems
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from aim.agent.aid.event_services import polling
from aim.tests.unit.agent.event_services import base


class TestEventServicePolling(base.TestEventServiceBase):

    def setUp(self):
        super(TestEventServicePolling, self).setUp()
        self.set_override('service_polling_interval', 0,
                          group='aim_event_service_polling')

    def test_run(self):
        polling_service = polling.Poller(self.cfg_manager)
        polling_service.loop_count = 1
        polling_service._poll()
        polling_service.sender.serve.assert_called_once()
