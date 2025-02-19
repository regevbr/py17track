"""Define a simple structure for a package."""
from datetime import datetime
from typing import Dict, Optional

import attr
from pytz import UTC, timezone

COUNTRY_MAP: Dict[int, str] = {
    0: "Unknown",
    102: "Afghanistan",
    103: "Albania",
    104: "Algeria",
    105: "Andorra",
    106: "Angola",
    108: "Antarctica",
    110: "Antigua and Barbuda",
    112: "Argentina",
    113: "Armenia",
    115: "Australia",
    116: "Austria",
    117: "Azerbaijan",
    201: "Bahamas",
    202: "Bahrain",
    203: "Bangladesh",
    204: "Barbados",
    205: "Belarus",
    206: "Belgium",
    207: "Belize",
    208: "Benin",
    210: "Bhutan",
    211: "Bolivia",
    212: "Bosnia and Herzegovina",
    213: "Botswana",
    215: "Brazil",
    216: "Brunei",
    217: "Bulgaria",
    218: "Burkina Faso",
    219: "Burundi",
    301: "China",
    302: "Cambodia",
    303: "Cameroon",
    304: "Canada",
    306: "Cape Verde",
    308: "Central African Republic",
    310: "Chile",
    312: "Ivory Coast",
    313: "Colombia",
    314: "Comoros",
    315: "Congo-Brazzaville",
    316: "Congo-Kinshasa",
    317: "Cook Islands",
    318: "Costa Rica",
    319: "Croatia",
    320: "Cuba",
    321: "Cyprus",
    322: "Czech Republic",
    323: "Chad",
    401: "Denmark",
    402: "Djibouti",
    403: "Dominica",
    404: "Dominican Republic",
    501: "Ecuador",
    502: "Egypt",
    503: "United Arab Emirates",
    504: "Estonia",
    505: "Ethiopia",
    506: "Eritrea",
    507: "Equatorial Guinea",
    508: "East Timor",
    603: "Fiji",
    604: "Finland",
    605: "France",
    701: "Gabon",
    702: "Gambia",
    703: "Georgia",
    704: "Germany",
    705: "Ghana",
    707: "Greece",
    709: "Grenada",
    712: "Guatemala",
    713: "Guinea",
    714: "Guyana",
    716: "Guinea-Bissau",
    801: "Hong Kong [CN]",
    802: "Haiti",
    804: "Honduras",
    805: "Hungary",
    901: "Iceland",
    902: "India",
    903: "Indonesia",
    904: "Iran",
    905: "Ireland",
    906: "Israel",
    907: "Italy",
    908: "Iraq",
    1001: "Jamaica",
    1002: "Japan",
    1003: "Jordan",
    1101: "Kazakhstan",
    1102: "Kenya",
    1103: "United Kingdom",
    1104: "Kiribati",
    1105: "Korea, South",
    1106: "Korea, North",
    1107: "Kosovo",
    1108: "Kuwait",
    1109: "Kyrgyzstan",
    1201: "Laos",
    1202: "Latvia",
    1203: "Lebanon",
    1204: "Lesotho",
    1205: "Liberia",
    1206: "Libya",
    1207: "Liechtenstein",
    1208: "Lithuania",
    1209: "Saint Lucia",
    1210: "Luxembourg",
    1301: "Macao [CN]",
    1302: "Macedonia",
    1303: "Madagascar",
    1304: "Malawi",
    1305: "Malaysia",
    1306: "Maldives",
    1307: "Mali",
    1308: "Malta",
    1310: "Marshall Islands",
    1312: "Mauritania",
    1313: "Mauritius",
    1314: "Mexico",
    1315: "Federated States of Micronesia",
    1316: "Moldova",
    1317: "Monaco",
    1318: "Mongolia",
    1319: "Montenegro",
    1321: "Morocco",
    1322: "Mozambique",
    1323: "Myanmar",
    1401: "Namibia",
    1402: "Nauru",
    1403: "Nepal",
    1404: "Netherlands",
    1406: "New Zealand",
    1407: "Nicaragua",
    1408: "Norway",
    1409: "Niger",
    1410: "Nigeria",
    1501: "Oman",
    1601: "Pakistan",
    1602: "Palestine",
    1603: "Panama",
    1604: "Papua New Guinea",
    1605: "Paraguay",
    1606: "Peru",
    1607: "Philippines",
    1608: "Poland",
    1610: "Portugal",
    1614: "Palau",
    1701: "Qatar",
    1802: "Romania",
    1803: "Russian Federation",
    1804: "Rwanda",
    1902: "Saint Vincent and the Grenadines",
    1903: "El Salvador",
    1905: "San Marino",
    1906: "Sao Tome and Principe",
    1907: "Saudi Arabia",
    1908: "Senegal",
    1909: "Serbia",
    1911: "Seychelles",
    1912: "Sierra Leone",
    1913: "Singapore",
    1914: "Slovakia",
    1915: "Slovenia",
    1916: "Solomon Islands",
    1917: "South Africa",
    1918: "Spain",
    1919: "Sri Lanka",
    1920: "Sudan",
    1921: "Suriname",
    1923: "Swaziland",
    1924: "Sweden",
    1925: "Switzerland",
    1926: "Syrian Arab Republic",
    1927: "Saint Kitts and Nevis",
    1928: "Samoa",
    1929: "Somalia",
    1930: "Scotland",
    1932: "South Ossetia",
    2001: "Taiwan [CN]",
    2002: "Tajikistan",
    2003: "Tanzania",
    2004: "Thailand",
    2005: "Togo",
    2006: "Tonga",
    2007: "Trinidad and Tobago",
    2009: "Tuvalu",
    2010: "Tunisia",
    2011: "Turkey",
    2012: "Turkmenistan",
    2101: "Uganda",
    2102: "Ukraine",
    2103: "Uzbekistan",
    2104: "Uruguay",
    2105: "United States",
    2202: "Vanuatu",
    2203: "Venezuela",
    2204: "Vietnam",
    2205: "Vatican City",
    2302: "Western Sahara",
    2501: "Yemen",
    2601: "Zambia",
    2602: "Zimbabwe",
    8901: "Overseas Territory [ES]",
    9001: "Overseas Territory [GB]",
    9002: "Anguilla [GB]",
    9003: "Ascension [GB]",
    9004: "Bermuda [GB]",
    9005: "Cayman Islands [GB]",
    9006: "Gibraltar [GB]",
    9007: "Guernsey [GB]",
    9008: "Saint Helena [GB]",
    9101: "Overseas Territory [FI]",
    9102: "Ã…aland Islands [FI]",
    9201: "Overseas Territory [NL]",
    9202: "Antilles [NL]",
    9203: "Aruba [NL]",
    9301: "Overseas Territory [PT]",
    9401: "Overseas Territory [NO]",
    9501: "Overseas Territory [AU]",
    9502: "Norfolk Island [AU]",
    9601: "Overseas Territory [DK]",
    9602: "Faroe Islands [DK]",
    9603: "Greenland [DK]",
    9701: "Overseas Territory [FR]",
    9702: "New Caledonia [FR]",
    9801: "Overseas Territory [US]",
    9901: "Overseas Territory [NZ]",
}

PACKAGE_STATUS_MAP: Dict[int, str] = {
    0: "Not Found",
    10: "In Transit",
    20: "Expired",
    30: "Ready to be Picked Up",
    35: "Undelivered",
    40: "Delivered",
    50: "Returned",
}

PACKAGE_TYPE_MAP: Dict[int, str] = {
    0: "Unknown",
    1: "Small Registered Package",
    2: "Registered Parcel",
    3: "EMS Package",
}


@attr.s(
    frozen=True
)  # pylint: disable=too-few-public-methods,too-many-instance-attributes
class Package:
    """Define a package object."""

    tracking_number: str = attr.ib()
    destination_country: int = attr.ib(default=0)
    id: Optional[str] = attr.ib(default=None)
    friendly_name: Optional[str] = attr.ib(default=None)
    info_text: Optional[str] = attr.ib(default=None)
    location: str = attr.ib(default="")
    timestamp: str = attr.ib(default="")
    origin_country: int = attr.ib(default=0)
    package_type: int = attr.ib(default=0)
    status: int = attr.ib(default=0)
    tracking_info_language: str = attr.ib(default="Unknown")
    tz: str = attr.ib(default="UTC")

    def __attrs_post_init__(self):
        """Do some post-init processing."""
        object.__setattr__(
            self, "destination_country", COUNTRY_MAP[self.destination_country]
        )
        object.__setattr__(self, "origin_country", COUNTRY_MAP[self.origin_country])
        object.__setattr__(self, "package_type", PACKAGE_TYPE_MAP[self.package_type])
        object.__setattr__(self, "status", PACKAGE_STATUS_MAP[self.status])

        if self.timestamp is not None:
            tz = timezone(self.tz)
            try:
                timestamp = tz.localize(
                    datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M")
                )
            except ValueError:
                try:
                    timestamp = tz.localize(
                        datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S")
                    )
                except ValueError:
                    timestamp = datetime(1970, 1, 1, tzinfo=UTC)

            if self.tz != "UTC":
                timestamp = timestamp.astimezone(UTC)

            object.__setattr__(self, "timestamp", timestamp)
