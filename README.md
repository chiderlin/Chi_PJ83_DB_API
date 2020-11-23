# PJ83_DB_API
## CRUD MySQL 功能


## 兩個Tables 各有CRUD
1. DomainTestLog
2. DomainListAll

# DomainTestLog  (以下參考網址路徑)  
### 新增資料(單筆)
http://127.0.0.1:8080/api/mysql/domaintestlog/c/

### 讀取
http://127.0.0.1:8080/api/mysql/domaintestlog/r/

### 修改(單筆)
http://127.0.0.1:8080/api/mysql/domaintestlog/u/"放id"/

### 刪除
http://127.0.0.1:8080/api/mysql/domaintestlog/d/

http://127.0.0.1:8080/api/mysql/domaintestlog/d/all/


### POSTMAN測試資料
{
     "id":1,
     "TestTime":"2020-11-19 00:00:00.000",
     "UrlIn":"Ttse",
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
     "CreatedTime":"Ttse"
 }



# DomainListAll (以下參考網址路徑) 
### 新增資料(單筆)
http://127.0.0.1:8080/api/mysql/domainlistall/c/

### 讀取
http://127.0.0.1:8080/api/mysql/domainlistall/r/

### 修改(單筆)
http://127.0.0.1:8080/api/mysql/domainlistall/u/"放codetomatch"/

### 刪除
http://127.0.0.1:8080/api/mysql/domainlistall/d/

http://127.0.0.1:8080/api/mysql/domainlistall/d/all/


### POSTMAN測試資料

{
    "AgentID":"222",
    "CodeToMatch":"dvdf",
    "DomainListAPP":"dfdf",
    "DomainListInner":"sfsf",
    "DomainListOuter":"trtu"
}




