from socket import *
import smtplib


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    # print('1\r\n')
    if recv[:3] != '220':
        pass
        # print('220 reply not received from server.')

    # Send HELO command and print server response.
    helocommand = 'HELO Alice\r\n'
    clientSocket.send(helocommand.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv1)
    # print('2\r\n')
    if recv[:3] != '250':
        pass
        # print('250 reply not received from server.')


    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfrom = 'Mail From: <sr5864@nyu.edu>\r\n'
    clientSocket.send(mailfrom.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv2)
    # print('3\r\n')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptto = 'RCPT TO: <sr5864@nyu.edu>\r\n'
    clientSocket.send(rcptto.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv3)
    # print('4\r\n')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = 'Data\r\n'
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv4)
    # print('5\r\n')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # print('6\r\n')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # print('7\r\n')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit = 'Quit\r\n'
    clientSocket.send(quit.encode())
    recv = clientSocket.recv(1024).decode()
    # print(recv5)
    # print('8\r\n')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
