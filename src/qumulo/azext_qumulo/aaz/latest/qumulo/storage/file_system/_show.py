# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "qumulo storage file-system show",
)
class Show(AAZCommand):
    """Retrieve details of a specific file system resource in Qumulo storage.
    """

    _aaz_info = {
        "version": "2024-06-19",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/qumulo.storage/filesystems/{}", "2024-06-19"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.file_system_name = AAZStrArg(
            options=["-n", "--name", "--file-system-name"],
            help="Name of the File System resource",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9_-]*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FileSystemsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FileSystemsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Qumulo.Storage/fileSystems/{fileSystemName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "fileSystemName", self.ctx.args.file_system_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-19",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZIdentityObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.admin_password = AAZStrType(
                serialized_name="adminPassword",
                flags={"secret": True},
            )
            properties.availability_zone = AAZStrType(
                serialized_name="availabilityZone",
            )
            properties.cluster_login_url = AAZStrType(
                serialized_name="clusterLoginUrl",
            )
            properties.delegated_subnet_id = AAZStrType(
                serialized_name="delegatedSubnetId",
                flags={"required": True},
            )
            properties.marketplace_details = AAZObjectType(
                serialized_name="marketplaceDetails",
                flags={"required": True},
            )
            properties.private_i_ps = AAZListType(
                serialized_name="privateIPs",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.storage_sku = AAZStrType(
                serialized_name="storageSku",
                flags={"required": True},
            )
            properties.user_details = AAZObjectType(
                serialized_name="userDetails",
                flags={"required": True},
            )

            marketplace_details = cls._schema_on_200.properties.marketplace_details
            marketplace_details.marketplace_subscription_id = AAZStrType(
                serialized_name="marketplaceSubscriptionId",
            )
            marketplace_details.marketplace_subscription_status = AAZStrType(
                serialized_name="marketplaceSubscriptionStatus",
                flags={"read_only": True},
            )
            marketplace_details.offer_id = AAZStrType(
                serialized_name="offerId",
                flags={"required": True},
            )
            marketplace_details.plan_id = AAZStrType(
                serialized_name="planId",
                flags={"required": True},
            )
            marketplace_details.publisher_id = AAZStrType(
                serialized_name="publisherId",
            )
            marketplace_details.term_unit = AAZStrType(
                serialized_name="termUnit",
            )

            private_i_ps = cls._schema_on_200.properties.private_i_ps
            private_i_ps.Element = AAZStrType()

            user_details = cls._schema_on_200.properties.user_details
            user_details.email = AAZStrType(
                flags={"secret": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
