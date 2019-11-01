# Vue - Vuex Store의 변경값 감지하기

```vue
date () {
	return {
		select : 0
	}
}
computed: {
		selectNo: function() {
			return this.$store.state.selectNo;
		}
	},
watch : {
		async selectNo(v){
			this.select = v
			//이렇게 해주면 변경되는 값을 data에 있는 select에 넣어줄 수 있음
		} 
	},
```

