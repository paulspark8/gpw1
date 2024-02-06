from filter_check import *


test_strings = ['add1 http://mit.edu.com abc',
                'add2 https://facebook.jp.com.2. abc',
                'add3 www.google.be. uvw',
                'add4 https://www.google.be. 123',
                'add5 www.website.gov.us test2',
                'Hey bob on www.test.com.',
                'another tgoogle.comest with ipv4 http://192.168.1.1/found/test.jpg. toto2',
                'website mta.ro with different port number www.test.com:8080/found/test.jpg not port 80',
                'www.website.gov.us/login.html',
                'test with ipv4 192.168.1.1',
                'search at google.co.jp/maps. 127.0.0.1',
                'propoziție este simplă cu ipv6 2001:0db8:0000:85a3:0000:0000:ac1f:8001/test.jpg.',
                "IPv4 addresses: wss://192.168.1.1:8080, 10.0.0.1. IPv6 addresses: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, ::1, 2001:db8::ff00:42:8329.",
                "This is 100% phishing https://share.formbold.com/3V0md and https://beachvacationhomerental.com/humid"]
mails = ["""Return-Path: paulanghel@mail.com
Received: from [192.168.134.1] (FX504GE [127.0.0.1])
	by FX504GE with ESMTP
	; Wed, 31 Jan 2024 21:32:26 +0200
Content-Type: multipart/alternative;
 boundary="------------38IptQcgf0551oL6r09Xcu9y"
Message-ID: <9fcf7300-ae21-4b8c-ad43-1ab10e859742@mail.com>
Date: Wed, 31 Jan 2024 21:32:24 +0200
MIME-Version: 1.0
User-Agent: Mozilla Thunderbird
Content-Language: en-US
To: andrei@mail.com
From: "paul.business" <paul@mail.com>
Subject: Do you have what it takes
X-Peer: 192.168.0.217

This is a multi-part message in MIME format.
--------------38IptQcgf0551oL6r09Xcu9y
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit

www.google.com

sum randmo link <192.168.0.200:43808>

GoPhish.com <mallware.it>

--------------38IptQcgf0551oL6r09Xcu9y
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: 7bit

<!DOCTYPE html>
<html>
  <head>

    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  </head>
  <body>
    <p align="center"><a class="moz-txt-link-abbreviated" href="http://www.google.com">www.google.com</a> <br>
    </p>
    <p align="center"><a moz-do-not-send="true"
        href="192.168.0.200:43808">sum randmo link</a></p>
    <p align="center"><a moz-do-not-send="true" href="mallware.it">GoPhish.com</a><br>
    </p>
  </body>
</html>

--------------38IptQcgf0551oL6r09Xcu9y--
""", """ Return-Path: paul@mail.com
Received: from [192.168.134.1] (FX504GE [127.0.0.1])
	by FX504GE with ESMTP
	; Thu, 1 Feb 2024 13:44:28 +0200
Message-ID: <db7353cd-0deb-4434-9325-6a624a105636@mail.com>
Date: Thu, 1 Feb 2024 13:44:26 +0200
MIME-Version: 1.0
User-Agent: Mozilla Thunderbird
Content-Language: en-US
To: andrei@mail.com
From: paul <paul@mail.com>
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit
X-Peer: 192.168.0.217

mail


""", """Content-Type: multipart/alternative;
 boundary="------------pvnyYm9X6P0pYraM4CJKPs1y"
Message-ID: <8a1a5911-5bfb-48cc-b4c1-e741d320499b@mail.com>
Date: Mon, 5 Feb 2024 10:49:16 +0200
MIME-Version: 1.0
User-Agent: Mozilla Thunderbird
Subject: Re: Something
Content-Language: en-US
From: paul <paul@mail.com>
To: andrei@mail.com
Cc: gelu@somemail.ro, andrei@mail.com
Reply-To: andrei@mail.com
References: <f99a0f9e-e067-4025-a1d4-4f816ccd4294@mail.com>
In-Reply-To: <f99a0f9e-e067-4025-a1d4-4f816ccd4294@mail.com>
X-Peer: 10.10.120.6

This is a multi-part message in MIME format.
--------------pvnyYm9X6P0pYraM4CJKPs1y
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit


On 05/02/2024 10:06 am, paul wrote:
>
> I have some info: *hello*
>
--------------pvnyYm9X6P0pYraM4CJKPs1y
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: 7bit

<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  </head>
  <body>
    <p><br>
    </p>
    <div class="moz-cite-prefix">On 05/02/2024 10:06 am, paul wrote:<br>
    </div>
    <blockquote type="cite"
      cite="mid:f99a0f9e-e067-4025-a1d4-4f816ccd4294@mail.com">
      <meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <p>I have some info: <b>hello</b><br>
      </p>
    </blockquote>
  </body>
</html>

--------------pvnyYm9X6P0pYraM4CJKPs1y--""", """From jose@monkey.org Tue Feb 15 19:08:55 2022 +0000
Return-Path: arnazom@lptaoyou.cn
Delivered-To: jose@monkey.org
X-FDA: 79145951430.25.7395303
Received: from lptaoyou.cn (lptaoyou.cn [194.147.87.116])
	by imf19.b.hostedemail.com (Postfix) with ESMTP id 4E13D1003C623
	for <jose@monkey.org>; Tue, 15 Feb 2022 19:08:51 +0000 (UTC)
Received: from qEP.amazon (unknown [175.42.87.23])
	by lptaoyou.cn (Postfix) with ESMTPA id 110B5AB7FD
	for <jose@monkey.org>; Wed, 16 Feb 2022 03:08:08 +0800 (CST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=lptaoyou.cn; s=default;
	t=1644952089;
	h=from:from:reply-to:subject:subject:date:date:message-id:message-id:
	 to:to:cc:mime-version:mime-version:content-type:content-type;
	bh=QUn5XNs6vb20lndjHBCWDS0can4+lmoLQIdMhPnMs/4=;
	b=X81DshZG1ErAIAHqGtreZbxY2HfSkHM2hnNSVwJIqoNI4rMuaB/clhys9py7hSFVKRGSwT
	5yqprCLAiMsHdmE9AiTksO/jrFHJRyZ/vLsL8GmIyiv2FlsSClmtklOWHyeoGmgQrbVjKQ
	jeqbJP73dfwza0x2To6z3xHKQ7b9VZE=
Message-ID: <20220216040811221877@lptaoyou.cn>
From: "Amazon.co.jp" <arnazom@lptaoyou.cn>
To: <jose@monkey.org>
Subject: =?utf-8?B?44GC44Gq44Gf44Gu44Ki44Kr44Km44Oz44OI44Gv5YGc5q2i44GV44KM44G+44GX44Gf?=
Date: Wed, 16 Feb 2022 04:08:03 +0900
MIME-Version: 1.0
Content-Type: multipart/alternative;
	boundary="----=_NextPart_000_0ADE_01FE4E5E.14DC5550"
X-Priority: 1
X-mailer: Fkfl 6
X-Spam-Status: No, score=8.40
X-Rspam-User: 
X-Rspamd-Queue-Id: 4E13D1003C623
X-Stat-Signature: kf49xn3sjnqiojiuhn4j3axbedorszx4
Authentication-Results: imf19.b.hostedemail.com;
	dkim=pass header.d=lptaoyou.cn header.s=default header.b=X81DshZG;
	spf=pass (imf19.b.hostedemail.com: domain of arnazom@lptaoyou.cn designates 194.147.87.116 as permitted sender) smtp.mailfrom=arnazom@lptaoyou.cn;
	dmarc=pass (policy=quarantine) header.from=lptaoyou.cn
X-Rspamd-Server: rspam08
X-HE-Tag: 1644952131-199432
Status: RO
X-Status: 
X-Keywords:                 
X-UID: 14

This is a multi-part message in MIME format.

------=_NextPart_000_0ADE_01FE4E5E.14DC5550
Content-Type: text/plain;
	charset="utf-8"
Content-Transfer-Encoding: base64

IOOBguOBquOBn+OBruOCouOCq+OCpuODs+ODiOOBr+WBnOatouOBleOCjOOBvuOBl+OBnw0KDQog
DQrmlrDjgZfjgYTjg4fjg5DjgqTjgrnjgYvjgonjgqLjgqvjgqbjg7Pjg4jjgrXjg7zjg5Pjgrnj
gbjjga7jgrXjgqTjg7PjgqTjg7PjgYzmpJzlh7rjgZXjgozjgb7jgZfjgZ/jgIINCuiqsOOBi+OB
jOOBguOBquOBn+OBrkFtYXpvbuOCouOCq+OCpuODs+ODiOOBp+S7luOBruODh+ODkOOCpOOCueOB
i+OCieizvOWFpeOBl+OCiOOBhuOBqOOBl+OBvuOBl+OBn+OAgkFtYXpvbuOBruS/neitt+OBq+OB
iuOBkeOCi+OCu+OCreODpeODquODhuOCo+OBqOaVtOWQiOaAp+OBruWVj+mhjOOBq+OCiOOCiuOA
geOCu+OCreODpeODquODhuOCo+S4iuOBrueQhueUseOBi+OCieOCouOCq+OCpuODs+ODiOOBjOOD
reODg+OCr+OBleOCjOOBvuOBmeOAgg0K44Ki44Kr44Km44Oz44OI44KS5byV44GN57aa44GN5L2/
55So44GZ44KL44Gr44Gv44CBMjTmmYLplpPliY3jgavmg4XloLHjgpLmm7TmlrDjgZnjgovjgZPj
gajjgpLjgYrli6fjgoHjgZfjgb7jgZnjgILjgZ3jgozku6XlpJbjga7loLTlkIjjgIHjgYLjgarj
gZ/jga7jgqLjgqvjgqbjg7Pjg4jjga/msLjkuYXjg63jg4Pjgq/jgIIgDQoNCueiuuiqjeeUqOOC
ouOCq+OCpuODs+ODiCANCg0KDQoNCg0KDQoNCsKpIDIwMjIgQW1hem9uLmNvbSwgSW5jLiBvciBp
dHMgYWZmaWxpYXRlcy4gQWxsIHJpZ2h0cyByZXNlcnZlZC4gQW1hem9uLCBBbWF6b24uY28uanAs
IEFtYXpvbiBQcmltZSwgUHJpbWUg44GK44KI44GzQW1hem9uLmNvLmpwIOOBruODreOCtOOBryBB
bWF6b24uY29tICwgSW5jLuOBvuOBn+OBr+OBneOBrumWoumAo+S8muekvuOBruWVhuaomeOBp+OB
meOAgiBBbWF6b24uY29tLCA0MTAgVGVycnkgQXZlbnVlIE4uLCBTZWF0dGxlLCBXQSA5ODEwOS01
MjEwIA==

------=_NextPart_000_0ADE_01FE4E5E.14DC5550
Content-Type: text/html;
	charset="utf-8"
Content-Transfer-Encoding: base64

PCFET0NUWVBFIEhUTUwgUFVCTElDICItLy9XM0MvL0RURCBIVE1MIDQuMCBUcmFuc2l0aW9uYWwv
L0VOIj4NCjxIVE1MPjxIRUFEPg0KPE1FVEEgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PXV0
Zi04IiBodHRwLWVxdWl2PUNvbnRlbnQtVHlwZT4NCjxNRVRBIG5hbWU9R0VORVJBVE9SIGNvbnRl
bnQ9Ik1TSFRNTCAxMS4wMC45NjAwLjE5NTk3Ij48L0hFQUQ+DQo8Qk9EWT4NCjxUQUJMRSBzdHls
ZT0iUEFERElORy1CT1RUT006IDIwcHgiIGNlbGxTcGFjaW5nPTAgY2VsbFBhZGRpbmc9MCB3aWR0
aD01NTAgDQphbGlnbj1jZW50ZXI+DQogIDxUQk9EWT4NCiAgPFRSPg0KICAgIDxURD4NCiAgICAg
IDxUQUJMRSBzdHlsZT0iTUFSR0lOOiAwcHggMjBweCIgY2VsbFNwYWNpbmc9MCBjZWxsUGFkZGlu
Zz0wIHdpZHRoPTU1MD4NCiAgICAgICAgPFRCT0RZPg0KICAgICAgICA8VFIgd2lkdGg9IjU1MCI+
DQogICAgICAgICAgPFREIHN0eWxlPSJCT1JERVItQk9UVE9NOiAjZWFlYWVhIDFweCBzb2xpZDsg
UEFERElORy1UT1A6IDEwcHgiIA0KICAgICAgICAgIGhlaWdodD01MiB3aWR0aD01NTA+DQogICAg
ICAgICAgICA8VEFCTEU+DQogICAgICAgICAgICAgIDxUQk9EWT4NCiAgICAgICAgICAgICAgPFRS
IHdpZHRoPSI1NTAiPg0KICAgICAgICAgICAgICAgIDxURCB3aWR0aD0xMDA+PElNRyBhbHQ9IkFt
YXpvbiBMb2dvIEltYWdlIiANCiAgICAgICAgICAgICAgICAgIHNyYz0iaHR0cHM6Ly9tLm1lZGlh
LWFtYXpvbi5jb20vaW1hZ2VzL0cvMDEvYXV0aHBvcnRhbC90aXYvYW1hem9uX2xvZ29fUkdCLl9D
QjQyNDg4NzgyMF8ucG5nIiANCiAgICAgICAgICAgICAgICAgIHdpZHRoPTkzIGhlaWdodD0yNz4g
PC9URD4NCiAgICAgICAgICAgICAgICA8VEQgDQogICAgICAgICAgICAgICAgc3R5bGU9IkZPTlQt
U0laRTogMjJweDsgRk9OVC1GQU1JTFk6ICdBbWF6b24gRW1iZXInLEFyaWFsLHNhbnMtc2VyaWY7
IFBBRERJTkctQk9UVE9NOiAxMHB4OyBURVhULUFMSUdOOiByaWdodDsgUEFERElORy1UT1A6IDJw
eDsgUEFERElORy1MRUZUOiAwcHg7IFBBRERJTkctUklHSFQ6IDBweCIgDQogICAgICAgICAgICAg
ICAgd2lkdGg9NDIwPg0KICAgICAgICAgICAgICAgICAgPFA+44GC44Gq44Gf44Gu44Ki44Kr44Km
44Oz44OI44Gv5YGc5q2i44GV44KM44G+44GX44GfPC9QPjwvVEQ+PC9UUj48L1RCT0RZPjwvVEFC
TEU+PC9URD48L1RSPg0KICAgICAgICA8VFI+DQogICAgICAgICAgPFREIHN0eWxlPSJURVhULUFM
SUdOOiBjZW50ZXIiIGNvbFNwYW49MiBhbGlnbj1jZW50ZXI+DQogICAgICAgICAgICA8RElWIHN0
eWxlPSJURVhULUFMSUdOOiBjZW50ZXIgIWltcG9ydGFudCI+PElNRyANCiAgICAgICAgICAgIHN0
eWxlPSJNQVgtV0lEVEg6IDEwMCU7IEJPUkRFUi1UT1A6IDBweDsgSEVJR0hUOiA0NSU7IEJPUkRF
Ui1SSUdIVDogMHB4OyBXSURUSDogNTAlOyBWRVJUSUNBTC1BTElHTjogdG9wOyBCT1JERVItQk9U
VE9NOiAwcHg7IEJPUkRFUi1MRUZUOiAwcHg7IE1BUkdJTi1UT1A6IDIwcHgiIA0KICAgICAgICAg
ICAgYWx0PSJBbWF6b24gTG9nbyBJbWFnZSIgDQogICAgICAgICAgICBzcmM9Imh0dHBzOi8vbS5t
ZWRpYS1hbWF6b24uY29tL2ltYWdlcy9HLzAxL0lTL1RJVi8zeDF0ZXNhMjgyY2ZnMGcucG5nIiAN
CiAgICAgICAgICAgIHdpZHRoPSI2MCUiIGhlaWdodD0iNjAlIj4gPC9ESVY+PC9URD48L1RSPg0K
ICAgICAgICA8VFI+DQogICAgICAgICAgPFREIA0KICAgICAgICAgIHN0eWxlPSJGT05ULVNJWkU6
IDE3cHg7IEZPTlQtRkFNSUxZOiAnQW1hem9uIEVtYmVyJyxBcmlhbCxzYW5zLXNlcmlmOyBQQURE
SU5HLUJPVFRPTTogMTBweDsgVEVYVC1BTElHTjogbGVmdDsgUEFERElORy1UT1A6IDI1cHgiIA0K
ICAgICAgICAgIGNvbFNwYW49MiBhbGlnbj1sZWZ0Pg0KICAgICAgICAgICAgPFA+5paw44GX44GE
44OH44OQ44Kk44K544GL44KJ44Ki44Kr44Km44Oz44OI44K144O844OT44K544G444Gu44K144Kk
44Oz44Kk44Oz44GM5qSc5Ye644GV44KM44G+44GX44Gf44CCPC9QPjwvVEQ+PC9UUj4NCiAgICAg
ICAgPFRSPg0KICAgICAgICAgIDxURCANCiAgICAgICAgICBzdHlsZT0iRk9OVC1TSVpFOiAxN3B4
OyBGT05ULUZBTUlMWTogJ0FtYXpvbiBFbWJlcicsQXJpYWwsc2Fucy1zZXJpZjsgUEFERElORy1C
T1RUT006IDEwcHg7IFRFWFQtQUxJR046IGxlZnQ7IFBBRERJTkctVE9QOiAyNXB4IiANCiAgICAg
ICAgICBjb2xTcGFuPTIgYWxpZ249bGVmdD4NCiAgICAgICAgICAgIDxQPuiqsOOBi+OBjOOBguOB
quOBn+OBrkFtYXpvbuOCouOCq+OCpuODs+ODiOOBp+S7luOBruODh+ODkOOCpOOCueOBi+OCieiz
vOWFpeOBl+OCiOOBhuOBqOOBl+OBvuOBl+OBn+OAgkFtYXpvbuOBruS/neitt+OBq+OBiuOBkeOC
i+OCu+OCreODpeODquODhuOCo+OBqOaVtOWQiOaAp+OBruWVj+mhjOOBq+OCiOOCiuOAgeOCu+OC
reODpeODquODhuOCo+S4iuOBrueQhueUseOBi+OCieOCouOCq+OCpuODs+ODiOOBjOODreODg+OC
r+OBleOCjOOBvuOBmeOAgjwvUD48L1REPjwvVFI+DQogICAgICAgIDxUUj4NCiAgICAgICAgICA8
VEQgDQogICAgICAgICAgc3R5bGU9IkZPTlQtU0laRTogMTdweDsgRk9OVC1GQU1JTFk6ICdBbWF6
b24gRW1iZXInLEFyaWFsLHNhbnMtc2VyaWY7IFBBRERJTkctQk9UVE9NOiAxMHB4OyBURVhULUFM
SUdOOiBsZWZ0OyBQQURESU5HLVRPUDogMjVweCIgDQogICAgICAgICAgY29sU3Bhbj0yIGFsaWdu
PWxlZnQ+DQogICAgICAgICAgICA8UD7jgqLjgqvjgqbjg7Pjg4jjgpLlvJXjgY3ntprjgY3kvb/n
lKjjgZnjgovjgavjga/jgIEyNOaZgumWk+WJjeOBq+aDheWgseOCkuabtOaWsOOBmeOCi+OBk+OB
qOOCkuOBiuWLp+OCgeOBl+OBvuOBmeOAguOBneOCjOS7peWkluOBruWgtOWQiOOAgeOBguOBquOB
n+OBruOCouOCq+OCpuODs+ODiOOBrzxTUEFOIA0KICAgICAgICAgICAgc3R5bGU9IkZPTlQtV0VJ
R0hUOiBib2xkIj7msLjkuYXjg63jg4Pjgq/jgII8L1NQQU4+IDwvUD48L1REPjwvVFI+DQogICAg
ICAgIDxUUj4NCiAgICAgICAgICA8VEQgdkFsaWduPXRvcCBhbGlnbj1sZWZ0Pg0KICAgICAgICAg
ICAgPERJViBhbGlnbj1jZW50ZXI+PEJSPg0KICAgICAgICAgICAgPFRBQkxFIA0KICAgICAgICAg
ICAgc3R5bGU9IkJPUkRFUi1UT1A6IDFweDsgQk9SREVSLVJJR0hUOiAxcHg7IEJPUkRFUi1DT0xM
QVBTRTogc2VwYXJhdGUgIWltcG9ydGFudDsgQk9SREVSLUJPVFRPTTogMXB4OyBCT1JERVItTEVG
VDogMXB4OyBCQUNLR1JPVU5ELUNPTE9SOiAjZmZhNzIzOyBib3JkZXItcmFkaXVzOiA1cHgiIA0K
ICAgICAgICAgICAgY2VsbFNwYWNpbmc9MCBjZWxsUGFkZGluZz0wIGFsaWduPWNlbnRlciBib3Jk
ZXI9MD4NCiAgICAgICAgICAgICAgPFRCT0RZPg0KICAgICAgICAgICAgICA8VFI+DQogICAgICAg
ICAgICAgICAgPFREIA0KICAgICAgICAgICAgICAgIHN0eWxlPSJGT05ULVNJWkU6IDE2cHg7IEZP
TlQtRkFNSUxZOiBBcmlhbDsgUEFERElORy1CT1RUT006IDE1cHg7IFBBRERJTkctVE9QOiAxNXB4
OyBQQURESU5HLUxFRlQ6IDI1cHg7IFBBRERJTkctUklHSFQ6IDI1cHgiIA0KICAgICAgICAgICAg
ICAgIHZBbGlnbj1taWRkbGUgYWxpZ249Y2VudGVyPjxBIA0KICAgICAgICAgICAgICAgICAgc3R5
bGU9IlRFWFQtREVDT1JBVElPTjogbm9uZTsgRk9OVC1XRUlHSFQ6IGJvbGQ7IENPTE9SOiAjZmZm
ZmZmOyBURVhULUFMSUdOOiBjZW50ZXI7IExFVFRFUi1TUEFDSU5HOiBub3JtYWw7IExJTkUtSEVJ
R0hUOiAxMDAlIiANCiAgICAgICAgICAgICAgICAgIGhyZWY9Imh0dHBzOi8vd3d3LmFybmF6b24u
Y2VwdG4uY24vIiByZWw9bm9vcGVuZXIgDQogICAgICAgICAgICAgICAgICB0YXJnZXQ9X2JsYW5r
PueiuuiqjeeUqOOCouOCq+OCpuODs+ODiDwvQT4gDQogICAgICAgIDwvVEQ+PC9UUj48L1RCT0RZ
PjwvVEFCTEU+PC9ESVY+PC9URD48L1RSPjwvVEJPRFk+PC9UQUJMRT48L1REPjwvVFI+DQogIDxU
Uj4NCiAgICA8VEQgc3R5bGU9IkJPUkRFUi1CT1RUT006ICNlYWVhZWEgMXB4IHNvbGlkOyBQQURE
SU5HLVRPUDogMjBweCIgd2lkdGg9NjAwIA0KICAgIGNvbFNwYW49MiBhbGlnbj1sZWZ0PjwvVEQ+
PC9UUj4NCiAgPFRSPg0KICAgIDxURCANCiAgICBzdHlsZT0iRk9OVC1TSVpFOiAxM3B4OyBGT05U
LUZBTUlMWTogJ0FtYXpvbiBFbWJlcicsQXJpYWwsc2Fucy1zZXJpZjsgUEFERElORy1CT1RUT006
IDEwcHg7IFRFWFQtQUxJR046IGxlZnQiIA0KICAgIHdpZHRoPTYwMCBjb2xTcGFuPTIgYWxpZ249
bGVmdD48QlI+PEJSPjxCUj7CqSAyMDIyPFNQQU4+Jm5ic3A7PC9TUEFOPjxGT05UIA0KICAgICAg
c3R5bGU9IkNVUlNPUjogcG9pbnRlcjsgRk9OVC1GQU1JTFk6IEFyaWFsLCBzYW5zLXNlcmlmICFp
bXBvcnRhbnQ7IENPTE9SOiByZ2IoODUsMjYsMTM5KTsgT1VUTElORS1XSURUSDogMHB4OyBPVVRM
SU5FLVNUWUxFOiBub25lOyBMSU5FLUhFSUdIVDogMjBweDsgdGV4dC1kZWNvcmF0aW9uLWxpbmU6
IHVuZGVybGluZSIgDQogICAgICBjb2xvcj1ibHVlPjxBIA0KICAgICAgc3R5bGU9IkNVUlNPUjog
cG9pbnRlcjsgVEVYVC1ERUNPUkFUSU9OOiB1bmRlcmxpbmU7IENPTE9SOiByZ2IoMzAsODQsMTQ4
KTsgT1VUTElORS1XSURUSDogbWVkaXVtOyBPVVRMSU5FLVNUWUxFOiBub25lOyBPVVRMSU5FLUNP
TE9SOiBpbnZlcnQiIA0KICAgICAgaHJlZj0iaHR0cHM6Ly93d3cuYmFpZHUuY29tIiByZWw9bm9v
cGVuZXIgDQogICAgICB0YXJnZXQ9X2JsYW5rPkFtYXpvbi5jb208L0E+PC9GT05UPiwgSW5jLiBv
ciBpdHMgYWZmaWxpYXRlcy4gQWxsIHJpZ2h0cyANCiAgICAgIHJlc2VydmVkLiBBbWF6b24sPFNQ
QU4+Jm5ic3A7PC9TUEFOPjxTUEFOIA0KICAgICAgc3R5bGU9IkNVUlNPUjogcG9pbnRlcjsgQ09M
T1I6IHJnYigzMCw4NCwxNDgpIj48QSANCiAgICAgIHN0eWxlPSJDVVJTT1I6IHBvaW50ZXI7IFRF
WFQtREVDT1JBVElPTjogdW5kZXJsaW5lOyBDT0xPUjogcmdiKDMwLDg0LDE0OCk7IE9VVExJTkUt
V0lEVEg6IG1lZGl1bTsgT1VUTElORS1TVFlMRTogbm9uZTsgT1VUTElORS1DT0xPUjogaW52ZXJ0
IiANCiAgICAgIGhyZWY9Imh0dHBzOi8vd3d3LnlhaG9vLmNvLmpwIiByZWw9bm9vcGVuZXIgDQog
ICAgICB0YXJnZXQ9X2JsYW5rPkFtYXpvbi5jby5qcDwvQT48L1NQQU4+LCBBbWF6b24gUHJpbWUs
IFByaW1lIOOBiuOCiOOBszxTUEFOIA0KICAgICAgc3R5bGU9IkNVUlNPUjogcG9pbnRlcjsgQ09M
T1I6IHJnYigzMCw4NCwxNDgpIj48QSANCiAgICAgIHN0eWxlPSJDVVJTT1I6IHBvaW50ZXI7IFRF
WFQtREVDT1JBVElPTjogdW5kZXJsaW5lOyBDT0xPUjogcmdiKDMwLDg0LDE0OCk7IE9VVExJTkUt
V0lEVEg6IG1lZGl1bTsgT1VUTElORS1TVFlMRTogbm9uZTsgT1VUTElORS1DT0xPUjogaW52ZXJ0
IiANCiAgICAgIGhyZWY9Imh0dHA6Ly93d3cueWFob28uY28uanAiIHJlbD1ub29wZW5lciANCiAg
ICAgIHRhcmdldD1fYmxhbms+QW1hem9uLmNvLmpwPC9BPjwvU1BBTj4mbmJzcDvjga7jg63jgrTj
ga88U1BBTj4mbmJzcDs8L1NQQU4+PEZPTlQgDQogICAgICBzdHlsZT0iQ1VSU09SOiBwb2ludGVy
OyBGT05ULUZBTUlMWTogQXJpYWwsIHNhbnMtc2VyaWYgIWltcG9ydGFudDsgQ09MT1I6IHJnYig4
NSwyNiwxMzkpOyBPVVRMSU5FLVdJRFRIOiAwcHg7IE9VVExJTkUtU1RZTEU6IG5vbmU7IExJTkUt
SEVJR0hUOiAyMHB4OyB0ZXh0LWRlY29yYXRpb24tbGluZTogdW5kZXJsaW5lIiANCiAgICAgIGNv
bG9yPWJsdWU+PEEgDQogICAgICBzdHlsZT0iQ1VSU09SOiBwb2ludGVyOyBURVhULURFQ09SQVRJ
T046IHVuZGVybGluZTsgQ09MT1I6IHJnYigzMCw4NCwxNDgpOyBPVVRMSU5FLVdJRFRIOiBtZWRp
dW07IE9VVExJTkUtU1RZTEU6IG5vbmU7IE9VVExJTkUtQ09MT1I6IGludmVydCIgDQogICAgICBo
cmVmPSJodHRwOi8vd3d3LnlhaG9vLmNvLmpwIiByZWw9bm9vcGVuZXIgdGFyZ2V0PV9ibGFuaz5B
bWF6b24uY29tPC9BPjxBIA0KICAgICAgc3R5bGU9IkNVUlNPUjogcG9pbnRlcjsgVEVYVC1ERUNP
UkFUSU9OOiB1bmRlcmxpbmU7IENPTE9SOiByZ2IoMzAsODQsMTQ4KTsgT1VUTElORS1XSURUSDog
bWVkaXVtOyBPVVRMSU5FLVNUWUxFOiBub25lOyBPVVRMSU5FLUNPTE9SOiBpbnZlcnQiIA0KICAg
ICAgcmVsPW5vZm9sbG93IHRhcmdldD1fYmxhbms+Jm5ic3A7PC9BPjwvRk9OVD4sIA0KICAgICAg
SW5jLuOBvuOBn+OBr+OBneOBrumWoumAo+S8muekvuOBruWVhuaomeOBp+OBmeOAgjxTUEFOPiZu
YnNwOzwvU1BBTj48Rk9OVCANCiAgICAgIHN0eWxlPSJDVVJTT1I6IHBvaW50ZXI7IEZPTlQtRkFN
SUxZOiBBcmlhbCwgc2Fucy1zZXJpZiAhaW1wb3J0YW50OyBDT0xPUjogcmdiKDg1LDI2LDEzOSk7
IE9VVExJTkUtV0lEVEg6IDBweDsgT1VUTElORS1TVFlMRTogbm9uZTsgTElORS1IRUlHSFQ6IDIw
cHg7IHRleHQtZGVjb3JhdGlvbi1saW5lOiB1bmRlcmxpbmUiIA0KICAgICAgY29sb3I9Ymx1ZT48
QSANCiAgICAgIHN0eWxlPSJDVVJTT1I6IHBvaW50ZXI7IFRFWFQtREVDT1JBVElPTjogdW5kZXJs
aW5lOyBDT0xPUjogcmdiKDMwLDg0LDE0OCk7IE9VVExJTkUtV0lEVEg6IG1lZGl1bTsgT1VUTElO
RS1TVFlMRTogbm9uZTsgT1VUTElORS1DT0xPUjogaW52ZXJ0IiANCiAgICAgIGhyZWY9Imh0dHA6
Ly93d3cueWFob28uY28uanAiIHJlbD1ub29wZW5lciANCiAgICAgIHRhcmdldD1fYmxhbms+QW1h
em9uLmNvbTwvQT48L0ZPTlQ+LCA0MTAgVGVycnkgQXZlbnVlIE4uLCBTZWF0dGxlLCANCiAgICAg
IFdBPFNQQU4+Jm5ic3A7PC9TUEFOPjxTUEFOIA0KICAgICAgc3R5bGU9IkJPUkRFUi1CT1RUT006
IHJnYigyMDQsMjA0LDIwNCkgMXB4IGRhc2hlZDsgWi1JTkRFWDogMSIgDQogICAgICBkYXRhPSI5
ODEwOS01MjEwIiB0PSI3Ij48U1BBTiANCiAgICAgIHN0eWxlPSJCT1JERVItQk9UVE9NOiByZ2Io
MjA0LDIwNCwyMDQpIDFweCBkYXNoZWQ7IFotSU5ERVg6IDEiIA0KICAgICAgZGF0YT0iOTgxMDkt
NTIxMCIgdD0iNyI+PFNQQU4gDQogICAgICBzdHlsZT0iQk9SREVSLUJPVFRPTTogcmdiKDIwNCwy
MDQsMjA0KSAxcHggZGFzaGVkOyBaLUlOREVYOiAxIiANCiAgICAgIGRhdGE9Ijk4MTA5LTUyMTAi
IHQ9IjciPjxTUEFOIA0KICAgICAgc3R5bGU9IkJPUkRFUi1CT1RUT006IHJnYigyMDQsMjA0LDIw
NCkgMXB4IGRhc2hlZDsgWi1JTkRFWDogMSIgDQogICAgICBkYXRhPSI5ODEwOS01MjEwIiB0PSI3
Ij48U1BBTiANCiAgICAgIHN0eWxlPSJCT1JERVItQk9UVE9NOiAjY2NjIDFweCBkYXNoZWQ7IFot
SU5ERVg6IDEiIGRhdGE9Ijk4MTA5LTUyMTAiIA0KICAgICAgdD0iNyI+OTgxMDktNTIxMDwvU1BB
Tj48L1NQQU4+PC9TUEFOPjwvU1BBTj48L1NQQU4+IA0KPC9URD48L1RSPjwvVEJPRFk+PC9UQUJM
RT48L0JPRFk+PC9IVE1MPg0K

------=_NextPart_000_0ADE_01FE4E5E.14DC5550--"""]


def test_IP_extractor():
    for test in test_strings:
        print(IP_extractor(test))


def test_URL_extractor():
    for test in test_strings:
        print(URL_extractor(test))


def test_html_check():
    strings = ['<p>This is an example HTML string.</p>',
            'hello <p> hoole',
            'a<b helo potato>',
            'nothing here']
    for s in strings:
        print(html_check(s))


def test_header_check_filter():
    for mail in mails:
        ex = "X-Peer"
        nonex = "X-Authorized"
        filter = "192.168.0.217"
        filter_rex = "192.*"

        print("T", header_check_filter(email.message_from_string(mail), ex))
        print("F", header_check_filter(email.message_from_string(mail), nonex))
        print("T", header_check_filter(
            email.message_from_string(mail), ex, [filter]))
        print("T", header_check_filter(
            email.message_from_string(mail), ex, [filter_rex]))
        print("===")


def test_content_type_extractor():
    for mail in mails:
        print(content_type_extractor(email.message_from_string(mail)))


def test_DNS_domain_extractor():
    for s in test_strings:
        for site in URL_extractor(s):
            a = domain_extractor(site)
            # print(DNS_record_extractor(a, 'MX'))
            print(a)
            res = all_DNS_record_extractor(a)
            for r in res:
                print(r)


def test_domain_age():
    for s in test_strings:
        for site in URL_extractor(s):
            a = domain_extractor(site)
            print(domain_age_extractor(a))


def test_sender_filter():
    fil = [".*anghel*", "@mail.com"]

    for mail in mails:
        mail = email.message_from_string(mail)
        print(sender_filter(mail, fil))


def test_tocc_filter():
    fil = [".*anghel*", "gelu@"]

    for mail in mails:
        mail = email.message_from_string(mail)
        print(tocc_filter(mail, fil))


def test_domain_rep():
    for s in test_strings:
        for site in URL_extractor(s):
            a = domain_extractor(site)
            print(domain_rep_extractor(a))


def test_language_detect():
    for text in test_strings:
        # print(text_language_extractor(text))
        print(text_language_filter(text, Language.ROMANIAN))


def test_subject_extract():
    for mail in mails:
        mail = email.message_from_string(mail)
        print(subject_extractor(mail))


def test_subject_filter():
    filters = [".*SUBJ.*", ".*Some.*"]
    for mail in mails:
        mail = email.message_from_string(mail)
        print(subject_filter(mail, filters))


def test_DKIM_DMARC_SPF():
    for s in test_strings:
        for site in URL_extractor(s):
            a = domain_extractor(site)
            print('++++', a, '++++')
            print(DMARC_extractor(a))
            print(SPF_extractor(a))


if __name__ == "__main__":
    # test_IP_extractor()
    # test_URL_extractor()
    # test_html_check()
    # test_header_check_filter()
    # test_extract_content_type()
    # test_DNS_domain_extractor()
    # test_domain_age()
    # test_sender_filter()
    # test_tocc_filter()
    # test_domain_rep()
    # test_language_detect()
    # test_subject_extract()
    # test_subject_filter()
    # test_DKIM_DMARC_SPF()
    pass
