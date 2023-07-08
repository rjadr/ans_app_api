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

class InlineResponse20023Result(object):
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
        'id': 'int',
        'mark': 'str',
        'letter_grade': 'str',
        'total_points': 'str',
        'approved': 'str',
        'archived': 'bool',
        'state': 'str',
        'attempt': 'int',
        'user_id': 'int',
        'group_id': 'int',
        'submitted_at': 'str',
        'trashed': 'bool',
        'trashed_at': 'str',
        'additional_time': 'int',
        'comment': 'str',
        'assignment_id': 'int',
        'external_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'mark': 'mark',
        'letter_grade': 'letter_grade',
        'total_points': 'total_points',
        'approved': 'approved',
        'archived': 'archived',
        'state': 'state',
        'attempt': 'attempt',
        'user_id': 'user_id',
        'group_id': 'group_id',
        'submitted_at': 'submitted_at',
        'trashed': 'trashed',
        'trashed_at': 'trashed_at',
        'additional_time': 'additional_time',
        'comment': 'comment',
        'assignment_id': 'assignment_id',
        'external_id': 'external_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, mark=None, letter_grade=None, total_points=None, approved=None, archived=None, state=None, attempt=None, user_id=None, group_id=None, submitted_at=None, trashed=None, trashed_at=None, additional_time=None, comment=None, assignment_id=None, external_id=None, created_at=None, updated_at=None):  # noqa: E501
        """InlineResponse20023Result - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._mark = None
        self._letter_grade = None
        self._total_points = None
        self._approved = None
        self._archived = None
        self._state = None
        self._attempt = None
        self._user_id = None
        self._group_id = None
        self._submitted_at = None
        self._trashed = None
        self._trashed_at = None
        self._additional_time = None
        self._comment = None
        self._assignment_id = None
        self._external_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if mark is not None:
            self.mark = mark
        if letter_grade is not None:
            self.letter_grade = letter_grade
        if total_points is not None:
            self.total_points = total_points
        if approved is not None:
            self.approved = approved
        if archived is not None:
            self.archived = archived
        if state is not None:
            self.state = state
        if attempt is not None:
            self.attempt = attempt
        if user_id is not None:
            self.user_id = user_id
        if group_id is not None:
            self.group_id = group_id
        if submitted_at is not None:
            self.submitted_at = submitted_at
        if trashed is not None:
            self.trashed = trashed
        if trashed_at is not None:
            self.trashed_at = trashed_at
        if additional_time is not None:
            self.additional_time = additional_time
        if comment is not None:
            self.comment = comment
        if assignment_id is not None:
            self.assignment_id = assignment_id
        if external_id is not None:
            self.external_id = external_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this InlineResponse20023Result.  # noqa: E501


        :return: The id of this InlineResponse20023Result.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20023Result.


        :param id: The id of this InlineResponse20023Result.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mark(self):
        """Gets the mark of this InlineResponse20023Result.  # noqa: E501


        :return: The mark of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._mark

    @mark.setter
    def mark(self, mark):
        """Sets the mark of this InlineResponse20023Result.


        :param mark: The mark of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._mark = mark

    @property
    def letter_grade(self):
        """Gets the letter_grade of this InlineResponse20023Result.  # noqa: E501


        :return: The letter_grade of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._letter_grade

    @letter_grade.setter
    def letter_grade(self, letter_grade):
        """Sets the letter_grade of this InlineResponse20023Result.


        :param letter_grade: The letter_grade of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._letter_grade = letter_grade

    @property
    def total_points(self):
        """Gets the total_points of this InlineResponse20023Result.  # noqa: E501


        :return: The total_points of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._total_points

    @total_points.setter
    def total_points(self, total_points):
        """Sets the total_points of this InlineResponse20023Result.


        :param total_points: The total_points of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._total_points = total_points

    @property
    def approved(self):
        """Gets the approved of this InlineResponse20023Result.  # noqa: E501


        :return: The approved of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this InlineResponse20023Result.


        :param approved: The approved of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._approved = approved

    @property
    def archived(self):
        """Gets the archived of this InlineResponse20023Result.  # noqa: E501


        :return: The archived of this InlineResponse20023Result.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this InlineResponse20023Result.


        :param archived: The archived of this InlineResponse20023Result.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def state(self):
        """Gets the state of this InlineResponse20023Result.  # noqa: E501


        :return: The state of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse20023Result.


        :param state: The state of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def attempt(self):
        """Gets the attempt of this InlineResponse20023Result.  # noqa: E501


        :return: The attempt of this InlineResponse20023Result.  # noqa: E501
        :rtype: int
        """
        return self._attempt

    @attempt.setter
    def attempt(self, attempt):
        """Sets the attempt of this InlineResponse20023Result.


        :param attempt: The attempt of this InlineResponse20023Result.  # noqa: E501
        :type: int
        """

        self._attempt = attempt

    @property
    def user_id(self):
        """Gets the user_id of this InlineResponse20023Result.  # noqa: E501


        :return: The user_id of this InlineResponse20023Result.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineResponse20023Result.


        :param user_id: The user_id of this InlineResponse20023Result.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """Gets the group_id of this InlineResponse20023Result.  # noqa: E501


        :return: The group_id of this InlineResponse20023Result.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InlineResponse20023Result.


        :param group_id: The group_id of this InlineResponse20023Result.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def submitted_at(self):
        """Gets the submitted_at of this InlineResponse20023Result.  # noqa: E501


        :return: The submitted_at of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this InlineResponse20023Result.


        :param submitted_at: The submitted_at of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._submitted_at = submitted_at

    @property
    def trashed(self):
        """Gets the trashed of this InlineResponse20023Result.  # noqa: E501


        :return: The trashed of this InlineResponse20023Result.  # noqa: E501
        :rtype: bool
        """
        return self._trashed

    @trashed.setter
    def trashed(self, trashed):
        """Sets the trashed of this InlineResponse20023Result.


        :param trashed: The trashed of this InlineResponse20023Result.  # noqa: E501
        :type: bool
        """

        self._trashed = trashed

    @property
    def trashed_at(self):
        """Gets the trashed_at of this InlineResponse20023Result.  # noqa: E501


        :return: The trashed_at of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._trashed_at

    @trashed_at.setter
    def trashed_at(self, trashed_at):
        """Sets the trashed_at of this InlineResponse20023Result.


        :param trashed_at: The trashed_at of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._trashed_at = trashed_at

    @property
    def additional_time(self):
        """Gets the additional_time of this InlineResponse20023Result.  # noqa: E501


        :return: The additional_time of this InlineResponse20023Result.  # noqa: E501
        :rtype: int
        """
        return self._additional_time

    @additional_time.setter
    def additional_time(self, additional_time):
        """Sets the additional_time of this InlineResponse20023Result.


        :param additional_time: The additional_time of this InlineResponse20023Result.  # noqa: E501
        :type: int
        """

        self._additional_time = additional_time

    @property
    def comment(self):
        """Gets the comment of this InlineResponse20023Result.  # noqa: E501


        :return: The comment of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this InlineResponse20023Result.


        :param comment: The comment of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def assignment_id(self):
        """Gets the assignment_id of this InlineResponse20023Result.  # noqa: E501


        :return: The assignment_id of this InlineResponse20023Result.  # noqa: E501
        :rtype: int
        """
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, assignment_id):
        """Sets the assignment_id of this InlineResponse20023Result.


        :param assignment_id: The assignment_id of this InlineResponse20023Result.  # noqa: E501
        :type: int
        """

        self._assignment_id = assignment_id

    @property
    def external_id(self):
        """Gets the external_id of this InlineResponse20023Result.  # noqa: E501


        :return: The external_id of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this InlineResponse20023Result.


        :param external_id: The external_id of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20023Result.  # noqa: E501


        :return: The created_at of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20023Result.


        :param created_at: The created_at of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse20023Result.  # noqa: E501


        :return: The updated_at of this InlineResponse20023Result.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse20023Result.


        :param updated_at: The updated_at of this InlineResponse20023Result.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(InlineResponse20023Result, dict):
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
        if not isinstance(other, InlineResponse20023Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
