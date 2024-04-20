import mysql.connector
from mysql.connector import Error


log = None

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
            )
        print("Connection to MySQL DB successful")
    
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
    return connection

def user_reg(login, passwd):
    con = create_connection("a0947494.xsph.ru", "a0947494_teams", "HzqIAQEc", "a0947494_teams")
    cursor = con.cursor()
    query = "SELECT login FROM User_reg WHERE login = (%s)"
    cursor.execute(query,(login, ))
    res = cursor.fetchall()
    print(res)
    if len(res) == 0:
        # cursor.execute('INSERT INTO User_reg (login, password) VALUES (?, ?)', (login, passwd))
        query = "INSERT INTO User_reg (login, password) VALUES (%s, %s)"
        cursor.execute(query,(login, passwd, ))
        print(f"successful registred user ({login}, {passwd})")
        con.commit()
        con.close()
        log = login
        return True
    else:
        print("login alredy used")
        con.close()
        return False

def sign_in(login, passwd):
    con = create_connection("a0947494.xsph.ru", "a0947494_teams", "HzqIAQEc", "a0947494_teams")
    cursor = con.cursor()
    # cursor.execute('SELECT login, password FROM User_reg WHERE login = ? AND password = ?', (login, passwd))
    query = "SELECT login, password FROM User_reg WHERE login = %s AND password = %s"
    cursor.execute(query,(login, passwd))
    res = cursor.fetchall()
    print(res)
    if len(res) == 1:
        con.close()
        log = login
        print("Log in successful")
        return True
    else:
        con.close()
        print("log in failed")
        return False

def team_reg(name, mail, login, passwd, mem_list):
    con = create_connection("a0947494.xsph.ru", "a0947494_teams", "HzqIAQEc", "a0947494_teams")
    cursor = con.cursor()
    query = "SELECT login FROM User_reg WHERE login = (%s)"
    cursor.execute(query,(login, ))
    res1 = cursor.fetchall()
    print(res1)
    query = "SELECT Team_name FROM User_reg WHERE Team_name = (%s)"
    cursor.execute(query,(name, ))
    res2 = cursor.fetchall()
    print(res2)
    if len(res1) == 0 and len(res2) == 0:
        er = False
        for x in mem_list[0]:
            if mem_list[0].count(x) > 1:
                er = True
        if er == False:
            for j in range(len(mem_list[0])):
                query = "SELECT Member_name FROM Member_list WHERE Member_name = (%s) AND Team_name = (%s)"
                cursor.execute(query,(mem_list[0][j], name))
                print(mem_list[0][j])
                res = cursor.fetchall()
                print(res)
                if len(res) == 0:
                    mem_reg(mem_list[0][j], mem_list[1][j], name)
                else: er = True 
            if er == False:
                user_reg(login, passwd)
                # cursor.execute('INSERT INTO User_reg (login, password) VALUES (?, ?)', (login, passwd))
                query = "UPDATE User_reg SET Team_name = %s WHERE login = %s"
                cursor.execute(query,(name, login))
                query = "UPDATE User_reg SET Team_mail = %s WHERE login = %s"
                cursor.execute(query,(mail, login))
                print(f"successful registred team ({name}, {mail})")
                con.commit()
                con.close()
                return True
            else:
                print("mem alredy used")
                con.close()
                return False

def mem_reg(name, desc, team_name):
    con = create_connection("a0947494.xsph.ru", "a0947494_teams", "HzqIAQEc", "a0947494_teams")
    cursor = con.cursor()
    query = "SELECT Member_name FROM Member_list WHERE Member_name = (%s) AND Team_name = (%s)"
    cursor.execute(query,(name, team_name))
    res = cursor.fetchall()
    print(res)
    if len(res) == 0:
        # cursor.execute('INSERT INTO User_reg (login, password) VALUES (?, ?)', (login, passwd))
        query = "INSERT INTO Member_list (Member_name, Member_desc, Team_name) VALUES (%s, %s, %s)"
        cursor.execute(query,(name, desc, team_name ))
        print(f"successful registred Member ({name}, {team_name})")
        con.commit()
        con.close()
        return True
    else:
        print("member alredy used")
        con.close()
        return False
test_ar = [["test", "test"],["test", "test"]]
team_reg("test", "test", "test", "test", test_ar)