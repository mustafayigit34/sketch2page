# sketch2page


# Document Api
#### [Api'lerin tamamını görmek için tıklayın.](http://document.product-plateau-happypath-int.plateauhappypath.plateaux.softtech/swagger-ui.html?urls.primaryName=document-v1-api#/document-api-controller-v-1)

---

### Create Document
Yeni bir doküman oluşturmak için kullanılır. Eğer varolan bir ***documentId*** verilirse veya ***sourcetype***, ***sourcevalue*** verilirse o dokümanın yeni versiyonu olarak yükler.

```
POST        /api/v1/document/documents
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

### Get Document By Id
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanının son versiyonunu cevap olarak döndürür.

```
GET        /api/v1/document/documents/{documentId}
```
Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Delete Documents By Id
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanın tüm versiyonlarını siler.

```
DELETE        /api/v1/document/documents/{documentId}
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Get Document Detail By Id Base64
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanının son versiyonunu cevap olarak döndürür.

```
GET        /api/v1/document/documents/{documentId}/base64
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Get Document Json By Id
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen ***excel***'in içindeki alanları döndürür.

```
GET        /api/v1/document/documents/{documentId}/excellines
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Get Document Json By Id
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen ***excel***'in içindeki alanları ***map***'li olarak döndürür.

```
GET        /api/v1/document/documents/{documentId}/excellinesmap
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Get Document Summary By Id
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanın özet bilgilerini json olarak döndürür.

```
GET        /api/v1/document/documents/{documentId}/lite
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---
<a name="/api/v1/document/documents/{documentId}/summary"></a>
### Get Document Summary By Id
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanın geçmişte gördüğü işlemler cevap olarak döndürülür.

```
GET        /api/v1/document/documents/{documentId}/summary
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Copy Document for Another Source
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanı çoğaltır. Bu işlemi yaparken bu dokümanı kopyalar ve ***sourcetype*** ile ***sourcevalue***'su verilen alana yapıştırır.

```
POST        /api/v1/document/documents/{documentId}/multiply
```

* İstek gerçekleştirilmeden önce ***Headers*** kısmına ***Content-Type: application/json*** kısmı eklenmelidir.
* İsteğin ***body*** kısmı örnek olarak aşağıdaki gibi doldurulduğunda başarılı bir şekilde doküman oluşturulacaktır. 

```
{
  "sourceType": "string",
  "sourceValue": "string"
}
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Update Document Properties
***Path Variables*** içerisindeki ***documentId*** değerine karşılık gelen ***id***  ile eşleşen dokümanın özelliklerini günceller.

```
PUT        /api/v1/document/documents/{documentId}/props
```

* İstek gerçekleştirilmeden önce ***Headers*** kısmına ***Content-Type: application/json*** kısmı eklenmelidir.
* İsteğin ***body*** kısmı örnek olarak aşağıdaki gibi doldurulduğunda başarılı bir şekilde doküman oluşturulacaktır. 

```
{
  "sourceValue": "string"
}
```

Her ortamda dokümanlar değişiklik göstereceğinden, *test aşamasında* öncelikle ***Create Document*** isteği çağrılarak bir doküman oluşturulabilir, daha sonra bu oluşan dokümanın ***id*** değeri ortam değişkenlerine kaydedilerek bu istekteki ***documentId*** değerine karşılık gelecek şekilde verilebilir. Bu şekilde, ortam fark etmeksizin değişken dinamiği sağlanır.

---

### Get Document By Id
***version*** ve ***versionId***'ler farklı tanımlamalar içeriyor. ***versiyonId***'yi bulmak için bir önceki [***summary api***](#/api/v1/document/documents/{documentId}/summary)'sinden istenilen döküman sorgulanabilir. İstenilen ***versiyonId*** verildiğinde bu api ile o dokümanın o ***versiyonId***'sine ait bilgileri getirilir.












