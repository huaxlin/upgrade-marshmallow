from marshmallow import Schema
from marshmallow.fields import Field
from marshmallow.fields import Raw
from marshmallow.fields import String
from marshmallow.fields import UUID
from marshmallow.fields import Number
from marshmallow.fields import Integer
from marshmallow.fields import Decimal
from marshmallow.fields import Boolean
from marshmallow.fields import Float
from marshmallow.fields import DateTime
from marshmallow.fields import NaiveDateTime
from marshmallow.fields import AwareDateTime
from marshmallow.fields import Time
from marshmallow.fields import Date
from marshmallow.fields import TimeDelta
from marshmallow.fields import Url
from marshmallow.fields import URL
from marshmallow.fields import Email
from marshmallow.fields import IP
from marshmallow.fields import IPv4
from marshmallow.fields import IPv6
from marshmallow.fields import IPInterface
from marshmallow.fields import IPv4Interface
from marshmallow.fields import IPv6Interface
from marshmallow.fields import Str
from marshmallow.fields import Bool
from marshmallow.fields import Int


class FooSchema(Schema):
    field = Field(metadata={'title': 'Field'})
    raw = Raw(metadata={'title': 'Raw'})
    string = String(metadata={'title': 'String'})
    uuid = UUID(metadata={'title': 'UUID'})
    number = Number(metadata={'title': 'Number'})
    integer = Integer(metadata={'title': 'Integer'})
    decimal = Decimal(metadata={'title': 'Decimal'})
    boolean = Boolean(metadata={'title': 'Boolean'})
    float = Float(metadata={'title': 'Float'})
    datetime = DateTime(metadata={'title': 'DateTime'})
    naivedatetime = NaiveDateTime(metadata={'title': 'NaiveDateTime'})
    awaredatetime = AwareDateTime(metadata={'title': 'AwareDateTime'})
    time = Time(metadata={'title': 'Time'})
    date = Date(metadata={'title': 'Date'})
    timedelta = TimeDelta(metadata={'title': 'TimeDelta'})
    url = Url(metadata={'title': 'Url'})
    url = URL(metadata={'title': 'URL'})
    email = Email(metadata={'title': 'Email'})
    ip = IP(metadata={'title': 'IP'})
    ipv4 = IPv4(metadata={'title': 'IPv4'})
    ipv6 = IPv6(metadata={'title': 'IPv6'})
    ipinterface = IPInterface(metadata={'title': 'IPInterface'})
    ipv4interface = IPv4Interface(metadata={'title': 'IPv4Interface'})
    ipv6interface = IPv6Interface(metadata={'title': 'IPv6Interface'})
    str = Str(metadata={'title': 'Str'})
    bool = Bool(metadata={'title': 'Bool'})
    int = Int(metadata={'title': 'Int'})
