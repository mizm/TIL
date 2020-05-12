# FI

[![img](https://mblogthumb-phinf.pstatic.net/MjAxODA3MDlfMTA0/MDAxNTMxMDkyNTU5Mjg1.Yvddj3OwsabW_bBWs2kwuE-fGay6dWScX3MTvlQMtH4g.Aw4Ru-k4XLBcxcBOlJYPgxinS9JBisj9q1tNzfHJR08g.JPEG.silercan/fi.jpg?type=w800)](https://m.blog.naver.com/PostView.nhn?blogId=silercan&logNo=221315252055&proxyReferer=https%3A%2F%2Fwww.google.com%2F#)

영업관리는 회사의 수익을 관리하는 곳이며, 회계적으로는 매출채권에 대응한다.

구매관리는 자재, 고정자산에 대한 획득에 대한 부분을 관리하며, 회계적으로는 매입채무에 해당한다.

(고정자산은 자산으로 잡히기 때문에 회계처리 방식이 다소 상이 할 수 있음.)

마찬가지로 생산관리/인사관리에 해당하는 부분도 비용에 해당하며, 제조원가와 판관비로 성격에 따라 구분이 된다.



회계의 경우 계정코드가 Company level 부터 분리가 되기 때문에 연결회계까지 고려하는 회사에서는 계정 mapping이 중요하다. COA(Chart of Account 계정과목표)는 Company별로 설정을 하게 되어 있다. 



**회계 결산 업무를 해 보신 분들이라면 매우 쉽게 접근이 가능한 것이 SAP의 FI모듈 이다. 왜냐하면 추적성이 매우 좋기 때문이다. 각각의 수익과 비용이 어느부서에서 왔는지, 또 어떠한 내용인지 명확하게 알려준다. (그렇기 때문에 SD, MM, PP의 경우 기존 시스템 보다 넣어야 할 항목들이 많아지는 것도 사실이다.) **



1. 총계정원장관리 (FI-General Ledger)



2. 채권관리 (FI-Account Receivable)



3. 채무관리 (FI-Account Payerble)



4. 고정자산관리 (FI-Asset Accounting)



- Account (계정)
  전통적으로 계정(Account) 이라고 하면 경리(재무회계) 에서 기표가 이루어지는 대상이 되는 계정과목 또는 계정코드를 의미한다. 그러나 SAP에서는 Account의 개념을 보다 확장하여 사용하고 있으므로 주의를 요한다. SAP에서는 다음과 같이 Account를 다섯 가지의 유형으로 구분하고 있으며, 이러한 유형구분을 Account Type이라고 한다.

  - Account Type 내 용 M G/L 계정 (전통적인 계정과목/계정코드)

  - D Customer (판매거래처, 기존의 거래처코드)

  - K Vendor (구매거래처, 기존의 거래처코드)

  - A Asset (고정자산 번호, 기존의 자산번호)

  - M Material (재고자산(자재)번호)

    이렇게 Account의 개념범위를 확장한 것은 계정과목 중심의 총계정원장(General Ledger)상의 금액과 거래처나 고정자산 번호, 자재번호 중심의 보조부(Sub-ledger) 상의 금액을 일치시키고, 물류프로세스의 재무회계와의 통합성을 가능하게 하기 위해서이다.
    **즉, 전통적으로 AR (매출채권), AP (매입채무), 고정자산등과 관련된 회계전표를 기표하는 경우 해당 계정코드를 지정하고 금액을 입력한 후, 거래처나 고정자산 관련 정보를 전표상의 관리항목으로 관리하는 방식을 택하고 있는 데에 반하여,  SAP는 해당 Customer, Vendor,  Asset 번호를 마치 기존의 계정코드인 것처럼 기표를 하면, 그 와 연결이 되는 계정코드(SAP의 G/L Account)는 자동으로 결정되는 방식으로 되어 있다.**



- Account Assignment (계정지정)
  거래가 어떤 계정에 전기될 것인지를 명시하는 것.
  ※ 추가계정 지정참조



- Account Group (계정그룹)
  마스터 레코드 입력을 제어하는 속성들의 요약으로 각 마스터 레코드는 하나의 계정 그룹에 지정되어야 한다. 계정그룹에 따라 마스터 레코드에 어떠한 Data 가 필요한지가 결정되면 마스터 레코드의 번호가 정해진다.



- Account Management (계정의 관리)
  계정은 그 관리방식에 따라 미결관리(Open Item Management)를 하는 계정과 미결관리를 하지 않는(Non-Open Item Management) 계정으로 나눌 수 있다. 미결관리를 하게 되면 그 계정에 기표 된 건 별 항목들은 반드시 반제처리(Clearing)에 의해서 그 미결상태가 정리(Cleared) 된다. 현금이나 예금과 같은 계정은 업무상으로 미결관리의 의미가 없거나 불가능하므로 미결관리를 하지 않는 계정으로 설정하게 된다.
  Customer나 Vendor의 경우에는 선택여부에 관계없이 시스템적으로 무조건 미결관리를 하는 것으로 설계되어 있으며, G/L계정의 경우에만 미결관리여부를 선택할 수 있다. Asset의 경우에는 명시적이지 않으나 미결관리를 하는 개념이며, Material의 경우에는 그렇지 않다.
  한편, 계정을 조회하는 경우 잔액조회 뿐만 아니라, 기표 건 별로 조회를 하는 경우도 있는 바, 이러한 선택사항을 Line Item Display라고 한다. 따라서 예금계정의 경우 미결관리는 하지 않으나 건 별 조회는 가능하도록 설정(G/L계정 마스터에서) 할 수 있다. 일반적으로 거의 모든 계정에 대해 건 별 조회가 가능하도록 하는데, 이 경우 정보조회에 편리한 반면 DB의 Space를 많이 차지한다는 단점을 가진다.



- Account Reconciliation (계정조정)
  회계가 GAAP(General Accepted Accounting Principle)에 어긋나지 않도록 이루어 지는가를 결정하는 절차. G/L계정 잔액이 전기 된 거래의 총합과 비교된다. 고객계정의 잔액과 구매처 계정잔액이 각각 채권잔액,채무잔액 및 전기된 거래와 비교된다.



- Account Type (계정유형)
  하나의 계정이 어떤 회계 영역에 속하는지를 알려 주는 키로서 예를 들면 Asset(고정자산), Customer (고객), Vender (구매처), Mat (자재 ), G/L 등이 있다. 동일한 계정번호가 서로 다른 계정 유형에 사용될 수 있으므로 계정을 파악하기 위해서는 계정번호와 계정유형이 모두 필요하다.



- Accounting Principle (기표원칙)
  SAP는 Customer, Vendor, Asset 등의 보조부관련 계정을 중심으로 기표하면, 시스템이 자동으로 General Ledger 와 Sub-ledger 에 동시에 금액을 반영하는 구조로 되어 있으며, 이를 Accounting Principle 이라고 부르기도 한다. Accounting Principle 하에서는 총계정원장과 보조부가 원천적으로 금액이 다를 수가 없으므로, 결산 시 많은 시간을 차지하는 Reconciliation작업이 필요 없게 된다. 이러한 기표방식은 물류와의 통합상황을 가정하면 더 큰 장점을 가진다. 즉 판매, 구매, 재고관리 등의 업무처리 시에는 거래처(Customer, Vendor) 나 자재번호를 중심으로 거래처리를 하고 이를 기준으로 재무회계전표가 생성될 때 사전에 정한 G/L 계정으로 자동기표가 생성되게 된다.
  참고로 외상매출금, 외상매입금 등 거래처와 관련된 계정들은 사전에 Customer나 Vendor Master Record에 정의된 계정으로 자동결정 되며, 이를 Reconciliation Account라고 부른다. 고정자산의 경우에는 Asset Class를 경유하여 사전에 정의된 고정자산과 관련된 여러 계정(건물, 감가충당금, 고정자산 처분손실 등)이 자동으로 정해지도록 되어 있으며, 자재 (Material)와 관련하여서는 별도의 Customizing 작업에 의해 관련 G/L계정들이 자동 결정된다.



- Accounting Transaction (회계거래)
  다른 EDP거래들과는 대조적으로 SAP거래는 항상 Document Header (거래 표제부)와 최소 2개의 Line Item(개별항목)으로 구성된다.
  차변 값과 대변 값은 동일해야 하며 회계거래를 전기 할 때 시스템은 계정 잔액을 갱신한다. 회계거래는 사업거래를 시스템에 기록한다.


- Additional Account Assignment (추가 계정 지정)
계정번호, 금액, 전기키 이외에 필요에 따라 선택적으로 입력되는 개별 항목과 관련된 모든 추가 Data 예를 들면 대금지급조건, 지급방식, 코스트센터 등이 추가 Data 에 해당된다.


- Allocation Concept (할당개념)
계정의 개별 항목들이 화면 출력될 때 분류되는 방식
유사어: Sorting Concept(분류개념)


- Authorization
실제로 시스템이 사용되는 상태에서는 각 사용자의 직급 또는 속한 부서등에 따라 시스템상에서 접근할 수 있는 정보나 거래 처리를 제한 할 필요가 있다. 이러한 SAP R/3 시스템에의 접근 권한을 통칭하여 Authorization이라고 한다. SAP 가 표준으로 제공하고 있는 기능 및 Configuration을 활용하여 Authorization의 체계를 구성할 수 있으며, 이것이 필요한 경우에는 일부 시스템을 수정할 필요가 있게 된다.


- Balance (계정잔액)
계정에 전기 된 총 차.대변이나 전표의 총 차/대변의 차액
잔액은 대변금액이 차변 금액보다 많을 경우에는 "대변잔액"으로, 차변이 대변 금액보다 많을 경우에는 "차변잔액"으로 불린다.


- Balance Audit Trail (계정잔액 감사 증적)
회계년도 중 한 기간이나 여러 기간 동안에 어떤 계정의 모든 거래내역을 기록한 것. 잔액 감사 증적은 기초의 잔액과 기말까지 그 계정에 전기 된 차변과 대변 엔트리를 보여 준다.


- Balance Verification (잔액검증)
회계전표가 정확히 입력되었는지를 확인하는 절차. 차변과 대변의 금액이 반드시 같아야 한다.


- Bill-to party
납품한 제품 또는 서비스에 대한 송장을 수령하는 사람 또는 회사.


- B/S Adjustment (대차대조표조정)
대차대조표를 작성하기 전에 준비를 한다.
특별히 준비해야 할 사항은
\- 외화로 전기 된 채권, 채무, 고정자산 금액을 환산하여 조정
\- 조정계정이 바뀔 경우 채권과 채무를 조정
\- 대변 잔액을 가진 고객계정 및 차변잔액을 가진 구매처 계정을 조정
\- 잔여 일수에 따라 채권과 채무를 분류하기 위해 조정


- Cash Discount (현금할인)
일정기일까지 대금이 지급될 경우 예정 대금액으로부터 공제되는 돈.


- Cash Management and Forecast (현금관리와 예측)
여유 현금과 현금 소요량에 대한 중단기 계획
유사어: 현금관리 위치


- CBO와 Modification
SAP가 표준으로 제공하고 있는 기능이나 프로세스가 회사의 실정에 비추어 부족하거나 부적합하다고 판단이 되는 경우에는 일부 기능을 개발하거나 표준 기능/프로세스를 변경하는 경우가 있다.
CBO (Customer Bolt-On)는 Enhancement 라고 불리기도 하는데, SAP R/3 의 표준기능, 테이블들에 영향을 미치지 않는 상태에서 추가 기능을 개발하는 것을 말한다. 추가적인 Report의 개발은 일반적으로 CBO라고 표현하지 않는다. Modification은 SAP의 표준기능을 직접 변경하는 것으로서, 기술적으로는 Source code나 표준 Table의 필드를 변경하는 작업을 말한다.
일반적으로 SAP사는 Modification은 권고하지 않는데, 그 이유는 SAP의 전체적인 기술구조에 대한 명확한 이해가 없는 상태에서 표준 Source Code나 테이블을 건드리는 작업이 예기치 못한 다른 영향을 미칠 수도 있기 때문이다. 또한 Modification의 내용은 Version Up시 반영이 되지 않으므로 이를 계속적으로 유지 보수 해야 하는 부담도 회사가 감수해야 한다.


- Change Document (변경전표)
마스터 레코드, Table, Transaction 등의 변경 Data를 담고 있는 기록


- Chart of Account (계정과목일람표)
총계정원장 계정의 모든 마스터 레코드를 체계적으로 정리해 놓은 목록으로 동일한 계정과목 일람표를 여러 개의 회사코드가 사용할 수 있다.
계정과목일람표에는 모든 총계정원장계정과 계정번호, 계정과목명, 및 관리정보가 들어 있다. 하나의 Client에 여러 개의 계정과목일람표를 정의 할 수 있다. 각 회사코드는 반드시 계정과목일람표를 지정하여야 한다.


- Chart of Accounts (계정과목표)
회사의 경리 (또는 재무회계) 시스템에서 기표가 이루어지는 계정과목/계정코드 들을 모은 것을 일반적으로 Chart of Accounts(COA) 라고 하는데, SAP에서도 동일한 의미로 사용하고 있다. 다만 좀 더 정확하게 표현하면 G/L Account들의 묶음이라고 할 수 있는데, G/L Account의 구체적인 의미는 다음에 살펴 보기로 한다.
SAP를 Customizing 하는 경우 CoCd (회사코드) 를 정의하면서, 그 회사가 어떤 COA를 사용할 것인가를 정의하도록 되어 있다. 이 때 하나의 시스템을 여러 회사가 공유하는 경우, 두 개 이상의 회사가 같은 COA를 사용하는 것으로 정의할 수 있다. 즉, COA와 CoCd의 관계는 1 : N 이다. 이런 이유로 SAP의 FI의 조직구조를 설명하는 경우 COA를 CoCd의 상단에 표시하는 경우가 있는데, 이는 COA와 CoCd의 연결관계를 나타낸 것일 뿐 COA가 조직코드는 아닌 것에 유의하여야 한다.
회사가 실제 기표에 사용하고 있는 COA를 Operative Chart of Accounts라고 부르기도 하는데, 연결회계등의 그룹차원의 Data집계를 위해 Operative COA기준으로 기표 된 것들을 그룹계정으로 전환할 수도 있는데, 이러한 그룹계정의 묶음을 Group Chart of Accounts라고 한다. 한편 Operative COA이외에 그 나라에서 통용되는 계정들로 전환을 하는 것이 필요한 경우도 있는데, 이러한 목적의 COA를 Country Chart of Accounts라고 한다.


- Clearing (반제)
계정의 미결 항목들을 반제, 즉 대금처리가 끝나거나 결제된 것으로 처리하는 과정. 미결항목으로 반제 할 수 있다. 한 예로 고객이 송장에 대한 대금을 지불하면 해당 미결 항목을 결제된 대금으로 반제 할 수 있다.


- Clearing Account (중간계정)
임시 엔트리가 전기 되는 계정 중간 계정은 회계 절차상 반제를 목적으로 설정되는 보조 계정이다.
중간계정을 만드는 이유는 아래와 같다.
\- 거래의 시간차(물건입고와 송장 수납간의 시간차로 생기는 중간계정 : GR/IR계정)
\- 조직의 업무 분할로 인해 생김(은행중간계정)
\- 불분명한 거래

- Clearing Procedure (반제 절차)
미결항목을 반제하는 절차. 시스템은 다음의 두 가지 절차를 제공한다.
첫번째: 계정의 반제
두번째: 미결항목을 반제 시키면서 전표를 전기하는 것이다.
계정을 반제 할 때는 동일한 통화로 입력된 항목만을 반제 할 수 있고, 추가 Data의 입력이 불가능하다. 이 첫번째 절차는 임시 계정을 반제 할 때 사용할 수 있다. 반제와 동시에 전기가 되는 두번째 절차에는 예를 들어 고객으로부터 받은 대금의 전기(해당 미결항목의 반제) 와 이 대금으로 결제된 송장의 반제를 하나의 Transaction으로 동시에 처리할 수 있다.


- Clearing Transaction (반제 거래)
현금 수납 및 구매처에 수표를 지급하는 것과 같이 반제 절차를 촉발 시키는 거래


- Client
일반적으로는 CS(Client-Server)환경 하에서 End User들이 사용하고 있는 PC들을 Client라고 부르지만 SAP R/3상에서의 Client는 이와는 다른 의미를 갖는다. 한 회사에 SAP를 설치한다고 하면 일반적으로 하나의 Database Server를 설치하는 것을 의미하는데(SAP는 3Tier Architecture를 기본으로 하고 있는데, 이는 DB Server, Application Server, Presentation Server 의 구조를 의미한다), DB 상에서 Data 들이 나누어지는 최상위 단위가 Client 이다.(예외적으로 국가나 통화등에 대한 정의사항등과 같이 특정 Client 와 무관하게 (Client Independent) 관리되는 Data 들도 있다). 따라서 SAP R/3시스템에 Logon 하는 경우 User name, Password와 함께 반드시 Client (숫자 3자리)의 이름을 입력해야 한다.
기술적으로는 시스템 내에 존재하는 Data들이 저장되어 있는 Table들의 대부분은 Client를 Key Field 에 포함하고 있는 것으로 이해할 수 있다.
한편 업무적으로는 Client는 Data집계의 최상위 단위이므로 그룹전체를 의미하는 것으로 볼 수도 있으나(SAP 내에서 사용되는 조직구조를 설명하는 경우 Client가 계층구조상의 최상위 단위로 제시되는 경우가 흔함), 실질적으로 그룹 대부분의 회사가 하나의 DB Server하의 하나의 Client를 사용하고 있는 상황이 아니라면 그 의미는 아니라고 볼 수 있다.


- Closing (마감)
다음과 같은 마감 절차들과 관련된 업무들의 계획과 수행
\- 일일마감
\- 월간마감
\- 년말마감


- Consignment
공급업체가 고객의 장소에 자재를 배치하여 관리하는 방식. 공급업체는 자재가 위탁창고에서 출고되기 전까지는 해당 자재에 대한 소유권을 보유한다. 자재가 출고되어야만 위탁재고에 대한 대금지급의무가 발생한다. 따라서 공급업체는 정기적으로 위탁재고 출고현황을 통고 받는다.


- Contact person
공급업체의 판매 또는 영업부서와 접촉하는 고객 직원.


- Contract
공급업체와 체결하는 장기계약으로 고객 필요에 따라 생성되는 개별적인 release order에 의해 이행된다.


- Correspondence (통신 문서)
회사가 발송하고 수신하는 서면으로 작성된 모든 의사소통 수단, 주문 확인서, 지급통지서, 독촉장 등이 포함된다.


- Credit Memo (대변메모)
고객으로부터 받을 외상매출금을 줄이는 거래. 고객이 손상된 제품을 반송할 경우 등이 이에 해당된다. 차변 메모는 외상매입금을 줄이는 거래로 손상된 제품을 구매처로 되돌려 보낼 경우 등이 해당된다.


- Customer Master Record (고객 마스터 레코드)
고객과의 거래를 처리하는데 필요한 모든 정보를 담고 있는 Data. 고객주소와 은행 Data 등이 포함된다.


- Customizing or Configuration
SAP R/3는 ERP시스템의 특성상 이미 완성이 되어 있는 상태이므로, 그대로 설치하기만 하면 사용할 수 있다. 그러나 회사가 원하는 프로세스나 기능을 수행하기 위해서는 회사의 실정에 맞도록 시스템을 조정하는 작업이 필요하다. 범용성이라는 특성을 갖고 있는 만큼 SAP는 각 프로세스나 기능별로 수 많은 선택 가능한 조건(Parameter) 들을 담고 있는데, 이러한 Parameter 들을 회사가 원하는 방식으로 설정하는 작업을 Customizing또는 Configuration이라고 한다.
SAP R/3를 Implementation하는 과정을 보면 먼저 현재의 프로세스를 정리하고 또는 To-Be 프로세스를 도출하여 확정하는 Process Define단계를 밟고 그것을 실현할 수 있도록 Customizing 작업을 하게 된다. 그런데 실질적으로 Implementation전체의 과정에서 시간이 많이 소요되는 부분은 Customizing단계가 아니라 Process Define단계이다. 즉, 프로세스와 그 구현 안이 확정이 된 상태에서는 SAP시스템을 잘 이해하고 있기만 하면 Customizing 작업자체에는 시간이 많이 소요되지는 않는다. 물론 SAP가 담고 있는 기능들과 그것을 위해 Customizing이 가능한 부분과 대체 안을 체계적으로 아는 데에는 많은 Study와 노력이 필요하다.
참고로 Customizing작업을 위해 과거(2.X Version 까지) 에는 메뉴방식으로 작업단계를 구성하였으나, 이를 변경하여 현재에는 Customizing작업을 Tree 형식으로 구조화 한 "IMG(Implementation Guide)"를 제공하고 있다. IMG는 SAP 가 표준으로 제공하고 있는 것을 기반으로 하여 회사가 원하는 항목들만 선택한 Enterprise IMG와 특정 SAP Implementation 작업에서 필요한 항목들만을 모은 Project IMG를 구성하는 것도 가능하다.


- Daily Closing (일일마감)
거래를 합리적으로 처리하기 위하여 하루의 업무를 마감하면서 취하는 조치


- Due-date (만기일)
채권자가 받아야 할 금액을 채무자가 지불해야 하는 날짜. 예를 들어 (환)어음을 시스템에 입력할 때 만기일을 입력한다.


- Discounting (어음 할인)
아직 만기가 되지 않는(환) 어음을 은행에 예치하여 만기일까지의 이자(할인)와 수수료를 공제한 금액만큼을 받음


- Distribution channel
판매자재가 고객에게 도달하는 방법을 결정하는 조직단위. 유통결로는 사업을 추진하는 방법과 유통활동에 관여하는 조직 등을 규정한다.


- Division
유통을 감독하고 특정 판매자재의 수익성을 관리하기 위해 설치된 조직단위. 분할납품, 단가, 지급조건 등 고객별로 특수한 사항을 제품군별로 지정할 수 있다.


- Document (전표)
거래행위의 증빙자료. SAP는 SAP전표와 송장, 수표, 은행잔고 명세서등과 같은 일반적인 전표를 구별한다. SAP전표에는 회계전표, 샘플전표, 반복입력전표 등이 있다. 회계전표는 시스템에 사업거래를 기록하고 샘플전표와 반복입력 전표는 Data입력을 간편하게 하기 위해 사용된다.
Document 라는 용어는 SAP 의 모듈 전체에서 사용된다. 즉, FI 의 Accounting(FI) Document, CO의 CO Document, MM의 Material Document, SD의 SD Document 또는 Sales Document 등이 그 예이다. 재무회계상의 거래나, 물류상의 Transaction에 대해 SAP는 그 거래처리의 내용을 담고 있는 Object를 Document라고 부르고 있다. 예를 들어 MM의 Material Document라 함은 자재전표로 해석 할 수도 있으며 원재료, 제품 등의 입고, 출고, 이동 등의 기록을 담고 있다.
FI의 Document는 회계전표(Accounting Document)를 말한다. FI의 회계전표는 Header와 Line Item의 2 단계구조로 되어 있으며, Header에는 그 전표에서 공통적으로 사용되는 사항들(예를 들어, 전표유형, 기표일자, 증빙일자, 거래통화, 회사코드, 적요, 참조번호 등)이 저장되며, Line Item에는 차/대변의 각각의 계정관련 사항들(Account, Posting Key, 금액, 비용귀속부서(Cost center), 참조번호, 적요 등)이 저장된다.


- Document Currency (전표통화)
전표가 전기될 때 사용되는 통화.


- Document Date (증빙일자)
구매처 송장과 같은 전표가 원래 준비된 일자. 이 날짜는 전기일자와 일치하지 않을 수 있다.


- Document Entry (전표입력)
SAP 시스템에 거래를 수동 또는 자동으로 기록하는 절차로 거래의 특성에 따라 조금씩 다른 일련의 Data입력 화면에 입력한다. Dialog Interface를 통해 자동으로 Data 입력이 진행된다.


- Document Header (전표헤더)
전표일자, 전표번호와 같은 전표에 관련된 전반적인 정보를 담고 있는 전표의 일부분


- Document Number (전표번호)
회계연도 동안 회사코드에서 발생한 모든 거래를 파악할 수 있는 키


- Document Type (전표유형)
전기 될 거래를 구분하는 키로 고객, 구매처 , 총계정원장등과 같은 계정 유형들 중 어떠한 유형의 계정에 전기할 것인지를 결정짓는다.

- Document Principle (전표생성원칙)
SAP 의 회계전표에는 "하나의 전표에는 하나의 거래(하나의 증빙)를 기록 (One Invoice(Transaction) = One Document)" 하는 원칙이 적용되며 이를 Document Principle이라고도 한다. 즉, 기존의 회계전표에는 여러 거래의 내용을 축약하거나 복합하는 이른 바, "복합분개"의 형식으로 기표를 하는 관행이 허용되었으나, SAP 에서는 이것이 제한되고 있다. 하나의 전표에 여러 거래를 기록하면, 정보가 혼재 된다는 업무상의 제약도 있을 수 있으나, SAP 의 구조상 복합분개를 하게 되면 전표생성 자체가 불가한 경우가 있거나, 전표생성은 되더라고 이후의 프로세스나 정보추출에 장애를 받게 되는 경우가 발생한다.(예를 들어 관계사와의 거래와 일반거래처와의 거래를 한번에 기표 처리하는 것은 불가능하며, AR과 AP발생거래를 하나의 전표로 하는 경우 차후의 부가세정보추출이나 CO-PCA로의 Data 이체상에 문제가 발생할 수 있음). 따라서 Document Principle은 차후의 정보 Processing을 원활하게 하는 것을 보장한다. 다만 End User입장에서는 이러한 원칙 때문에 전표입력이 기존 시스템보다 번거롭거나 복잡해지는 것으로 느낄 수도 있으므로, 전표입력을 쉽게 하는 CBO를 행하기도 하는데, 신재무 시스템에서도 "유형별 전표입력"기능을 개발하여 사용자의 편의를 돕고 있다.


- Down Payment (선금)
아직 공급되지 않은 제품이나 제공되지 않은 서비스에 대한 대금, 선금은 반드시 다른 종류의 채권이나 채무와는 별도의 대차대조표에 기록되어야 한다. 지급한 선금(선급급)은 자산으로 기록되고 받은 선금(선수금)은 부채로 기록된다.


- Down Payment Request (선금요청)
특정일자에 선급이 지급될 것을 요청하는 것. 선금요청은 시스템에 별도로 저장되어 월간 차변과 대변금액을 갱신하지는 않지만 독촉프로그램과 지급 프로그램에 의해 처리될 수는 있다.


- Entry Automatic (자동입력)
거래의 종류에 따라 시스템이 자동으로 계산하고 전기하는 엔트리로 다음과 같은 사항들이 해당된다.
\- 매출 부가세와 매입부가세의 전기
\- 환율 차의 전기
\- 현금할인 비용과 수입의 전기
모든 자동입력사항은 별도의 거래 개별 항목에 기록된다.


- Exchange rate
두 통화간의 관계. 환율은 특정금액을 다른 화폐로 전환할 때 사용된다.


- Field Status (필드상태)
개별 항목을 입력할 때 특정 필드가 필 수 요소인지 선택 사항인지 아니면 필요 없는 내용인지를 명시하는 표기. 필드상태는 주로 총계정원장과 전기키(Posting Key)에 따라 좌우된다.


- Foreign Currency Evaluation (외화 평가)
외화로 전기된 자산과 부채를 현지통화로 그 가치를 환산하는 것. 이러한 평가는 대개 미결항목수준에서 이루어 진다. 즉 각 미결항목금액이 하나하나 현지 통화로 환산된다. 만일 은행 계정의 경우처럼 계정관리가 미결 항목단위로 행해지지 않을 때에는 계정 잔액을 평가한다.


- General Ledger : G/L (총계정원장)
모든 총계정원장 계정들이 들어 있는 원장. 대차대조표와 손익계산서는 총계정원장에 근거하여 작성한다.


- Goods issue
자재를 외부로 이동시키거나 고객에게 납품 함으로서 창고재고가 감소되는 것을 나타내는 재고관리 용어.


- Goods receipt
자재 접수를 가리키는 재고관리 용어. 입고는 구매 오더를 참조하거나 참조하지 않고 입력된다.


- Inventory management
특정자재의 지고수량 및 금액관리와 입고, 출고, 재고이전, 이전전기등을 포함하는 모든 재고이동관리 및 재고조사 활동 등을 포함한다.


- Invoice (송장)
고객이 제공 받는 재화나 용역에 관한 정보를 보여 주는 전표로 재화난 용역의 종류, 수량, 세액 및 금액등에 관한 내용을 볼 수 있다.


- Invoice verification
공급업체 송장의 입력 및 확인을 지칭하는 용어. 공급업체 송장이 구매오더와 입고 Data와 비교된다.


- Journal (분개장)
회계년도 중 특정기간 동안에 기입된 모든 사항들을 정리해 놓은 목록으로 흔히 전표 유형에 따라 분류한다. 원하는 때에 언제든지 준비할 수 있다.


- Ledger (원장)
시스템이 유지 보수하는 일련의 연관관계를 가진 계정 잔액들은 적어 놓은 장부. 한 예로 시스템은 항상 G/L계정들을 기록하는 원장을 관리한다.


- Line Item (개별항목)
거래의 세부내역을 담고 있는 전표의 일부분으로 금액, 계정번호 및 항목이 대변항목인지 차변항목인가 등을 비롯한 기타 거래의 종류에 따라 포함 되어야 할 정보


- Liquidity (유동성)
사업체나 개인이 지급 의무를 신속하게 처리할 수 있는 능력


- Local Currency (현지통화)
한 회사코드의 자국통화 이종통화로 현지 재정이 관리된다.


- Match code
특정필드에 입력할 값을 선택할 때 다른 조건에 의해 값을 선택할 수 있도록 하는 기능.


- Month-End Closing (월간마감)
하나의 전기기간을 마감하기 위하여 수행되는 모든 업무


- Net price
공급업체 할증 및 할인을 포함한 단가.


- Noted Item (비망항목)
계정잔액에 영향을 미치지 않는 특별 항목. 시스템은 각 비망 항목에 대하여 SAP전표를 기록한다. 비망 항목을 계정의 다른 일반 항목들과 함께 화면출력 할 수 있다. 지급프로그램과 독촉 프로그램은 선급 요청과 같은 비망 항목들을 처리한다.


- Offsetting Entry (상계 엔트리)
복식 부기 원칙에 따라 거래를 분개하여 전기할 때 상대 차변이나 대변에 기입되는 사항


- Open Item Management (미결 항목 관리)
계정의 항목들이 동일한 계정의 다른 항목들과 대응(반제)되도록 유지하는 것. 계정의 항목을 반제할 때 차변과 대변이 반드시 같아야 한다. 따라서 계정잔액은 항상 미결 항목의 합이 된다.


- Organizational Structure (조직구조)
SAP를 올바로 활용하기 위해서는 각 모듈별로 존재하는 조직구조와 관련된 Code들의 의미와 활용방법을 정확이 이해하고 이를 회사의 실정에 맞도록 구성하는 것이 매우 중요하다. 이러한 각 모듈들의 조직구조와 관련된 Code들을 통칭하여 Organizational Structure라고 한다.
한편 하나의 모듈에 존재하는 하나의 조직구조는 다른 모듈의 조직구조와 연관성을 갖게 되는데, 이렇게 하나의 조직구조 관련 Code가 다른 Code와 연결관계를 갖는 것을 Assignment라고 한다. 특히 Integration환경하에서의 조직구조의 Assignment작업이 매우 중요하다.
회사의 실제 조직 구조들을 SAP가 표준으로 제공하고 있는 조직 구조들과 어떻게 Mapping을 하여 각 모듈들을 어떻게 활용할 것인가를 정하는 작업은 특히 Enterprise Modeling이라고도 한다. Enterprise Modeling단계에서는 회사의 조직구조를 여러 View (재무회계, 관리회계, 자금, 물류 등)에서 정리하고, 각 조직 Level이 원하는 정보요건(예 : 사업부별 재무제표의 산출 등)을 정의 후, SAP에 존재하는 조직 Code와 그것들이 제공할 수 있는 정보들을 감안하여 작업을 진행한다. Enterprise Modeling은 이후의 Implementation전체의 작업에 영향을 미치므로 매우 신중하게 결정을 하여야 한다.

- Partial Payment (부분지급)
  미불 송장 금액의 일부분만이 지급되는 경우

- Payer
  납품된 물품과 제공된 서비스에 대한 청구서를 결재하는 개인 또는 회사.

- Payment Advice (지급명세서)
  배송, 지급, 수출입 신용장 수령에 관한 서면 통지서


- Payment Block (지급 블럭)
미결항목이나 계정에 대한 대금이 지급 프로그램에 의해 결제되는 것을 막는 표지. 고객이나 구매처 마스터레코드 또는 개별 항목에 지급 블럭을 설정할 수 있다.

- Payment History (지급이력)
  고객의 지급형태를 분석한 것으로 특히 체불이나 현금 할인에 관한 내용을 다룬다.

- Payment Method (지급방법)
  대금처리를 어떻게 한 것인가를 의미함 즉 수표, 어음, 계좌이체를 이용한 외화지급 등이 있다.

- Posting Key (전기키)
  개별 항목이 전기 되는 방식을 결정짓는 두 자리의 숫자로 이루어진 키. 전기 키에 의해 다음과 같은 사항들이 결정된다.
  계정유형
  차변항목 대변항목
  개별항목의 Data 입력화면

- Posting Period (전기기간)
  회계년도를 구성하는 단위기간.시스템은 전표표제부위전기일자에 따라 모든 전표를 해당 전기기간에 기록하고 전기기간별로 계정 잔액을 갱신한다.
  Posting Block(전기블럭) 특정계정에 전기가 되지 못하도록 하는 표시.
  중앙에서 모든 회사코드에 대하여 계정을 블럭하거나 하나의 회사코드만을 대상으로 계정을 블럭 할 수 있다.


- Posting Statistical (전기. 통계)
중간계정을 통해 자동으로 상계 되는 특수 G/L 거래
예를 들면 구매처로부터 받은 보증의 전기


- Pricing procedure
특정문서에 허용된 조건과 가격결정을 위해 시스템이 이러한 조건을 접근하는 순서를 정의한다. 가격결정 절차에는 자재가격 및 다양한 할인, 부가금 등이 포함되어 있다.


- Purchasing group
특정 구매 활동을 책임지는 구매 담당자 또는 구매 담당자 그룹을 나타내는 키.


- Reconciliation Account (조정계정)
고객, 구매처, 자산과 같은 보조원장의 Data에 의해 자동 갱신되는 G/L계정


- Recurring Entry (반복엔트리)
정기적으로 반복되어 입력되는 Data. 반복입력 프로그램은 반복적으로 발생하는 Data를 반복적으로 전표를 기준으로 전기한다. 예를 들면 은행이 지속적으로 일정금액을 지급하는 경우와 거의 비슷하게 임차료, 보험료, 융자 등을 반복 입력 사항으로 설정할 수 있다.


- Recurring Entry Document (반복입력 전표)
반복입력 프로그램에 의해 전기 되는 개별 항목들을 담고 있는 특수 EDP 전표


- Reference Document(참조전표)
회계전표를 전기할 때 참고 틀로 사용되는 전표이전에 전기 된 전표나 샘플전표가 참조전표로 이용된다.


- Residual item (잔여 항목)
송장 항목의 금액과 지불된 금액간의 차이를 나타내는 항목. 고객이 지급한 부분 대금을 전기하면서 미결항목을 반제 할 때 시스템은 잔여 항목을 이월시킨다.


- Reversal (역 분개)
같은 금액의 다른 전표를 동일한 계정의 반대쪽에 전기함으로써 전표를 역 분개하는 것


- Sales area
판매조직, 유통경로, 제품 군으로 구성되는 조직단위. 판매영역은 동일한 방식으로 판매할 수 있는 모든 자재를 분류하기 위해 이용된다. 또한 판매영역은 통계 뿐만 아니라 가격결정을 위한 토대를 제공한다.


- Sales organization
자재 및 서비스의 유통과 판매조건 협상을 책임지는 조직단위. 판매조직은 지리적 기준 또는 산업기준 등에 따라 기업이 시장을 세분하는 방식을 나타낼 수 있다. 각 비지니스 Transaction은 판매조직에 의해 처리된다.


- Sample Account (샘플계정)
특수 G/L계정 마스터 레코드로 G/L계정 마스터 레코드 중 특정 회사 코드에 공통적인 부분을 만들고자 할 때 사용자가 이용할 수 있는 기본값들을 담고 있다.


- Sample Document (샘플전표)
회계전표를 입력할 때 사용자가 하나의 보기로 참조할 수 있도록 기본 Data를 포함하고 있는 특수한 유형의 참조 전표이다. 회계전표와는 다르게 샘플전표는 계정 잔액에 영향을 미치지 않고 회계전표에 Data를 제공하는 기능만을 가지고 있다.


- Shipping condition
제품을 고객에게 인도하기 위한 전반적인 전략. 예를 들어 제품이 가급적 빨리 고객 위치에 도착되어야 한다고 출하조건에 규정되어 있는 경우 제품을 가장 빨리 납품할 수 있는 출하점과 운송경로가 시스템에 의해 자동적으로 제안된다.


- Shipping point
특정장소에 고정되어 출하활동을 수행하는 조직단위. 출하점은 기업의 발송부서, 또는 플랜트의 철도역 등이 될 수 있다.


- Ship-to party
제품을 수령하는 개인 또는 기업.


- Sold-to party
제품 또는 서비스를 발주하는 사람 또는 회사. 판매처는 지급처, 청구처, 인도처의 역할을 수행할 수도 있다.


- Sorting Conception (분류개념)
계정의 개별 항목들이 화면 출력될 때 분류되는 방식, 즉 서로 서로에게 할당되거나 그룹으로 묶인다.


- Special G/L Account (특수 총계정원장 계정)
특수 보조원장 거래를 위한 조정 계정으로 일반 조정계정과는 구별된다. 대게 특수 G/L계정은 선금, (환)어음, 담보 보증 및 판매나 구매와 직접 관련이 없고 외상매입금이나 외상매출금과 상계되지 않는 기타 거래들을 기록하는데 사용된다.


- Special G/L Indicator (특수 총계정원장 표시자)
특수 G/L 거래를 표시하는 한자리 코드로 일반 판매 및 구매거래와 특수 G/L거래에는 선금, (환)어음, 담보 및 보증이 있다.


- Storage location
플랜트내에서 재고를 구별할 수 있게 하는 조직단위.


- Sub-Ledger Accounting (보조원장 회계)
채권, 채무, 고정자산등과 같은 보조원장을 사용하는 회계보조원장을 통해 G/L 조정계정이 전기 된 전표의 내역을 알 수 있다.


- Valuation (평가)
대차대조표 용어로 정해진 일자에 법적 요구사항에 따라 모든 유동자산과 부채의 가치를 결정하는 것


- Valuation area
재고 가액이 관리되는 조직수준. 플랜트 수준이다.

- Vendor
자재 또는 서비스를 조달할 수 있는 외부 공급원.

- Year-end Closing (년말 결산)
년간 대차대조표(B/S)와 손익 계산서(P/L)로 현지의 법 규정에 맞도록 작성되어야 한다. 모든 자산, 부채, 이연항목(B/S) 과 모든 수익과 비용(P/L)은 GAAP에 따라 제시되어야 한다.