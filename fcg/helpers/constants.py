ORIGIN_TEXT = ['hello', 'thanks', 'the love', 'peace', 'responsibility',
               'discipline', 'calm', 'balance', 'modest', 'happiness', 'patience', 'perseverance']

ISO_ALPHA2_COUNTRY_CODES = {
    "AF": "Afghanistan",
    "BO": "Bolivia",
    "BN": "Brunei",
    "BR": "Brazil",
    "BW": "Botswana",
    "BA": "Bosnia and Herzegovina",
    "BG": "Bulgaria",
    "BI": "Burundi",
    "BT": "Bhutan",
    "BJ": "Benin",
    "BF": "Burkina Faso",
    "BY": "Belarus",
    "BB": "Barbados",
    "BE": "Belgium",
    "BZ": "Belize",
    "LV": "Latvia",
    "ZW": "Zimbabwe",
    "YE": "Yemen",
    "ZM": "Zambia",
    "VN": "Vietnam",
    "VE": "Venezuela",
    "EH": "Western Sahara",
    "VA": "Vatican City",
    "VU": "Vanuatu",
    "BD": "Bangladesh",
    "UY": "Uruguay",
    "US": "United States",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "TV": "Tuvalu",
    "GB": "United Kingdom",
    "TR": "Turkey",
    "TN": "Tunisia",
    "TT": "Trinidad and Tobago",
    "UG": "Uganda",
    "TM": "Turkmenistan",
    "TO": "Tonga",
    "TG": "Togo",
    "TH": "Thailand",
    "TZ": "Tanzania",
    "TJ": "Tajikistan",
    "CH": "Switzerland",
    "UZ": "Uzbekistan",
    "SE": "Sweden",
    "SZ": "Swaziland",
    "SY": "Syria",
    "SD": "Sudan",
    "LK": "Sri Lanka",
    "ES": "Spain",
    "SS": "South Sudan",
    "SR": "Suriname",
    "SB": "Solomon Islands",
    "ZA": "South Africa",
    "SO": "Somalia",
    "KR": "South Korea",
    "SG": "Singapore",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "SL": "Sierra Leone",
    "SC": "Seychelles",
    "SN": "Senegal",
    "RS": "Serbia",
    "SA": "Saudi Arabia",
    "ST": "Sao Tome and Principe",
    "SM": "San Marino",
    "WS": "Samoa",
    "RO": "Romania",
    "KN": "Saint Kitts and Nevis",
    "LC": "Saint Lucia",
    "RU": "Russia",
    "RW": "Rwanda",
    "VC": "Saint Vincent and the Grenadines",
    "CG": "Republic of the Congo",
    "PL": "Poland",
    "PE": "Peru",
    "PT": "Portugal",
    "CN": "People's Republic of China",
    "PH": "Philippines",
    "QA": "Qatar",
    "PG": "Papua New Guinea",
    "PA": "Panama",
    "PY": "Paraguay",
    "PW": "Palau",
    "OM": "Oman",
    "PK": "Pakistan",
    "NO": "Norway",
    "KP": "North Korea",
    "NI": "Nicaragua",
    "NZ": "New Zealand",
    "NL": "Netherlands",
    "NU": "Niue",
    "NG": "Nigeria",
    "NE": "Niger",
    "TW": "Republic of China",
    "NR": "Nauru",
    "MM": "Myanmar",
    "NA": "Namibia",
    "MZ": "Mozambique",
    "MA": "Morocco",
    "ME": "Montenegro",
    "MC": "Monaco",
    "MD": "Moldova",
    "FM": "Micronesia",
    "MX": "Mexico",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "MH": "Marshall Islands",
    "ML": "Mali",
    "MV": "Maldives",
    "NP": "Nepal",
    "MG": "Madagascar",
    "MT": "Malta",
    "MY": "Malaysia",
    "MW": "Malawi",
    "MN": "Mongolia",
    "MK": "Macedonia",
    "LU": "Luxembourg",
    "LT": "Lithuania",
    "LR": "Liberia",
    "LA": "Laos",
    "KG": "Kyrgyzstan",
    "KW": "Kuwait",
    "LS": "Lesotho",
    "LB": "Lebanon",
    "LY": "Libya",
    "LI": "Liechtenstein",
    "KZ": "Kazakhstan",
    "JM": "Jamaica",
    "JP": "Japan",
    "JO": "Jordan",
    "KI": "Kiribati",
    "KE": "Kenya",
    "KS": "Kosovo",
    "IE": "Ireland",
    "ID": "Indonesia",
    "IR": "Iran",
    "IN": "India",
    "IL": "Israel",
    "IS": "Iceland",
    "HU": "Hungary",
    "IQ": "Iraq",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HT": "Haiti",
    "HN": "Honduras",
    "GD": "Grenada",
    "GN": "Guinea",
    "GT": "Guatemala",
    "GR": "Greece",
    "GH": "Ghana",
    "DE": "Germany",
    "GE": "Georgia",
    "GM": "Gambia",
    "FR": "France",
    "GA": "Gabon",
    "FI": "Finland",
    "FJ": "Fiji",
    "EE": "Estonia",
    "ET": "Ethiopia",
    "GQ": "Equatorial Guinea",
    "ER": "Eritrea",
    "EG": "Egypt",
    "DM": "Dominica",
    "DJ": "Djibouti",
    "DK": "Denmark",
    "TL": "East Timor",
    "DO": "Dominican Republic",
    "CD": "Democratic Republic of the Congo",
    "CZ": "Czech Republic",
    "HR": "Croatia",
    "CU": "Cuba",
    "CR": "Costa Rica",
    "CI": "Cote d'Ivoire",
    "CK": "Cook Islands",
    "CY": "Cyprus",
    "KM": "Comoros",
    "CO": "Colombia",
    "CL": "Chile",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CV": "Cape Verde",
    "CM": "Cameroon",
    "BH": "Bahrain",
    "KH": "Cambodia",
    "BS": "Bahamas",
    "AU": "Australia",
    "AM": "Armenia",
    "AT": "Austria",
    "AR": "Argentina",
    "SV": "El Salvador",
    "AG": "Antigua and Barbuda",
    "EC": "Ecuador",
    "AD": "Andorra",
    "AO": "Angola",
    "AL": "Albania",
    "DZ": "Algeria",
    "IT": "Italy",
    "AZ": "Azerbaijan",
    "CA": "Canada"
}

COUNTRY_CODE_TO_LANG = {
    'AD': 'ca',
    'AE': 'ar',
    'AF': 'fa,ps',
    'AG': 'en',
    'AI': 'en',
    'AL': 'sq',
    'AM': 'hy',
    'AN': 'nl,en',
    'AO': 'pt',
    'AR': 'es',
    'AS': 'en,sm',
    'AT': 'de',
    'AU': 'en',
    'AW': 'nl,pap',
    'AX': 'sv',
    'BA': 'bs,hr,sr',
    'BB': 'en',
    'BD': 'bn',
    'BE': 'nl,fr,de',
    'BF': 'fr',
    'BH': 'ar',
    'BI': 'fr',
    'BJ': 'fr',
    'BL': 'fr',
    'BM': 'en',
    'BN': 'ms',
    'BO': 'es,qu,ay',
    'BR': 'pt',
    'BS': 'en',
    'BT': 'dz',
    'BV': 'no',
    'BW': 'en,tn',
    'BY': 'be,ru',
    'BZ': 'en',
    'CA': 'en,fr',
    'CC': 'en',
    'CD': 'fr',
    'CF': 'fr',
    'CG': 'fr',
    'CH': 'de,fr,it,rm',
    'CI': 'fr',
    'CK': 'en,rar',
    'CL': 'es',
    'CM': 'fr,en',
    'CN': 'zh-cn, zh-tw',
    'CO': 'es',
    'CR': 'es',
    'CU': 'es',
    'CV': 'pt',
    'CX': 'en',
    'CY': 'el,tr',
    'CZ': 'cs',
    'DE': 'de',
    'DJ': 'fr,ar,so',
    'DK': 'da',
    'DM': 'en',
    'DO': 'es',
    'DZ': 'ar',
    'EC': 'es',
    'EE': 'et',
    'EG': 'ar',
    'EH': 'ar,es,fr',
    'ER': 'ti,ar,en',
    'ES': 'ast,ca,es,eu,gl',
    'ET': 'am,om',
    'FI': 'fi,sv,se',
    'FJ': 'en',
    'FK': 'en',
    'FM': 'en',
    'FO': 'fo',
    'FR': 'fr',
    'GA': 'fr',
    'GB': 'en,ga,cy,gd,kw',
    'GD': 'en',
    'GE': 'ka',
    'GF': 'fr',
    'GG': 'en',
    'GH': 'en',
    'GI': 'en',
    'GL': 'kl,da',
    'GM': 'en',
    'GN': 'fr',
    'GP': 'fr',
    'GQ': 'es,fr,pt',
    'GR': 'el',
    'GS': 'en',
    'GT': 'es',
    'GU': 'en,ch',
    'GW': 'pt',
    'GY': 'en',
    'HK': 'zh,en',
    'HM': 'en',
    'HN': 'es',
    'HR': 'hr',
    'HT': 'fr,ht',
    'HU': 'hu',
    'ID': 'id',
    'IE': 'en,ga',
    'IL': 'he',
    'IM': 'en',
    'IN': 'hi,en',
    'IO': 'en',
    'IQ': 'ar,ku',
    'IR': 'fa',
    'IS': 'is',
    'IT': 'it,de,fr',
    'JE': 'en',
    'JM': 'en',
    'JO': 'ar',
    'JP': 'ja',
    'KE': 'sw,en',
    'KG': 'ky,ru',
    'KH': 'km',
    'KI': 'en',
    'KM': 'ar,fr',
    'KN': 'en',
    'KP': 'ko',
    'KR': 'ko,en',
    'KW': 'ar',
    'KY': 'en',
    'KZ': 'kk,ru',
    'LA': 'lo',
    'LB': 'ar,fr',
    'LC': 'en',
    'LI': 'de',
    'LK': 'si,ta',
    'LR': 'en',
    'LS': 'en,st',
    'LT': 'lt',
    'LU': 'lb,fr,de',
    'LV': 'lv',
    'LY': 'ar',
    'MA': 'ar',
    'MC': 'fr',
    'MD': 'ru,uk,ro',
    'ME': 'srp,sq,bs,hr,sr',
    'MF': 'fr',
    'MG': 'mg,fr',
    'MH': 'en,mh',
    'MK': 'mk',
    'ML': 'fr',
    'MM': 'my',
    'MN': 'mn',
    'MO': 'zh,pt',
    'MP': 'ch',
    'MQ': 'fr',
    'MR': 'ar,fr',
    'MS': 'en',
    'MT': 'mt,en',
    'MU': 'mfe,fr,en',
    'MV': 'dv',
    'MW': 'en,ny',
    'MX': 'es',
    'MY': 'ms',
    'MZ': 'pt',
    'NA': 'en,sf,de',
    'NC': 'fr',
    'NE': 'fr',
    'NF': 'en,pih',
    'NG': 'en',
    'NI': 'es',
    'NL': 'nl',
    'NO': 'nb,nn,no,se',
    'NP': 'ne',
    'NR': 'na,en',
    'NU': 'niu,en',
    'NZ': 'mi,en',
    'OM': 'ar',
    'PA': 'es',
    'PE': 'es',
    'PF': 'fr',
    'PG': 'en,tpi,ho',
    'PH': 'en,tl',
    'PK': 'en,ur',
    'PL': 'pl',
    'PM': 'fr',
    'PN': 'en,pih',
    'PR': 'es,en',
    'PS': 'ar,he',
    'PT': 'pt',
    'PW': 'en,pau,ja,sov,tox',
    'PY': 'es,gn',
    'QA': 'ar',
    'RE': 'fr',
    'RO': 'ro',
    'RS': 'sr',
    'RU': 'ru',
    'RW': 'rw,fr,en',
    'SA': 'ar',
    'SB': 'en',
    'SC': 'fr,en,crs',
    'SD': 'ar,en',
    'SE': 'sv',
    'SG': 'en,ms,zh,ta',
    'SH': 'en',
    'SI': 'sl',
    'SJ': 'no',
    'SK': 'sk',
    'SL': 'en',
    'SM': 'it',
    'SN': 'fr',
    'SO': 'so,ar',
    'SR': 'nl',
    'ST': 'pt',
    'SS': 'en',
    'SV': 'es',
    'SY': 'ar',
    'SZ': 'en,ss',
    'TC': 'en',
    'TD': 'fr,ar',
    'TF': 'fr',
    'TG': 'fr',
    'TH': 'th',
    'TJ': 'tg,ru',
    'TK': 'tkl,en,sm',
    'TL': 'pt,tet',
    'TM': 'tk',
    'TN': 'ar',
    'TO': 'en',
    'TR': 'tr',
    'TT': 'en',
    'TV': 'en',
    'TW': 'zh',
    'TZ': 'sw,en',
    'UA': 'uk',
    'UG': 'en,sw',
    'UM': 'en',
    'US': 'en',
    'UY': 'es',
    'UZ': 'uz,kaa',
    'VA': 'it',
    'VC': 'en',
    'VE': 'es',
    'VG': 'en',
    'VI': 'en',
    'VN': 'vi',
    'VU': 'bi,en,fr',
    'WF': 'fr',
    'WS': 'sm,en',
    'YE': 'ar',
    'YT': 'fr',
    'ZA': 'zu,xh,af,st,tn,en',
    'ZM': 'en',
    'ZW': 'en,sn,nd ',
}

COUNTRIES_RANKINGS_BY_EDU = {'the united kingdom': 4, 'the united states': 8, 'canada': 2, 'germany': 3, 'france': 9, 'australia': 7, 'switzerland': 1, 'japan': 5, 'sweden': 6, 'denmark': 11, 'the netherlands': 10, 'austria': 17, 'new zealand': 13, 'norway': 12, 'italy': 15, 'finland': 14, 'ireland': 21, 'spain': 19, 'luxembourg': 18, 'singapore': 16, 'south korea': 22, 'russia': 26, 'israel': 30, 'portugal': 24, 'china': 20, 'the czech republic': 33, 'poland': 32, 'hungary': 38, 'greece': 28, 'argentina': 40, 'south africa': 39, 'india': 25, 'the united arab emirates': 23, 'brazil': 29, 'turkey': 36, 'malaysia': 34, 'chile': 52, 'ukraine': 69,
                             'mexico': 31, 'bulgaria': 56, 'romania': 54, 'slovenia': 53, 'croatia': 50, 'egypt': 42, 'qatar': 35, 'saudi arabia': 37, 'colombia': 55, 'latvia': 59, 'uruguay': 58, 'belarus': 72, 'thailand': 27, 'indonesia': 41, 'jordan': 68, 'costa rica': 45, 'the philippines': 49, 'morocco': 47, 'peru': 43, 'bahrain': 61, 'ecuador': 60, 'serbia': 78, 'panama': 48, 'azerbaijan': 64, 'oman': 73, 'the dominican republic': 46, 'tunisia': 65, 'bolivia': 67, 'lebanon': 75, 'iran': 77, 'sri lanka': 51, 'kazakhstan': 70, 'angola': 79, 'ghana': 71, 'kenya': 57, 'vietnam': 44, 'nigeria': 76, 'guatemala': 66, 'myanmar': 63, 'tanzania': 62, 'algeria': 80, 'pakistan': 74}
