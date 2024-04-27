def searcher():
    import  time
    #some 4 sec time consuming taske
    book="this is a book on harry and code with dfsdhgfsjhfkjdsfklwc wgfr"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text in book")
        else:
            print("your text is not in book")

search=searcher()
print("srach started")
next(search)
print("next methode search")
search.send("harry")
search.close()