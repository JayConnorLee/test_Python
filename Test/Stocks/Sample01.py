import pythoncom
import win32com.client as winAPI
import datetime

STAND_BY = 0
RECEIVED = 1


class XASessionEvents:

    login_state = STAND_BY

    def OnLogin(self, code, msg):
        XASessionEvents.login_state = RECEIVED
        print(msg)

    def OnDisconnect(self, code, msg):
        pass


class XAQueryEvents:
    query_state = STAND_BY

    def OnReceiveData(self, code):
        XAQueryEvents.query_state = RECEIVED

    def OnReceiveMessage(self, error, nMessageCode, szMessage):
        print(szMessage)


    SERVER_PORT = 20001
    SHOW_CERTIFICATE_ERROR_DIALOG = False
    REPEATED_DATA_QUERY = 1
    TRANSACTION_REQUEST_EXCESS = -21
    TODAY = datetime.datetime.now().strftime('%Y%m%d')

    if __name__ == "__main__":
        id = "아이디"
        password = "비밀번호"
        certificate_password = "공인인증서_비밀번호"
        xa_session = winAPI.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
        if xa_session.IsConnected() is True:
            xa_session.DisconnectServer()

    # demo.ebestsec.co.kr => 모의투자
    # hts.ebestsec.co.kr => 실투자
    xa_session.ConnectServer("hts.ebestsec.co.kr", SERVER_PORT)
    xa_session.Login(id, password, certificate_password, SERVER_PORT, SHOW_CERTIFICATE_ERROR_DIALOG)

    while XASessionEvents.login_state is STAND_BY:
        pythoncom.PumpWaitingMessages()
        XASessionEvents.login_state = STAND_BY

