# Spring Boot - Service Scope 문제



service annotation 에서 전역 변수를 선언할 경우 모든 세션에 대해서 전역적으로 생각한다?

```java
public class ExcelService {
    @Autowired
    private ExcelMapper excelMapper;
    //sheet의 최대라인수
    private final int maxRow = 1048575;
    //최대 sheet 개수
    private final int maxSheet = 10;
    ** Service 단의 전역 변수는 밑에 함수에서 세션들이 동일하게 모두 공유함 싱글톤디자인 **

    @Transactional
    public void selectExcelList(HttpServletResponse response, String query) {
        log.info("service 시작");
//        log.info(String.valueOf(sheetCount));

        //sheet객체 배열
        Sheet[] sheet = new Sheet[maxSheet];
        String test = "";
        // 메모리에 500개의 행을 유지합니다. 행의 수가 넘으면 디스크에 적습니다.
        // keep 500 rows in memory, exceeding rows will be flushed to disk
        SXSSFWorkbook wb = new SXSSFWorkbook(500);
        sheet[0] = wb.createSheet("sheet1");//최초 sheet1 생성

        try {
            log.info("service - try문 시작");

            excelMapper.dynamicQueryForList(query, new ResultHandler<LinkedHashMap<String, String>>() {
                private int sheetCount = 1;
				// **excelMapper context로 넘어가기 때문에 변수 사용 시에 안쪽에 저장해야함. 
                public void handleResult(ResultContext<? extends LinkedHashMap<String, String>> context) {
                }
            });
        }
                   
    }
}
```





 

