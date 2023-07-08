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

class Apiv2coursescourseIdassignmentsGradesSettings(object):
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
        'grade_calculation': 'str',
        'grade_formula': 'str',
        'rounding': 'str',
        'grade_lower_bound': 'bool',
        'grade_lower_limit': 'str',
        'grade_upper_bound': 'bool',
        'grade_upper_limit': 'str',
        'guess_correction': 'bool',
        'guess_correction_lower_bound': 'bool',
        'passed_grade': 'str'
    }

    attribute_map = {
        'grade_calculation': 'grade_calculation',
        'grade_formula': 'grade_formula',
        'rounding': 'rounding',
        'grade_lower_bound': 'grade_lower_bound',
        'grade_lower_limit': 'grade_lower_limit',
        'grade_upper_bound': 'grade_upper_bound',
        'grade_upper_limit': 'grade_upper_limit',
        'guess_correction': 'guess_correction',
        'guess_correction_lower_bound': 'guess_correction_lower_bound',
        'passed_grade': 'passed_grade'
    }

    def __init__(self, grade_calculation=None, grade_formula=None, rounding=None, grade_lower_bound=None, grade_lower_limit=None, grade_upper_bound=None, grade_upper_limit=None, guess_correction=None, guess_correction_lower_bound=None, passed_grade=None):  # noqa: E501
        """Apiv2coursescourseIdassignmentsGradesSettings - a model defined in Swagger"""  # noqa: E501
        self._grade_calculation = None
        self._grade_formula = None
        self._rounding = None
        self._grade_lower_bound = None
        self._grade_lower_limit = None
        self._grade_upper_bound = None
        self._grade_upper_limit = None
        self._guess_correction = None
        self._guess_correction_lower_bound = None
        self._passed_grade = None
        self.discriminator = None
        if grade_calculation is not None:
            self.grade_calculation = grade_calculation
        if grade_formula is not None:
            self.grade_formula = grade_formula
        if rounding is not None:
            self.rounding = rounding
        if grade_lower_bound is not None:
            self.grade_lower_bound = grade_lower_bound
        if grade_lower_limit is not None:
            self.grade_lower_limit = grade_lower_limit
        if grade_upper_bound is not None:
            self.grade_upper_bound = grade_upper_bound
        if grade_upper_limit is not None:
            self.grade_upper_limit = grade_upper_limit
        if guess_correction is not None:
            self.guess_correction = guess_correction
        if guess_correction_lower_bound is not None:
            self.guess_correction_lower_bound = guess_correction_lower_bound
        if passed_grade is not None:
            self.passed_grade = passed_grade

    @property
    def grade_calculation(self):
        """Gets the grade_calculation of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The grade_calculation of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: str
        """
        return self._grade_calculation

    @grade_calculation.setter
    def grade_calculation(self, grade_calculation):
        """Sets the grade_calculation of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param grade_calculation: The grade_calculation of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: str
        """

        self._grade_calculation = grade_calculation

    @property
    def grade_formula(self):
        """Gets the grade_formula of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The grade_formula of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: str
        """
        return self._grade_formula

    @grade_formula.setter
    def grade_formula(self, grade_formula):
        """Sets the grade_formula of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param grade_formula: The grade_formula of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: str
        """

        self._grade_formula = grade_formula

    @property
    def rounding(self):
        """Gets the rounding of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The rounding of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: str
        """
        return self._rounding

    @rounding.setter
    def rounding(self, rounding):
        """Sets the rounding of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param rounding: The rounding of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: str
        """

        self._rounding = rounding

    @property
    def grade_lower_bound(self):
        """Gets the grade_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The grade_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: bool
        """
        return self._grade_lower_bound

    @grade_lower_bound.setter
    def grade_lower_bound(self, grade_lower_bound):
        """Sets the grade_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param grade_lower_bound: The grade_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: bool
        """

        self._grade_lower_bound = grade_lower_bound

    @property
    def grade_lower_limit(self):
        """Gets the grade_lower_limit of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The grade_lower_limit of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: str
        """
        return self._grade_lower_limit

    @grade_lower_limit.setter
    def grade_lower_limit(self, grade_lower_limit):
        """Sets the grade_lower_limit of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param grade_lower_limit: The grade_lower_limit of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: str
        """

        self._grade_lower_limit = grade_lower_limit

    @property
    def grade_upper_bound(self):
        """Gets the grade_upper_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The grade_upper_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: bool
        """
        return self._grade_upper_bound

    @grade_upper_bound.setter
    def grade_upper_bound(self, grade_upper_bound):
        """Sets the grade_upper_bound of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param grade_upper_bound: The grade_upper_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: bool
        """

        self._grade_upper_bound = grade_upper_bound

    @property
    def grade_upper_limit(self):
        """Gets the grade_upper_limit of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The grade_upper_limit of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: str
        """
        return self._grade_upper_limit

    @grade_upper_limit.setter
    def grade_upper_limit(self, grade_upper_limit):
        """Sets the grade_upper_limit of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param grade_upper_limit: The grade_upper_limit of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: str
        """

        self._grade_upper_limit = grade_upper_limit

    @property
    def guess_correction(self):
        """Gets the guess_correction of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The guess_correction of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: bool
        """
        return self._guess_correction

    @guess_correction.setter
    def guess_correction(self, guess_correction):
        """Sets the guess_correction of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param guess_correction: The guess_correction of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: bool
        """

        self._guess_correction = guess_correction

    @property
    def guess_correction_lower_bound(self):
        """Gets the guess_correction_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The guess_correction_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: bool
        """
        return self._guess_correction_lower_bound

    @guess_correction_lower_bound.setter
    def guess_correction_lower_bound(self, guess_correction_lower_bound):
        """Sets the guess_correction_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param guess_correction_lower_bound: The guess_correction_lower_bound of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: bool
        """

        self._guess_correction_lower_bound = guess_correction_lower_bound

    @property
    def passed_grade(self):
        """Gets the passed_grade of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501


        :return: The passed_grade of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :rtype: str
        """
        return self._passed_grade

    @passed_grade.setter
    def passed_grade(self, passed_grade):
        """Sets the passed_grade of this Apiv2coursescourseIdassignmentsGradesSettings.


        :param passed_grade: The passed_grade of this Apiv2coursescourseIdassignmentsGradesSettings.  # noqa: E501
        :type: str
        """

        self._passed_grade = passed_grade

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
        if issubclass(Apiv2coursescourseIdassignmentsGradesSettings, dict):
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
        if not isinstance(other, Apiv2coursescourseIdassignmentsGradesSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
