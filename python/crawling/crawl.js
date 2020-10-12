var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();
var url = 'http://openapi.epost.go.kr/postal/downloadAreaCodeService/downloadAreaCodeService/getAreaCodeInfo'; /*URL*/
var queryParams = '?' + encodeURIComponent('ServiceKey') + '='+'AggSeUXyjkR0ETSS4W6bf6erMLfCg6WjfRk518sN9717gpL9LOekNJz%2Fe6gjLvFKS0W6BzoukbUx204wayh%2FAg%3D%3D'; /*Service Key*/
queryParams += '&' + encodeURIComponent('dwldSe') + '=' + encodeURIComponent('2'); /**/
xhr.open('GET', url + queryParams);
xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
        console.log('Status: '+this.status+'nHeaders: '+JSON.stringify(this.getAllResponseHeaders())+'nBody: '+this.responseText);
    }
};

xhr.send('');