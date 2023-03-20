# coding: utf-8

"""
    Damacansu Sepeti

    caner bir şeyler yapıyor  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_damacana_damacana_db_new_post(self, body, **kwargs):  # noqa: E501
        """Create Damacana  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_damacana_damacana_db_new_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DamacanaDBModel body: (required)
        :return: DamacanaDBModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_damacana_damacana_db_new_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_damacana_damacana_db_new_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def create_damacana_damacana_db_new_post_with_http_info(
        self, body, **kwargs
    ):  # noqa: E501
        """Create Damacana  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_damacana_damacana_db_new_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DamacanaDBModel body: (required)
        :return: DamacanaDBModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_damacana_damacana_db_new_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `create_damacana_damacana_db_new_post`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/damacana/db/new",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DamacanaDBModel",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_damacana_from_id_damacana_db_id_get(
        self, damacana_id, **kwargs
    ):  # noqa: E501
        """Get Damacana From Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_damacana_from_id_damacana_db_id_get(damacana_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str damacana_id: (required)
        :return: DamacanaDBModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_damacana_from_id_damacana_db_id_get_with_http_info(
                damacana_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_damacana_from_id_damacana_db_id_get_with_http_info(
                damacana_id, **kwargs
            )  # noqa: E501
            return data

    def get_damacana_from_id_damacana_db_id_get_with_http_info(
        self, damacana_id, **kwargs
    ):  # noqa: E501
        """Get Damacana From Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_damacana_from_id_damacana_db_id_get_with_http_info(damacana_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str damacana_id: (required)
        :return: DamacanaDBModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["damacana_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_damacana_from_id_damacana_db_id_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'damacana_id' is set
        if "damacana_id" not in params or params["damacana_id"] is None:
            raise ValueError(
                "Missing the required parameter `damacana_id` when calling `get_damacana_from_id_damacana_db_id_get`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "damacana_id" in params:
            query_params.append(("damacana_id", params["damacana_id"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/damacana/db/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DamacanaDBModel",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_damacana_from_name_damacana_db_search_get(
        self, damacana_name, **kwargs
    ):  # noqa: E501
        """Get Damacana From Name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_damacana_from_name_damacana_db_search_get(damacana_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str damacana_name: (required)
        :return: list[DamacanaDBModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_damacana_from_name_damacana_db_search_get_with_http_info(
                damacana_name, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_damacana_from_name_damacana_db_search_get_with_http_info(
                damacana_name, **kwargs
            )  # noqa: E501
            return data

    def get_damacana_from_name_damacana_db_search_get_with_http_info(
        self, damacana_name, **kwargs
    ):  # noqa: E501
        """Get Damacana From Name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_damacana_from_name_damacana_db_search_get_with_http_info(damacana_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str damacana_name: (required)
        :return: list[DamacanaDBModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["damacana_name"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_damacana_from_name_damacana_db_search_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'damacana_name' is set
        if "damacana_name" not in params or params["damacana_name"] is None:
            raise ValueError(
                "Missing the required parameter `damacana_name` when calling `get_damacana_from_name_damacana_db_search_get`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "damacana_name" in params:
            query_params.append(
                ("damacana_name", params["damacana_name"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/damacana/db/search/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[DamacanaDBModel]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_damacana_storage_damacana_db_get(self, **kwargs):  # noqa: E501
        """List Damacana Storage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_damacana_storage_damacana_db_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DamacanaDBModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_damacana_storage_damacana_db_get_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_damacana_storage_damacana_db_get_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def list_damacana_storage_damacana_db_get_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """List Damacana Storage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_damacana_storage_damacana_db_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DamacanaDBModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_damacana_storage_damacana_db_get" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/damacana/db/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[DamacanaDBModel]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def login_user_login_post(self, body, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_user_login_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserLogin body: (required)
        :return: UserToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.login_user_login_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.login_user_login_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def login_user_login_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Login  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.login_user_login_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserLogin body: (required)
        :return: UserToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login_user_login_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `login_user_login_post`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/user/login",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UserToken",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def refresh_auth_user_refresh_auth_post(self, body, **kwargs):  # noqa: E501
        """Refresh Auth  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_auth_user_refresh_auth_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshTokenEndpoint body: (required)
        :return: UserToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.refresh_auth_user_refresh_auth_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.refresh_auth_user_refresh_auth_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def refresh_auth_user_refresh_auth_post_with_http_info(
        self, body, **kwargs
    ):  # noqa: E501
        """Refresh Auth  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_auth_user_refresh_auth_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RefreshTokenEndpoint body: (required)
        :return: UserToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_auth_user_refresh_auth_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `refresh_auth_user_refresh_auth_post`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/user/refresh_auth",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UserToken",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def sign_up_user_signup_post(self, body, **kwargs):  # noqa: E501
        """Sign Up  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_up_user_signup_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserSignup body: (required)
        :return: UserToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.sign_up_user_signup_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.sign_up_user_signup_post_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def sign_up_user_signup_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Sign Up  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_up_user_signup_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserSignup body: (required)
        :return: UserToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sign_up_user_signup_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `sign_up_user_signup_post`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/user/signup",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UserToken",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
