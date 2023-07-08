# coding: utf-8

"""
    API V2

    #### Authorization The API can only be accessed by creating a token at: [https://ans.app/users/tokens](https://ans.app/users/tokens).<br> The provided token is a Bearer token and needs to be set in the Request Header with key Authorization and value \"Bearer [token]\" for every request.<br>  #### Pagination The API generates several headers due to its use of pagination, this includes:      - Link, the standard link header defined in RFC 8288     - Current-Page, which shows the current page of the requested data     - Page-Items, which shows the amount of items per page     - Total-Pages, which shows the total amount of pages available     - Total-Count, which shows the total count of objects that was requested  #### Rate Limits The API enforces a rate limit of 500 request per minute per ip-address. If the rate limit is exceeded, the API responds with a HTTP 429 Too Many Requests response code.<br> You can use the following response headers to confirm the current rate limit and monitor the number of requests remaining in the current minute.<br>      - RateLimit-Limit, the current limit for your account     - RateLimit-Remaining, the number of remaining requests in the current minute     - RateLimit-Reset, the number of seconds until the limit is reset  #### Search The API offers search functionality through GET requests with a query. For all search endpoints see the [Search](#/Search) section.<br>      - The query must consist of the attribute and the search value connected with a colon (:) or a greater than (>) or smaller than (<) sign.     - You can use the greater and smaller than symbols for numeric and date values.     - If your search value contains whitespaces, you must quote your search query with single or double quotes.     - You can also combine searches by using a whitespace to separate the attributes.     - If your search value is equal to \"null\", all records with null values for that attribute will be found.     - We perform case sensitive exact match searches only.     - You can search for multiple values, by adding square brackets around the search parameters and seperating the parameters using commas without spaces.     - You can see some example queries in the documented search endpoints.   #### Webhooks The API offers you the ability to listen to specific events that occur within the application. For example, you can use webhooks to:      - Archive results when an assignment is archived     - Add users after an assignment is created     - Export a result after it has been approved  When creating a webhook you can specify which events you want to listen to. You can listen to all events, all events for a specific object or only one event for an object.<br> You can listen to 'create', 'update' and 'destroy' events on an object or a combination for example:      - '*' - all events for all objects     - 'assignment' - All events for an assignment     - 'assignment.update' - Only notify when an assignment is updated  The webhooks API returns a secret after creating a new webhook. This secret can be used to verify that the webhook call comes from Ans by creating a sha256 HMAC with the request body and this secret and comparing it to the X-Ans-Signature Header.<br>  Webhook requests are automatically retried up to five times if the endpoint returns certain HTTP response codes. The time interval between retries is gradually extended. Every webhook event is logged and contains the response code, headers and body of the response for debugging purposes.<br>  The following objects are currently supported:      - Assignment     - Result     - User   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ans_app_api.api_client import ApiClient


class ScoreMarksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_assignments_assignment_id_score_marks_get(self, assignment_id, **kwargs):  # noqa: E501
        """List score marks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_assignments_assignment_id_score_marks_get(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str assignment_id: assignment_id (required)
        :param int items: Items per page, possible values are 5, 10, 20, 50 and 100
        :param int page: Page number
        :return: list[InlineResponse20024]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_assignments_assignment_id_score_marks_get_with_http_info(assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_assignments_assignment_id_score_marks_get_with_http_info(assignment_id, **kwargs)  # noqa: E501
            return data

    def api_v2_assignments_assignment_id_score_marks_get_with_http_info(self, assignment_id, **kwargs):  # noqa: E501
        """List score marks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_assignments_assignment_id_score_marks_get_with_http_info(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str assignment_id: assignment_id (required)
        :param int items: Items per page, possible values are 5, 10, 20, 50 and 100
        :param int page: Page number
        :return: list[InlineResponse20024]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_id', 'items', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_assignments_assignment_id_score_marks_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_id' is set
        if ('assignment_id' not in params or
                params['assignment_id'] is None):
            raise ValueError("Missing the required parameter `assignment_id` when calling `api_v2_assignments_assignment_id_score_marks_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assignment_id' in params:
            path_params['assignment_id'] = params['assignment_id']  # noqa: E501

        query_params = []
        if 'items' in params:
            query_params.append(('items', params['items']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/assignments/{assignment_id}/score_marks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20024]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_assignments_assignment_id_score_marks_post(self, assignment_id, **kwargs):  # noqa: E501
        """Create score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_assignments_assignment_id_score_marks_post(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str assignment_id: assignment_id (required)
        :param AssignmentIdScoreMarksBody body:
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_assignments_assignment_id_score_marks_post_with_http_info(assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_assignments_assignment_id_score_marks_post_with_http_info(assignment_id, **kwargs)  # noqa: E501
            return data

    def api_v2_assignments_assignment_id_score_marks_post_with_http_info(self, assignment_id, **kwargs):  # noqa: E501
        """Create score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_assignments_assignment_id_score_marks_post_with_http_info(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str assignment_id: assignment_id (required)
        :param AssignmentIdScoreMarksBody body:
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_assignments_assignment_id_score_marks_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_id' is set
        if ('assignment_id' not in params or
                params['assignment_id'] is None):
            raise ValueError("Missing the required parameter `assignment_id` when calling `api_v2_assignments_assignment_id_score_marks_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assignment_id' in params:
            path_params['assignment_id'] = params['assignment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/assignments/{assignment_id}/score_marks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get(self, question_bank_assignment_id, **kwargs):  # noqa: E501
        """List question bank assignment score marks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get(question_bank_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str question_bank_assignment_id: question_bank_assignment_id (required)
        :param int items: Items per page, possible values are 5, 10, 20, 50 and 100
        :param int page: Page number
        :return: list[InlineResponse20024]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get_with_http_info(question_bank_assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get_with_http_info(question_bank_assignment_id, **kwargs)  # noqa: E501
            return data

    def api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get_with_http_info(self, question_bank_assignment_id, **kwargs):  # noqa: E501
        """List question bank assignment score marks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get_with_http_info(question_bank_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str question_bank_assignment_id: question_bank_assignment_id (required)
        :param int items: Items per page, possible values are 5, 10, 20, 50 and 100
        :param int page: Page number
        :return: list[InlineResponse20024]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['question_bank_assignment_id', 'items', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'question_bank_assignment_id' is set
        if ('question_bank_assignment_id' not in params or
                params['question_bank_assignment_id'] is None):
            raise ValueError("Missing the required parameter `question_bank_assignment_id` when calling `api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'question_bank_assignment_id' in params:
            path_params['question_bank_assignment_id'] = params['question_bank_assignment_id']  # noqa: E501

        query_params = []
        if 'items' in params:
            query_params.append(('items', params['items']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/question_bank_assignments/{question_bank_assignment_id}/score_marks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20024]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post(self, question_bank_assignment_id, **kwargs):  # noqa: E501
        """Create question bank assignment score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post(question_bank_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str question_bank_assignment_id: question_bank_assignment_id (required)
        :param QuestionBankAssignmentIdScoreMarksBody body:
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post_with_http_info(question_bank_assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post_with_http_info(question_bank_assignment_id, **kwargs)  # noqa: E501
            return data

    def api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post_with_http_info(self, question_bank_assignment_id, **kwargs):  # noqa: E501
        """Create question bank assignment score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post_with_http_info(question_bank_assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str question_bank_assignment_id: question_bank_assignment_id (required)
        :param QuestionBankAssignmentIdScoreMarksBody body:
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['question_bank_assignment_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'question_bank_assignment_id' is set
        if ('question_bank_assignment_id' not in params or
                params['question_bank_assignment_id'] is None):
            raise ValueError("Missing the required parameter `question_bank_assignment_id` when calling `api_v2_question_bank_assignments_question_bank_assignment_id_score_marks_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'question_bank_assignment_id' in params:
            path_params['question_bank_assignment_id'] = params['question_bank_assignment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/question_bank_assignments/{question_bank_assignment_id}/score_marks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_score_marks_id_delete(self, id, **kwargs):  # noqa: E501
        """Delete score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_score_marks_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_score_marks_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_score_marks_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_v2_score_marks_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_score_marks_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_score_marks_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v2_score_marks_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/score_marks/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_score_marks_id_get(self, id, **kwargs):  # noqa: E501
        """Show score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_score_marks_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_score_marks_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_score_marks_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_v2_score_marks_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Show score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_score_marks_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_score_marks_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v2_score_marks_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/score_marks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_score_marks_id_patch(self, id, **kwargs):  # noqa: E501
        """Update score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_score_marks_id_patch(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param ScoreMarksIdBody body:
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_score_marks_id_patch_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_score_marks_id_patch_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def api_v2_score_marks_id_patch_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update score mark  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_score_marks_id_patch_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :param ScoreMarksIdBody body:
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_score_marks_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v2_score_marks_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/score_marks/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
