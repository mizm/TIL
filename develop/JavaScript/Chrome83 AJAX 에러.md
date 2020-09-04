# chrome v83 이슈

jquery.form.js 사용 중 file 업로드를 위해

ajaxSubmit , ajaxForm 사용 시 cancled 나 리턴값이 없어지는 경우가 발생합니다.



에러 해결을 위해

함수 호출 시 option에

```javascript
{
    'iframeSrc' : 'about:blank',
}
```

추가 필요