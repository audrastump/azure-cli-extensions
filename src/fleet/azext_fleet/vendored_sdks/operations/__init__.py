# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

# Import operations from the current API version
from ..v2025_04_01_preview.operations._fleets_operations import FleetsOperations
from ..v2025_04_01_preview.operations._fleet_members_operations import FleetMembersOperations
from ..v2025_04_01_preview.operations._update_runs_operations import UpdateRunsOperations
from ..v2025_04_01_preview.operations._fleet_update_strategies_operations import FleetUpdateStrategiesOperations
from ..v2025_04_01_preview.operations._auto_upgrade_profiles_operations import AutoUpgradeProfilesOperations
from ..v2025_04_01_preview.operations._auto_upgrade_profile_operations_operations import AutoUpgradeProfileOperationsOperations
from ..v2025_04_01_preview.operations._operations import Operations

__all__ = [
    'FleetsOperations',
    'FleetMembersOperations', 
    'UpdateRunsOperations',
    'FleetUpdateStrategiesOperations',
    'AutoUpgradeProfilesOperations',
    'AutoUpgradeProfileOperationsOperations',
    'Operations'
]