#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Generic HPC principal node charm.
"""

import logging

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus, BlockedStatus

logger = logging.getLogger(__name__)


class HpcNodeCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)
        # self.framework.observe(self.on.config_changed, self._on_config_changed)

        self.framework.observe(self.on.node_relation_created, self._on_node_relation_created)
        self.framework.observe(self.on.node_relation_departed, self._on_node_relation_departed)
        self.framework.observe(self.on.node_relation_joined, self._on_node_relation_joined)

    def _on_install(self, event):
        self.unit.status = BlockedStatus("waiting for node relation")

    def _on_node_relation_created(self, event):
        self.unit.status = ActiveStatus()

    def _on_node_relation_joined(self, event):
        msg = f"principal: subordinate ({event.unit.name}) joined"
        logger.info(msg)
        self.unit.status = ActiveStatus()

    def _on_node_relation_departed(self, event):
        msg = f"principal: subordinate ({event.unit.name}) joined"
        logger.info(msg)


if __name__ == "__main__":  # pragma: nocover
    main(HpcNodeCharm)
