import logging
import re
import smtplib
import email
import filter_check
from aiosmtpd.smtp import SMTP, Session, Envelope
from aiosmtpd.controller import Controller

log = logging.getLogger("mail.debug")


class Gateway:
    def __init__(self, remote_hostname: str = "127.0.0.1", remote_port: int = 25):
        self._hostname = remote_hostname
        self._port = remote_port

    async def handle_DATA(
        self, server: SMTP, session: Session, envelope: Envelope
    ) -> str:
        if isinstance(envelope.content, str):
            content = envelope.original_content
        else:
            content = envelope.content
        lines = content.splitlines(keepends=True)

        _i = 0
        ending = b"\r\n"
        for _i, line in enumerate(lines): 
            if re.compile(br"\r\n|\r|\n").match(line):
                ending = line
                break
        print(envelope.mail_from,"->",envelope.rcpt_tos)
        peer = session.peer[0].encode("ascii")
        lines.insert(_i, b"X-Peer: " + peer + ending)
        data = b''.join(lines)
        print("Analiyzing...")
        
        one_email = email.message_from_bytes(data)
        # print(filter_check.url_finder(str(one_email)))
        print(one_email)
        
        print("End of analysis")
        refused = self._deliver(envelope.mail_from, envelope.rcpt_tos, data)

        log.info("we got some refusals: %s", refused)
        return "250 OK"

    def _deliver(self, mail_from, rcpt_tos, data):
        refused = {}
        try:
            s = smtplib.SMTP()
            s.connect(self._hostname, self._port)
            try:
                refused = s.sendmail(mail_from, rcpt_tos, data)  # pytype: disable=wrong-arg-types  # noqa: E501
            finally:
                s.quit()
        except smtplib.SMTPRecipientsRefused as e:
            log.info("got SMTPRecipientsRefused")
            refused = e.recipients
        except (OSError, smtplib.SMTPException) as e:
            log.exception("got %s", e.__class__)
            # All recipients were refused.  If the exception had an associated
            # error code, use it.  Otherwise, fake it with a non-triggering
            # exception code.
            errcode = getattr(e, "smtp_code", -1)
            errmsg = getattr(e, "smtp_error", b"ignore")
            for r in rcpt_tos:
                refused[r] = (errcode, errmsg)
        return refused



def start_gateway_server(outbound_hostname:str=None, outbound_port:int=None, inbound_hostname: str=None, inbound_port: int=None):
    try:
        controller = Controller(Gateway(outbound_hostname, outbound_port), inbound_hostname, inbound_port)
        controller.start()
        print(controller.hostname, controller.port)
        
        input("Waiting messages (press enter to exit)...\n")
    except Exception as e:
        log.exception("got %s", e)
    finally:
        controller.stop()
    
start_gateway_server(outbound_port=8025,inbound_hostname='192.168.0.217',inbound_port=25)
        