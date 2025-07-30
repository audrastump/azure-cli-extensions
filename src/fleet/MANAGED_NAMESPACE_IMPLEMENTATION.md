# Fleet Managed Namespace Implementation

This document describes the implementation of the managed namespace functionality for Azure Fleet Manager CLI extension.

## Overview

The implementation adds support for the `az fleet managednamespace` command group with the following commands:

- `create` - Creates or updates a managed namespace
- `delete` - Deletes a fleet managed namespace  
- `list` - Lists a fleet's managed namespaces
- `show` - Gets a fleet managed namespace
- `update` - Update a managed namespace

## Implementation Details

### 1. SDK Models Added

**ManagedNamespace** - Main resource model with properties:
- `namespace_name` - The Kubernetes namespace name to create on member clusters
- `labels` - Labels for the managed namespace
- `annotations` - Annotations for the managed namespace
- `provisioning_state` - Status of the last operation
- `status` - Detailed status information

**ManagedNamespaceListResult** - List response model
**ManagedNamespaceStatus** - Status information model  
**ManagedNamespaceStatusCondition** - Individual status condition model
**ManagedNamespaceProvisioningState** - Enum for provisioning states

### 2. Operations Added

**ManagedNamespacesOperations** - SDK operations class with methods:
- `list_by_fleet()` - Lists managed namespaces in a fleet
- `get()` - Gets a specific managed namespace
- `begin_create_or_update()` - Creates or updates a managed namespace (LRO)
- `begin_delete()` - Deletes a managed namespace (LRO)

### 3. CLI Commands Added

**Command Group**: `az fleet managednamespace`

**Commands**:
```bash
# Create a managed namespace
az fleet managednamespace create -g MyFleetResourceGroup -f MyFleetName -n my-namespace

# List managed namespaces  
az fleet managednamespace list -g MyFleetResourceGroup -f MyFleetName

# Show managed namespace details
az fleet managednamespace show -g MyFleetResourceGroup -f MyFleetName -n my-namespace

# Update managed namespace
az fleet managednamespace update -g MyFleetResourceGroup -f MyFleetName -n my-namespace --labels env=staging

# Delete managed namespace
az fleet managednamespace delete -g MyFleetResourceGroup -f MyFleetName -n my-namespace
```

### 4. Files Modified

1. **vendored_sdks/v2025_04_01_preview/operations/_managed_namespaces_operations.py** - New operations class
2. **vendored_sdks/v2025_04_01_preview/models/_models_py3.py** - Added models
3. **vendored_sdks/v2025_04_01_preview/models/_container_service_fleet_mgmt_client_enums.py** - Added enum
4. **vendored_sdks/v2025_04_01_preview/models/__init__.py** - Updated exports
5. **vendored_sdks/v2025_04_01_preview/operations/__init__.py** - Updated exports
6. **vendored_sdks/v2025_04_01_preview/_container_service_fleet_mgmt_client.py** - Added operations client
7. **_client_factory.py** - Added client factory
8. **commands.py** - Added command group
9. **custom.py** - Added custom command implementations
10. **_params.py** - Added parameter definitions
11. **_help.py** - Added help documentation

### 5. API Endpoints

The implementation assumes the following REST API endpoints:

- `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces`
- `GET /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}`
- `PUT /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}`
- `DELETE /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/fleets/{fleetName}/managedNamespaces/{managedNamespaceName}`

API Version: `2025-04-01-preview`

## Testing

The implementation includes unit tests in `test_fleet_managed_namespace_scenario.py` that verify:

- Creating a managed namespace
- Listing managed namespaces
- Showing managed namespace details
- Updating managed namespace properties
- Deleting a managed namespace

## Notes

- The implementation follows the same patterns as existing fleet subcommands (members, updaterun, etc.)
- All operations support long-running operations (LRO) with `--no-wait` parameter
- The delete operation includes confirmation prompt by default
- Labels and annotations support the same validation as other fleet resources
- The namespace name can be different from the managed namespace resource name