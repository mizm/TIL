```javascript
const comics = {
 'DC': ['Aquaman', 'SHAZAM'],
 'Marvel': ['Captain Marvel', 'Avengers']
};
const magazines = null;

const bookShop = {
	comics,
 	magazines,
    plus() {
        
    },
};

//동일

const bookShop = {
    comics : comics,
    magazines : magzines,
    plus : function(){
        
    },
}

(function(){ console.log('나는 익명!') }) () 
// 익명함수 실행시 뒤에 괄호를 붙여주면됨.


