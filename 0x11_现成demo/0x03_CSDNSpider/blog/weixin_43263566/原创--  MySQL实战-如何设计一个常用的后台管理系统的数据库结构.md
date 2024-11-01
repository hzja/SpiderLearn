# 原创
：  MySQL实战：如何设计一个常用的后台管理系统的数据库结构

# MySQL实战：如何设计一个常用的后台管理系统的数据库结构

**部分数据来源：**ChatGPT  

### 什么是后台管理系统？

        后台管理系统是指用于管理和维护网站或应用程序的后台界面系统，通常包含用户管理、权限管理、数据管理等功能，能够方便快捷地管理网站或应用程序。常见的后台管理系统有Cms、OA等，下面我们就来介绍如何使用MySQL设计一个常用的后台管理系统。

### 如何使用MySQL设计一个常用的后台管理系统？

#### 1. 数据库设计

我们首先需要设计一个合适的数据库结构，建立不同的数据表来存放数据。

安装MySQL和Navicat数据库工具后，我们可以登录到MySQL中，选择创建一个数据库：

```
CREATE DATABASE management_system;

```

在新建的这个数据库内，我们可以创建用户表（user）、角色表（role）、权限表（permission）、用户角色关联表（user_role）、角色权限关联表（role_permission）等多个数据表。

如何创建这些数据表和对这些表进行相关操作，下面我们会做更详细的介绍。

#### 2. 数据库表设计

#### **【用户表（user）】**

        用户表（user）存储了所有的用户信息，包括用户ID、用户名、密码等。下面是用户表的设计及创建代码：

```
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT, -- 用户ID，自动增加
  `username` varchar(50) NOT NULL, -- 用户名
  `password` varchar(50) NOT NULL, -- 密码
  PRIMARY KEY (`id`), -- 设置用户ID为主键
  UNIQUE KEY `username` (`username`) -- 设置用户名唯一
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

```

**我们可以在数据表中插入一些数据，以供后面的操作使用：**

```
INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'admin', '123456'),
(2, 'user01', '123456');

```

上述代码就是向用户表中插入了两条数据，id为1的用户为管理员，用户名为admin，密码为123456；id为2的用户为普通用户，用户名为user01，密码为123456。

#### **【角色表（role）】**

        角色表（role）存储了所有的角色信息，包括角色ID、角色名称等。下面是角色表的设计及创建代码：

```
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT, -- 角色ID，自动增加
  `name` varchar(50) NOT NULL, -- 角色名
  PRIMARY KEY (`id`), -- 设置角色ID为主键
  UNIQUE KEY `name` (`name`) -- 设置角色名唯一
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

```

**我们可以在数据表中插入一些数据，以供后面的操作使用：**

```
INSERT INTO `role` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'user');

```

上述代码中插入了两个角色，id为1的角色为管理员，名称为admin；id为2的角色为普通用户，名称为user。

#### **【权限表（permission）】**

        权限表（permission）存储了所有的权限信息，包括权限ID、权限名称、权限URL等。下面是权限表的设计及创建代码：

```
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT, -- 权限ID，自动增加
  `name` varchar(50) NOT NULL, -- 权限名称
  `url` varchar(50) NOT NULL, -- 权限URL
  PRIMARY KEY (`id`), -- 设置权限ID为主键
  UNIQUE KEY `name` (`name`) -- 设置权限名称唯一
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

```

**我们可以在数据表中插入一些数据，以供后面的操作使用：**

```
INSERT INTO `permission` (`id`, `name`, `url`) VALUES
(1, '查看用户', '/user/list'),
(2, '添加用户', '/user/add');

```

上述代码中插入了两个权限，id为1的权限为查看用户信息，URL为/user/list；id为2的权限为添加用户信息，URL为/user/add。

#### **【用户角色关联表（user_role）】**

        用户角色关联表（user_role）存储了用户和角色的关联信息，包括用户ID和角色ID。下面是用户角色关联表的设计及创建代码：

```
CREATE TABLE `user_role` (
  `user_id` int(11) NOT NULL, -- 用户ID
  `role_id` int(11) NOT NULL, -- 角色ID
  PRIMARY KEY (`user_id`,`role_id`), -- 设置用户ID和角色ID为联合主键
  KEY `role_id` (`role_id`), -- 设置角色ID为索引
  CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`), -- 设置外键规则，关联用户表
  CONSTRAINT user_role_ibfk_2 FOREIGN KEY (role_id) REFERENCES role (id) -- 设置外键规则，关联角色表
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**我们可以在数据表中插入一些数据，以供后面的操作使用：**

```
INSERT INTO `user_role` (`user_id`, `role_id`) VALUES
(1, 1),
(1, 2),
(2, 2);
```

上述代码中插入了两条记录，表示id为1的用户为管理员，id为2的用户为普通用户。

#### 【角色权限关联表（role_permission）】

        角色权限关联表（role_permission）存储了角色和权限的关联信息，包括角色ID和权限ID。下面是角色权限关联表的设计及创建代码：

```
CREATE TABLE `role_permission` (
  `role_id` int(11) NOT NULL,     -- 角色ID
  `permission_id` int(11) NOT NULL,  -- 权限ID
  PRIMARY KEY (`role_id`,`permission_id`), -- 设置角色ID和权限ID为联合主键
  KEY `permission_id` (`permission_id`),   -- 设置权限ID为索引
  CONSTRAINT `role_permission_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`), -- 设置外键规则，关联角色表
  CONSTRAINT `role_permission_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`) -- 设置外键规则，关联权限表
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**我们可以在数据表中插入一些数据，以供后面的操作使用：**

```
INSERT INTO `role_permission` (`role_id`, `permission_id`) VALUES
(1, 1),
(1, 2),
(2, 1);
```

上述代码中插入了三条记录，表示管理员角色有两个权限（查看用户信息和添加用户信息），普通用户角色只有一个权限（查看用户信息）。

#### 3. 数据库表操作

        在建立好数据库和数据表之后，我们需要对表格进行增删改查或修改表结构等操作，下面我们就来详细介绍一下。

#### 【增加数据】

增加数据可以使用INSERT INTO语句，具体示例如下：

```
INSERT INTO `user` (`username`, `password`) VALUES ('user02', '123456'); -- 插入一条用户数据

INSERT INTO `role` ( `name`) VALUES ('visitor');  -- 插入一条角色数据

INSERT INTO `permission` (`id`, `name`, `url`) VALUES ('修改用户', '/user/edit');  -- 插入一条权限数据

INSERT INTO `user_role` (`user_id`, `role_id`) VALUES (3, 1); -- 插入一条用户角色关联信息

INSERT INTO `role_permission` (`role_id`, `permission_id`) VALUES (3, 3);  -- 插入一条角色权限关联信息
```

上述代码中，分别向用户、角色、权限、用户角色关联和角色权限关联表中插入了一条数据。注意，本文中为了演示简便，有些数据表暂时只有少量数据，实际应用中可能需要更多的数据。

#### 【查询数据】

查询数据可以使用SELECT语句，可以选择列出所有的数据，也可以根据条件筛选数据。下面是查询数据的基本语句：

```
SELECT * FROM `user`; -- 查询所有用户信息
SELECT `id`, `username` FROM `user` WHERE id=1; -- 查询id为1的用户ID和用户名
SELECT `name`,`url` FROM `permission` WHERE `id` IN (1,2); -- 查询id为1和2的权限名称和URL
SELECT * FROM `user_role_permission`; -- 查询用户角色权限视图中所有记录
```

#### 【更新数据】

更新数据可以使用UPDATE语句，可以根据条件对数据进行修改。下面是更新数据的示例：

```
UPDATE `user` SET `password` = 'newpassword' WHERE `id` = 3; -- 将id为3的用户密码修改为newpassword
UPDATE `role` SET `name` = 'vip' WHERE `id` = 3; -- 将id为3的角色名称修改为vip

```

#### 【删除数据】

删除数据可以使用DELETE语句，可以根据条件删除数据。下面是删除数据的示例：

```
DELETE FROM `user` WHERE `id` = 3; -- 删除id为3的用户信息
DELETE FROM `role` WHERE `id` = 3; -- 删除id为3的角色信息
DELETE FROM `permission` WHERE `id` = 3; -- 删除id为3的权限信息
DELETE FROM `user_role` WHERE `user_id` = 3; -- 删除和id为3的用户关联的角色信息
DELETE FROM `role_permission` WHERE `permission_id` = 3; -- 删除和id为3的权限关联的角色信息

```

#### 【视图创建】

视图是一种虚拟的表格，可以根据实际表格中的数据进行定义，而不是真正存在。我们可以对视图进行增删改查等操作。下面是一个创建用户角色权限视图的示例：

```
CREATE VIEW `user_role_permission` AS
SELECT `user`.`username`, `role`.`name`, `permission`.`url` 
FROM `user`, `user_role`, `role_permission`, `role`, `permission` 
WHERE `user`.`id` = `user_role`.`user_id` AND `user_role`.`role_id` = `role_permission`.`role_id` AND `role_permission`.`permission_id` = `permission`.`id` AND `role`.`id` = `role_permission`.`role_id`;

```

上述代码中，我们创建了一个用户角色权限视图，来展示所有用户、角色和权限的信息。这个视图包含了用户名、角色名称和权限URL。我们可以使用SELECT语句对视图进行查询，如：

```
SELECT * FROM `user_role_permission`;

```

可以看到，此时我们就可以基于这个视图进行查询，实际查询的是多张表格的关联信息。

#### 【触发器创建】

触发器可以在表格中插入、删除或更新数据时自动执行一段程序。下面是创建一个插入数据时自动更新用户表的数据行数的触发器的示例：

```
CREATE TRIGGER `user_count` AFTER INSERT ON `user`
FOR EACH ROW BEGIN
   -- ...执行动作...
   SET @total_count = (SELECT COUNT(*) FROM `user`);
   UPDATE `system_info` SET `value` = @total_count WHERE `key` = 'user_count';
END;

-- 这段代码是用来创建一个触发器的，该触发器被命名为user_count，在每次向user表格插入一行新数据后，就会被触发执行。
```

上述代码中，我们定义了一个触发器，在用户表中插入数据时，自动更新系统信息表中的用户行数。这个操作会在每个插入操作之后执行，统计用户表格中的所有行数，并更新系统信息表格中的值。我们可以在插入用户数据后，查询系统信息表格的值，来确认是否已经更新。

#### 最后的效果图

#### 总结

        本文主要介绍了如何使用MySQL设计一个常用的后台管理系统，包括数据库的设计、表格的操作、视图和触发器的创建等内容，适合有一定MySQL基础的用户学习。通过这篇文章的学习，你可以了解到如何设计一个常见的后台管理系统的数据库结构，以及如何进行常见的表格操作，比如增删改查等。同时，你也可以学习如何创建视图和触发器来优化数据库操作。希望这篇文章对你有所帮助！

#### ER图

```
+-------------+       +------------+       +-------------+
|   用户    |       |   角色   |       |    权限   |
+-------------+       +------------+       +-------------+
| 用户ID (PK)  |       | 角色ID (PK)|       | 权限ID (PK) |
| 用户名        |       | 角色名称    |       | 权限名称     |
+-------------+       +------------+       +-------------+
      |                       |                       |
      |                       |                       |
      |                 +-------------------+
      |                 |   用户角色    |
      |                 +-------------------+
      |                 | 用户ID (FK)       |
      |                 | 角色ID (FK)       |
      |                 +-------------------+
      |                       |
      |                       |
      |                 +-------------------+
      |                 |   角色权限    |
      |                 +-------------------+
      |                 | 角色ID (FK)       |
      |                 | 权限ID (FK)       |
      |                 +-------------------+
```

这个简化的ER图中，有三个实体：用户、角色和权限。每个实体都有对应的属性列，主键使用 `(PK)` 标识。用户实体有用户ID和用户名，角色实体有角色ID和角色名称，权限实体有权限ID和权限名称。

用户角色关联表和角色权限关联表分别表示用户与角色之间的关系，以及角色与权限之间的关系。这两个关联表使用外键来链接各个实体。
