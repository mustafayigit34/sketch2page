# sketch2page


# Document Api

---

### Create Document <span style="color:blue">**POST**</span>
Yeni bir doküman oluşturmak için kullanılır.



```
/api/v1/document/documents
```
* İstek gerçekleştirilmeden önce ***Headers*** kısmına ***Content-Type: application/json*** kısmı eklenmelidir.
* İsteğin ***body*** kısmı örnek olarak aşağıdaki gibi doldurulduğunda başarılı bir şekilde doküman oluşturulacaktır. 
```
{
"documentTypeCode":"OTH",
"documentFile":
    {
    "fileName":"test.pdf",
    "file": (Base64 formatında girdi),
    "mimeType":"application/pdf",
    "size":39395
    },
"validityEndTime":null,
"multiple":false,
"dispensation":false
}
```

---
