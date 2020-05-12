# Spring @NotFound  어노테이션

```java
@Entity
@Table(name = "PC_PROGRAM_GROUP")
@Getter
@Setter
public class ProgramGroup {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "SEQ_PCPROGRAMGROUP")
    @SequenceGenerator(name = "SEQ_PCPROGRAMGROUP", sequenceName = "SEQ_PCPROGRAMGROUP", allocationSize = 1)
    @Column(name= "ID")
    private int id;

    @ManyToOne
    @NotFound(action = NotFoundAction.IGNORE)
    @JoinColumn(name = "PROGRAMID", insertable = false, updatable = false)
    private ProgramInfo programInfo;
    private String createBy;
    private Date creationDate;
    
    @ManyToOne
    @NotFound(action = NotFoundAction.IGNORE)
    @JoinColumn(name = "GROUPID", insertable = false, updatable = false)
    private AuthGroup authGroup;
```



Error `javax.persistence.EntityNotFoundException: Unable to find`

에러가 발생하는 원인은 @manytoone으로 연결되어있는 것이 하나도 없는데 일단 검색해서 오류가 뜸

그럴 때 @NotFound 어노테이션을 달아주면 해결!