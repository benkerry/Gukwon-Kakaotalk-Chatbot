import smtplib
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, str_email:str, str_password:str, str_smtp_name:str, smtp_port:int):
        self.str_email = str_email
        self.str_password = str_password
        self.str_smtp_name = str_smtp_name
        self.smtp_port = smtp_port

    def send(self, str_title:str, str_description:str, lst_to:list):
        msg = MIMEText(str_description)
        msg['Subject'] = str_title
        msg['From'] = self.str_email

        if len(lst_to) == 1:
            msg['To'] = lst_to[0]
        else:
            msg['To'] = ",".join(lst_to)

        smtp = smtplib.SMTP(self.str_smtp_name, self.smtp_port)
        smtp.starttls()
        smtp.login(self.str_email, self.str_password)
        smtp.sendmail(self.str_email, lst_to, msg.as_string())

        smtp.quit()

    def send_passed_issues(self, db_manager, lst_passed:list):
        str_sql = "SELECT email FROM sign_info"
        cursor = db_manager.mysql_query(str_sql)

        lst_destination = []

        for i in cursor:
            lst_destination.append(i[0])

        for i in lst_passed:
            self.send(
                str_title = "#{0}번 건의가 통과되었습니다!".format(i[0]),
                str_description = i[1] + '\n\n\n' + '[링크]', ### 링크 추가할 것
                lst_to = lst_destination
            )

    def send_error_message(self, e:Exception, str_error:str):
        self.send("[Error Report]: " + str(e), str_error, ["developer_kerry@kakao.com"])