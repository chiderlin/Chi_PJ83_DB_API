# PJ83_DB_API => CRUD MySQL 功能


## models.py裡的class Meta是什麼?
https://zhuanlan.zhihu.com/p/61732533


## 為什麼序列化Serialize?  /  Serializers.py是什麼?
https://zh.wikipedia.org/wiki/%E5%BA%8F%E5%88%97%E5%8C%96

1. 對同步控制而言，表示強制在同一時間內進行單一存取。
2. 在數據儲存與傳送的部分指 將一個資料儲存至檔案或是記憶體緩衝。或者網絡傳送資料時進行編碼的過程。或者伺服器將資料儲存到檔案或資料庫。
相反過程則稱 反序列化。

* 序列化 serialization 也稱 物件編組(marshalling) (python一個序列化模組叫marshmallow)
* 反序列化 deserialization 也稱 解編組(unmarshalling)




## 以下是API document 
## 兩個Tables
1. DomainTestLog
2. DomainListAll

### 新增資料(單/多筆):POST
http://127.0.0.1:8080/app5/api/mysql/c/

參數:
1. tablename 

### 讀取:GET
http://127.0.0.1:8080/app5/api/mysql/r/

參數:
1. tablename 
2. filter_data => json格式  {"column_name1":"value1", "column_name2":"value2",... }



### 修改(單筆):PUT
http://127.0.0.1:8080/app5/api/mysql/u/{id}/

參數:
1. tablename 

### 刪除:DELETE
http://127.0.0.1:8080/app5/api/mysql/d/{tablename}/{id}/

參數:
1. tablename 

http://127.0.0.1:8080/app5/api/mysql/d/{tablename}/all/

參數:
1. tablename 

### DomainTestLog測試資料
{
    "tablename":"domaintestlog",
    "data":[
        {
            "TestTime":"2020-11-19 00:00:00.000",
            "UrlIn":"Ttse01",
            "UrlOut":"Ttse",
            "MyIP":"Ttse",
            "MyZone":"Ttse",
            "CDN":"Ttse",
            "CDNIP":"Ttse",
            "PageLoadTime":12,
            "Status":"Ttse",
            "IPScreenshot":"Ttse",
            "ProductScreenshot1":"Ttse",
            "ProductScreenshot2":"Ttse",
            "ProductScreenshot3":"Ttse",
            "ProductScreenshot4":"Ttse",
            "DomainType":"2"
        },
        {
            "TestTime":"2020-11-19 00:00:00.000",
            "UrlIn":"Ttse02",
            "UrlOut":"Ttse",
            "MyIP":"Ttse",
            "MyZone":"Ttse",
            "CDN":"Ttse",
            "CDNIP":"Ttse",
            "PageLoadTime":12,
            "Status":"Ttse",
            "IPScreenshot":"Ttse",
            "ProductScreenshot1":"Ttse",
            "ProductScreenshot2":"Ttse",
            "ProductScreenshot3":"Ttse",
            "ProductScreenshot4":"Ttse",
            "DomainType":"2"
        }
    ]    
}




### DomainListAll測試資料
{
    "tablename":"domainlistall",
    "data":[
        {
            "AgentID":"222",  // 不可重複
            "CodeToMatch":"dvdf", // 不可重複
            "DomainListAPP":"dfdf",
            "DomainListInner":"sfsf",
            "DomainListOuter":"trtu",
            "DomainType":"2"
        },
        {
            "AgentID":"333",  // 不可重複
            "CodeToMatch":"dvdg", // 不可重複
            "DomainListAPP":"dfdf",
            "DomainListInner":"sfsf",
            "DomainListOuter":"trtu",
            "DomainType":"2"
        }
    ]
}



