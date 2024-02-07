import io
import re
from typing import List
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import dns.resolver
import concurrent.futures
from datetime import datetime
import whois
import email.utils
import email.message
import email.header
import pydnsbl
from lingua import LanguageDetectorBuilder, Language
from PIL import Image
import pytesseract
# IP


def IP_extractor(input):
    ipv4 = r'\b(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(?:\.(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}\b'
    ipv6 = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){6}:[0-9a-fA-F]{1,4}\b|\b::[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){5}(?::[0-9a-fA-F]{1,4}){1,2}\b|\b(?:[0-9a-fA-F]{1,4}:){4}(?::[0-9a-fA-F]{1,4}){1,3}\b|\b(?:[0-9a-fA-F]{1,4}:){3}(?::[0-9a-fA-F]{1,4}){1,4}\b|\b(?:[0-9a-fA-F]{1,4}:){2}(?::[0-9a-fA-F]{1,4}){1,5}\b|\b[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}\b|\b(?:[0-9a-fA-F]{1,4}:){1,7}:\b|\b:(?::[0-9a-fA-F]{1,4}){1,7}\b|\b::1\b'

    ipv4_found = re.findall(ipv4, input)
    ipv6_found = re.findall(ipv6, input)
    return ipv4_found+ipv6_found

# URL


def URL_extractor(input):
    root_zones = r'aaa|aarp|abarth|abb|abbott|abbvie|abc|able|abogado|abudhabi|ac|academy|accenture|accountant|accountants|aco|active|actor|ad|adac|ads|adult|ae|aeg|aero|aetna|af|afamilycompany|afl|africa|ag|agakhan|agency|ai|aig|aigo|airbus|airforce|airtel|akdn|al|alfaromeo|alibaba|alipay|allfinanz|allstate|ally|alsace|alstom|am|amazon|americanexpress|americanfamily|amex|amfam|amica|amsterdam|an|analytics|android|anquan|anz|ao|aol|apartments|app|apple|aq|aquarelle|ar|arab|aramco|archi|army|arpa|art|arte|as|asda|asia|associates|at|athleta|attorney|au|auction|audi|audible|audio|auspost|author|auto|autos|avianca|aw|aws|ax|axa|az|azure|ba|baby|baidu|banamex|bananarepublic|band|bank|bar|barcelona|barclaycard|barclays|barefoot|bargains|baseball|basketball|bauhaus|bayern|bb|bbc|bbt|bbva|bcg|bcn|bd|be|beats|beauty|beer|bentley|berlin|best|bestbuy|bet|bf|bg|bh|bharti|bi|bible|bid|bike|bing|bingo|bio|biz|bj|bl|black|blackfriday|blanco|blockbuster|blog|bloomberg|blue|bm|bms|bmw|bn|bnl|bnpparibas|bo|boats|boehringer|bofa|bom|bond|boo|book|booking|boots|bosch|bostik|boston|bot|boutique|box|bq|br|bradesco|bridgestone|broadway|broker|brother|brussels|bs|bt|budapest|bugatti|build|builders|business|buy|buzz|bv|bw|by|bz|bzh|ca|cab|cafe|cal|call|calvinklein|cam|camera|camp|cancerresearch|canon|capetown|capital|capitalone|car|caravan|cards|care|career|careers|cars|cartier|casa|case|caseih|cash|casino|cat|catering|catholic|cba|cbn|cbre|cbs|cc|cd|ceb|center|ceo|cern|cf|cfa|cfd|cg|ch|chanel|channel|charity|chase|chat|cheap|chintai|chloe|christmas|chrome|chrysler|church|ci|cipriani|circle|cisco|citadel|citi|citic|city|cityeats|ck|cl|claims|cleaning|click|clinic|clinique|clothing|cloud|club|clubmed|cm|cn|co|coach|codes|coffee|college|cologne|com|comcast|commbank|community|company|compare|computer|comsec|condos|construction|consulting|contact|contractors|cooking|cookingchannel|cool|coop|corsica|country|coupon|coupons|courses|cpa|cr|credit|creditcard|creditunion|cricket|crown|crs|cruise|cruises|csc|cu|cuisinella|cv|cw|cx|cy|cymru|cyou|cz|dabur|dad|dance|data|date|dating|datsun|day|dclk|dds|de|deal|dealer|deals|degree|delivery|dell|deloitte|delta|democrat|dental|dentist|desi|design|dev|dhl|diamonds|diet|digital|direct|directory|discount|discover|dish|diy|dj|dk|dm|dnp|do|docs|doctor|dodge|dog|doha|domains|doosan|dot|download|drive|dtv|dubai|duck|dunlop|duns|dupont|durban|dvag|dvr|dz|earth|eat|ec|eco|edeka|edu|education|ee|eg|eh|email|emerck|energy|engineer|engineering|enterprises|epost|epson|equipment|er|ericsson|erni|es|esq|estate|esurance|et|etisalat|eu|eurovision|eus|events|everbank|exchange|expert|exposed|express|extraspace|fage|fail|fairwinds|faith|family|fan|fans|farm|farmers|fashion|fast|fedex|feedback|ferrari|ferrero|fi|fiat|fidelity|fido|film|final|finance|financial|fire|firestone|firmdale|fish|fishing|fit|fitness|fj|fk|flickr|flights|flir|florist|flowers|flsmidth|fly|fm|fo|foo|food|foodnetwork|football|ford|forex|forsale|forum|foundation|fox|fr|free|fresenius|frl|frogans|frontdoor|frontier|ftr|fujitsu|fujixerox|fun|fund|furniture|futbol|fyi|ga|gal|gallery|gallo|gallup|game|games|gap|garden|gay|gb|gbiz|gd|gdn|ge|gea|gent|genting|george|gf|gg|ggee|gh|gi|gift|gifts|gives|giving|gl|glade|glass|gle|global|globo|gm|gmail|gmbh|gmo|gmx|gn|godaddy|gold|goldpoint|golf|goo|goodhands|goodyear|goog|google|gop|got|gov|gp|gq|gr|grainger|graphics|gratis|green|gripe|grocery|group|gs|gt|gu|guardian|gucci|guge|guide|guitars|guru|gw|gy|hair|hamburg|hangout|haus|hbo|hdfc|hdfcbank|health|healthcare|help|helsinki|here|hermes|hgtv|hiphop|hisamitsu|hitachi|hiv|hk|hkt|hm|hn|hockey|holdings|holiday|homedepot|homegoods|homes|homesense|honda|honeywell|horse|hospital|host|hosting|hot|hoteles|hotels|hotmail|house|how|hr|hsbc|ht|htc|hu|hughes|hyatt|hyundai|ibm|icbc|ice|icu|id|ie|ieee|ifm|iinet|ikano|il|im|imamat|imdb|immo|immobilien|in|inc|industries|infiniti|info|ing|ink|institute|insurance|insure|int|intel|international|intuit|investments|io|ipiranga|iq|ir|irish|is|iselect|ismaili|ist|istanbul|it|itau|itv|iveco|iwc|jaguar|java|jcb|jcp|je|jeep|jetzt|jewelry|jio|jlc|jll|jm|jmp|jnj|jo|jobs|joburg|jot|joy|jp|jpmorgan|jprs|juegos|juniper|kaufen|kddi|ke|kerryhotels|kerrylogistics|kerryproperties|kfh|kg|kh|ki|kia|kids|kim|kinder|kindle|kitchen|kiwi|km|kn|koeln|komatsu|kosher|kp|kpmg|kpn|kr|krd|kred|kuokgroup|kw|ky|kyoto|kz|la|lacaixa|ladbrokes|lamborghini|lamer|lancaster|lancia|lancome|land|landrover|lanxess|lasalle|lat|latino|latrobe|law|lawyer|lb|lc|lds|lease|leclerc|lefrak|legal|lego|lexus|lgbt|li|liaison|lidl|life|lifeinsurance|lifestyle|lighting|like|lilly|limited|limo|lincoln|linde|link|lipsy|live|living|lixil|lk|llc|llp|loan|loans|locker|locus|loft|lol|london|lotte|lotto|love|lpl|lplfinancial|lr|ls|lt|ltd|ltda|lu|lundbeck|lupin|luxe|luxury|lv|ly|ma|macys|madrid|maif|maison|makeup|man|management|mango|map|market|marketing|markets|marriott|marshalls|maserati|mattel|mba|mc|mcd|mcdonalds|mckinsey|md|me|med|media|meet|melbourne|meme|memorial|men|menu|meo|merckmsd|metlife|mf|mg|mh|miami|microsoft|mil|mini|mint|mit|mitsubishi|mk|ml|mlb|mls|mm|mma|mn|mo|mobi|mobile|mobily|moda|moe|moi|mom|monash|money|monster|montblanc|mopar|mormon|mortgage|moscow|moto|motorcycles|mov|movie|movistar|mp|mq|mr|ms|msd|mt|mtn|mtpc|mtr|mu|museum|music|mutual|mutuelle|mv|mw|mx|my|mz|na|nab|nadex|nagoya|name|nationwide|natura|navy|nba|nc|ne|nec|net|netbank|netflix|network|neustar|new|newholland|news|next|nextdirect|nexus|nf|nfl|ng|ngo|nhk|ni|nico|nike|nikon|ninja|nissan|nissay|nl|no|nokia|northwesternmutual|norton|now|nowruz|nowtv|np|nr|nra|nrw|ntt|nu|nyc|nz|obi|observer|off|office|okinawa|olayan|olayangroup|oldnavy|ollo|om|omega|one|ong|onl|online|onyourside|ooo|open|oracle|orange|org|organic|orientexpress|origins|osaka|otsuka|ott|ovh|pa|page|pamperedchef|panasonic|panerai|paris|pars|partners|parts|party|passagens|pay|pccw|pe|pet|pf|pfizer|pg|ph|pharmacy|phd|philips|phone|photo|photography|photos|physio|piaget|pics|pictet|pictures|pid|pin|ping|pink|pioneer|pizza|pk|pl|place|play|playstation|plumbing|plus|pm|pn|pnc|pohl|poker|politie|porn|post|pr|pramerica|praxi|press|prime|pro|prod|productions|prof|progressive|promo|properties|property|protection|pru|prudential|ps|pt|pub|pw|pwc|py|qa|qpon|quebec|quest|qvc|racing|radio|raid|re|read|realestate|realtor|realty|recipes|red|redstone|redumbrella|rehab|reise|reisen|reit|reliance|ren|rent|rentals|repair|report|republican|rest|restaurant|review|reviews|rexroth|rich|richardli|ricoh|rightathome|ril|rio|rip|rmit|ro|rocher|rocks|rodeo|rogers|room|rs|rsvp|ru|rugby|ruhr|run|rw|rwe|ryukyu|sa|saarland|safe|safety|sakura|sale|salon|samsclub|samsung|sandvik|sandvikcoromant|sanofi|sap|sapo|sarl|sas|save|saxo|sb|sbi|sbs|sc|sca|scb|schaeffler|schmidt|scholarships|school|schule|schwarz|science|scjohnson|scor|scot|sd|se|search|seat|secure|security|seek|select|sener|services|ses|seven|sew|sex|sexy|sfr|sg|sh|shangrila|sharp|shaw|shell|shia|shiksha|shoes|shop|shopping|shouji|show|showtime|shriram|si|silk|sina|singles|site|sj|sk|ski|skin|sky|skype|sl|sling|sm|smart|smile|sn|sncf|so|soccer|social|softbank|software|sohu|solar|solutions|song|sony|soy|spa|space|spiegel|sport|spot|spreadbetting|sr|srl|srt|ss|st|stada|staples|star|starhub|statebank|statefarm|statoil|stc|stcgroup|stockholm|storage|store|stream|studio|study|style|su|sucks|supplies|supply|support|surf|surgery|suzuki|sv|swatch|swiftcover|swiss|sx|sy|sydney|symantec|systems|sz|tab|taipei|talk|taobao|target|tatamotors|tatar|tattoo|tax|taxi|tc|tci|td|tdk|team|tech|technology|tel|telecity|telefonica|temasek|tennis|teva|tf|tg|th|thd|theater|theatre|tiaa|tickets|tienda|tiffany|tips|tires|tirol|tj|tjmaxx|tjx|tk|tkmaxx|tl|tm|tmall|tn|to|today|tokyo|tools|top|toray|toshiba|total|tours|town|toyota|toys|tp|tr|trade|trading|training|travel|travelchannel|travelers|travelersinsurance|trust|trv|tt|tube|tui|tunes|tushu|tv|tvs|tw|tz|ua|ubank|ubs|uconnect|ug|uk|um|unicom|university|uno|uol|ups|us|uy|uz|va|vacations|vana|vanguard|vc|ve|vegas|ventures|verisign|versicherung|vet|vg|vi|viajes|video|vig|viking|villas|vin|vip|virgin|visa|vision|vista|vistaprint|viva|vivo|vlaanderen|vn|vodka|volkswagen|volvo|vote|voting|voto|voyage|vu|vuelos|wales|walmart|walter|wang|wanggou|warman|watch|watches|weather|weatherchannel|webcam|weber|website|wed|wedding|weibo|weir|wf|whoswho|wien|wiki|williamhill|win|windows|wine|winners|wme|wolterskluwer|woodside|work|works|world|wow|ws|wtc|wtf|xbox|xerox|xfinity|xihuan|xin|测试|कॉम|परीक्षा|セール|佛山|ಭಾರತ|慈善|集团|在线|한국|ଭାରତ|大众汽车|点看|คอม|ভাৰত|ভারত|八卦|.ישראל‎|.موقع‎|বাংলা|公益|公司|香格里拉|网站|移动|我爱你|москва|испытание|қаз|католик|онлайн|сайт|联通|срб|бг|бел|.קום‎|时尚|微博|테스트|淡马锡|ファッション|орг|नेट|ストア|アマゾン|삼성|சிங்கப்பூர்|商标|商店|商城|дети|мкд|.טעסט‎|ею|ポイント|新闻|工行|家電|.كوم‎|中文网|中信|中国|中國|娱乐|谷歌|భారత్|ලංකා|電訊盈科|购物|測試|クラウド|ભારત|通販|भारतम्|भारत|भारोत|.آزمایشی‎|பரிட்சை|网店|संगठन|餐厅|网络|ком|укр|香港|亚马逊|诺基亚|食品|δοκιμή|飞利浦|.إختبار‎|台湾|台灣|手表|手机|мон|.الجزائر‎|.عمان‎|.ارامكو‎|.ایران‎|.العليان‎|.اتصالات‎|.امارات‎|.بازار‎|.موريتانيا‎|.پاکستان‎|.الاردن‎|.موبايلي‎|.بارت‎|.بھارت‎|.المغرب‎|.ابوظبي‎|.البحرين‎|.السعودية‎|.ڀارت‎|.كاثوليك‎|.سودان‎|.همراه‎|.عراق‎|.مليسيا‎|澳門|닷컴|政府|.شبكة‎|.بيتك‎|.عرب‎|გე|机构|组织机构|健康|ไทย|.سورية‎|招聘|рус|рф|珠宝|.تونس‎|大拿|ລາວ|みんな|グーグル|ευ|ελ|世界|書籍|ഭാരതം|ਭਾਰਤ|网址|닷넷|コム|天主教|游戏|vermögensberater|vermögensberatung|企业|信息|嘉里大酒店|嘉里|.مصر‎|.قطر‎|广东|இலங்கை|இந்தியா|հայ|新加坡|.فلسطين‎|テスト|政务|xperia|xxx|xyz|yachts|yahoo|yamaxun|yandex|ye|yodobashi|yoga|yokohama|you|youtube|yt|yun|za|zappos|zara|zero|zip|zippo|zm|zone|zuerich|zw'
    rx = r'\b(?:https?|ftp|wss?):\/\/(?:[^\s\d]+\.)?[^\s\d]+(?::\d+)?(?:\/[^\s]*)?\b|\b(?:www\.)?[^\s\d]+\.(?:' + \
        root_zones+r'|[a-z]{2})(?::\d+)?(?:\/[^\s]*)?\b'
    urls = re.findall(rx, input)
    return urls

# HTML


def html_check(input):
    soup = BeautifulSoup(input, 'html.parser')
    return soup.find() is not None


# DOMAIN


def domain_extractor(site: str):
    # print(site, "=> ", end="")
    url = urlparse(site)
    domain = url.netloc
    if not domain:
        return site.replace(':', '/').split('/')[0].removeprefix('www.')
    return domain.removeprefix('www.')


def domain_age_extractor(domain: str) -> int:
    try:
        domain_info = whois.whois(domain)
        # print(domain_info)
        creation_date = domain_info.creation_date
        if isinstance(creation_date, str):
            return None

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            return (datetime.now() - creation_date).days
        return None

    except whois.parser.PywhoisError:
        print(f"Error retrieving WHOIS information for {domain}.")
        return None


def DNS_record_extractor(domain: str, entry_type):
    try:
        return {entry_type: [str(ans) for ans in dns.resolver.resolve(domain, entry_type)]}
    except dns.resolver.NXDOMAIN:
        return {entry_type: f"Domain {domain} does not exist."}
    except dns.resolver.NoAnswer:
        return {entry_type: f"No {entry_type} records found for {domain}."}
    except dns.resolver.NoNameservers:
        return {entry_type: f"No nameservers found for {domain}."}


def all_DNS_record_extractor(domain):
    dns_entries = [
        "A",
        "AAAA",
        "CNAME",
        "MX",
        "NS",
        "PTR",
        "SOA",
        "SPF",
        "TXT"
    ]
    try:
        dns.resolver.resolve(domain, 'A')
    except dns.resolver.NXDOMAIN:
        return {f"Domain {domain} does not exist."}
    with concurrent.futures.ThreadPoolExecutor() as exec:
        return exec.map(lambda dns_entry: DNS_record_extractor(domain, dns_entry), dns_entries)

# TODO: find a reliable way to check the domain reputation/report status


def domain_rep_extractor(domain: str) -> float:

    try:
        res = pydnsbl.DNSBLDomainChecker().check(domain)
        return str(res)
    except ValueError as ve:
        print(f"ERROR: Invalid data ({ve})")

# DMARC, DKIM, SPF


def DMARC_extractor(domain: str) -> (str, int):
    try:
        response = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
        for data in response:
            if 'DMARC1' in str(data):
                return f"{data}", 1
        return 'DMARC not found', 0
    except:
        return 'DMARC not found', -1


def DKIM_extractor(domain: str, selector: str) -> (str, int):
    try:
        response = dns.resolver.resolve(
            selector + '._domainkey.' + domain, 'TXT')
        for data in response:
            if 'DKIM1' in str(data):
                return f"{data}", 1
        return 'DKIM not found', 0
    except:
        return 'DKIM not found', -1


def SPF_extractor(domain: str) -> (str, int):
    try:
        response = dns.resolver.resolve(domain, 'TXT')
        for data in response:
            if 'spf1' in str(data):
                return f"{data}", 1
        return 'SPF not found', 0
    except:
        return 'SPF not found', -1

# HEADER


def header_check_filter(mail, header: str, filters: list = None) -> bool:
    if mail[header] is None:
        return False
    if filters is None:
        return True
    # print(mail[header])
    return text_based_filter(mail[header], filters)


def text_based_filter(text: str, filters: list) -> bool:
    if any(re.match(regex, text) for regex in filters):
        # print(text,"In rex")
        return True
        # print(text,"In any")
    return any(fil in text for fil in filters)


# CONTENT_TYPE
def content_type_extractor(mail) -> list:
    if not mail.is_multipart():
        return [mail.get_content_type()]
    return [part.get_content_type() for part in mail.get_payload()]


# SENDER

def sender_filter(mail, filter: list) -> int:
    '''
    Return list codes:
    - 0 = Not found
    - 1 = Everything is ok. Sender found.
    - 2 = Return-Path mismatch. Sender found.
    - 3 = Reply-To mismatch. Sender found.
    '''

    if header_check_filter(mail, "From", filter):
        fr = email.utils.parseaddr(mail['From'])
        # print(fr[1], mail['Return-Path'], mail['Replay-To'])
        if mail['Return-Path'] and fr[1] != mail['Return-Path']:
            return 2
        if mail['Reply-To'] and fr[1] != mail['Reply-To']:
            return 3
        return 1
    return 0

# RECV


def tocc_filter(mail, filter: list) -> bool:
    return header_check_filter(mail, "Cc", filter) | header_check_filter(mail, "To", filter)

# LANGUAGE
# TODO: Insert at start of API async load


__detector = None


def text_language_extractor(text):
    global __detector
    if not __detector:
        __detector = LanguageDetectorBuilder.from_all_languages(
        ).with_preloaded_language_models().build()
    if isinstance(text, list):
        return __detector.detect_languages_in_parallel_of(text)
    return __detector.detect_language_of(str(text))


def text_language_filter(text, filter: Language) -> bool:
    global __detector
    if not __detector:
        __detector = LanguageDetectorBuilder.from_all_languages(
        ).with_preloaded_language_models().build()
    if isinstance(text, list):
        for response in text_language_extractor(text):
            if response == filter:
                return True
    elif text_language_extractor(text) == filter:
        return True
    return False

# SUBJECT


def subject_extractor(mail: email.message.Message) -> str:
    if mail['subject'] is None:
        return '<WARNING: NO_SUBJECT>'
    subject = email.header.decode_header(mail['subject'])[0][0]
    if not isinstance(subject, str):
        return subject.decode()
    return subject


def subject_filter(mail: email.message.Message, filter: list) -> bool:
    if subject_extractor(mail) == '<WARNING: NO_SUBJECT>':
        return False
    return text_based_filter(subject_extractor(mail), filter)


# IMAGES

def image_text_extractor(mail: email.message.Message)->list:
    images = []
    for part in mail.walk():
        if part.get_content_maintype() == 'image':
            data = part.get_payload(decode=True)
            try:
                image = Image.open(io.BytesIO(data))
                images.append(image)
            except Exception as e:
                print('Error on image proccesing:', e)
    extracted_text = []
    for idx, image in enumerate(images):
        try:
            text = pytesseract.image_to_string(image)
            extracted_text.append(text)
        except Exception as e:
            print("Error on character detection:", e)
    return extracted_text