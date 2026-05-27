# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B11409015  
**系級：** 資管系大一  
**姓名：** 錢宥鈞 

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) | 儲存從檔案 lib_data.txt 中讀取的所有行 | file_lines |
| Q2 d2 (in main) | 儲存所有圖書的資料 | library_data |
| Q3 c_res (in check) | 判斷某個 ISBN 是否已經存在於 d2 中 | is_isbn_exist |

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：** 缺乏資源管理，當檔案操作中斷時可能導致資源洩漏
- **Q2：** 缺乏封裝，當全域變數 d2 被多處修改時，程式狀態難以追蹤
- **Q3：** 缺乏錯誤處理，當檔案不存在或格式錯誤時，程式無法提供明確的錯誤訊息
- **Q4：** 缺乏描述性命名，當開發者閱讀函式名稱時，無法快速理解其功能
- **Q5：** 缺乏輸入驗證，當使用者輸入不符合預期格式時，可能導致程式異常

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A：請將程式中的全域變數 `d2` 封裝到一個類別中，並提供方法來操作圖書資料，例如新增、檢查 ISBN 是否存在、顯示所有圖書等功能。

Prompt B：請將程式中所有的檔案操作改為使用 `with` 語法，確保檔案在操作後能正確關閉，並處理檔案不存在的情況。

Prompt C：請將函式名稱改為更具描述性的名稱，例如 `load_proc` 改為 `load_library_data`，並在函式中加入錯誤處理邏輯，提示檔案不存在或資料格式錯誤。
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？

    Ans:是的，AI漏寫功能。在檢查程式碼時，發現檔案操作使用了 open 和 close，但未使用 with 語法。

2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)

    Ans:AI 忘記在 exit 指令執行時，應該將圖書資料儲存到檔案中

3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)

    Ans:我告訴它「請將程式中所有的檔案操作改為使用 `with` 語法，確保檔案在操作後能正確關閉，避免資源洩漏。」

---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log
PS C:\Users\pclab\Desktop\NTUST-0527-Final-master> python -u "c:\Users\pclab\Desktop\NTUST-0527-Final-master\refined_tracker.py"
=== 圖書管理系統 v0.1 ===
> add 深入淺出Python/978001/available
Success
> add 資料結構理論/978002/available
Success
> add 演算法實作/978003/available
Success
> add 重複測試書/978001/available
ISBN Exist
> borrow 978002
Updated
> show
書名: 深入淺出Python, ISBN: 978001, 狀態: available
書名: 資料結構理論, ISBN: 978002, 狀態: borrowed
書名: 演算法實作, ISBN: 978003, 狀態: available
> exit
系統關閉
```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
    {
        "t": "深入淺出Python",
        "i": "978001",
        "s": "available"
    },
    {
        "t": "資料結構理論",
        "i": "978002",
        "s": "borrowed"
    },
    {
        "t": "演算法實作",
        "i": "978003",
        "s": "available"
    }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
# 請在此處貼上 git log 內容
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
# 請貼上你的 Repo 網址
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
