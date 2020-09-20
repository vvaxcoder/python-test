from Parser import ParserFromLesson34 as Parser

parser = Parser("https://www.ua-football.com/sport", "news.txt")

parser.run()

# print(parser.raw_html)
# print(parser.html)