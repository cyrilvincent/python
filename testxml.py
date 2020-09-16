import xml.dom.minidom as dom

doc = dom.parse("data/books.xml")
nodes = doc.getElementsByTagName("book")
for node in nodes:
    print(node.getAttribute("title"))
book_node = doc.createElement("book")
book_node.setAttribute("id","99")
book_node.setAttribute("title","XML")
book_node.setAttribute("price","10")
doc.documentElement.appendChild(book_node)
with open("data/books_new.xml","w") as f:
    doc.writexml(f)

