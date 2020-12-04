# PJ83_DB_API
## CRUD MySQL 功能


## 兩個Tables
1. DomainTestLog
2. DomainListAll

### 新增資料(單/多筆):POST
http://127.0.0.1:8080/app5/api/mysql/c/

### 讀取:GET
http://127.0.0.1:8080/app5/api/mysql/r/

### 修改(單筆):PUT
http://127.0.0.1:8080/app5/api/mysql/u/{id}/

### 刪除:DELETE
http://127.0.0.1:8080/app5/api/mysql/d/{tablename}/{id}/

http://127.0.0.1:8080/app5/api/mysql/d/{tablename}/all/


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



