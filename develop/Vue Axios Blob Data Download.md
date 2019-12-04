# Vue Axios Blob Data Download

```javascript
Axios
      .post(url, {
        headers: this.headers,
        params: params,
      }, {
        responseType : "blob"
      })
      .then(response => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
				const link = document.createElement('a');
				link.href = url;
				link.setAttribute('download', 'data.xlsx'); //or any other extension
				document.body.appendChild(link);
				link.click();
      })
      .catch(e => {
        this.ErrorToLogin(e)
      })
```

