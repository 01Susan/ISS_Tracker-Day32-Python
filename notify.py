import smtplib

# Sender information
my_email = "kunalbhatiya06@gmail.com"
password = "wzzmlwyjynuldzec"


# establish connection
def iss_notification(notification):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # secure connection by using starttls
        connection.starttls()
        # login in the connection
        connection.login(my_email, password)
        # send email
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dhitalsusan2@gmail.com",
            msg=f"Subject:iss overhead\n\n{notification}"
        )
