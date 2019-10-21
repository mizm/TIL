# Spring Boot 에서 DB를 두개 사용할 시 사용방법



```java
package com.example.demo.board.domain;
import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.core.io.ClassPathResource;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@Configuration
@MapperScan(value={"com.example.demo.board.mapper.db1"}, sqlSessionFactoryRef="db1SqlSessionFactory")
@EnableTransactionManagement
public class Db1DatabaseConfig {

    @Bean(name = "db1DataSource")
    @Primary
    @ConfigurationProperties(prefix = "spring.db1.datasource")
    public DataSource db1DataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "db1SqlSessionFactory")
    @Primary
    public SqlSessionFactory db1SqlSessionFactory(@Qualifier("db1DataSource") DataSource db1DataSource, ApplicationContext applicationContext) throws Exception {
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        sqlSessionFactoryBean.setDataSource(db1DataSource);
//        sqlSessionFactoryBean.setMapperLocations(applicationContext.getResources("classpath:com/example/demo/board/mapper/prmiary/*.xml"));
        sqlSessionFactoryBean.setConfigLocation(new ClassPathResource("mybatis-config.xml"));
        return sqlSessionFactoryBean.getObject();
    }

    @Bean(name = "db1SqlSessionTemplate")
    @Primary
    public SqlSessionTemplate db1SqlSessionTemplate(SqlSessionFactory db1SqlSessionFactory) throws Exception {

        return new SqlSessionTemplate(db1SqlSessionFactory);
    }
}

```

Config 파일을 두개 만들고

@MapperScan 어노테이션을 통해서 접근하는 Mapper 폴더 경로를 지정 시에 그 Config에 설정된 DB는 해당 Mapper을 사용함.

결국 @MapperScan 과 @Configuration 을 통해서 해당 Mapper를 호출 하면 연결 되어 있는 DB를 통해 정보를 가져옴.