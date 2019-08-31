import logging
import threading
import time
import mysql.connector
import Comment


def thread_function(product_id):
    Comment.find_comment_by_id(product_id)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="web_crawler"
    )

    mycursor = mydb.cursor()
    sql = "select * from products"
    mycursor.execute(sql)
    res = mycursor.fetchall()

    threads = list()
    for val in res:

        logging.info(val)
        x = threading.Thread(target=thread_function, args=(val[1],))
        threads.append(x)
        x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     logging.info(thread)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)
