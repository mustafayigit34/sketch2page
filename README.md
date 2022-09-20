# sketch2page

---
title: "DYS Vuetify Komponentleri"
date: 2021-11-27T08:54:26Z
---

### İçindekiler

* [**Ortamın Hazırlanması**](#1)

* [**Vuetify Komponentleri**](#2)
    * [**VFileUpload**](#3)
        * [**Fonksiyonel Özellikler**](#4)   
        * [**External Props**](#5)
        * [**Event Üzerinden Set'lenen Proplar (setProp Event'i)**](#6)
            * [**VFileUpload setProp Event'i Üzerinden Set'lenebilecek Prop'lar**](#7)
        * [**External Events**](#8)
        * [**External Visible Events**](#9)
            * [**fillComponent**](#10)
            * [**uploadNow**](#11)
            * [**clearAllFields**](#12)
        * [**Örnek Sayfa**](#13)
    * [**VDocumentCreate**](#14)
        * [**Fonksiyonel Özellikler**](#15) 
        * [**External Props**](#16)
            * [**VDocumentCreate setProp Event'i Üzerinden Set'lenebilecek Prop'lar**](#17)
        * [**External Events**](#18)
        * [**External Visible Events**](#19)
            * [**clearAllFields**](#20)
        * [**Örnek Sayfa**](#21)
    * [**VDocumentViewer**](#22)
        * [**Fonksiyonel Özellikler**](#23) 
        * [**External Props**](#24)
        * [**Event Üzerinden Prop Set'lenmesi**](#25)
            * [**VDocumentViewer setProp Event'i Üzerinden Set'lenebilecek Prop'lar**](#26)
        * [**External Events**](#27)
        * [**Örnek Sayfa**](#28)
    * [**VCustomerProductDocument**](#29)
        * [**Fonksiyonel Özellikler**](#30) 
        * [**External Props**](#31)
            * [**VCustomerProductDocuments setProp Event'i Üzerinden Set'lenebilecek Prop'lar**](#32)
        * [**External Events**](#33)
        * [**External Visible Events**](#34)
            * [**fillComponent**](#35)
            * [**validation**](#36)
        * [**Örnek Sayfa**](#37)
    
---

<a name="1"></a>
## Ortamların Hazırlanması
Komponentlere http://editor.quick.plateau.softtech/ üzerinden erişebilmek için;

1.  *Settings -> Domain Service Prefix -> QJson Url Prefix*‘ e gidip içine
    ***"/microui/document/":"http://caperaui.capera.dev.rally.softtech/microui/document***
    *path*'ini ekliyoruz.

![p1](/images/document/p1.png)

2. Daha sonra komponenti ekleyeceğimiz ‘*Custom Component*’in *QJsonPath Prop*’unu         
   ***‘/microui/document/qjson/{komponentAdı}.qjson’***
   olarak *set*'liyoruz. 

![p2](/images/document/p2.png)

3. *‘Custom Component’* ekranda belirecektir.

![p3](/images/document/p3.png)

<a name="2"></a>
## Vuetify Komponentleri
1. VFileUpload
2. VDocumentCreate
3. VDocumentViewer
4. VCustomerProductDocument

<a name="3"></a>
### VFileUpload

![p4](/images/document/p4.png)

<a name="4"></a>
#### Fonksiyonel Özellikler

* *‘documentTypeCode’* set edilmeden komponent çalışmayacaktır! *setProp* eventi üzerinden *set* edebilirsiniz!
* Çoklu ve tekli doküman yükleme
* Yüklenen dokümanı indirme 
* Yüklenen dokümanı silme 
* Yüklenen dokümanı görüntüleme

<a name="5"></a>
#### External Props

| Property | Type  | Default  | Description  |
|:--------:|---|---|---|
|title|String|-|Komponentin üzerine bir başlık ekler.|
|autoUpload|Boolean|True|Komponentin otomatik upload özelliğini aktif/pasif duruma getirir.|
|deleteAPI|String|'/services/document/api/v1/document/documents/'|Delete isteğinin atılacağı url’i belirler.|
|uploadAPI|String|'/services/document/api/v1/document/documents/'|Upload isteğinin atılacağı url’i belirler.|
|multiple|Boolean|False|Çoklu doküman yükleme|
|icon|String|'mdi-folder-upload'|Yükleme icon'unu belirler.|
|documentId|String|null|Daha önceden yüklenmiş dokümanı komponent içinde getirir.|

<a name="6"></a>
#### Event Üzerinden Set'lenen Prop'lar (setProp Event'i)
Komponentin *render* aşamasından sonra *set*'lediğimiz ‘*External Prop*’lar çalışmamaktadır. Bu sorunu aşmak için *render* aşamasından sonra *set*'lemek istediğimiz *prop*'ları *parent* sayfadan şu şekilde *set*'liyoruz;
**“documentTypeCode” girilmesi zorunludur! Diğer alanlar opsiyoneldir.**

```
(<any>components.”CustomComponent-QID”.setProp)({ 
    params:{ 
        "documentTypeCode" : String, 
        "sourceType" : String, 
        "sourceValue" : String, 
        “customerNumber” : String, 
  …... 
        } 
}); 
```

<a name="7"></a>
* **VFileUpload setProp Event'i Üzerinden Set'lenebilecek Prop'lar**

    |Property|Type|Description|
    |:--------:|---|---|
    |folderId|Long|Yüklenen dokümanı verilen *folderId*'deki klasör içine oluşturur.|
    |documentId|Long|Yüklenen dokümanı verilen *documentId*'deki dokümanın yeni versiyonu olarak oluşturur.|
    |documentTypeCode|String|Yüklenen dokümanın doküman tipini belirler. **Bu alan zorunludur!**|
    |customerNumber|String|Yüklenen dokümanı verilen *customerNumber* ile ilişkilendirir.|
    |sourceType|String|Yüklenen dokümanı verilen *sourceType* ile ilişkilendirir.|
    |sourceValue|String|Yüklenen dokümanı verilen *sourceValue* ile ilişkilendirir.|
    |documentFile|Object|-|
    |validityEndTime|-|-|
    |approved|Boolean|-|

<a name="8"></a>
#### External Events

|Property|Description|
|:--------:|---|
|getDocumentId(documentId)|*“documentId”* üzerinden yüklenen doküman *id*'sinin alınması|
|onDeleteSuccess()|*Delete* işlemi başarılı olduğunda çalışacak kısım|
|onDeleteFail()|*Delete* işlemi başarısız olduğunda çalışacak kısım|
|onUploadSuccess(document)|*Upload* işlemi başarılı olduğunda çalışacak kısım|
|onUploadFail()|*Upload* işlemi başarısız olduğunda çalışacak kısım |
|getDocumentList(uploadedDocumentList)|*“uploadedDocumentList”* üzerinden yüklenen dokümanların alınması|
|rowClick(row)|Çoklu doküman yüklemede, yüklenen dokümanlar listesinde *row*'a tıklandığında o *row* ile ilgili bilgileri getirir.|

<a name="9"></a>
#### External Visible Events
Bu eventler komponent üzerinde görünmeyecektir ancak *parent* sayfadan çağırılabilir.

<a name="10"></a>
* **fillComponent**

    Komponente dışarıdan *documentId* ve *documentName* vererek doldurmamızı sağlar. Bu *event* tetiklendiğinde dokümanı görüntüleme ve dokümanı silme butonları görünür olacaktır. Doküman indirme işlemini görüntüleme penceresi içerisinden yapabilirsiniz.
    
    Çoklu doküman görüntüleme istenirse, *documentId* ve *documentName* alanları ***null*** gönderilmelidir, *"documentIdList"* parametresi sayı içeren *array* şeklinde gönderilmelidir.
    
    ```
    (<any>components.”CustomComponent-QID”.fillComponent)({ 
    documentId: int, 
    documentName: String,
    documentIdList: Array
          }); 
    ```
    Çoklu doküman görüntüleme script örneği;
    
    ```
    //TypeScript
    quick.MM.trigger('fillComponent', [{ "documentId":null, "documentName":null,"documentIdList":[53588, 53618]}]);
    ```

<a name="11"></a>
* **uploadNow**

    Komponentin *autoUpload prop*'unu ***false*** olarak *set*'lediğimizde *upload* işlemini gerçekleştirmek için bu *event*'i *trigger* etmeliyiz. 

    ```
    (<any>components.”CustomComponent-QID”.uploadNow)({}); 
    ```

<a name="12"></a>
* **clearAllFields**

    Komponentin içeriğini temizleyip, komponenti ilk haline getirecektir.
    
    ```
    (<any>components.”CustomComponent-QID”.clearAllFields)({});
    ```

<a name="13"></a>
#### Örnek Sayfa

exampleVFileUpload.qjson

<a name="14"></a>
### VDocumentCreate

![p5](/images/document/p5.png)

![p6](/images/document/p6.png)

<a name="15"></a>
#### Fonksiyonel Özellikler

* Doküman tipi seçme 
* Doküman yükleme 
* Doküman tipi ve yüklenecek döküman seçildikten sonra *“Kaydet”* butonuna tıklanarak döküman yüklemenin gerçekleşmesi.

Müşteri numarası girme özelliği henüz eklenmemiştir. 

<a name="16"></a>
#### External Props

|Property|Type|Default|Description|
|:--------:|---|---|---|
|isCustomerNumberMandatory|Boolean|False|Müşteri numarası *combobox*’ı görünür hale getirilir.|
|multiple|Boolean|False|Çoklu doküman yüklemeye izin verilir.|

<a name="17"></a>
* **VDocumentCreate setProp Event'i Üzerinden Set'lenebilecek Prop'lar**

    *selectedDocumentType*, *documentTypeGroupCode*, *documentTypeList prop*'ları tek başlarına kullanılmalıdır. Bu *prop*'ların herhangi ikisini aynı anda *set*'lemek istediğinizde birbirini ezme durumları oluşabilecektir. *VFileUpload*'un *setProp event*'i içerisinde verebildiğiniz tüm *prop*'ları burada da verebilirsiniz.
    
    ```
    (<any>components.”CustomComponent-QID”.setProp)({ 
        selectedDocumentType:{ 
            text : "DocumentTypeName”, 
            value : “DocumentTypeCode” 
    } , 
    “customerNumber” : String, 
      …... 
    }); 
    ```
    
    |Property|Type|Description|
    |:--------:|---|---|
    |selectedDocumentType|Object| Doküman tipi seçme *combobox*'ı *disable* olacak ve seçilen doküman verilen doküman tipi ile ilişkilendirilecektir. Kullanımını aşağıdaki örnek sayfada görebilirsiniz.|
    |documentTypeGroupCode|String|Doküman tipi seçme *combobox*'ının içerisinde verilen doküman başlığına bağlı doküman tipleri gösterilecektir.|
    |customerNumber|String|Müşteri numarası alanı *disable* olacak ve seçilen doküman verilen *customerNumber* ile ilişkilendirilecektir.|
    |documentTypeList|Object Array|Doküman tipi *combobox*'ını verilen doküman tipi listesi ile dolduracaktır. *Array*'in içerisindeki objenin yapısı şu şekilde olmalıdır; ``` {"text": "{DocumentTypeName}","value":"{DocumentTypeCode}"}```|

<a name="18"></a>
#### External Events

|Property|Description|
|:--------:|---|
|onDocumentCreateSuccess(document)|Doküman oluşturma işlemi başarılı olduğunda bu *event* çalışır.|
|onDocumentCreateFail()|Doküman oluşturma işlemi başarısız olduğunda bu *event* çalışır.|
|getDocumentId(documentId)|Oluşan dökümanın *ID*'sini döndürür.|

<a name="19"></a>
#### External Visible Events

Bu *event*'ler komponent üzerinde görünmeyecektir ancak *parent* sayfadan çağırılabilir. 

<a name="20"></a>
* **clearAllFields**

    Komponentin içeriğini temizleyip, komponenti ilk haline getirecektir.
    
    ```
    (<any>components.”CustomComponent-QID”.clearAllFields)({});
    ```

<a name="21"></a>
#### Örnek Sayfa

exampleVDocumentCreate.qjson

<a name="22"></a>
### VDocumentViewer

![p7](/images/document/p7.png)

<a name="23"></a>
#### Fonksiyonel Özellikler

Yüklenen dokümanların
- Doküman içeriğini
- Doküman adını
- Doküman tipini
- Yükleme tarihi
- Yükleyen kullanıcının özelliklerini göstermektedir. Görüntülenen dosya indirilebilir.

<a name="24"></a>
#### External Props

--

<a name="25"></a>
#### Event Üzerinden Prop Set'lenmesi

```
(<any>components.”CustomComponent-QID”.setProp)({
documentId : Long
});
```

<a name="26"></a>
* VDocumentCreate setProp Event’i Üzerinden Set’lenebilecek Prop’lar

    |Property|Type|Description|
    |:--------:|---|---|
    |documentId|Long|Verilen *documentId*'yi kullanarak komponent içindeki gerekli alanları doldurur.|

<a name="27"></a>
#### External Events

--

<a name="28"></a>
#### Örnek Sayfa

exampleVDocumentViewer.qjson

<a name="29"></a>
### VCustomerProductDocument

![p8](/images/document/p8.png)

![p9](/images/document/p9.png)

<a name="30"></a>
#### Fonksiyonel Özellikler

Komponentin 2 farklı kullanım şekli bulunmaktadır. Bunlar;
* Belli bir süreç içerisindeki dokümanları listelemek (Bu özellik için ***setProp event***'i üzerinden komponent tetiklenmelidir.)
* *ID*'si elimizde bulunan dokümanları listelemek (Bu özellik için ***fillComponent event***'i üzerinden komponent tetiklenmelidir.)

Bu yöntemler hakkında detaylı bilgileri aşağıda bulabilirsiniz.

1. yöntemde dökümanlar üzerinde
- Doküman Ekleme,
- Doküman Görüntüleme,
- Doküman Düzenleme,
- Doküman Silme

işlemlerine izin verilmektedir.

2. yöntemde ise Doküman Ekleme işlemi yapılamamaktadır.

<a name="31"></a>
#### External Props

|Property|Type|Default|Description|
|:--------:|---|---|---|
|showDeleteIcon|Boolean|True|Buradaki tüm *prop*'lar belirtilen alanların *visible* değerlerine etki etmektedir.|
|showCreateIcon|Boolean|True|   |
|showEditIcon|Boolean|True|   |
|showViewIcon|Boolean|True|   |
|showButtonsColumn|Boolean|True|   |
|showValidityDateTimeColumn|Boolean|True|   |
|showUploadDateTimeColumn|Boolean|True|   |
|showDocumentNameColumn|Boolean|True|   |
|showIsMandatoryColumn|Boolean|True|   |
|showDocumentTypeColumn|Boolean|True|   |

<a name="32"></a>
* VCustomerProductDocuments setProp Event'i Üzerinden Set'lenebilecek Prop'lar

    ```
    (<any>components.”CustomComponent-QID”.setProp)({ 
        "documentTypeGroupCode" : String,
        "sourceType" : String,
        "sourceValue" : String,
        "dispensationDataList" : [{}],
        "multiple" : true
    }); 
    ```
    
    |Property|Type|Description|
    |:--------:|---|---|
    |documentTypeGroupCode|String|Burada verilen *documentTypeGroupCode* altındaki doküman tipleri listelenecektir.|
    |sourceType|String|Verilen *sourceType*'daki dokümanları getirip, ilgili doküman tiplerinin bulunduğu satırları dolduracaktır.|
    |sourceValue|String|Verilen *sourceValue*'daki dokümanları getirip, ilgili doküman tiplerinin bulunduğu satırları dolduracaktır.|
    |dispensationDataList|JSON Object List|Önceden girilmiş *dispensation data*'sını görüntülemek için bu *prop*'a değer atanmalıdır. Örnek data yapısı; ``` [{"documentId": 51303, "documentTypeCode": "KB", "documentTypeName": "Kimlik Belgesi", "dispensationData": {"description": "sdsd", "dispensationReason": [ "Aslı Ulaşmadı","Diğer"], "dispensationDate": "2022-05-17"}}, {"documentId": 51304, "documentTypeCode": "TAXB", "documentTypeName": "Vergi Levhası", "dispensationData": {"description": "ddd", "dispensationReason": ["Diğer"], "dispensationDate": "2022-05-17", "isDispensationRequired": true}}]| ```
    |multiple|Boolean|*VFileUpload* komponentinin çoklu ya da tekli dokümanla çalışmasını sağlar.|

<a name="33"></a>
#### External Events

|Property|Description|
|:--------:|---|
|rowClick(row)|Üzerinde işlem yapılan *row* ile ilgili bilgileri getirir.|
|onDeleteSuccess()|Doküman silme başarılı olduğunda bu *event* çalışır.|
|onDocumentCreateSuccess(document)|	Doküman oluşturma işlemi başarılı olduğunda bu *event* çalışır.|
|onDocumentCreateFail()|Doküman oluşturma işlemi başarısız olduğunda bu *event* çalışır.|
|onDeleteFail()|Doküman Silme işlemi başarısız olduğunda bu *event* çalışır.|
|getDocumentList(documentList)|O sırada doküman içerisinde bulunan dokümanların *ID* listelerini döndürür.|
|dispensationDataListChanged(dispensationDataList)|*Dispensation data list* güncellendiğinde çalışır ve listenin tamamını döner.|

<a name="34"></a>
#### External Visible Events

Bu *event*'ler komponent üzerinde görünmeyecektir ancak *parent* sayfadan çağırılabilir. 

<a name="35"></a>
* fillComponent

    Verilen *ID* listesi içindeki dokümanları listeleyecektir. Bu kullanımda doküman ekleme işlemi gerçekleştirilememektedir.
    
    ```
    (<any>components.”CustomComponent-QID”.fillComponent)({
            documentIdList: int []
    });
    ```

<a name="36"></a>
* validation

    Tüm zorunlu alanlara doküman yüklenip yüklenmediğini kontrol eder. Yüklenmişse *'true'* yüklenmemişse *'false'* cevabını döner.
    
    ```
    (<any>components."CustomComponent-QID”.validation)({});
    ```

<a name="37"></a>
#### Örnek Sayfa

exampleVCustomerProductDocument.qjson
