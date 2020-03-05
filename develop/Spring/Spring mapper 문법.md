# Spring mapper 문법



1. `<include refid="a">`

   같은 쿼리를 다른 쿼리에서 일부분 사용한다거나  그렇게 반복이 될 때

   다음과 같이 사용하면 좋다

```sql
 ...<mapper>....  **<sql id="a">**	SELECT * FROM TABLE1</sql>  <select id="getList" resultType="hashmap"> 	**<include refid="a" />**	WHRE name = #{value}</select> </mapper>
```



2. `<if test = "조건">`

   조건에 따라 코드 실행

```sql
<if test="numberValue != null"> <!-- if 태그에서 조건 분기 --> 
and number_value = #{numberValue} 
</if>
```

3. `<choose> <when> <otherwise>`

   <choose> 태그를 사용하면 여러 옵션 중 하나를 적용하는 조건을 정의할 수 있다.

   <when> 태그에서 지정한 조건이 충족된 경우 SQL을 작성한다.

   <otherwise> 태그는 그 이외의 모든 조건이 충족되지 않은 경우 SQL을 작성한다.

```java
<select id="selectTest" resultType="sample.mybatis.TestTable"> 
	select * from test_table 
	<choose> 
		<when test="value == null"> 
			where value is null 
    	</when> 
    	<otherwise> 
    		where value = #{value} 
		</otherwise> 
	</choose> 
</select>
```





\- @RequestMapping 적용 메서드의 리턴타입



-> ModelAndView : 아래 데이터가 뷰에 전달

-=> 모델과 뷰 정보를 담은 ModelAndView 객체

-=> 커맨드 객체

-=> @ModelAttribute 적용 메서드의 리턴 데이터

-=> Map, ModelMap 타입의 파라미터 데이터

-=> 스프링 2.5.0 에서 ModelMap.mergeAttribute(Map) 메서드 사용시 버그가 존재

-=> ModelAndView 리턴시 모델 데이터가 올바르게 전달되지 않음

-=> 2.5.1 에서 수정됨



-> Map : 아래 데이터가 뷰에 전달

-=> 뷰에 전달할 객체 정보가 있는 Map을 리턴

-=> 뷰의 이름은 요청 URL에 의해 결정 (RequestToViewNameTranlator가 결정)

-=> 커맨드 객체

-=> @ModelAttribute 적용 메서드의 리턴 데이터



-> String : 아래 데이터가 뷰에 전달

-=> 뷰 이름을 리턴

-=> 커맨드 객체

-=> @ModelAttribute 적용 메서드의 리턴 데이터

-=> Map, ModelMap 타입의 파라미터 데이터



-> void

-=> 메서드에서 응답을 직접 처리