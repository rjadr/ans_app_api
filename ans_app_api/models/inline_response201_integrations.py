# coding: utf-8

"""
    API V2

    #### Authorization The API can only be accessed by creating a token at: [https://ans.app/users/tokens](https://ans.app/users/tokens).<br> The provided token is a Bearer token and needs to be set in the Request Header with key Authorization and value \"Bearer [token]\" for every request.<br>  #### Pagination The API generates several headers due to its use of pagination, this includes:      - Link, the standard link header defined in RFC 8288     - Current-Page, which shows the current page of the requested data     - Page-Items, which shows the amount of items per page     - Total-Pages, which shows the total amount of pages available     - Total-Count, which shows the total count of objects that was requested  #### Rate Limits The API enforces a rate limit of 500 request per minute per ip-address. If the rate limit is exceeded, the API responds with a HTTP 429 Too Many Requests response code.<br> You can use the following response headers to confirm the current rate limit and monitor the number of requests remaining in the current minute.<br>      - RateLimit-Limit, the current limit for your account     - RateLimit-Remaining, the number of remaining requests in the current minute     - RateLimit-Reset, the number of seconds until the limit is reset  #### Search The API offers search functionality through GET requests with a query. For all search endpoints see the [Search](#/Search) section.<br>      - The query must consist of the attribute and the search value connected with a colon (:) or a greater than (>) or smaller than (<) sign.     - You can use the greater and smaller than symbols for numeric and date values.     - If your search value contains whitespaces, you must quote your search query with single or double quotes.     - You can also combine searches by using a whitespace to separate the attributes.     - If your search value is equal to \"null\", all records with null values for that attribute will be found.     - We perform case sensitive exact match searches only.     - You can search for multiple values, by adding square brackets around the search parameters and seperating the parameters using commas without spaces.     - You can see some example queries in the documented search endpoints.   #### Webhooks The API offers you the ability to listen to specific events that occur within the application. For example, you can use webhooks to:      - Archive results when an assignment is archived     - Add users after an assignment is created     - Export a result after it has been approved  When creating a webhook you can specify which events you want to listen to. You can listen to all events, all events for a specific object or only one event for an object.<br> You can listen to 'create', 'update' and 'destroy' events on an object or a combination for example:      - '*' - all events for all objects     - 'assignment' - All events for an assignment     - 'assignment.update' - Only notify when an assignment is updated  The webhooks API returns a secret after creating a new webhook. This secret can be used to verify that the webhook call comes from Ans by creating a sha256 HMAC with the request body and this secret and comparing it to the X-Ans-Signature Header.<br>  Webhook requests are automatically retried up to five times if the endpoint returns certain HTTP response codes. The time interval between retries is gradually extended. Every webhook event is logged and contains the response code, headers and body of the response for debugging purposes.<br>  The following objects are currently supported:      - Assignment     - Result     - User   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse201Integrations(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'exam_services': 'InlineResponse201IntegrationsExamServices',
        'ouriginal': 'InlineResponse201IntegrationsOuriginal',
        'proctorio': 'InlineResponse201IntegrationsProctorio',
        'proctor_exam': 'InlineResponse201IntegrationsProctorExam',
        'safe_exam_browser_server': 'Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserServer',
        'safe_exam_browser': 'Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowser',
        'step': 'InlineResponse201IntegrationsStep',
        'schoolyear': 'InlineResponse201IntegrationsSchoolyear'
    }

    attribute_map = {
        'exam_services': 'exam_services',
        'ouriginal': 'ouriginal',
        'proctorio': 'proctorio',
        'proctor_exam': 'proctor_exam',
        'safe_exam_browser_server': 'safe_exam_browser_server',
        'safe_exam_browser': 'safe_exam_browser',
        'step': 'step',
        'schoolyear': 'schoolyear'
    }

    def __init__(self, exam_services=None, ouriginal=None, proctorio=None, proctor_exam=None, safe_exam_browser_server=None, safe_exam_browser=None, step=None, schoolyear=None):  # noqa: E501
        """InlineResponse201Integrations - a model defined in Swagger"""  # noqa: E501
        self._exam_services = None
        self._ouriginal = None
        self._proctorio = None
        self._proctor_exam = None
        self._safe_exam_browser_server = None
        self._safe_exam_browser = None
        self._step = None
        self._schoolyear = None
        self.discriminator = None
        if exam_services is not None:
            self.exam_services = exam_services
        if ouriginal is not None:
            self.ouriginal = ouriginal
        if proctorio is not None:
            self.proctorio = proctorio
        if proctor_exam is not None:
            self.proctor_exam = proctor_exam
        if safe_exam_browser_server is not None:
            self.safe_exam_browser_server = safe_exam_browser_server
        if safe_exam_browser is not None:
            self.safe_exam_browser = safe_exam_browser
        if step is not None:
            self.step = step
        if schoolyear is not None:
            self.schoolyear = schoolyear

    @property
    def exam_services(self):
        """Gets the exam_services of this InlineResponse201Integrations.  # noqa: E501


        :return: The exam_services of this InlineResponse201Integrations.  # noqa: E501
        :rtype: InlineResponse201IntegrationsExamServices
        """
        return self._exam_services

    @exam_services.setter
    def exam_services(self, exam_services):
        """Sets the exam_services of this InlineResponse201Integrations.


        :param exam_services: The exam_services of this InlineResponse201Integrations.  # noqa: E501
        :type: InlineResponse201IntegrationsExamServices
        """

        self._exam_services = exam_services

    @property
    def ouriginal(self):
        """Gets the ouriginal of this InlineResponse201Integrations.  # noqa: E501


        :return: The ouriginal of this InlineResponse201Integrations.  # noqa: E501
        :rtype: InlineResponse201IntegrationsOuriginal
        """
        return self._ouriginal

    @ouriginal.setter
    def ouriginal(self, ouriginal):
        """Sets the ouriginal of this InlineResponse201Integrations.


        :param ouriginal: The ouriginal of this InlineResponse201Integrations.  # noqa: E501
        :type: InlineResponse201IntegrationsOuriginal
        """

        self._ouriginal = ouriginal

    @property
    def proctorio(self):
        """Gets the proctorio of this InlineResponse201Integrations.  # noqa: E501


        :return: The proctorio of this InlineResponse201Integrations.  # noqa: E501
        :rtype: InlineResponse201IntegrationsProctorio
        """
        return self._proctorio

    @proctorio.setter
    def proctorio(self, proctorio):
        """Sets the proctorio of this InlineResponse201Integrations.


        :param proctorio: The proctorio of this InlineResponse201Integrations.  # noqa: E501
        :type: InlineResponse201IntegrationsProctorio
        """

        self._proctorio = proctorio

    @property
    def proctor_exam(self):
        """Gets the proctor_exam of this InlineResponse201Integrations.  # noqa: E501


        :return: The proctor_exam of this InlineResponse201Integrations.  # noqa: E501
        :rtype: InlineResponse201IntegrationsProctorExam
        """
        return self._proctor_exam

    @proctor_exam.setter
    def proctor_exam(self, proctor_exam):
        """Sets the proctor_exam of this InlineResponse201Integrations.


        :param proctor_exam: The proctor_exam of this InlineResponse201Integrations.  # noqa: E501
        :type: InlineResponse201IntegrationsProctorExam
        """

        self._proctor_exam = proctor_exam

    @property
    def safe_exam_browser_server(self):
        """Gets the safe_exam_browser_server of this InlineResponse201Integrations.  # noqa: E501


        :return: The safe_exam_browser_server of this InlineResponse201Integrations.  # noqa: E501
        :rtype: Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserServer
        """
        return self._safe_exam_browser_server

    @safe_exam_browser_server.setter
    def safe_exam_browser_server(self, safe_exam_browser_server):
        """Sets the safe_exam_browser_server of this InlineResponse201Integrations.


        :param safe_exam_browser_server: The safe_exam_browser_server of this InlineResponse201Integrations.  # noqa: E501
        :type: Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowserServer
        """

        self._safe_exam_browser_server = safe_exam_browser_server

    @property
    def safe_exam_browser(self):
        """Gets the safe_exam_browser of this InlineResponse201Integrations.  # noqa: E501


        :return: The safe_exam_browser of this InlineResponse201Integrations.  # noqa: E501
        :rtype: Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowser
        """
        return self._safe_exam_browser

    @safe_exam_browser.setter
    def safe_exam_browser(self, safe_exam_browser):
        """Sets the safe_exam_browser of this InlineResponse201Integrations.


        :param safe_exam_browser: The safe_exam_browser of this InlineResponse201Integrations.  # noqa: E501
        :type: Apiv2coursescourseIdassignmentsIntegrationsSafeExamBrowser
        """

        self._safe_exam_browser = safe_exam_browser

    @property
    def step(self):
        """Gets the step of this InlineResponse201Integrations.  # noqa: E501


        :return: The step of this InlineResponse201Integrations.  # noqa: E501
        :rtype: InlineResponse201IntegrationsStep
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this InlineResponse201Integrations.


        :param step: The step of this InlineResponse201Integrations.  # noqa: E501
        :type: InlineResponse201IntegrationsStep
        """

        self._step = step

    @property
    def schoolyear(self):
        """Gets the schoolyear of this InlineResponse201Integrations.  # noqa: E501


        :return: The schoolyear of this InlineResponse201Integrations.  # noqa: E501
        :rtype: InlineResponse201IntegrationsSchoolyear
        """
        return self._schoolyear

    @schoolyear.setter
    def schoolyear(self, schoolyear):
        """Sets the schoolyear of this InlineResponse201Integrations.


        :param schoolyear: The schoolyear of this InlineResponse201Integrations.  # noqa: E501
        :type: InlineResponse201IntegrationsSchoolyear
        """

        self._schoolyear = schoolyear

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse201Integrations, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse201Integrations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
