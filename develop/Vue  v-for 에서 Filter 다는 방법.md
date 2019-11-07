# Vue : v-for 에서 Filter 다는 방법

```javascript
<v-text-field v-model = "search"> </v-text-field>
<v-card v-for="item in Filter"></v-card>

data() {
	return {
		items : [
			--
			--
			--
		], // items 라는 배열을 filtering 할 때 각각의 title이 있다고 가정
		search : "", // filter 할 문자열
	}
}
computed : {
	Filter() {
		if(this.search)
        {
            return this.items.filter(item => {
                return item.title.startsWith(this.search);
            });
        } else {
            return this.items;
        }
	}
}
```

