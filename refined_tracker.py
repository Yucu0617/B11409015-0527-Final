import os
import json

class LibraryManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.library_data = []

    def load_library_data(self):
        if not os.path.exists(self.file_name):
            print(f"檔案 {self.file_name} 不存在，無法載入資料，將初始化為空資料。")
            self.library_data = []  # 初始化為空資料
            return
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:  # 檢查檔案是否為空
                    print(f"檔案 {self.file_name} 為空，將初始化為空資料。")
                    self.library_data = []  # 初始化為空資料
                else:
                    self.library_data = json.loads(content)  # 嘗試解析 JSON
        except json.JSONDecodeError:
            print(f"檔案 {self.file_name} 的內容不是有效的 JSON 格式，將初始化為空資料。")
            self.library_data = []  # 初始化為空資料

    def save_library_data(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.library_data, file, ensure_ascii=False, indent=4)  # 使用 JSON 儲存資料

    def is_isbn_exist(self, isbn):
        return any(book['i'] == isbn for book in self.library_data)

    def borrow_book(self, isbn):
        for book in self.library_data:
            if book['i'] == isbn:
                if book['s'] != "borrowed":
                    book['s'] = "borrowed"
                    print("Updated")
                else:
                    print("Book already borrowed")
                return
        print("Book not found")

    def show_books(self):
        if not self.library_data:
            print("No books available")
        else:
            for book in self.library_data:
                print(f"書名: {book['t']}, ISBN: {book['i']}, 狀態: {book['s']}")

# 主程式
def main():
    manager = LibraryManager("books.json")  # 修改為 JSON 檔案
    manager.load_library_data()
    print("=== 圖書管理系統 v0.1 ===")
    
    while True:
        op = input("> ").strip()
        if op == "exit":
            manager.save_library_data()
            print("系統關閉")
            break
        elif op.startswith("add "):
            raw = op[4:].split("/")
            if len(raw) == 3:
                if not manager.is_isbn_exist(raw[1]):
                    manager.library_data.append({"t": raw[0], "i": raw[1], "s": raw[2]})
                    print("Success")
                else:
                    print("ISBN Exist")
            else:
                print("Format Error")
        elif op.startswith("borrow "):
            isbn = op[7:]
            manager.borrow_book(isbn)
        elif op == "show":
            manager.show_books()
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()