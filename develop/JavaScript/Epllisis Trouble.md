# Epllisis Trouble

- Epllisis 는 jquery vendor로 텍스트가 길어질 경우 줄어주는 라이브러리



## issues

## "/"이 text에 들어갈 시 undefined가 뜸

```javascript
"&":"&","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#x27;","`":"&#x60;"
//이 부분을 찾아야함 min 파일과 그냥 파일이 차이가 있는걸로 보임
//마지막에 추가
,"/":"&#x2F;"

//아래는 min 파일 수정본
/* jQuery ellipsis | Copyright (c) 2013 J. Smith (@jjenzz) | http://github.com/jjenzz/jquery.ellipsis */
(function(e){"use strict";if(typeof define==="function"&&define.amd){define(["jquery"],e)}else{e(jQuery)}})(function(e){"use strict";function i(i,s){function g(){o.text=o.$cont.text();o.opts.ellipLineClass=o.opts.ellipClass+"-line";o.$el=e('<span class="'+o.opts.ellipClass+'" />');o.$el.text(o.text);o.$cont.empty().append(o.$el);y()}function y(){if(typeof o.opts.lines==="number"&&o.opts.lines<2){o.$el.addClass(o.opts.ellipLineClass);return}d=o.$cont.height();if(o.opts.lines==="auto"&&o.$el.prop("scrollHeight")<=d){return}if(!f){return}v=e.trim(w(o.text)).split(/\s+/);o.$el.html(n+v.join("</span> "+n)+"</span>");o.$el.find("span").each(f);if(l!=null){b(l)}}function b(e){v[e]='<span class="'+o.opts.ellipLineClass+'">'+v[e];v.push("</span>");o.$el.html(v.join(" "))}function w(e){return String(e).replace(/[&<>"'\/]/g,function(e){return m[e]})}var o=this,u=0,a=[],f,l,c,h,p,d,v,m;m={"&":"&","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#x27;","`":"&#x60;","/":"&#x2F;"};o.$cont=e(i);o.opts=e.extend({},r,s);if(o.opts.lines==="auto"){var E=function(t,n){var r=e(n),i=r.position().top;p=p||r.height();if(i===h){a[u].push(r)}else{h=i;u+=1;a[u]=[r]}if(i+p>d){l=t-a[u-1].length;return false}};f=E}if(typeof o.opts.lines==="number"&&o.opts.lines>1){var S=function(t,n){var r=e(n),i=r.position().top;if(i!==h){h=i;u+=1}if(u===o.opts.lines){l=t;return false}};f=S}if(o.opts.responsive){var x=function(){a=[];u=0;h=null;l=null;o.$el.html(w(o.text));clearTimeout(c);c=setTimeout(y,100)};e(window).on("resize."+t,x)}g()}var t="ellipsis",n='<span style="white-space: nowrap;">',r={lines:"auto",ellipClass:"ellip",responsive:false};e.fn[t]=function(n){return this.each(function(){try{e(this).data(t,new i(this,n))}catch(r){if(window.console){console.error(t+": "+r)}}})}})
```
