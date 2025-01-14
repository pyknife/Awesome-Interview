# Awesome Java Interview | Java 面试题集锦

# 语法基础

## 类与对象

- 为什么 Java 文件中只能含有一个 public 类?

## 异常处理

- Java 中 Error 与 Exception 有何设计区别？

- catch 与 finally 类中都存在 return 语句的情况下，会实际得到哪个值？

# 数据结构

## 基础类型

- 写出下面代码的输出结果：

```java
public static void main(String[] args) {
    String str1 = "Hello,World";
    String str2 = "Hello,World";
    String str3 = new String("Hello,World");
    String str4 = str3.intern();

    System.out.println("str1 == str2 ? " + (str1 == str2));
    System.out.println("str2 == str3 ? " + (str2 == str3));
    System.out.println("str2 == str4 ? " + (str2 == str4));
}
```

- StringBuilder 为什么线程不安全？

# 工程实践

- 你是如何进行线上应用调试的？

- 当发现 CPU 利用率及平均负载较高时，应该如何排查？

## Maven

- Maven 插件（plugin）goal 的执行与生命周期（lifecycle）phase 的关系？

# 并发编程

## 线程协作

- 为什么不建议使用 Executors？

## 线程安全

### 锁

- synchronized 关键字是如何保证原子性、可见性、有序性这几个问题的？

- 常见的锁优化的思路有哪些？

### 同步

- CountDownLatch、CyclicBarrier、Semaphore 共同之处与区别以及各自使用场景？

### 并发容器

- ConcurrentHashMap 是如何提高吞吐量的？

## NIO

## Akka

# Spring

## IoC

- 为什么不推荐使用 Autowired？在多线程环境下为何有时候 Autowired 会无效？应该如何保证多线程下的注入？

## MyBatis

## Hibernate

- 简述下 Hibernate 的优劣特性。

# Toolkits & Framework

# JVM

## 类

- 简单讲下 JVM 中的类加载过程。JVM 中的类加载和卸载的时机？如何理解 JVM 中不同类加载器的概念和作用？ClassLoader 的作用是什么？

- 简单讲下 JVM 中的双亲委派模型？什么情况下会破坏双亲委派模型？为什么？可否举个例子？

- Tomcat 中的类加载机制有了解吗？为什么这么设计？实际开发中有遇到哪些类加载器相关的问题？你又是如何解决的？

- JVM 之上的弱类型语言例如 Groovy 是如何实现？简单讲下动态类加载机制？
