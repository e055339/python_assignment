# QSearch Assignments

1. **[程式能力] 請用 Python 實作實作一個函式，會餵入任意如範例的字串，回傳的值則是一
  個數字，表示這個字串四則運算的結果。
  例： a = "(2+3) * 2"，要得到 10 。**
    
    
    一開始用正則表達式檢查 input 是否只有包含數字、運算符(加減乘除)、小括號跟空格，如果有包含無效字元則會報錯。
    
    因為有先經過檢查，所以可以使用
    
    ```python
    eval()
    ```
    
    做運算。
    
    ---
    
2. **[程式能力] 請用 Python-fastapi or flask 實作 API Server，完成登入跟登出功能。**
    
    
    為何使用 FastAPI 而不是 Flask?
    
    1. FastAPI 支援非同步操作，雖然作業是簡單的驗證登入，但若考量到該 API 可能會跟資料庫互動，就需要使用到非同步操作，於是選擇 FastAPI。
    2. FastAPI 提供很棒的 GUI 介面方便測試。
    3. 跟 OAuth2PasswordBearer 搭配 Token 可以很輕鬆地完成使用者的驗證。
    
    ---
    
3. **[程式能力] 延續上題請寫另一支 API 需通過上題 API Server 驗證，並根據輸入的寬高數
    值，給予對應大小的 png ，圖片顏色不限，可使用各種 pip 套件。回傳時間需小於 0.7 秒**

    雖然在這支 API 只需處理 PNG ，但是 Pillow 可以很簡單的處理影像尺寸的問題，以及轉檔的部分，所以選用 Pillow 這個強大的套件。

    BytesIO 將記憶體的資料視為類似文件 object ，可以將圖像資訊儲存在記憶體並 return。

---

4. **[程式能力]申請GoogleCloud免費額度，使用GoogleCloudLogging紀錄第二題的 API
  使用狀況上傳。**

    ![google_log](https://github.com/user-attachments/assets/d56a3103-1682-4e3e-bca3-bdfbd19c95d2)



---

5. **[測試能力] 呈上，請實作 unit testing/e2e testing 。**
    
    
    - Unit Test
        
        `test_login`和 `test_invalid_login` 分別測試輸入正確和不正確的使用者時回傳的 status code 跟 token 是不是正確的。
        
        `test_logout` 先取得 token 向 /logout 發出 post request 並檢查 status code。
        
         `test_generate_image` 先取得 token 後向 /generate_image/ 發出 get request 並檢查 status code 跟回傳的 content-type 應為 image/png。
        
    
    - E2E Test
        
        為何使用 pytest ?
        
        1. 提供簡單性和強大的功能，例如 fixtures and markers。
        2. 支援單元測試和整合測試，能靈活適用不同場景。
        
        為何使用 httpx ?
        
        1. 支援同步和非同步請求，對於測試 API 以及模擬使用者行為非常有用。
        
        整體流程就是先打 /login 登入，然後獲取 token 後打 /generate_image/?width=100&height=100 取得 png，兩個都成功就算通過測試。
        

---

6. **[系統評估]RDB/NoSQLDB各有什麼優缺點？**
    
    RDB (關聯式資料庫)
    
    由多個資料表(Table)所組成，並且可以用外鍵將資料表關聯起來，去連結多個資料表之間的關係。
    
    優點: 
    
    - ACID 特性。
    - 可以透過 SQL 語法執行複雜的查詢。
    - 安全性: 可以設定權限決定誰可以獲得哪些資料的存取權。
    - 快速備份: 匯入和匯出很方便，sql dump 只需要短短一行指令便可備份。
    
    缺點: 
    
    - 對於水平擴展困難，通常會是垂直擴展，但成本較高。
    - 要更改數據結構時也需要更改 schema ，相較 NoSQL 較嚴格，且維護成本較高。
    
    NoSQL (非關聯式資料庫)
    
    NoSQL中的資料儲存不需要定義schema、也沒有固定架構，不保證ACID的特性，常用於分散式雲端系統。
    
    優點:
    
    - 彈性較高，不需要結構化資料。可以用來存放檔案、影片和其他非結構化內容。
    - 相較於 RDB 會有 JOIN 查詢，NoSQL 不包含資料關聯性，查詢速度相對較快。
    - 很適合分散式架構和大型數據的儲存，且水平擴展的能力較佳。
    
    缺點
    
    - 因為通常是遵循 BASE 原則，所以可能會犧牲資料完整性的部分 ( Mongo DB 現在也可以實現 ACID )。
    - 語言標準化: 大部分 RDB 都通用 SQL 作為查詢語言，但不同的 NoSQL 資料庫各有獨自的語言。
    - 當資料越複雜時沒有辦法用像 JOIN 去做複雜的查詢。
    
    ---
    
7. **根據https://roadmap.sh/backend ，盤點你既有哪些技能。**

    - **Environment & Framework**: Node.js, Express, Linux, Docker
    - **Programming Language**: JavaScript
    - **Database**: MySQL, Redis
    - **Cloud Service (AWS)**: EC2, RDS, Load Balancer, ElastiCache, S3, CloudWatch
    - **Others**: Git, GitHub Actions, Nginx
      
    以上工具為有實際使用經驗，但深入程度還有待精進，也期待進入貴公司能快速擴展自身的 Roadmap，接觸更深入的技術。

    [我的 Backend Roadmap](https://roadmap.sh/backend)
